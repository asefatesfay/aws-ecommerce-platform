import uuid
import json
import random
from datetime import datetime
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.models import ProductCatalog, UserEvent
from app.schemas import ProductOut, UserEventRequest

router = APIRouter(tags=["Recommendations"])

SEED_PRODUCTS = [
    ("Wireless Headphones Pro", 149.99, "SKU-ELEC-001"),
    ("Smart Watch Series X", 299.99, "SKU-ELEC-002"),
    ("Bluetooth Speaker", 79.99, "SKU-ELEC-003"),
    ("USB-C Hub 7-in-1", 49.99, "SKU-ELEC-004"),
    ("Mechanical Keyboard", 129.99, "SKU-ELEC-005"),
    ("Running Shoes Pro", 119.99, "SKU-SPRT-001"),
    ("Yoga Mat Premium", 39.99, "SKU-SPRT-002"),
    ("Resistance Bands Set", 24.99, "SKU-SPRT-003"),
    ("Water Bottle 32oz", 29.99, "SKU-SPRT-004"),
    ("Cycling Helmet", 89.99, "SKU-SPRT-005"),
    ("Men's T-Shirt Classic", 29.99, "SKU-CLTH-001"),
    ("Women's Jeans Slim", 59.99, "SKU-CLTH-002"),
    ("Hoodie Pullover", 49.99, "SKU-CLTH-003"),
    ("Sneakers Casual", 79.99, "SKU-CLTH-004"),
    ("Winter Jacket", 149.99, "SKU-CLTH-005"),
    ("Coffee Maker Drip", 69.99, "SKU-HOME-001"),
    ("Air Purifier HEPA", 199.99, "SKU-HOME-002"),
    ("Garden Hose 50ft", 34.99, "SKU-HOME-003"),
    ("Python Programming", 39.99, "SKU-BOOK-001"),
    ("Clean Code", 34.99, "SKU-BOOK-002"),
]


async def seed_data(db: AsyncSession):
    result = await db.execute(select(func.count()).select_from(ProductCatalog))
    if result.scalar() > 0:
        return
    for name, price, sku in SEED_PRODUCTS:
        p = ProductCatalog(
            id=str(uuid.uuid4()),
            name=name, price=price, sku=sku,
            image_url=f"https://cdn.example.com/products/{sku.lower()}.jpg",
        )
        db.add(p)
    await db.commit()


@router.get("/{userId}", response_model=list[ProductOut])
async def get_recommendations(userId: str, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(ProductCatalog))
    all_products = result.scalars().all()
    sample = random.sample(all_products, min(10, len(all_products)))
    return sample


@router.get("/similar/{productId}", response_model=list[ProductOut])
async def get_similar(productId: str, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(ProductCatalog).where(ProductCatalog.id != productId))
    all_products = result.scalars().all()
    sample = random.sample(all_products, min(6, len(all_products)))
    return sample


@router.post("/events", status_code=204)
async def record_event(body: UserEventRequest, db: AsyncSession = Depends(get_db)):
    event = UserEvent(
        id=str(uuid.uuid4()),
        user_id=body.user_id,
        event_type=body.event_type,
        product_id=body.product_id,
        metadata_json=json.dumps(body.metadata or {}),
    )
    db.add(event)
    await db.commit()
    return Response(status_code=204)
