import uuid
from datetime import datetime
from sqlalchemy import String, Float, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ProductCatalog(Base):
    __tablename__ = "product_catalog"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String, nullable=True)
    sku: Mapped[str] = mapped_column(String, unique=True, nullable=False)


class UserEvent(Base):
    __tablename__ = "user_events"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, index=True, nullable=False)
    event_type: Mapped[str] = mapped_column(String, nullable=False)
    product_id: Mapped[str] = mapped_column(String, nullable=False)
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
