import uuid
from sqlalchemy import String, Float, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ProductIndex(Base):
    __tablename__ = "product_index"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    brand: Mapped[str | None] = mapped_column(String, nullable=True)
    category: Mapped[str | None] = mapped_column(String, nullable=True)
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)
    sku: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String, nullable=True)
