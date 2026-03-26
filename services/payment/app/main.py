"""Payment Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "payment-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Payment Service")

# Routers are added in later tasks
# from app.routers import payment
# app.include_router(payment.router, prefix="/payments")
