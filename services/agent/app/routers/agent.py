"""
Agent Service router — Shopping Assistant, Ops Agent, Price/Deal Agent.

When AGENTCORE_RUNTIME_ARN is set, real AgentCore Runtime invocations are used.
Otherwise, a local mock loop runs tool calls directly for development.
"""
import os
import json
import uuid
import logging
from typing import Any

import boto3
import httpx
from fastapi import APIRouter, Depends, Header, HTTPException, status

from app.schemas import ChatRequest, ChatResponse, PricingRunResponse, ToolCall
from app.tools import shopping, ops, pricing

logger = logging.getLogger(__name__)
router = APIRouter()

AGENTCORE_RUNTIME_ARN = os.getenv("AGENTCORE_RUNTIME_ARN", "")
BEDROCK_MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID", "anthropic.claude-3-5-sonnet-20241022-v2:0"
)
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def _get_user_id(x_user_id: str = Header(..., alias="X-User-Id")) -> str:
    """Extract user_id from the X-User-Id header (set by API Gateway after JWT validation)."""
    return x_user_id


def _get_user_role(x_user_role: str = Header("customer", alias="X-User-Role")) -> str:
    """Extract user role from the X-User-Role header."""
    return x_user_role


def _require_admin(role: str = Depends(_get_user_role)) -> str:
    if role != "admins":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return role


# ---------------------------------------------------------------------------
# AgentCore / mock invocation
# ---------------------------------------------------------------------------

SHOPPING_TOOL_MAP: dict[str, Any] = {
    "search_products": shopping.search_products,
    "add_to_cart": shopping.add_to_cart,
    "get_cart": shopping.get_cart,
    "get_order_status": shopping.get_order_status,
    "get_recommendations": shopping.get_recommendations,
    "check_stock": shopping.check_stock,
}

OPS_TOOL_MAP: dict[str, Any] = {
    "get_stuck_orders": ops.get_stuck_orders,
    "get_low_stock_items": ops.get_low_stock_items,
    "get_revenue_report": ops.get_revenue_report,
    "get_dashboard_metrics": ops.get_dashboard_metrics,
    "export_orders": ops.export_orders,
}


async def _invoke_mock(
    message: str,
    session_id: str,
    user_id: str,
    tool_map: dict[str, Any],
) -> ChatResponse:
    """
    Local dev mock: ask Bedrock directly via converse API, execute tool calls,
    and return the final text reply.
    """
    bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)
    tool_calls_log: list[ToolCall] = []

    system_prompt = (
        "You are a helpful ecommerce assistant. "
        "Use the available tools to answer the user's request. "
        f"The current user_id is {user_id}."
    )

    messages = [{"role": "user", "content": [{"text": message}]}]

    tools_spec = [
        {
            "toolSpec": {
                "name": name,
                "description": fn.__doc__ or name,
                "inputSchema": {"json": {"type": "object", "properties": {}}},
            }
        }
        for name, fn in tool_map.items()
    ]

    # Agentic loop — max 5 iterations to prevent runaway calls
    for _ in range(5):
        response = bedrock.converse(
            modelId=BEDROCK_MODEL_ID,
            system=[{"text": system_prompt}],
            messages=messages,
            toolConfig={"tools": tools_spec},
        )

        stop_reason = response["stopReason"]
        assistant_content = response["output"]["message"]["content"]
        messages.append({"role": "assistant", "content": assistant_content})

        if stop_reason == "end_turn":
            # Extract final text
            reply = next(
                (block["text"] for block in assistant_content if "text" in block),
                "Done.",
            )
            return ChatResponse(
                reply=reply,
                session_id=session_id,
                tool_calls=tool_calls_log or None,
            )

        if stop_reason == "tool_use":
            tool_results = []
            for block in assistant_content:
                if "toolUse" not in block:
                    continue
                tool_use = block["toolUse"]
                tool_name = tool_use["name"]
                tool_input = tool_use.get("input", {})
                tool_id = tool_use["toolUseId"]

                try:
                    fn = tool_map.get(tool_name)
                    if fn is None:
                        raise ValueError(f"Unknown tool: {tool_name}")
                    # Inject user_id for tools that need it
                    if "user_id" in fn.__code__.co_varnames:
                        tool_input["user_id"] = user_id
                    result = await fn(**tool_input)
                    tool_calls_log.append(
                        ToolCall(name=tool_name, input=tool_input, output=result)
                    )
                    tool_results.append(
                        {
                            "toolResult": {
                                "toolUseId": tool_id,
                                "content": [{"text": json.dumps(result)}],
                            }
                        }
                    )
                except Exception as exc:
                    logger.warning("Tool %s failed: %s", tool_name, exc)
                    tool_results.append(
                        {
                            "toolResult": {
                                "toolUseId": tool_id,
                                "content": [{"text": f"Error: {exc}"}],
                                "status": "error",
                            }
                        }
                    )

            messages.append({"role": "user", "content": tool_results})

    return ChatResponse(
        reply="I was unable to complete your request. Please try again.",
        session_id=session_id,
        tool_calls=tool_calls_log or None,
    )


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    user_id: str = Depends(_get_user_id),
) -> ChatResponse:
    """POST /agent/chat — Shopping Assistant."""
    session_id = body.session_id or str(uuid.uuid4())

    if AGENTCORE_RUNTIME_ARN:
        # Real AgentCore Runtime invocation (production path)
        agentcore = boto3.client("bedrock-agentcore-runtime", region_name=AWS_REGION)
        response = agentcore.invoke_agent(
            agentAliasArn=AGENTCORE_RUNTIME_ARN,
            sessionId=session_id,
            inputText=body.message,
            sessionState={
                "sessionAttributes": {"user_id": user_id},
            },
        )
        reply = "".join(
            chunk.get("chunk", {}).get("bytes", b"").decode()
            for chunk in response.get("completion", [])
        )
        return ChatResponse(reply=reply, session_id=session_id)

    # Local dev mock
    return await _invoke_mock(
        message=body.message,
        session_id=session_id,
        user_id=user_id,
        tool_map=SHOPPING_TOOL_MAP,
    )


@router.post("/ops", response_model=ChatResponse)
async def ops_chat(
    body: ChatRequest,
    user_id: str = Depends(_get_user_id),
    _role: str = Depends(_require_admin),
) -> ChatResponse:
    """POST /agent/ops — Ops Agent (admin only)."""
    session_id = body.session_id or str(uuid.uuid4())

    if AGENTCORE_RUNTIME_ARN:
        agentcore = boto3.client("bedrock-agentcore-runtime", region_name=AWS_REGION)
        response = agentcore.invoke_agent(
            agentAliasArn=AGENTCORE_RUNTIME_ARN,
            sessionId=session_id,
            inputText=body.message,
            sessionState={"sessionAttributes": {"user_id": user_id, "role": "admin"}},
        )
        reply = "".join(
            chunk.get("chunk", {}).get("bytes", b"").decode()
            for chunk in response.get("completion", [])
        )
        return ChatResponse(reply=reply, session_id=session_id)

    return await _invoke_mock(
        message=body.message,
        session_id=session_id,
        user_id=user_id,
        tool_map=OPS_TOOL_MAP,
    )


@router.post("/pricing/run", response_model=PricingRunResponse)
async def run_pricing_agent() -> PricingRunResponse:
    """POST /agent/pricing/run — triggered by EventBridge daily at 08:00 UTC."""
    run_id = str(uuid.uuid4())
    suggestions = 0
    restock = 0

    try:
        slow_moving = await pricing.get_slow_moving_products(days_in_stock=30, max_units_sold=5)
        for product in slow_moving:
            await pricing.publish_pricing_suggestion(
                product_id=product["product_id"],
                action="markdown",
                suggested_price=None,
                reason=f"Slow-moving: {product.get('units_sold', 0)} units sold in 30 days",
            )
            suggestions += 1

        restock_items = await pricing.get_restock_recommendations()
        for item in restock_items:
            await pricing.publish_pricing_suggestion(
                product_id=item["product_id"],
                action="restock",
                suggested_price=None,
                reason=f"Below reorder threshold: {item.get('quantity_available', 0)} units available",
            )
            restock += 1

    except Exception as exc:
        logger.error("Pricing agent run %s failed: %s", run_id, exc)

    return PricingRunResponse(
        suggestions_published=suggestions,
        restock_recommendations=restock,
        run_id=run_id,
    )
