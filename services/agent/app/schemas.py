from pydantic import BaseModel
from typing import Any


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class ToolCall(BaseModel):
    name: str
    input: dict[str, Any]
    output: Any


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    tool_calls: list[ToolCall] | None = None


class PricingRunResponse(BaseModel):
    suggestions_published: int
    restock_recommendations: int
    run_id: str
