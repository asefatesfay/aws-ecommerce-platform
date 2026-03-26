"""Search Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "search-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Search Service")

# Routers are added in later tasks
# from app.routers import search
# app.include_router(search.router, prefix="/search")
