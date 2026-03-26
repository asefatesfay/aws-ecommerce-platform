from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CartItemOut(BaseModel):
    id: str
    product_id: str
    sku: str
    name: str
    unit_price: float
    quantity: int
    image_url: Optional[str] = None
    subtotal: float = 0.0

    model_config = {"from_attributes": True}


class CartOut(BaseModel):
    id: str
    user_id: str
    items: List[CartItemOut] = []
    total: float = 0.0
    updated_at: datetime

    model_config = {"from_attributes": True}


class AddItemRequest(BaseModel):
    product_id: str
    sku: str
    name: str
    unit_price: float
    quantity: int
    image_url: Optional[str] = None


class UpdateItemRequest(BaseModel):
    quantity: int
