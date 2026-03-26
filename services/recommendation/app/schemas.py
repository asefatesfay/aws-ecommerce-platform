from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class ProductOut(BaseModel):
    id: str
    name: str
    price: float
    image_url: Optional[str] = None
    sku: str

    model_config = {"from_attributes": True}


class UserEventRequest(BaseModel):
    user_id: str
    event_type: str
    product_id: str
    metadata: Optional[Dict[str, Any]] = None
