"""Price/Deal Agent tool implementations — inventory velocity analysis and SNS publishing."""
import json
import os
from typing import Any

import boto3
import httpx

INVENTORY_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory:8000")
ADMIN_URL = os.getenv("ADMIN_SERVICE_URL", "http://admin:8000")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
PRICING_TOPIC_ARN = os.getenv("PRICING_TOPIC_ARN", "")

_TIMEOUT = 15.0


async def get_slow_moving_products(
    days_in_stock: int = 30,
    max_units_sold: int = 5,
    **_: Any,
) -> list[dict]:
    """Find products with low sales velocity relative to stock age."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(
            f"{INVENTORY_URL}/inventory/slow-moving",
            params={"days_in_stock": days_in_stock, "max_units_sold": max_units_sold},
        )
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else data.get("items", [])


async def suggest_markdown(
    product_id: str,
    suggested_discount_pct: float,
    **_: Any,
) -> dict:
    """Calculate and publish a markdown suggestion for a slow-moving product."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        # Fetch current price from catalog
        resp = await client.get(f"{ADMIN_URL}/admin/products/{product_id}")
        resp.raise_for_status()
        product = resp.json()

    current_price = float(product.get("price", 0))
    discount = max(0.0, min(50.0, suggested_discount_pct))
    suggested_price = round(current_price * (1 - discount / 100), 2)

    return {
        "product_id": product_id,
        "current_price": current_price,
        "suggested_discount_pct": discount,
        "suggested_price": suggested_price,
    }


async def get_restock_recommendations(**_: Any) -> list[dict]:
    """List products below reorder threshold with suggested reorder quantities."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{INVENTORY_URL}/inventory/low-stock")
        resp.raise_for_status()
        data = resp.json()
        items = data if isinstance(data, list) else data.get("items", [])

    recommendations = []
    for item in items:
        reorder_qty = item.get("reorder_quantity", 50)
        recommendations.append(
            {
                "product_id": item.get("product_id"),
                "quantity_available": item.get("quantity_available", 0),
                "reorder_threshold": item.get("reorder_threshold", 0),
                "suggested_reorder_quantity": reorder_qty,
            }
        )
    return recommendations


async def publish_pricing_suggestion(
    product_id: str,
    action: str,
    suggested_price: float | None,
    reason: str,
    **_: Any,
) -> dict:
    """Publish a pricing suggestion event to SNS for admin review."""
    payload = {
        "event_type": "pricing.suggestion",
        "product_id": product_id,
        "action": action,
        "suggested_price": suggested_price,
        "reason": reason,
    }

    if PRICING_TOPIC_ARN:
        sns = boto3.client("sns", region_name=AWS_REGION)
        sns.publish(
            TopicArn=PRICING_TOPIC_ARN,
            Message=json.dumps(payload),
            MessageAttributes={
                "event_type": {"DataType": "String", "StringValue": "pricing.suggestion"}
            },
        )

    return {"published": True, **payload}
