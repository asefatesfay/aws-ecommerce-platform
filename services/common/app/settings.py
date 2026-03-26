"""
Shared settings for all microservices.
Values are read from environment variables; secrets are injected by ECS
from AWS Secrets Manager at task startup.
"""
from __future__ import annotations

import json
import logging
from functools import lru_cache
from typing import Optional

import boto3
from botocore.exceptions import ClientError
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Service identity ──────────────────────────────────────────────────────
    service_name: str = "ecommerce-service"
    environment: str = "development"
    log_level: str = "INFO"

    # ── Database (Aurora PostgreSQL) ──────────────────────────────────────────
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ecommerce"

    # ── Redis (ElastiCache) ───────────────────────────────────────────────────
    redis_url: str = "redis://localhost:6379/0"

    # ── AWS ───────────────────────────────────────────────────────────────────
    aws_region: str = "us-east-1"
    aws_account_id: Optional[str] = None

    # ── SNS topic ARNs ────────────────────────────────────────────────────────
    order_events_topic_arn: Optional[str] = None
    payment_events_topic_arn: Optional[str] = None
    product_events_topic_arn: Optional[str] = None
    inventory_events_topic_arn: Optional[str] = None

    # ── Stripe ────────────────────────────────────────────────────────────────
    stripe_secret_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None

    # ── Cognito ───────────────────────────────────────────────────────────────
    cognito_user_pool_id: Optional[str] = None
    cognito_client_id: Optional[str] = None
    cognito_region: Optional[str] = None

    # ── S3 ────────────────────────────────────────────────────────────────────
    s3_bucket_name: Optional[str] = None
    cloudfront_domain: Optional[str] = None

    # ── OpenSearch ────────────────────────────────────────────────────────────
    opensearch_url: Optional[str] = None

    # ── DynamoDB ──────────────────────────────────────────────────────────────
    dynamodb_cart_table: str = "ecommerce-carts"

    # ── Amazon Personalize ────────────────────────────────────────────────────
    personalize_campaign_arn: Optional[str] = None
    personalize_event_tracker_id: Optional[str] = None

    # ── Secrets Manager (optional — for local override) ───────────────────────
    secrets_manager_secret_id: Optional[str] = None

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        valid = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        upper = v.upper()
        if upper not in valid:
            raise ValueError(f"log_level must be one of {valid}")
        return upper


def _load_secrets_from_manager(secret_id: str, region: str) -> dict:
    """Fetch a JSON secret from AWS Secrets Manager and return it as a dict."""
    client = boto3.client("secretsmanager", region_name=region)
    try:
        response = client.get_secret_value(SecretId=secret_id)
        secret_string = response.get("SecretString", "{}")
        return json.loads(secret_string)
    except ClientError as exc:
        logger.warning("Could not load secret %s: %s", secret_id, exc)
        return {}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance, optionally enriched from Secrets Manager."""
    settings = Settings()

    if settings.secrets_manager_secret_id:
        overrides = _load_secrets_from_manager(
            settings.secrets_manager_secret_id,
            settings.aws_region,
        )
        if overrides:
            # Re-instantiate with the secret values merged in
            settings = Settings(**overrides)

    logging.basicConfig(level=settings.log_level)
    return settings
