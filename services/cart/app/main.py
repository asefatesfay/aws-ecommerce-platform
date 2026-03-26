"""Cart Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "cart-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Cart Service")

# Routers are added in later tasks
# from app.routers import cart
# app.include_router(cart.router, prefix="/cart")
