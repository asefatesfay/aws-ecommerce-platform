import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_cognito as cognito
from constructs import Construct

from stacks.config import ProjectSettings


class IdentityStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        user_pool = cognito.UserPool(
            self,
            "UserPool",
            user_pool_name=f"{settings.name_prefix}-users",
            self_sign_up_enabled=True,
            sign_in_aliases=cognito.SignInAliases(email=True),
        )

        user_pool_client = user_pool.add_client(
            "WebClient",
            user_pool_client_name=f"{settings.name_prefix}-web-client",
        )

        CfnOutput(self, "UserPoolId", value=user_pool.user_pool_id)
        CfnOutput(self, "UserPoolClientId", value=user_pool_client.user_pool_client_id)
