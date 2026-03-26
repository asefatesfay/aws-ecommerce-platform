from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CategoryOut(BaseModel):
    id: str
    name: str
    slug: str
    description: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ProductOut(BaseModel):
    id: str
    sku: str
    name: str
    description: str
    price: float
    compare_at_price: Optional[float] = None
    category_id: str
    brand: Optional[str] = None
    images: List[str] = []
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class CreateProductRequest(BaseModel):
    sku: str
    name: str
    description: str
    price: float
    compare_at_price: Optional[float] = None
    category_id: str
    brand: Optional[str] = None
    images: Optional[List[str]] = []
    is_active: bool = True


class UpdateProductRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    compare_at_price: Optional[float] = None
    category_id: Optional[str] = None
    brand: Optional[str] = None
    images: Optional[List[str]] = None
    is_active: Optional[bool] = None


class ImageUploadResponse(BaseModel):
    url: str
    product_id: str


class PaginatedProducts(BaseModel):
    items: List[ProductOut]
    total: int
    page: int
    limit: int
