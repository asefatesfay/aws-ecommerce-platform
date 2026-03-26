"""
Async Redis connection pool shared by all microservices.
"""
from __future__ import annotations

from typing import Optional

import redis.asyncio as aioredis
from redis.asyncio import Redis

from shared.app.settings import get_settings

# ── Module-level singleton ────────────────────────────────────────────────────

_redis: Optional[Redis] = None


def get_redis() -> Redis:
    if _redis is None:
        raise RuntimeError("Redis pool has not been initialised. Call init_cache() first.")
    return _redis


def init_cache(redis_url: Optional[str] = None) -> Redis:
    """
    Create the async Redis client.
    Call once during application startup (lifespan).
    """
    global _redis

    url = redis_url or get_settings().redis_url
    _redis = aioredis.from_url(
        url,
        encoding="utf-8",
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
        retry_on_timeout=True,
        health_check_interval=30,
    )
    return _redis


async def close_cache() -> None:
    """Close the Redis connection pool. Call during application shutdown (lifespan)."""
    global _redis
    if _redis is not None:
        await _redis.aclose()
        _redis = None


async def get_cache() -> Redis:
    """
    FastAPI dependency that returns the shared Redis client.

    Usage::

        @router.get("/items")
        async def list_items(cache: Redis = Depends(get_cache)):
            ...
    """
    return get_redis()
