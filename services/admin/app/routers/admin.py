import uuid
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas import (
    DashboardMetrics, AdminOrderOut, PaginatedAdminOrders,
    AdminUserOut, PaginatedAdminUsers, ExportResponse, RevenueReport
)

router = APIRouter(tags=["Admin"])

# Mock data
MOCK_ORDERS = [
    {"id": str(uuid.uuid4()), "user_id": str(uuid.uuid4()), "status": s, "total": t,
     "created_at": datetime.utcnow() - timedelta(days=i)}
    for i, (s, t) in enumerate([
        ("delivered", 249.98), ("pending", 89.99), ("confirmed", 179.97),
        ("processing", 59.99), ("shipped", 319.95), ("cancelled", 49.99),
        ("delivered", 129.99), ("delivered", 399.97), ("pending", 74.99),
        ("confirmed", 219.98),
    ])
]

MOCK_USERS = [
    {"id": str(uuid.uuid4()), "email": f"user{i}@example.com", "full_name": f"User {i}",
     "role": "admin" if i == 1 else "customer", "created_at": datetime.utcnow() - timedelta(days=i * 3)}
    for i in range(1, 11)
]


def _require_admin(x_user_role: Optional[str] = Header(None)):
    if x_user_role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")


@router.get("/metrics", response_model=DashboardMetrics)
async def get_metrics(_: None = Depends(_require_admin)):
    total_revenue = sum(o["total"] for o in MOCK_ORDERS if o["status"] == "delivered")
    pending = sum(1 for o in MOCK_ORDERS if o["status"] == "pending")
    return DashboardMetrics(
        total_orders=len(MOCK_ORDERS),
        total_users=len(MOCK_USERS),
        total_revenue=round(total_revenue, 2),
        pending_orders=pending,
        low_stock_items=3,
    )


@router.get("/orders", response_model=PaginatedAdminOrders)
async def list_all_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    _: None = Depends(_require_admin),
):
    total = len(MOCK_ORDERS)
    start = (page - 1) * limit
    end = start + limit
    items = [AdminOrderOut(**o) for o in MOCK_ORDERS[start:end]]
    return PaginatedAdminOrders(items=items, total=total, page=page, limit=limit)


@router.post("/orders/export", response_model=ExportResponse)
async def export_orders(_: None = Depends(_require_admin)):
    fake_key = uuid.uuid4().hex
    return ExportResponse(
        url=f"https://s3.amazonaws.com/exports/orders-{fake_key}.csv?X-Amz-Expires=3600",
        expires_at=datetime.utcnow() + timedelta(hours=1),
    )


@router.get("/users", response_model=PaginatedAdminUsers)
async def list_users(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    _: None = Depends(_require_admin),
):
    total = len(MOCK_USERS)
    start = (page - 1) * limit
    end = start + limit
    items = [AdminUserOut(**u) for u in MOCK_USERS[start:end]]
    return PaginatedAdminUsers(items=items, total=total, page=page, limit=limit)


@router.get("/revenue", response_model=RevenueReport)
async def get_revenue(
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    _: None = Depends(_require_admin),
):
    delivered = [o for o in MOCK_ORDERS if o["status"] == "delivered"]
    total_revenue = sum(o["total"] for o in delivered)
    order_count = len(delivered)
    avg = round(total_revenue / order_count, 2) if order_count else 0.0

    # Generate daily breakdown for last 7 days
    daily = []
    for i in range(7):
        day = (datetime.utcnow() - timedelta(days=i)).strftime("%Y-%m-%d")
        daily.append({"date": day, "revenue": round(total_revenue / 7, 2), "orders": max(1, order_count // 7)})

    return RevenueReport(
        start_date=start_date or (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d"),
        end_date=end_date or datetime.utcnow().strftime("%Y-%m-%d"),
        total_revenue=round(total_revenue, 2),
        order_count=order_count,
        average_order_value=avg,
        daily_breakdown=daily,
    )
