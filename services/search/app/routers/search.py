import uuid
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_

from app.database import get_db
from app.models import ProductIndex
from app.schemas import SearchResponse, SearchProductOut, AutocompleteResponse

router = APIRouter(tags=["Search"])

SEED_PRODUCTS = [
    ("Wireless Headphones Pro", "Premium wireless headphones with ANC", 149.99, "Sony", "Electronics", "SKU-ELEC-001"),
    ("Smart Watch Series X", "Advanced smartwatch with health tracking", 299.99, "Apple", "Electronics", "SKU-ELEC-002"),
    ("Bluetooth Speaker", "Portable waterproof speaker", 79.99, "JBL", "Electronics", "SKU-ELEC-003"),
    ("USB-C Hub 7-in-1", "Multi-port USB-C hub", 49.99, "Anker", "Electronics", "SKU-ELEC-004"),
    ("Mechanical Keyboard", "Compact mechanical keyboard", 129.99, "Keychron", "Electronics", "SKU-ELEC-005"),
    ("Running Shoes Pro", "Lightweight running shoes", 119.99, "Nike", "Sports", "SKU-SPRT-001"),
    ("Yoga Mat Premium", "Non-slip yoga mat", 39.99, "Lululemon", "Sports", "SKU-SPRT-002"),
    ("Resistance Bands Set", "Set of 5 resistance bands", 24.99, "TheraBand", "Sports", "SKU-SPRT-003"),
    ("Water Bottle 32oz", "Insulated stainless steel bottle", 29.99, "Hydro Flask", "Sports", "SKU-SPRT-004"),
    ("Cycling Helmet", "Lightweight road cycling helmet", 89.99, "Giro", "Sports", "SKU-SPRT-005"),
    ("Men's T-Shirt Classic", "100% cotton classic fit", 29.99, "Hanes", "Clothing", "SKU-CLTH-001"),
    ("Women's Jeans Slim", "Slim fit stretch denim", 59.99, "Levi's", "Clothing", "SKU-CLTH-002"),
    ("Hoodie Pullover", "Fleece pullover hoodie", 49.99, "Champion", "Clothing", "SKU-CLTH-003"),
    ("Sneakers Casual", "Everyday casual sneakers", 79.99, "Adidas", "Clothing", "SKU-CLTH-004"),
    ("Winter Jacket", "Insulated winter jacket", 149.99, "North Face", "Clothing", "SKU-CLTH-005"),
    ("Coffee Maker Drip", "12-cup programmable coffee maker", 69.99, "Cuisinart", "Home", "SKU-HOME-001"),
    ("Air Purifier HEPA", "True HEPA air purifier", 199.99, "Dyson", "Home", "SKU-HOME-002"),
    ("Garden Hose 50ft", "Flexible garden hose", 34.99, "Flexzilla", "Home", "SKU-HOME-003"),
    ("Python Programming", "Learn Python the hard way", 39.99, "O'Reilly", "Books", "SKU-BOOK-001"),
    ("Clean Code", "A handbook of agile software craftsmanship", 34.99, "Prentice Hall", "Books", "SKU-BOOK-002"),
]


async def seed_data(db: AsyncSession):
    result = await db.execute(select(func.count()).select_from(ProductIndex))
    if result.scalar() > 0:
        return
    for name, desc, price, brand, category, sku in SEED_PRODUCTS:
        p = ProductIndex(
            id=str(uuid.uuid4()),
            name=name, description=desc, price=price,
            brand=brand, category=category, in_stock=True, sku=sku,
            image_url=f"https://cdn.example.com/products/{sku.lower()}.jpg",
        )
        db.add(p)
    await db.commit()


@router.get("", response_model=SearchResponse)
async def search_products(
    q: str = Query(..., max_length=500),
    priceMin: Optional[float] = Query(None, ge=0),
    priceMax: Optional[float] = Query(None),
    inStock: Optional[bool] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    await seed_data(db)
    query = select(ProductIndex).where(
        or_(
            ProductIndex.name.ilike(f"%{q}%"),
            ProductIndex.description.ilike(f"%{q}%"),
            ProductIndex.brand.ilike(f"%{q}%"),
            ProductIndex.category.ilike(f"%{q}%"),
        )
    )
    if priceMin is not None:
        query = query.where(ProductIndex.price >= priceMin)
    if priceMax is not None:
        query = query.where(ProductIndex.price <= priceMax)
    if inStock is not None:
        query = query.where(ProductIndex.in_stock == inStock)

    total_result = await db.execute(select(func.count()).select_from(query.subquery()))
    total = total_result.scalar()
    result = await db.execute(query.offset((page - 1) * limit).limit(limit))
    products = result.scalars().all()
    return SearchResponse(items=products, total=total, page=page, limit=limit)


@router.get("/autocomplete", response_model=AutocompleteResponse)
async def autocomplete(
    q: str = Query(..., min_length=1),
    db: AsyncSession = Depends(get_db),
):
    await seed_data(db)
    result = await db.execute(
        select(ProductIndex.name).where(ProductIndex.name.ilike(f"{q}%")).limit(10)
    )
    names = [row[0] for row in result.fetchall()]
    return AutocompleteResponse(suggestions=names)
