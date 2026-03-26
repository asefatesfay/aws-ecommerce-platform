from pydantic import BaseModel
from typing import Optional, List


class SearchProductOut(BaseModel):
    id: str
    name: str
    description: str
    price: float
    brand: Optional[str] = None
    category: Optional[str] = None
    in_stock: bool
    sku: str
    image_url: Optional[str] = None

    model_config = {"from_attributes": True}


class SearchResponse(BaseModel):
    items: List[SearchProductOut]
    total: int
    page: int
    limit: int


class AutocompleteResponse(BaseModel):
    suggestions: List[str]
