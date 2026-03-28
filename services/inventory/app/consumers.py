"""
SQS consumer for inventory service.
Listens to order.confirmed events and deducts stock.
Run as a background task on service startup.
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
INVENTORY_QUEUE_URL = os.getenv("INVENTORY_QUEUE_URL", "")
POLL_INTERVAL = int(os.getenv("SQS_POLL_INTERVAL", "5"))


def _get_sqs():
    kwargs = {"region_name": AWS_REGION}
    if AWS_ENDPOINT_URL:
        kwargs["endpoint_url"] = AWS_ENDPOINT_URL
    return boto3.client("sqs", **kwargs)


async def _handle_order_confirmed(payload: dict):
    """Deduct reserved stock when an order is confirmed."""
    from app.database import get_session_factory
    from app.models import Inventory, Reservation
    from sqlalchemy import select
    from datetime import datetime

    order_id = payload.get("order_id")
    if not order_id:
        return

    factory = get_session_factory()
    async with factory() as db:
        # Find all active reservations for this order
        result = await db.execute(
            select(Reservation).where(
                Reservation.order_id == order_id,
                Reservation.status == "active",
            )
        )
        reservations = result.scalars().all()

        for reservation in reservations:
            inv_result = await db.execute(
                select(Inventory).where(Inventory.product_id == reservation.product_id)
            )
            inv = inv_result.scalar_one_or_none()
            if inv:
                inv.quantity_reserved = max(0, inv.quantity_reserved - reservation.quantity)
                inv.quantity_on_hand = max(0, inv.quantity_on_hand - reservation.quantity)
                inv.quantity_available = inv.quantity_on_hand - inv.quantity_reserved
                inv.version += 1
                inv.updated_at = datetime.utcnow()
            reservation.status = "fulfilled"

        await db.commit()
        logger.info("Deducted stock for order %s (%d reservations)", order_id, len(reservations))


async def _handle_order_cancelled(payload: dict):
    """Release stock reservations when an order is cancelled."""
    from app.database import get_session_factory
    from app.models import Inventory, Reservation
    from sqlalchemy import select
    from datetime import datetime

    order_id = payload.get("order_id")
    if not order_id:
        return

    factory = get_session_factory()
    async with factory() as db:
        result = await db.execute(
            select(Reservation).where(
                Reservation.order_id == order_id,
                Reservation.status == "active",
            )
        )
        reservations = result.scalars().all()

        for reservation in reservations:
            inv_result = await db.execute(
                select(Inventory).where(Inventory.product_id == reservation.product_id)
            )
            inv = inv_result.scalar_one_or_none()
            if inv:
                inv.quantity_reserved = max(0, inv.quantity_reserved - reservation.quantity)
                inv.quantity_available = inv.quantity_on_hand - inv.quantity_reserved
                inv.version += 1
                inv.updated_at = datetime.utcnow()
            reservation.status = "released"

        await db.commit()
        logger.info("Released stock for cancelled order %s", order_id)


async def poll_sqs():
    """Long-poll SQS queue for inventory events."""
    if not INVENTORY_QUEUE_URL:
        logger.info("INVENTORY_QUEUE_URL not set — SQS consumer disabled")
        return

    sqs = _get_sqs()
    logger.info("Starting SQS consumer for %s", INVENTORY_QUEUE_URL)

    while True:
        try:
            response = sqs.receive_message(
                QueueUrl=INVENTORY_QUEUE_URL,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=10,
                MessageAttributeNames=["All"],
            )
            messages = response.get("Messages", [])

            for msg in messages:
                try:
                    # SNS wraps the message body in an envelope
                    outer = json.loads(msg["Body"])
                    body = json.loads(outer.get("Message", msg["Body"]))
                    event_type = body.get("event_type", "")
                    payload = body.get("payload", body)

                    if event_type == "order.confirmed":
                        await _handle_order_confirmed(payload)
                    elif event_type == "order.cancelled":
                        await _handle_order_cancelled(payload)

                    # Delete processed message
                    sqs.delete_message(
                        QueueUrl=INVENTORY_QUEUE_URL,
                        ReceiptHandle=msg["ReceiptHandle"],
                    )
                except Exception as exc:
                    logger.error("Failed to process SQS message: %s", exc)

        except ClientError as exc:
            logger.error("SQS receive error: %s", exc)
            await asyncio.sleep(POLL_INTERVAL)
        except Exception as exc:
            logger.error("Unexpected consumer error: %s", exc)
            await asyncio.sleep(POLL_INTERVAL)

        await asyncio.sleep(1)
