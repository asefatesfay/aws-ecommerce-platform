from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from datetime import datetime


class OrderItemIn(BaseModel):
    product_id: str
    sku: str
    name: str
    unit_price: float
    quantity: int


class ShippingAddress(BaseModel):
    street: str
    city: str
    state: Optional[str] = None
    country: str
    postal_code: str


class CreateOrderRequest(BaseModel):
    items: List[OrderItemIn]
    shipping_address: ShippingAddress
    notes: Optional[str] = None


class UpdateStatusRequest(BaseModel):
    status: str


class OrderItemOut(BaseModel):
    id: str
    product_id: str
    sku: str
    name: str
    unit_price: float
    quantity: int
    subtotal: float

    model_config = {"from_attributes": True}


class OrderOut(BaseModel):
    id: str
    user_id: str
    status: str
    items: List[OrderItemOut] = []
    subtotal: float
    tax: float
    shipping_cost: float
    total: float
    shipping_address: Dict[str, Any]
    payment_id: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PaginatedOrders(BaseModel):
    items: List[OrderOut]
    total: int
    page: int
    limit: int
