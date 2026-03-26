"""Unit tests for shared Settings (Req 13.8, 14.6)."""
import os

import pytest
from pydantic import ValidationError


def test_settings_defaults(monkeypatch):
    """Settings should load with sensible defaults when no env vars are set."""
    # Clear any cached instance
    from app import settings as settings_module

    settings_module.get_settings.cache_clear()

    # Ensure no .env file interferes
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("REDIS_URL", raising=False)

    s = settings_module.Settings()
    assert s.environment == "development"
    assert "asyncpg" in s.database_url
    assert s.redis_url.startswith("redis://")
    assert s.aws_region == "us-east-1"


def test_settings_reads_env_vars(monkeypatch):
    """Settings should pick up values from environment variables."""
    from app import settings as settings_module

    settings_module.get_settings.cache_clear()

    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://user:pass@db:5432/test")
    monkeypatch.setenv("REDIS_URL", "redis://cache:6379/1")
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("SERVICE_NAME", "test-service")

    s = settings_module.Settings()
    assert s.database_url == "postgresql+asyncpg://user:pass@db:5432/test"
    assert s.redis_url == "redis://cache:6379/1"
    assert s.environment == "production"
    assert s.service_name == "test-service"


def test_settings_invalid_log_level(monkeypatch):
    """An invalid log_level should raise a ValidationError."""
    from app import settings as settings_module

    settings_module.get_settings.cache_clear()
    monkeypatch.setenv("LOG_LEVEL", "VERBOSE")

    with pytest.raises(ValidationError):
        settings_module.Settings()


def test_settings_log_level_case_insensitive(monkeypatch):
    """log_level should be normalised to uppercase."""
    from app import settings as settings_module

    settings_module.get_settings.cache_clear()
    monkeypatch.setenv("LOG_LEVEL", "debug")

    s = settings_module.Settings()
    assert s.log_level == "DEBUG"
