import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.models import Inventory, Reservation
from app.schemas import StockLevelOut, ReserveStockRequest, ReservationOut, AdjustStockRequest

router = APIRouter(tags=["Inventory"])

SEED_SKUS = [
    "SKU-ELEC-001", "SKU-ELEC-002", "SKU-ELEC-003", "SKU-ELEC-004", "SKU-ELEC-005",
    "SKU-SPRT-001", "SKU-SPRT-002", "SKU-SPRT-003", "SKU-SPRT-004", "SKU-SPRT-005",
    "SKU-CLTH-001", "SKU-CLTH-002", "SKU-CLTH-003", "SKU-CLTH-004", "SKU-CLTH-005",
    "SKU-HOME-001", "SKU-HOME-002", "SKU-HOME-003", "SKU-BOOK-001", "SKU-BOOK-002",
]


async def seed_data(db: AsyncSession):
    result = await db.execute(select(func.count()).select_from(Inventory))
    if result.scalar() > 0:
        return
    import random
    for sku in SEED_SKUS:
        qty = random.randint(5, 100)
        inv = Inventory(
            id=str(uuid.uuid4()),
            product_id=sku,
            quantity_on_hand=qty,
            quantity_reserved=0,
            quantity_available=qty,
            reorder_threshold=10,
            reorder_quantity=50,
        )
        db.add(inv)
    await db.commit()


@router.get("/low-stock", response_model=list[StockLevelOut])
async def list_low_stock(
    threshold: int = Query(10, ge=0),
    db: AsyncSession = Depends(get_db),
):
    await seed_data(db)
    result = await db.execute(
        select(Inventory).where(Inventory.quantity_available <= threshold)
    )
    return result.scalars().all()


@router.get("/{productId}", response_model=StockLevelOut)
async def get_stock(productId: str, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(Inventory).where(Inventory.product_id == productId))
    inv = result.scalar_one_or_none()
    if not inv:
        raise HTTPException(status_code=404, detail="Inventory record not found")
    return inv


@router.post("/reserve", response_model=ReservationOut, status_code=201)
async def reserve_stock(body: ReserveStockRequest, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(Inventory).where(Inventory.product_id == body.product_id))
    inv = result.scalar_one_or_none()
    if not inv:
        raise HTTPException(status_code=404, detail="Inventory record not found")
    if inv.quantity_available < body.quantity:
        raise HTTPException(status_code=409, detail=f"Insufficient stock. Only {inv.quantity_available} units available.")

    inv.quantity_reserved += body.quantity
    inv.quantity_available -= body.quantity
    inv.version += 1
    inv.updated_at = datetime.utcnow()

    reservation = Reservation(
        id=str(uuid.uuid4()),
        product_id=body.product_id,
        order_id=body.order_id,
        quantity=body.quantity,
        status="active",
    )
    db.add(reservation)
    await db.commit()
    await db.refresh(reservation)
    return reservation


@router.delete("/reservations/{reservationId}", status_code=204)
async def release_reservation(reservationId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reservation).where(Reservation.id == reservationId))
    reservation = result.scalar_one_or_none()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if reservation.status == "active":
        inv_result = await db.execute(
            select(Inventory).where(Inventory.product_id == reservation.product_id)
        )
        inv = inv_result.scalar_one_or_none()
        if inv:
            inv.quantity_reserved = max(0, inv.quantity_reserved - reservation.quantity)
            inv.quantity_available = inv.quantity_on_hand - inv.quantity_reserved
            inv.version += 1
            inv.updated_at = datetime.utcnow()
    reservation.status = "released"
    await db.commit()


@router.patch("/{productId}/adjust", response_model=StockLevelOut)
async def adjust_stock(productId: str, body: AdjustStockRequest, db: AsyncSession = Depends(get_db)):
    await seed_data(db)
    result = await db.execute(select(Inventory).where(Inventory.product_id == productId))
    inv = result.scalar_one_or_none()
    if not inv:
        raise HTTPException(status_code=404, detail="Inventory record not found")
    new_qty = inv.quantity_on_hand + body.adjustment
    if new_qty < 0:
        raise HTTPException(status_code=422, detail="Adjustment would result in negative stock")
    inv.quantity_on_hand = new_qty
    inv.quantity_available = max(0, new_qty - inv.quantity_reserved)
    inv.version += 1
    inv.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(inv)
    return inv
