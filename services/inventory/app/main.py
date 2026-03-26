"""Inventory Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "inventory-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Inventory Service")

# Routers are added in later tasks
# from app.routers import inventory
# app.include_router(inventory.router, prefix="/inventory")
