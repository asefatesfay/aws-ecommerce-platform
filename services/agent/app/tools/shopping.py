"""Shopping Assistant tool implementations — each calls the corresponding microservice via HTTP."""
import os
from typing import Any

import httpx

SEARCH_URL = os.getenv("SEARCH_SERVICE_URL", "http://search:8000")
CART_URL = os.getenv("CART_SERVICE_URL", "http://cart:8000")
ORDER_URL = os.getenv("ORDER_SERVICE_URL", "http://order:8000")
INVENTORY_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory:8000")
RECO_URL = os.getenv("RECOMMENDATION_SERVICE_URL", "http://recommendation:8000")

_TIMEOUT = 10.0


async def search_products(
    query: str,
    price_min: float | None = None,
    price_max: float | None = None,
    category: str | None = None,
    limit: int = 5,
    **_: Any,
) -> dict:
    """Search the product catalog by keyword with optional price and category filters."""
    params: dict[str, Any] = {"q": query, "limit": limit}
    if price_min is not None:
        params["price_min"] = price_min
    if price_max is not None:
        params["price_max"] = price_max
    if category:
        params["category"] = category

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{SEARCH_URL}/search", params=params)
        resp.raise_for_status()
        return resp.json()


async def add_to_cart(
    user_id: str,
    product_id: str,
    quantity: int = 1,
    **_: Any,
) -> dict:
    """Add a product to the authenticated user's cart."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.post(
            f"{CART_URL}/cart/{user_id}/items",
            json={"product_id": product_id, "quantity": quantity},
        )
        resp.raise_for_status()
        return resp.json()


async def get_cart(user_id: str, **_: Any) -> dict:
    """Retrieve the current cart contents and subtotal for the authenticated user."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{CART_URL}/cart/{user_id}")
        resp.raise_for_status()
        return resp.json()


async def get_order_status(
    user_id: str,
    order_id: str | None = None,
    **_: Any,
) -> dict:
    """Get the status and details of a specific order or the most recent order."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        if order_id:
            resp = await client.get(
                f"{ORDER_URL}/orders/{order_id}",
                headers={"X-User-Id": user_id},
            )
        else:
            # Fetch most recent order
            resp = await client.get(
                f"{ORDER_URL}/orders",
                params={"limit": 1},
                headers={"X-User-Id": user_id},
            )
        resp.raise_for_status()
        return resp.json()


async def get_recommendations(
    user_id: str,
    limit: int = 5,
    **_: Any,
) -> dict:
    """Get personalized product recommendations for the authenticated user."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(
            f"{RECO_URL}/recommendations/{user_id}",
            params={"limit": limit},
        )
        resp.raise_for_status()
        return resp.json()


async def check_stock(product_id: str, **_: Any) -> dict:
    """Check the available stock level for a specific product."""
    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(f"{INVENTORY_URL}/inventory/{product_id}")
        resp.raise_for_status()
        return resp.json()
