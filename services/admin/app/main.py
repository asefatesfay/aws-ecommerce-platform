"""Admin Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "admin-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Admin Service")

# Routers are added in later tasks
# from app.routers import admin
# app.include_router(admin.router, prefix="/admin")
