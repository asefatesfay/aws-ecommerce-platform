"""
SNS publish helper shared by all microservices.

Each message envelope contains:
  - event_type  : dot-separated event name, e.g. "order.confirmed"
  - timestamp   : ISO-8601 UTC string
  - payload     : arbitrary dict with event-specific data

MessageAttributes are set so SQS subscribers can filter by event_type.
"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any, Optional
from uuid import UUID

import boto3
from botocore.exceptions import ClientError

from shared.app.settings import get_settings

logger = logging.getLogger(__name__)

# ── Lazy SNS client ───────────────────────────────────────────────────────────

_sns_client = None


def _get_sns_client():
    global _sns_client
    if _sns_client is None:
        settings = get_settings()
        _sns_client = boto3.client("sns", region_name=settings.aws_region)
    return _sns_client


# ── Helpers ───────────────────────────────────────────────────────────────────


def _serialise(obj: Any) -> Any:
    """JSON-serialise UUIDs and datetimes."""
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serialisable")


def publish_event(
    topic_arn: str,
    event_type: str,
    payload: dict[str, Any],
    *,
    subject: Optional[str] = None,
) -> str:
    """
    Publish a structured event to an SNS topic.

    Parameters
    ----------
    topic_arn:
        The ARN of the SNS topic to publish to.
    event_type:
        Dot-separated event name, e.g. ``"order.confirmed"``.
    payload:
        Event-specific data dict.  UUIDs and datetimes are auto-serialised.
    subject:
        Optional SNS message subject (max 100 chars).

    Returns
    -------
    str
        The SNS ``MessageId`` of the published message.

    Raises
    ------
    RuntimeError
        If the SNS publish call fails.
    """
    message = {
        "event_type": event_type,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "payload": payload,
    }
    message_body = json.dumps(message, default=_serialise)

    kwargs: dict[str, Any] = {
        "TopicArn": topic_arn,
        "Message": message_body,
        "MessageAttributes": {
            "event_type": {
                "DataType": "String",
                "StringValue": event_type,
            }
        },
    }
    if subject:
        kwargs["Subject"] = subject[:100]

    try:
        response = _get_sns_client().publish(**kwargs)
        message_id: str = response["MessageId"]
        logger.debug("Published %s → %s (MessageId=%s)", event_type, topic_arn, message_id)
        return message_id
    except ClientError as exc:
        logger.error("Failed to publish %s to %s: %s", event_type, topic_arn, exc)
        raise RuntimeError(f"SNS publish failed for event '{event_type}'") from exc


# ── Convenience wrappers ──────────────────────────────────────────────────────


def publish_order_event(event_type: str, payload: dict[str, Any]) -> str:
    """Publish to the order events SNS topic."""
    topic_arn = get_settings().order_events_topic_arn
    if not topic_arn:
        raise RuntimeError("ORDER_EVENTS_TOPIC_ARN is not configured")
    return publish_event(topic_arn, event_type, payload)


def publish_payment_event(event_type: str, payload: dict[str, Any]) -> str:
    """Publish to the payment events SNS topic."""
    topic_arn = get_settings().payment_events_topic_arn
    if not topic_arn:
        raise RuntimeError("PAYMENT_EVENTS_TOPIC_ARN is not configured")
    return publish_event(topic_arn, event_type, payload)


def publish_product_event(event_type: str, payload: dict[str, Any]) -> str:
    """Publish to the product events SNS topic."""
    topic_arn = get_settings().product_events_topic_arn
    if not topic_arn:
        raise RuntimeError("PRODUCT_EVENTS_TOPIC_ARN is not configured")
    return publish_event(topic_arn, event_type, payload)


def publish_inventory_event(event_type: str, payload: dict[str, Any]) -> str:
    """Publish to the inventory events SNS topic."""
    topic_arn = get_settings().inventory_events_topic_arn
    if not topic_arn:
        raise RuntimeError("INVENTORY_EVENTS_TOPIC_ARN is not configured")
    return publish_event(topic_arn, event_type, payload)
