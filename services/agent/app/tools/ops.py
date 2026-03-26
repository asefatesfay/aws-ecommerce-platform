"""Ops Agent tool implementations — admin-facing queries via Admin and Inventory services."""
import os
from typing import Any

import httpx

ADMIN_URL = os.getenv("ADMIN_SERVICE_URL", "http://admin:8000")
INVENTORY_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory:8000")

_TIMEOUT = 15.0


async def get_stuck_orders(
    status: str = "processing",
    hours: int = 24,
    **_: Any,
) -> dict:
    """Find orders that have been in a given status for longer than a specified duration."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(
            f"{ADMIN_URL}/admin/orders",
            params={"status": status, "stuck_hours": hours},
        )
        resp.raise_for_status()
        return resp.json()


async def get_low_stock_items(
    threshold: int | None = None,
    **_: Any,
) -> dict:
    """List products where available quantity is below the reorder threshold."""
    params: dict[str, Any] = {}
    if threshold is not None:
        params["threshold"] = threshold

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{INVENTORY_URL}/inventory/low-stock", params=params)
        resp.raise_for_status()
        return resp.json()


async def get_revenue_report(
    start_date: str,
    end_date: str,
    granularity: str = "day",
    **_: Any,
) -> dict:
    """Generate a revenue summary for a date range."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(
            f"{ADMIN_URL}/admin/revenue",
            params={"start": start_date, "end": end_date, "granularity": granularity},
        )
        resp.raise_for_status()
        return resp.json()


async def get_dashboard_metrics(**_: Any) -> dict:
    """Get current platform metrics: order counts, revenue totals, user counts."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{ADMIN_URL}/admin/metrics")
        resp.raise_for_status()
        return resp.json()


async def export_orders(
    status: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    **_: Any,
) -> dict:
    """Generate a CSV export of orders and return a presigned download URL."""
    payload: dict[str, Any] = {}
    if status:
        payload["status"] = status
    if date_from:
        payload["date_from"] = date_from
    if date_to:
        payload["date_to"] = date_to

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.post(f"{ADMIN_URL}/admin/orders/export", json=payload)
        resp.raise_for_status()
        return resp.json()
