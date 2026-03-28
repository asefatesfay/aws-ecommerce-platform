"""
SQS consumer for order service.
Listens for payment.succeeded / payment.failed events and transitions order status.
"""
import asyncio
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
ORDER_PAYMENT_QUEUE_URL = os.getenv("ORDER_PAYMENT_QUEUE_URL", "")
ORDER_EVENTS_TOPIC_ARN = os.getenv("ORDER_EVENTS_TOPIC_ARN", "")


def _get_sqs():
    kwargs = {"region_name": AWS_REGION}
    if AWS_ENDPOINT_URL:
        kwargs["endpoint_url"] = AWS_ENDPOINT_URL
    return boto3.client("sqs", **kwargs)


def _get_sns():
    kwargs = {"region_name": AWS_REGION}
    if AWS_ENDPOINT_URL:
        kwargs["endpoint_url"] = AWS_ENDPOINT_URL
    return boto3.client("sns", **kwargs)


def _publish(event_type: str, order_id: str, status: str):
    if not ORDER_EVENTS_TOPIC_ARN:
        return
    try:
        _get_sns().publish(
            TopicArn=ORDER_EVENTS_TOPIC_ARN,
            Message=json.dumps({"event_type": event_type, "order_id": order_id, "status": status}),
            MessageAttributes={"event_type": {"DataType": "String", "StringValue": event_type}},
        )
    except Exception as exc:
        logger.warning("SNS publish failed (%s): %s", event_type, exc)


async def _handle_payment_succeeded(payload: dict):
    from app.database import get_session_factory
    from app.models import Order
    from sqlalchemy import select
    from datetime import datetime

    order_id = payload.get("order_id")
    if not order_id:
        return

    factory = get_session_factory()
    async with factory() as db:
        result = await db.execute(select(Order).where(Order.id == order_id))
        order = result.scalar_one_or_none()
        if order and order.status in ("pending", "under_review"):
            order.status = "confirmed"
            order.updated_at = datetime.utcnow()
            await db.commit()
            logger.info("Order %s confirmed after payment succeeded", order_id)
            _publish("order.confirmed", order_id, "confirmed")


async def _handle_payment_failed(payload: dict):
    from app.database import get_session_factory
    from app.models import Order
    from sqlalchemy import select
    from datetime import datetime

    order_id = payload.get("order_id")
    if not order_id:
        return

    factory = get_session_factory()
    async with factory() as db:
        result = await db.execute(select(Order).where(Order.id == order_id))
        order = result.scalar_one_or_none()
        if order and order.status in ("pending", "under_review"):
            order.status = "cancelled"
            order.updated_at = datetime.utcnow()
            await db.commit()
            logger.info("Order %s cancelled after payment failed", order_id)
            _publish("order.cancelled", order_id, "cancelled")


async def poll_sqs():
    if not ORDER_PAYMENT_QUEUE_URL:
        logger.info("ORDER_PAYMENT_QUEUE_URL not set — SQS consumer disabled")
        return

    sqs = _get_sqs()
    logger.info("Order SQS consumer started: %s", ORDER_PAYMENT_QUEUE_URL)

    while True:
        try:
            response = sqs.receive_message(
                QueueUrl=ORDER_PAYMENT_QUEUE_URL,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=10,
            )
            for msg in response.get("Messages", []):
                try:
                    outer = json.loads(msg["Body"])
                    body = json.loads(outer.get("Message", msg["Body"]))
                    event_type = body.get("event_type", "")
                    payload = body.get("payload", body)

                    if event_type == "payment.succeeded":
                        await _handle_payment_succeeded(payload)
                    elif event_type == "payment.failed":
                        await _handle_payment_failed(payload)

                    sqs.delete_message(
                        QueueUrl=ORDER_PAYMENT_QUEUE_URL,
                        ReceiptHandle=msg["ReceiptHandle"],
                    )
                except Exception as exc:
                    logger.error("Failed to process message: %s", exc)
        except ClientError as exc:
            logger.error("SQS receive error: %s", exc)
            await asyncio.sleep(5)
        except Exception as exc:
            logger.error("Consumer error: %s", exc)
            await asyncio.sleep(5)

        await asyncio.sleep(1)
