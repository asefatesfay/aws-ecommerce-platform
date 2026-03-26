"""
AI helpers for the Catalog Service.

- generate_product_description: calls Bedrock Claude to produce SEO-optimized
  title, description, and bullet points for a product.
"""

import json
import logging
import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
CLAUDE_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"

DESCRIPTION_PROMPT_TEMPLATE = """\
You are an expert ecommerce copywriter. Generate product content for:
Product: {name}
SKU: {sku}
Category: {category}
Brand: {brand}
Attributes: {attributes}

Return ONLY a JSON object with these keys:
- title: SEO-optimized product title (max 80 characters)
- description: 150-300 word product description (benefit-focused, no hallucinated specs)
- bullets: list of exactly 5 benefit-focused bullet points (each a short string)

Example format:
{{
  "title": "...",
  "description": "...",
  "bullets": ["...", "...", "...", "...", "..."]
}}"""


def _bedrock_client():
    return boto3.client("bedrock-runtime", region_name=AWS_REGION)


async def generate_product_description(product: dict) -> dict:
    """
    Call Bedrock Claude to generate an SEO-optimized product description.

    *product* should contain: name, sku, category, brand, attributes (dict).

    Returns:
        {
            "title": str,        # max 80 chars
            "description": str,  # 150-300 words
            "bullets": list[str] # 5 items
        }

    Raises ValueError on Bedrock or parsing errors.
    """
    prompt = DESCRIPTION_PROMPT_TEMPLATE.format(
        name=product.get("name", ""),
        sku=product.get("sku", ""),
        category=product.get("category", ""),
        brand=product.get("brand", ""),
        attributes=json.dumps(product.get("attributes", {})),
    )

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    })

    try:
        client = _bedrock_client()
        response = client.invoke_model(
            modelId=CLAUDE_MODEL_ID,
            body=body,
            contentType="application/json",
            accept="application/json",
        )
        result = json.loads(response["body"].read())
        text_content = result["content"][0]["text"].strip()
    except (BotoCoreError, ClientError) as exc:
        raise ValueError(f"Bedrock call failed: {exc}") from exc
    except (KeyError, IndexError) as exc:
        raise ValueError(f"Unexpected Bedrock response structure: {exc}") from exc

    # Strip markdown code fences if present
    if text_content.startswith("```"):
        text_content = text_content.split("```")[1]
        if text_content.startswith("json"):
            text_content = text_content[4:]

    try:
        generated = json.loads(text_content)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Claude returned non-JSON content: {exc}") from exc

    # Validate required keys
    for key in ("title", "description", "bullets"):
        if key not in generated:
            raise ValueError(f"Claude response missing required key: '{key}'")

    # Enforce title length
    if len(generated["title"]) > 80:
        generated["title"] = generated["title"][:80]

    # Ensure exactly 5 bullets
    bullets = generated.get("bullets", [])
    if not isinstance(bullets, list):
        bullets = []
    generated["bullets"] = bullets[:5] if len(bullets) >= 5 else bullets

    return generated
