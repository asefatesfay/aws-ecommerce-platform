import uuid
import hashlib
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from app.database import get_db
from app.models import User
from app.schemas import RegisterRequest, LoginRequest, RefreshRequest, UpdateProfileRequest, UserOut, TokenResponse

router = APIRouter(tags=["Auth"])


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _fake_token(user_id: str) -> str:
    return f"fake_access_token_{user_id}_{uuid.uuid4().hex[:8]}"


def _fake_refresh_token(user_id: str) -> str:
    return f"fake_refresh_token_{user_id}_{uuid.uuid4().hex[:8]}"


async def get_current_user(
    x_user_id: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db),
) -> User:
    if not x_user_id:
        raise HTTPException(status_code=401, detail="X-User-Id header required")
    result = await db.execute(select(User).where(User.id == x_user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/register", status_code=201, response_model=UserOut)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == body.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email address is already registered.")
    user = User(
        id=str(uuid.uuid4()),
        email=body.email,
        full_name=body.full_name,
        phone=body.phone,
        role="customer",
        cognito_sub=str(uuid.uuid4()),
        hashed_password=_hash_password(body.password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()
    if not user or user.hashed_password != _hash_password(body.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(
        access_token=_fake_token(user.id),
        refresh_token=_fake_refresh_token(user.id),
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(body: RefreshRequest):
    if not body.refresh_token.startswith("fake_refresh_token_"):
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    parts = body.refresh_token.split("_")
    user_id = parts[3] if len(parts) > 3 else str(uuid.uuid4())
    return TokenResponse(
        access_token=_fake_token(user_id),
        refresh_token=_fake_refresh_token(user_id),
    )


@router.get("/profile", response_model=UserOut)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/profile", response_model=UserOut)
async def update_profile(
    body: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if body.full_name is not None:
        current_user.full_name = body.full_name
    if body.phone is not None:
        current_user.phone = body.phone
    current_user.updated_at = datetime.utcnow()
    await db.commit()
    await db.refresh(current_user)
    return current_user
