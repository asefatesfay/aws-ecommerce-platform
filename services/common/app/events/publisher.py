"""
SNS event publisher for local dev (LocalStack) and production (AWS).
Reads endpoint URL from AWS_ENDPOINT_URL env var — set to http://localstack:4566 in docker-compose.
"""
import json
import logging
import os
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")  # http://localstack:4566 in dev

_sns_client = None


def _get_sns():
    global _sns_client
    if _sns_client is None:
        kwargs: dict = {"region_name": AWS_REGION}
        if AWS_ENDPOINT_URL:
            kwargs["endpoint_url"] = AWS_ENDPOINT_URL
        _sns_client = boto3.client("sns", **kwargs)
    return _sns_client


def _serialize(obj: Any) -> Any:
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")


def publish_event(topic_arn: str, event_type: str, payload: dict) -> str | None:
    """Publish a structured event to SNS. Returns MessageId or None on failure."""
    if not topic_arn:
        logger.warning("publish_event: topic_arn is empty, skipping publish for %s", event_type)
        return None
    message = {
        "event_type": event_type,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "payload": payload,
    }
    try:
        resp = _get_sns().publish(
            TopicArn=topic_arn,
            Message=json.dumps(message, default=_serialize),
            MessageAttributes={
                "event_type": {"DataType": "String", "StringValue": event_type}
            },
        )
        logger.debug("Published %s → %s (%s)", event_type, topic_arn, resp["MessageId"])
        return resp["MessageId"]
    except ClientError as exc:
        logger.error("Failed to publish %s: %s", event_type, exc)
        return None
