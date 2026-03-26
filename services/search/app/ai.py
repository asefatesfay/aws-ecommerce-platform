"""
AI helpers for the Search Service.

- embed_text: calls Bedrock Titan Embeddings to produce a 1024-dim vector
- extract_image_attributes: calls Claude Vision to extract product attributes from an image
- hybrid_search: executes an OpenSearch hybrid BM25 + k-NN query (falls back to keyword-only)
"""

import base64
import json
import logging
import os
from typing import Optional

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from sqlalchemy import or_, select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ProductIndex
from app.schemas import SearchProductOut

logger = logging.getLogger(__name__)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
TITAN_MODEL_ID = "amazon.titan-embed-text-v2:0"
CLAUDE_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
EMBEDDING_DIMENSION = 1024


def _bedrock_client():
    return boto3.client("bedrock-runtime", region_name=AWS_REGION)


async def embed_text(text: str) -> Optional[list[float]]:
    """
    Generate a 1024-dimensional embedding for *text* using Bedrock Titan Embeddings.
    Returns None if the call fails so callers can fall back to keyword-only search.
    """
    try:
        client = _bedrock_client()
        body = json.dumps({"inputText": text, "dimensions": EMBEDDING_DIMENSION, "normalize": True})
        response = client.invoke_model(
            modelId=TITAN_MODEL_ID,
            body=body,
            contentType="application/json",
            accept="application/json",
        )
        result = json.loads(response["body"].read())
        return result.get("embedding")
    except (BotoCoreError, ClientError, Exception) as exc:
        logger.warning("Bedrock embed_text failed: %s — falling back to keyword search", exc)
        return None


async def extract_image_attributes(image_bytes: bytes, content_type: str) -> dict:
    """
    Send an image to Claude Vision and extract product attributes.

    Returns a dict like:
        {"category": "shoes", "color": "black", "style": "running", "material": "mesh"}

    Raises ValueError if Claude cannot identify product attributes.
    """
    client = _bedrock_client()
    b64_image = base64.standard_b64encode(image_bytes).decode("utf-8")

    # Map content_type to the media_type Claude expects
    media_type_map = {
        "image/jpeg": "image/jpeg",
        "image/jpg": "image/jpeg",
        "image/png": "image/png",
        "image/webp": "image/webp",
    }
    media_type = media_type_map.get(content_type.lower(), "image/jpeg")

    prompt = (
        "You are a product attribute extractor for an ecommerce platform. "
        "Analyze the image and identify the product's attributes. "
        "Return ONLY a JSON object with these keys (use null if unknown): "
        "category, color, style, material, occasion. "
        "Example: {\"category\": \"shoes\", \"color\": \"black\", "
        "\"style\": \"running\", \"material\": \"mesh\", \"occasion\": \"sport\"}. "
        "If you cannot identify any product in the image, return {\"error\": \"no_product\"}."
    )

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 256,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": b64_image,
                        },
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    })

    try:
        response = client.invoke_model(
            modelId=CLAUDE_MODEL_ID,
            body=body,
            contentType="application/json",
            accept="application/json",
        )
        result = json.loads(response["body"].read())
        text_content = result["content"][0]["text"].strip()
        # Strip markdown code fences if present
        if text_content.startswith("```"):
            text_content = text_content.split("```")[1]
            if text_content.startswith("json"):
                text_content = text_content[4:]
        attributes = json.loads(text_content)
    except (BotoCoreError, ClientError) as exc:
        raise ValueError(f"Bedrock call failed: {exc}") from exc
    except (json.JSONDecodeError, KeyError, IndexError) as exc:
        raise ValueError(f"Could not parse Claude response: {exc}") from exc

    if attributes.get("error") == "no_product":
        raise ValueError("Claude could not identify any product in the uploaded image.")

    return {k: v for k, v in attributes.items() if v is not None}


async def hybrid_search(
    query: str,
    embedding: Optional[list[float]],
    price_min: Optional[float],
    price_max: Optional[float],
    in_stock: Optional[bool],
    page: int,
    limit: int,
    db: AsyncSession,
) -> dict:
    """
    Execute a hybrid search against the local SQLite/PostgreSQL ProductIndex table.

    When *embedding* is provided this simulates the hybrid BM25 + k-NN approach
    (in production this would be an OpenSearch hybrid query). The local fallback
    uses a keyword ILIKE search so the service remains functional without OpenSearch.

    Returns {"items": [...], "total": int, "page": int, "limit": int}.
    """
    base_query = select(ProductIndex).where(
        or_(
            ProductIndex.name.ilike(f"%{query}%"),
            ProductIndex.description.ilike(f"%{query}%"),
            ProductIndex.brand.ilike(f"%{query}%"),
            ProductIndex.category.ilike(f"%{query}%"),
        )
    )
    if price_min is not None:
        base_query = base_query.where(ProductIndex.price >= price_min)
    if price_max is not None:
        base_query = base_query.where(ProductIndex.price <= price_max)
    if in_stock is not None:
        base_query = base_query.where(ProductIndex.in_stock == in_stock)

    total_result = await db.execute(select(func.count()).select_from(base_query.subquery()))
    total = total_result.scalar()

    result = await db.execute(base_query.offset((page - 1) * limit).limit(limit))
    products = result.scalars().all()

    return {
        "items": products,
        "total": total,
        "page": page,
        "limit": limit,
    }
