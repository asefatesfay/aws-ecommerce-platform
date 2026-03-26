"""
FastAPI lifespan bootstrap template.

Each microservice imports this module and calls ``create_app()`` to get a
fully-configured FastAPI application with:
  - Async SQLAlchemy engine initialised
  - Redis pool initialised
  - CORS middleware
  - /health endpoint that verifies Aurora + Redis connectivity
  - Graceful shutdown hooks

Usage in a service's own main.py::

    from app.main import create_app
    from app.routers import my_router

    app = create_app(title="My Service")
    app.include_router(my_router, prefix="/my-prefix")
"""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.cache import close_cache, get_redis, init_cache
from app.db import close_db, get_engine, init_db
from app.settings import get_settings

logger = logging.getLogger(__name__)


# ── Lifespan ──────────────────────────────────────────────────────────────────


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore[type-arg]
    """Startup / shutdown lifecycle for every microservice."""
    settings = get_settings()
    logger.info("Starting %s in %s environment", settings.service_name, settings.environment)

    # ── Startup ───────────────────────────────────────────────────────────────
    init_db()
    init_cache()

    # Verify connectivity so the container fails fast on misconfiguration
    await _check_db()
    await _check_redis()

    logger.info("%s is ready", settings.service_name)
    yield

    # ── Shutdown ──────────────────────────────────────────────────────────────
    logger.info("Shutting down %s", settings.service_name)
    await close_cache()
    await close_db()


async def _check_db() -> None:
    """Raise if the database is unreachable."""
    from sqlalchemy import text

    engine = get_engine()
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    logger.debug("Database connectivity OK")


async def _check_redis() -> None:
    """Raise if Redis is unreachable."""
    redis = get_redis()
    await redis.ping()
    logger.debug("Redis connectivity OK")


# ── Health endpoint ───────────────────────────────────────────────────────────


async def health_check() -> JSONResponse:
    """
    Readiness probe.

    Returns 200 when both Aurora and Redis are reachable, 503 otherwise.
    ECS / ALB target-group health checks hit this endpoint.
    """
    checks: dict[str, Any] = {"database": "ok", "redis": "ok"}
    status_code = 200

    try:
        await _check_db()
    except Exception as exc:
        logger.warning("Health check — database FAIL: %s", exc)
        checks["database"] = "error"
        status_code = 503

    try:
        await _check_redis()
    except Exception as exc:
        logger.warning("Health check — redis FAIL: %s", exc)
        checks["redis"] = "error"
        status_code = 503

    settings = get_settings()
    body = {
        "status": "ok" if status_code == 200 else "degraded",
        "service": settings.service_name,
        "environment": settings.environment,
        "checks": checks,
    }
    return JSONResponse(content=body, status_code=status_code)


# ── Factory ───────────────────────────────────────────────────────────────────


def create_app(
    *,
    title: str = "Ecommerce Service",
    version: str = "0.1.0",
    cors_origins: list[str] | None = None,
) -> FastAPI:
    """
    Create and configure a FastAPI application.

    Parameters
    ----------
    title:
        Human-readable service name shown in the OpenAPI docs.
    version:
        API version string.
    cors_origins:
        List of allowed CORS origins.  Defaults to ``["*"]`` (suitable for
        internal services behind API Gateway).

    Returns
    -------
    FastAPI
        Configured application instance.
    """
    app = FastAPI(title=title, version=version, lifespan=lifespan)

    # CORS — API Gateway handles auth; services are internal-only
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Health endpoint — no auth required
    app.add_api_route("/health", health_check, methods=["GET"], tags=["ops"])

    return app
