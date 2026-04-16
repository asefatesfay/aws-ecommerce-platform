from dataclasses import dataclass

import aws_cdk as cdk


@dataclass(frozen=True)
class ServiceSpec:
    name: str
    port: int


SERVICE_SPECS = (
    ServiceSpec(name="auth", port=8001),
    ServiceSpec(name="catalog", port=8002),
    ServiceSpec(name="cart", port=8003),
    ServiceSpec(name="order", port=8004),
    ServiceSpec(name="payment", port=8005),
    ServiceSpec(name="search", port=8006),
    ServiceSpec(name="recommendation", port=8007),
    ServiceSpec(name="inventory", port=8008),
    ServiceSpec(name="admin", port=8009),
)


@dataclass(frozen=True)
class ProjectSettings:
    project: str
    environment: str
    region: str
    account: str | None
    service_image_tag: str
    frontend_price_class: str

    @property
    def name_prefix(self) -> str:
        return f"{self.project}-{self.environment}"

    @property
    def stack_prefix(self) -> str:
        return f"{self.project.capitalize()}{self.environment.capitalize()}"


def _context_value(app: cdk.App, key: str, default: str) -> str:
    value = app.node.try_get_context(key)
    if value is None:
        return default
    return str(value)


def load_settings(app: cdk.App) -> ProjectSettings:
    return ProjectSettings(
        project=_context_value(app, "project", "ecommerce"),
        environment=_context_value(app, "environment", "dev"),
        region=_context_value(app, "aws_region", "us-east-1"),
        account=app.account or None,
        service_image_tag=_context_value(app, "service_image_tag", "latest"),
        frontend_price_class=_context_value(app, "frontend_price_class", "PRICE_CLASS_100"),
    )
