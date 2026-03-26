"""Recommendation Service entry point."""
import os

os.environ.setdefault("SERVICE_NAME", "recommendation-service")

from app.main import create_app  # noqa: E402

app = create_app(title="Recommendation Service")

# Routers are added in later tasks
# from app.routers import recommendation
# app.include_router(recommendation.router, prefix="/recommendations")
