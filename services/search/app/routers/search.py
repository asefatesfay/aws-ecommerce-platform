import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_

from app.database import get_db
from app.models import ProductIndex
from app.schemas import SearchResponse, SearchProductOut, AutocompleteResponse
from app.ai import embed_text, extract_image_attributes, hybrid_search

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

    # Attempt to embed the query for hybrid search (Requirement 18.4)
    embedding = await embed_text(q)  # returns None on failure → keyword-only fallback

    result = await hybrid_search(
        query=q,
        embedding=embedding,
        price_min=priceMin,
        price_max=priceMax,
        in_stock=inStock,
        page=page,
        limit=limit,
        db=db,
    )
    return SearchResponse(items=result["items"], total=result["total"], page=page, limit=limit)


# ---------------------------------------------------------------------------
# Visual Search (Requirements 19.1–19.6)
# ---------------------------------------------------------------------------

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/jpg", "image/png", "image/webp"}
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB


class VisualSearchResponse(BaseModel):
    items: list[SearchProductOut]
    total: int
    page: int
    limit: int
    extracted_attributes: dict


@router.post("/visual", response_model=VisualSearchResponse)
async def visual_search(
    file: UploadFile = File(...),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """
    Visual search — upload a product image (JPEG, PNG, WebP, max 5 MB) and
    receive matching products based on AI-extracted attributes.
    """
    await seed_data(db)

    # Validate content type
    content_type = (file.content_type or "").lower()
    if content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported image format '{content_type}'. Accepted: JPEG, PNG, WebP.",
        )

    # Read and validate size
    image_bytes = await file.read()
    if len(image_bytes) > MAX_IMAGE_SIZE_BYTES:
        raise HTTPException(status_code=422, detail="Image exceeds the 5 MB size limit.")

    # Extract product attributes via Claude Vision
    try:
        attributes = await extract_image_attributes(image_bytes, content_type)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    # Build a natural-language query from the extracted attributes
    query_parts = [v for v in attributes.values() if isinstance(v, str) and v]
    query_text = " ".join(query_parts) if query_parts else "product"

    # Embed the query for hybrid search
    embedding = await embed_text(query_text)

    result = await hybrid_search(
        query=query_text,
        embedding=embedding,
        price_min=None,
        price_max=None,
        in_stock=None,
        page=page,
        limit=limit,
        db=db,
    )

    return VisualSearchResponse(
        items=result["items"],
        total=result["total"],
        page=page,
        limit=limit,
        extracted_attributes=attributes,
    )


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
