"""Unit tests for the /health endpoint (Req 14.6)."""
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def app_with_mocked_deps(monkeypatch):
    """Return a TestClient with DB and Redis mocked out."""
    # Patch init_db and init_cache so lifespan doesn't need real connections
    with (
        patch("app.main.init_db"),
        patch("app.main.init_cache"),
        patch("app.main._check_db", new_callable=AsyncMock),
        patch("app.main._check_redis", new_callable=AsyncMock),
    ):
        from app.main import create_app

        application = create_app(title="Test Service")
        with TestClient(application, raise_server_exceptions=False) as client:
            yield client


def test_health_returns_200_when_deps_ok(app_with_mocked_deps):
    response = app_with_mocked_deps.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["checks"]["database"] == "ok"
    assert body["checks"]["redis"] == "ok"


def test_health_returns_503_when_db_down():
    with (
        patch("app.main.init_db"),
        patch("app.main.init_cache"),
        patch("app.main._check_db", new_callable=AsyncMock, side_effect=ConnectionError("db down")),
        patch("app.main._check_redis", new_callable=AsyncMock),
    ):
        from app.main import create_app

        application = create_app(title="Test Service")
        with TestClient(application, raise_server_exceptions=False) as client:
            response = client.get("/health")

    assert response.status_code == 503
    body = response.json()
    assert body["status"] == "degraded"
    assert body["checks"]["database"] == "error"
    assert body["checks"]["redis"] == "ok"


def test_health_returns_503_when_redis_down():
    with (
        patch("app.main.init_db"),
        patch("app.main.init_cache"),
        patch("app.main._check_db", new_callable=AsyncMock),
        patch(
            "app.main._check_redis",
            new_callable=AsyncMock,
            side_effect=ConnectionError("redis down"),
        ),
    ):
        from app.main import create_app

        application = create_app(title="Test Service")
        with TestClient(application, raise_server_exceptions=False) as client:
            response = client.get("/health")

    assert response.status_code == 503
    body = response.json()
    assert body["status"] == "degraded"
    assert body["checks"]["redis"] == "error"
    assert body["checks"]["database"] == "ok"
