import uuid
import json
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.models import Product, Category
from app.schemas import (
    ProductOut, CategoryOut, CreateProductRequest, UpdateProductRequest,
    ImageUploadResponse, PaginatedProducts
)
from app.ai import generate_product_description

router = APIRouter(tags=["Catalog"])

SEED_CATEGORIES = [
    {"name": "Electronics", "slug": "electronics", "description": "Gadgets and devices"},
    {"name": "Clothing", "slug": "clothing", "description": "Apparel and accessories"},
    {"name": "Sports", "slug": "sports", "description": "Sports and outdoor gear"},
    {"name": "Home & Garden", "slug": "home-garden", "description": "Home improvement and garden"},
    {"name": "Books", "slug": "books", "description": "Books and media"},
]

SEED_PRODUCTS = [
    ("Wireless Headphones Pro", "electronics", "SKU-ELEC-001", 149.99, "Sony", "Premium wireless headphones with ANC"),
    ("Smart Watch Series X", "electronics", "SKU-ELEC-002", 299.99, "Apple", "Advanced smartwatch with health tracking"),
    ("Bluetooth Speaker", "electronics", "SKU-ELEC-003", 79.99, "JBL", "Portable waterproof speaker"),
    ("USB-C Hub 7-in-1", "electronics", "SKU-ELEC-004", 49.99, "Anker", "Multi-port USB-C hub"),
    ("Mechanical Keyboard", "electronics", "SKU-ELEC-005", 129.99, "Keychron", "Compact mechanical keyboard"),
    ("Running Shoes Pro", "sports", "SKU-SPRT-001", 119.99, "Nike", "Lightweight running shoes"),
    ("Yoga Mat Premium", "sports", "SKU-SPRT-002", 39.99, "Lululemon", "Non-slip yoga mat"),
    ("Resistance Bands Set", "sports", "SKU-SPRT-003", 24.99, "TheraBand", "Set of 5 resistance bands"),
    ("Water Bottle 32oz", "sports", "SKU-SPRT-004", 29.99, "Hydro Flask", "Insulated stainless steel bottle"),
    ("Cycling Helmet", "sports", "SKU-SPRT-005", 89.99, "Giro", "Lightweight road cycling helmet"),
    ("Men's T-Shirt Classic", "clothing", "SKU-CLTH-001", 29.99, "Hanes", "100% cotton classic fit"),
    ("Women's Jeans Slim", "clothing", "SKU-CLTH-002", 59.99, "Levi's", "Slim fit stretch denim"),
    ("Hoodie Pullover", "clothing", "SKU-CLTH-003", 49.99, "Champion", "Fleece pullover hoodie"),
    ("Sneakers Casual", "clothing", "SKU-CLTH-004", 79.99, "Adidas", "Everyday casual sneakers"),
    ("Winter Jacket", "clothing", "SKU-CLTH-005", 149.99, "North Face", "Insulated winter jacket"),
    ("Coffee Maker Drip", "home-garden", "SKU-HOME-001", 69.99, "Cuisinart", "12-cup programmable coffee maker"),
    ("Air Purifier HEPA", "home-garden", "SKU-HOME-002", 199.99, "Dyson", "True HEPA air purifier"),
    ("Garden Hose 50ft", "home-garden", "SKU-HOME-003", 34.99, "Flexzilla", "Flexible garden hose"),
    ("Python Programming", "books", "SKU-BOOK-001", 39.99, "O'Reilly", "Learn Python the hard way"),
    ("Clean Code", "books", "SKU-BOOK-002", 34.99, "Prentice Hall", "A handbook of agile software craftsmanship"),
]


def _product_to_out(p: Product) -> ProductOut:
    images = json.loads(p.images) if p.images else []
    return ProductOut(
        id=p.id, sku=p.sku, name=p.name, description=p.description,
        price=p.price, compare_at_price=p.compare_at_price,
        category_id=p.category_id, brand=p.brand, images=images,
        is_active=p.is_active, created_at=p.created_at, updated_at=p.updated_at,
    )


async def seed_data(db: AsyncSession):
    result = await db.execute(select(func.count()).select_from(Category))
    if result.scalar() > 0:
        return

    cat_map = {}
    for c in SEED_CATEGORIES:
        cat = Category(id=str(uuid.uuid4()), **c)
        db.add(cat)
        cat_map[c["slug"]] = cat.id
    await db.flush()

    for name, cat_slug, sku, price, brand, desc in SEED_PRODUCTS:
        p = Product(
            id=str(uuid.uuid4()),
            sku=sku, name=name, description=desc, price=price,
            compare_at_price=round(price * 1.2, 2),
            category_id=cat_map[cat_slug],
            brand=brand,
            images=json.dumps([f"https://cdn.example.com/products/{sku.lower()}.jpg"]),
            is_active=True,
        )
        db.add(p)
    await db.commit()


@router.get("/products", response_model=PaginatedProducts)
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    categoryId: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    await seed_data(db)
    q = select(Product).where(Product.is_active == True)
    if categoryId:
        q = q.where(Product.category_id == categoryId)
    total_result = await db.execute(select(func.count()).select_from(q.subquery()))
    total = total_result.scalar()
    result = await db.execute(q.offset((page - 1) * limit).limit(limit))
    products = result.scalars().all()
    return PaginatedProducts(items=[_product_to_out(p) for p in products], total=total, page=page, limit=limit)


@router.get("/products/{productId}", response_model=ProductOut)
async def get_product(productId: str, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return _product_to_out(product)


@router.post("/products", status_code=201, response_model=ProductOut)
async def create_product(body: CreateProductRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.sku == body.sku))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="A product with this SKU already exists.")
    product = Product(
        id=str(uuid.uuid4()),
        sku=body.sku, name=body.name, description=body.description,
        price=body.price, compare_at_price=body.compare_at_price,
        category_id=body.category_id, brand=body.brand,
        images=json.dumps(body.images or []),
        is_active=body.is_active,
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return _product_to_out(product)


@router.put("/products/{productId}", response_model=ProductOut)
async def update_product(productId: str, body: UpdateProductRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in body.model_dump(exclude_none=True).items():
        if field == "images":
            setattr(product, field, json.dumps(value))
        else:
            setattr(product, field, value)
    product.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(product)
    return _product_to_out(product)


@router.delete("/products/{productId}", status_code=204)
async def delete_product(productId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await db.delete(product)
    await db.commit()


@router.post("/products/{productId}/images", status_code=201, response_model=ImageUploadResponse)
async def upload_image(productId: str, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    fake_url = f"https://d1234abcd.cloudfront.net/products/{productId}/{uuid.uuid4().hex}.jpg"
    images = json.loads(product.images) if product.images else []
    images.append(fake_url)
    product.images = json.dumps(images)
    await db.commit()
    return ImageUploadResponse(url=fake_url, product_id=productId)


@router.get("/categories", response_model=list[CategoryOut])
async def list_categories(db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(Category))
    return result.scalars().all()


# ---------------------------------------------------------------------------
# AI Product Description Generator (Requirements 20.1–20.6)
# ---------------------------------------------------------------------------

class GeneratedDescriptionResponse(BaseModel):
    product_id: str
    title: str
    description: str
    bullets: list[str]


class ApplyDescriptionRequest(BaseModel):
    title: str
    description: str


@router.post("/products/{productId}/generate-description", response_model=GeneratedDescriptionResponse)
async def generate_description(productId: str, db: AsyncSession = Depends(get_db)):
    """
    Generate an AI-powered SEO-optimized title, description, and bullet points
    for a product using Claude 3.5 Sonnet via Amazon Bedrock.

    The product is NOT updated automatically — the generated content is returned
    for admin review. Call /apply-description to persist the changes.
    """
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Resolve category name for the prompt
    category_name = ""
    if product.category_id:
        cat_result = await db.execute(select(Category).where(Category.id == product.category_id))
        cat = cat_result.scalar_one_or_none()
        if cat:
            category_name = cat.name

    product_dict = {
        "name": product.name,
        "sku": product.sku,
        "category": category_name,
        "brand": product.brand or "",
        "attributes": {},  # attributes stored as JSON string in this model
    }

    try:
        generated = await generate_product_description(product_dict)
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=f"AI generation failed: {exc}")

    return GeneratedDescriptionResponse(
        product_id=productId,
        title=generated["title"],
        description=generated["description"],
        bullets=generated["bullets"],
    )


@router.post("/products/{productId}/apply-description", response_model=ProductOut)
async def apply_description(
    productId: str,
    body: ApplyDescriptionRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Apply a previously generated description to the product record in Aurora.
    Updates the product name (title) and description fields.
    """
    result = await db.execute(select(Product).where(Product.id == productId))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = body.title
    product.description = body.description
    product.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(product)
    return _product_to_out(product)
