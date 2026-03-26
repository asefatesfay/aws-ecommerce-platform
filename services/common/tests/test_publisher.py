"""Unit tests for SNS event publisher (Req 13.8)."""
from unittest.mock import MagicMock, patch
from uuid import uuid4

import pytest

from app.events.publisher import _serialise, publish_event


def test_serialise_uuid():
    uid = uuid4()
    assert _serialise(uid) == str(uid)


def test_serialise_datetime():
    from datetime import datetime, timezone

    dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
    result = _serialise(dt)
    assert "2024-01-15" in result


def test_serialise_unknown_type():
    with pytest.raises(TypeError):
        _serialise(object())


def test_publish_event_calls_sns(monkeypatch):
    """publish_event should call SNS.publish with correct structure."""
    mock_sns = MagicMock()
    mock_sns.publish.return_value = {"MessageId": "test-message-id"}

    # Reset cached client
    import app.events.publisher as pub_module

    pub_module._sns_client = mock_sns

    msg_id = publish_event(
        topic_arn="arn:aws:sns:us-east-1:123456789012:test-topic",
        event_type="order.confirmed",
        payload={"order_id": str(uuid4()), "total": 99.99},
    )

    assert msg_id == "test-message-id"
    mock_sns.publish.assert_called_once()
    call_kwargs = mock_sns.publish.call_args.kwargs
    assert call_kwargs["TopicArn"] == "arn:aws:sns:us-east-1:123456789012:test-topic"

    import json

    message = json.loads(call_kwargs["Message"])
    assert message["event_type"] == "order.confirmed"
    assert "timestamp" in message
    assert "payload" in message
    assert message["payload"]["total"] == 99.99

    # MessageAttributes must include event_type for SQS filter policies
    assert "event_type" in call_kwargs["MessageAttributes"]
    assert call_kwargs["MessageAttributes"]["event_type"]["StringValue"] == "order.confirmed"

    # Cleanup
    pub_module._sns_client = None


def test_publish_event_raises_on_client_error(monkeypatch):
    """publish_event should raise RuntimeError when SNS.publish fails."""
    from botocore.exceptions import ClientError

    mock_sns = MagicMock()
    mock_sns.publish.side_effect = ClientError(
        {"Error": {"Code": "InvalidParameter", "Message": "bad"}}, "Publish"
    )

    import app.events.publisher as pub_module

    pub_module._sns_client = mock_sns

    with pytest.raises(RuntimeError, match="SNS publish failed"):
        publish_event(
            topic_arn="arn:aws:sns:us-east-1:123456789012:test-topic",
            event_type="order.confirmed",
            payload={},
        )

    pub_module._sns_client = None


def test_publish_event_subject_truncated(monkeypatch):
    """Subject longer than 100 chars should be truncated."""
    mock_sns = MagicMock()
    mock_sns.publish.return_value = {"MessageId": "abc"}

    import app.events.publisher as pub_module

    pub_module._sns_client = mock_sns

    long_subject = "x" * 200
    publish_event(
        topic_arn="arn:aws:sns:us-east-1:123456789012:test-topic",
        event_type="test.event",
        payload={},
        subject=long_subject,
    )

    call_kwargs = mock_sns.publish.call_args.kwargs
    assert len(call_kwargs["Subject"]) == 100

    pub_module._sns_client = None
