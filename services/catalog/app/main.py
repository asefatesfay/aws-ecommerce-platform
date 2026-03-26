"""Catalog Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "catalog-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Catalog Service")
