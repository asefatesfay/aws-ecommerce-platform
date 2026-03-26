import uuid
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Cart, CartItem
from app.schemas import CartOut, CartItemOut, AddItemRequest, UpdateItemRequest

router = APIRouter(tags=["Cart"])


def _cart_to_out(cart: Cart) -> CartOut:
    items = []
    total = 0.0
    for item in cart.items:
        subtotal = round(item.unit_price * item.quantity, 2)
        total += subtotal
        items.append(CartItemOut(
            id=item.id, product_id=item.product_id, sku=item.sku,
            name=item.name, unit_price=item.unit_price, quantity=item.quantity,
            image_url=item.image_url, subtotal=subtotal,
        ))
    return CartOut(id=cart.id, user_id=cart.user_id, items=items, total=round(total, 2), updated_at=cart.updated_at)


async def _get_or_create_cart(user_id: str, db: AsyncSession) -> Cart:
    result = await db.execute(select(Cart).where(Cart.user_id == user_id))
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(id=str(uuid.uuid4()), user_id=user_id)
        db.add(cart)
        await db.flush()
    return cart


@router.get("/{userId}", response_model=CartOut)
async def get_cart(userId: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId)
    )
    cart = result.scalar_one_or_none()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    # Eagerly load items
    from sqlalchemy.orm import selectinload
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one_or_none()
    return _cart_to_out(cart)


@router.post("/{userId}/items", response_model=CartOut)
async def add_item(userId: str, body: AddItemRequest, db: AsyncSession = Depends(get_db)):
    from sqlalchemy.orm import selectinload
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(id=str(uuid.uuid4()), user_id=userId)
        db.add(cart)
        await db.flush()

    # Check if product already in cart
    existing = next((i for i in cart.items if i.product_id == body.product_id), None)
    if existing:
        existing.quantity += body.quantity
    else:
        item = CartItem(
            id=str(uuid.uuid4()),
            cart_id=cart.id,
            product_id=body.product_id,
            sku=body.sku,
            name=body.name,
            unit_price=body.unit_price,
            quantity=body.quantity,
            image_url=body.image_url,
        )
        db.add(item)
        cart.items.append(item)

    cart.updated_at = datetime.utcnow()
    await db.commit()
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one()
    return _cart_to_out(cart)


@router.put("/{userId}/items/{itemId}", response_model=CartOut)
async def update_item(userId: str, itemId: str, body: UpdateItemRequest, db: AsyncSession = Depends(get_db)):
    from sqlalchemy.orm import selectinload
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one_or_none()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    item = next((i for i in cart.items if i.id == itemId), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if body.quantity <= 0:
        await db.delete(item)
    else:
        item.quantity = body.quantity
    cart.updated_at = datetime.utcnow()
    await db.commit()
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one()
    return _cart_to_out(cart)


@router.delete("/{userId}/items/{itemId}", response_model=CartOut)
async def remove_item(userId: str, itemId: str, db: AsyncSession = Depends(get_db)):
    from sqlalchemy.orm import selectinload
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one_or_none()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    item = next((i for i in cart.items if i.id == itemId), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    await db.delete(item)
    cart.updated_at = datetime.utcnow()
    await db.commit()
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one()
    return _cart_to_out(cart)


@router.delete("/{userId}", status_code=204)
async def clear_cart(userId: str, db: AsyncSession = Depends(get_db)):
    from sqlalchemy.orm import selectinload
    result = await db.execute(
        select(Cart).where(Cart.user_id == userId).options(selectinload(Cart.items))
    )
    cart = result.scalar_one_or_none()
    if cart:
        for item in list(cart.items):
            await db.delete(item)
        cart.updated_at = datetime.utcnow()
        await db.commit()
