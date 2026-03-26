"""Order Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "order-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Order Service")

# Routers are added in later tasks
# from app.routers import order
# app.include_router(order.router, prefix="/orders")
