import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id: Mapped[str] = mapped_column(String, index=True, nullable=False)
    stripe_payment_intent_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String, default="usd")
    status: Mapped[str] = mapped_column(String, default="pending")
    stripe_charge_id: Mapped[str | None] = mapped_column(String, nullable=True)
    refunded_amount: Mapped[float] = mapped_column(Float, default=0.0)
    client_secret: Mapped[str] = mapped_column(String, nullable=False)
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
