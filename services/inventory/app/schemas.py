from pydantic import BaseModel
from typing import List
from datetime import datetime


class StockLevelOut(BaseModel):
    id: str
    product_id: str
    quantity_on_hand: int
    quantity_reserved: int
    quantity_available: int
    reorder_threshold: int
    reorder_quantity: int
    updated_at: datetime

    model_config = {"from_attributes": True}


class ReserveStockRequest(BaseModel):
    product_id: str
    quantity: int
    order_id: str


class ReservationOut(BaseModel):
    id: str
    product_id: str
    order_id: str
    quantity: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}


class AdjustStockRequest(BaseModel):
    adjustment: int
    reason: str = ""
