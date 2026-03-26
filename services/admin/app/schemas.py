from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from datetime import datetime, date


class DashboardMetrics(BaseModel):
    total_orders: int
    total_users: int
    total_revenue: float
    pending_orders: int
    low_stock_items: int


class AdminOrderOut(BaseModel):
    id: str
    user_id: str
    status: str
    total: float
    created_at: datetime


class PaginatedAdminOrders(BaseModel):
    items: List[AdminOrderOut]
    total: int
    page: int
    limit: int


class AdminUserOut(BaseModel):
    id: str
    email: str
    full_name: str
    role: str
    created_at: datetime


class PaginatedAdminUsers(BaseModel):
    items: List[AdminUserOut]
    total: int
    page: int
    limit: int


class ExportResponse(BaseModel):
    url: str
    expires_at: datetime


class RevenueReport(BaseModel):
    start_date: str
    end_date: str
    total_revenue: float
    order_count: int
    average_order_value: float
    daily_breakdown: List[Dict[str, Any]]
