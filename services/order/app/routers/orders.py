import uuid
import json
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import Order, OrderItem
from app.schemas import CreateOrderRequest, UpdateStatusRequest, OrderOut, OrderItemOut, PaginatedOrders
from app.fraud import score_order

router = APIRouter(tags=["Orders"])

ORDER_STATE_MACHINE = {
    "pending":    ["confirmed", "cancelled"],
    "confirmed":  ["processing", "cancelled"],
    "processing": ["shipped", "cancelled"],
    "shipped":    ["delivered"],
    "delivered":  ["refunded"],
    "cancelled":  [],
    "refunded":   [],
}

TAX_RATE = 0.08
SHIPPING_COST = 9.99


def _order_to_out(order: Order) -> OrderOut:
    items = [
        OrderItemOut(
            id=i.id, product_id=i.product_id, sku=i.sku,
            name=i.name, unit_price=i.unit_price, quantity=i.quantity, subtotal=i.subtotal,
        )
        for i in order.items
    ]
    return OrderOut(
        id=order.id, user_id=order.user_id, status=order.status,
        items=items, subtotal=order.subtotal, tax=order.tax,
        shipping_cost=order.shipping_cost, total=order.total,
        shipping_address=json.loads(order.shipping_address),
        payment_id=order.payment_id, notes=order.notes,
        created_at=order.created_at, updated_at=order.updated_at,
    )


@router.post("", status_code=201, response_model=OrderOut)
async def create_order(
    body: CreateOrderRequest,
    x_user_id: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db),
):
    user_id = x_user_id or str(uuid.uuid4())
    subtotal = sum(i.unit_price * i.quantity for i in body.items)
    tax = round(subtotal * TAX_RATE, 2)
    total = round(subtotal + tax + SHIPPING_COST, 2)

    # --- Fraud detection (Requirement 21) ---
    order_data = {
        "total": total,
        "items": [i.model_dump() for i in body.items],
        "shipping_address": body.shipping_address.model_dump(),
        "billing_address": body.shipping_address.model_dump(),  # use shipping as billing if not provided
        "shipping_method": getattr(body, "shipping_method", "standard"),
    }
    user_data = {
        "created_at": None,  # unknown without auth service call; treated as new account
        "recent_order_count": 0,
    }
    fraud_result = await score_order(order_data, user_data)
    fraud_score = fraud_result["score"]
    fraud_signals = fraud_result["signals"]
    recommendation = fraud_result["recommendation"]

    if recommendation == "block":
        raise HTTPException(
            status_code=422,
            detail="Order flagged for review",
        )

    order_status = "under_review" if recommendation == "review" else "pending"
    # -----------------------------------------

    order = Order(
        id=str(uuid.uuid4()),
        user_id=user_id,
        status=order_status,
        subtotal=round(subtotal, 2),
        tax=tax,
        shipping_cost=SHIPPING_COST,
        total=total,
        shipping_address=json.dumps(body.shipping_address.model_dump()),
        notes=body.notes,
        fraud_score=fraud_score,
        fraud_signals=fraud_signals,
    )
    db.add(order)
    await db.flush()

    for item_in in body.items:
        item = OrderItem(
            id=str(uuid.uuid4()),
            order_id=order.id,
            product_id=item_in.product_id,
            sku=item_in.sku,
            name=item_in.name,
            unit_price=item_in.unit_price,
            quantity=item_in.quantity,
            subtotal=round(item_in.unit_price * item_in.quantity, 2),
        )
        db.add(item)

    await db.commit()
    result = await db.execute(
        select(Order).where(Order.id == order.id).options(selectinload(Order.items))
    )
    order = result.scalar_one()
    return _order_to_out(order)


@router.get("", response_model=PaginatedOrders)
async def list_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    x_user_id: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db),
):
    if not x_user_id:
        raise HTTPException(status_code=401, detail="X-User-Id header required")
    q = select(Order).where(Order.user_id == x_user_id)
    total_result = await db.execute(select(func.count()).select_from(q.subquery()))
    total = total_result.scalar()
    result = await db.execute(
        q.options(selectinload(Order.items)).offset((page - 1) * limit).limit(limit)
    )
    orders = result.scalars().all()
    return PaginatedOrders(items=[_order_to_out(o) for o in orders], total=total, page=page, limit=limit)


@router.get("/{orderId}", response_model=OrderOut)
async def get_order(orderId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(Order.id == orderId).options(selectinload(Order.items))
    )
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return _order_to_out(order)


@router.patch("/{orderId}/status", response_model=OrderOut)
async def update_order_status(orderId: str, body: UpdateStatusRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(Order.id == orderId).options(selectinload(Order.items))
    )
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    allowed = ORDER_STATE_MACHINE.get(order.status, [])
    if body.status not in allowed:
        raise HTTPException(
            status_code=422,
            detail=f"Cannot transition from '{order.status}' to '{body.status}'."
        )
    order.status = body.status
    order.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(order)
    result = await db.execute(
        select(Order).where(Order.id == orderId).options(selectinload(Order.items))
    )
    order = result.scalar_one()
    return _order_to_out(order)


@router.post("/{orderId}/cancel", response_model=OrderOut)
async def cancel_order(orderId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Order).where(Order.id == orderId).options(selectinload(Order.items))
    )
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if "cancelled" not in ORDER_STATE_MACHINE.get(order.status, []):
        raise HTTPException(
            status_code=422,
            detail=f"Cannot cancel an order with status '{order.status}'."
        )
    order.status = "cancelled"
    order.updated_at = datetime.utcnow()
    await db.commit()
    result = await db.execute(
        select(Order).where(Order.id == orderId).options(selectinload(Order.items))
    )
    order = result.scalar_one()
    return _order_to_out(order)
