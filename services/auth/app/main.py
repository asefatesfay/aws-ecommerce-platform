"""Auth Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "auth-service")

from app.main import create_app  # noqa: E402  (common package)

app = create_app(title="Auth Service")

# Routers are added in later tasks
# from app.routers import auth
# app.include_router(auth.router, prefix="/auth")
