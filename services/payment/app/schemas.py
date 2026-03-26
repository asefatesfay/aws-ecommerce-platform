from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class PaymentIntentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str = "usd"


class PaymentIntentResponse(BaseModel):
    payment_id: str
    stripe_payment_intent_id: str
    client_secret: str
    amount: float
    currency: str
    status: str


class PaymentOut(BaseModel):
    id: str
    order_id: str
    stripe_payment_intent_id: str
    amount: float
    currency: str
    status: str
    stripe_charge_id: Optional[str] = None
    refunded_amount: float
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class RefundRequest(BaseModel):
    amount: Optional[float] = None
    reason: Optional[str] = None


class RefundOut(BaseModel):
    id: str
    payment_id: str
    amount: float
    reason: Optional[str] = None
    status: str
    created_at: datetime
