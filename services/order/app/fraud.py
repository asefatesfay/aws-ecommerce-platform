"""
Fraud detection for order creation.

Uses rule-based scoring by default (suitable for local dev / unit tests).
When BEDROCK_FRAUD_ENABLED=true, augments the rule score with a Claude
classifier via Amazon Bedrock for enhanced accuracy.

Usage:
    result = await score_order(order_data, user_data)
    # result = {"score": 0.55, "signals": ["new_account", "address_mismatch"],
    #           "recommendation": "review"}
"""

import json
import logging
import os
from datetime import datetime, timezone
from typing import Optional

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
CLAUDE_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
BEDROCK_FRAUD_ENABLED = os.getenv("BEDROCK_FRAUD_ENABLED", "false").lower() == "true"

# Signal weights — sum of triggered signals is capped at 1.0
FRAUD_SIGNALS = {
    "new_account": 0.30,           # account < 7 days old
    "high_value_new_account": 0.25, # order > $200 AND new account
    "address_mismatch": 0.20,      # billing country != shipping country
    "high_velocity": 0.15,         # > 3 orders in the last hour
    "expedited_high_value": 0.10,  # overnight/express shipping + order > $500
}

FRAUD_PROMPT_TEMPLATE = """\
You are a fraud detection classifier for an ecommerce platform.
Analyze the following order and return a JSON object with:
- additional_score: float between 0.0 and 0.3 representing additional fraud risk
  beyond the rule-based signals already detected
- reasoning: one sentence explaining your assessment

Order context:
{context}

Already triggered rule signals: {signals}
Current rule-based score: {rule_score}

Return ONLY valid JSON, no markdown:
{{"additional_score": 0.0, "reasoning": "..."}}"""


def _bedrock_client():
    return boto3.client("bedrock-runtime", region_name=AWS_REGION)


def _rule_based_score(order_data: dict, user_data: dict) -> tuple[float, list[str]]:
    """Evaluate rule-based fraud signals. Returns (raw_score, triggered_signals)."""
    signals: list[str] = []
    score = 0.0

    # Signal: new account (< 7 days old)
    created_at = user_data.get("created_at")
    if created_at:
        if isinstance(created_at, str):
            try:
                created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            except ValueError:
                created_at = None
    if created_at is None:
        # Default: treat missing created_at as a new account
        account_age_days = 0
    else:
        now = datetime.now(tz=timezone.utc)
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=timezone.utc)
        account_age_days = (now - created_at).days

    if account_age_days < 7:
        signals.append("new_account")
        score += FRAUD_SIGNALS["new_account"]

    # Signal: high-value order from a new account
    order_total = float(order_data.get("total", 0))
    if order_total > 200 and account_age_days < 7:
        signals.append("high_value_new_account")
        score += FRAUD_SIGNALS["high_value_new_account"]

    # Signal: billing/shipping country mismatch
    billing = order_data.get("billing_address") or {}
    shipping = order_data.get("shipping_address") or {}
    billing_country = billing.get("country", "")
    shipping_country = shipping.get("country", "")
    if billing_country and shipping_country and billing_country != shipping_country:
        signals.append("address_mismatch")
        score += FRAUD_SIGNALS["address_mismatch"]

    # Signal: high order velocity (> 3 orders in the last hour)
    recent_order_count = int(user_data.get("recent_order_count", 0))
    if recent_order_count > 3:
        signals.append("high_velocity")
        score += FRAUD_SIGNALS["high_velocity"]

    # Signal: expedited shipping on a high-value order
    shipping_method = str(order_data.get("shipping_method", "")).lower()
    expedited_keywords = ("overnight", "express", "next_day", "next-day", "priority")
    if any(kw in shipping_method for kw in expedited_keywords) and order_total > 500:
        signals.append("expedited_high_value")
        score += FRAUD_SIGNALS["expedited_high_value"]

    return score, signals


async def _bedrock_augment(
    order_data: dict,
    user_data: dict,
    rule_score: float,
    signals: list[str],
) -> float:
    """
    Ask Claude for an additional risk score (0.0–0.3) on top of the rule-based score.
    Returns 0.0 on any error so the rule-based score is used as-is.
    """
    context = json.dumps({
        "order_total": order_data.get("total"),
        "item_count": len(order_data.get("items", [])),
        "shipping_method": order_data.get("shipping_method"),
        "billing_country": (order_data.get("billing_address") or {}).get("country"),
        "shipping_country": (order_data.get("shipping_address") or {}).get("country"),
        "account_age_days": user_data.get("account_age_days"),
        "recent_order_count": user_data.get("recent_order_count", 0),
    })

    prompt = FRAUD_PROMPT_TEMPLATE.format(
        context=context,
        signals=json.dumps(signals),
        rule_score=rule_score,
    )

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": prompt}],
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
        text = result["content"][0]["text"].strip()
        parsed = json.loads(text)
        additional = float(parsed.get("additional_score", 0.0))
        # Clamp to [0.0, 0.3]
        return max(0.0, min(0.3, additional))
    except (BotoCoreError, ClientError, json.JSONDecodeError, KeyError, ValueError) as exc:
        logger.warning("Bedrock fraud augmentation failed: %s — using rule score only", exc)
        return 0.0


async def score_order(order_data: dict, user_data: dict) -> dict:
    """
    Score an order for fraud risk.

    Args:
        order_data: dict with keys: total, items, billing_address, shipping_address,
                    shipping_method (optional)
        user_data:  dict with keys: created_at (ISO str or datetime),
                    recent_order_count (int, orders in last hour)

    Returns:
        {
            "score": float,              # 0.0 – 1.0
            "signals": list[str],        # triggered signal names
            "recommendation": str        # "allow" | "review" | "block"
        }
    """
    rule_score, signals = _rule_based_score(order_data, user_data)

    if BEDROCK_FRAUD_ENABLED:
        additional = await _bedrock_augment(order_data, user_data, rule_score, signals)
        total_score = rule_score + additional
    else:
        total_score = rule_score

    # Cap at 1.0
    total_score = min(1.0, total_score)

    if total_score >= 0.8:
        recommendation = "block"
    elif total_score >= 0.5:
        recommendation = "review"
    else:
        recommendation = "allow"

    return {
        "score": round(total_score, 3),
        "signals": signals,
        "recommendation": recommendation,
    }
