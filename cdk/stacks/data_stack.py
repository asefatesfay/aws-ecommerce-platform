import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_secretsmanager as secretsmanager
from constructs import Construct

from stacks.config import ProjectSettings


class DataStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.database_secret = secretsmanager.Secret(
            self,
            "DatabaseSecret",
            secret_name=f"{settings.name_prefix}/platform/database",
        )

        self.redis_secret = secretsmanager.Secret(
            self,
            "RedisSecret",
            secret_name=f"{settings.name_prefix}/platform/redis",
        )

        self.search_secret = secretsmanager.Secret(
            self,
            "SearchSecret",
            secret_name=f"{settings.name_prefix}/platform/search",
        )

        CfnOutput(self, "DatabaseSecretArn", value=self.database_secret.secret_arn)
        CfnOutput(self, "RedisSecretArn", value=self.redis_secret.secret_arn)
        CfnOutput(self, "SearchSecretArn", value=self.search_secret.secret_arn)
