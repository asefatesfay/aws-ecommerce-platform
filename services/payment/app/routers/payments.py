import uuid
from datetime import datetime
from typing import Any, Dict, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Payment
from app.schemas import PaymentIntentRequest, PaymentIntentResponse, PaymentOut, RefundRequest, RefundOut

router = APIRouter(tags=["Payments"])


def _fake_pi_id() -> str:
    return f"pi_{uuid.uuid4().hex[:24]}"


def _fake_client_secret(pi_id: str) -> str:
    return f"{pi_id}_secret_{uuid.uuid4().hex[:16]}"


@router.post("/intent", status_code=201, response_model=PaymentIntentResponse)
async def create_payment_intent(body: PaymentIntentRequest, db: AsyncSession = Depends(get_db)):
    pi_id = _fake_pi_id()
    client_secret = _fake_client_secret(pi_id)
    payment = Payment(
        id=str(uuid.uuid4()),
        order_id=body.order_id,
        stripe_payment_intent_id=pi_id,
        amount=body.amount,
        currency=body.currency,
        status="pending",
        client_secret=client_secret,
        metadata_json=f'{{"order_id": "{body.order_id}"}}',
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return PaymentIntentResponse(
        payment_id=payment.id,
        stripe_payment_intent_id=pi_id,
        client_secret=client_secret,
        amount=body.amount,
        currency=body.currency,
        status="pending",
    )


@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    stripe_signature: Optional[str] = Header(None, alias="Stripe-Signature"),
    db: AsyncSession = Depends(get_db),
):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid payload")

    event_type = payload.get("type", "")
    data_obj = payload.get("data", {}).get("object", {})
    pi_id = data_obj.get("id")

    if pi_id:
        result = await db.execute(select(Payment).where(Payment.stripe_payment_intent_id == pi_id))
        payment = result.scalar_one_or_none()
        if payment:
            if event_type == "payment_intent.succeeded":
                payment.status = "succeeded"
                payment.stripe_charge_id = f"ch_{uuid.uuid4().hex[:24]}"
            elif event_type == "payment_intent.payment_failed":
                payment.status = "failed"
            payment.updated_at = datetime.utcnow()
            await db.commit()

    return {"received": True}


@router.get("/{paymentId}", response_model=PaymentOut)
async def get_payment(paymentId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Payment).where(Payment.id == paymentId))
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@router.post("/{paymentId}/refund", response_model=RefundOut)
async def refund_payment(paymentId: str, body: RefundRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Payment).where(Payment.id == paymentId))
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    if payment.status not in ("succeeded",):
        raise HTTPException(status_code=422, detail="Payment is not refundable in its current state")

    refund_amount = body.amount if body.amount else payment.amount
    if refund_amount > payment.amount:
        raise HTTPException(status_code=422, detail="Refund amount exceeds original payment")

    payment.refunded_amount += refund_amount
    if payment.refunded_amount >= payment.amount:
        payment.status = "refunded"
    else:
        payment.status = "partially_refunded"
    payment.updated_at = datetime.utcnow()
    await db.commit()

    return RefundOut(
        id=str(uuid.uuid4()),
        payment_id=paymentId,
        amount=refund_amount,
        reason=body.reason,
        status="succeeded",
        created_at=datetime.utcnow(),
    )
