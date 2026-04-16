import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from constructs import Construct

from constructs.ecs_microservice import EcsMicroservice
from stacks.config import ProjectSettings
from stacks.config import SERVICE_SPECS


class ApplicationStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        cluster: ecs.Cluster,
        listener: elbv2.ApplicationListener,
        vpc: ec2.IVpc,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        for priority, spec in enumerate(SERVICE_SPECS, start=10):
            repository = ecr.Repository(
                self,
                f"{spec.name.capitalize()}Repository",
                repository_name=f"{settings.project}/{spec.name}",
                image_scan_on_push=True,
            )

            service = EcsMicroservice(
                self,
                f"{spec.name.capitalize()}Service",
                cluster=cluster,
                image=ecs.ContainerImage.from_ecr_repository(
                    repository,
                    tag=settings.service_image_tag,
                ),
                container_port=spec.port,
                environment={
                    "APP_ENVIRONMENT": settings.environment,
                    "SERVICE_NAME": spec.name,
                    "PORT": str(spec.port),
                    "AWS_REGION": settings.region,
                },
            )

            listener.add_targets(
                f"{spec.name.capitalize()}Rule",
                priority=priority,
                conditions=[
                    elbv2.ListenerCondition.path_patterns(
                        [f"/{spec.name}", f"/{spec.name}/*"],
                    ),
                ],
                port=spec.port,
                protocol=elbv2.ApplicationProtocol.HTTP,
                targets=[service.service],
                health_check=elbv2.HealthCheck(
                    path="/health",
                    healthy_http_codes="200-399",
                ),
            )

            CfnOutput(
                self,
                f"{spec.name.capitalize()}RepositoryUri",
                value=repository.repository_uri,
            )

        CfnOutput(
            self,
            "AlbServiceBaseUrl",
            value=f"http://{listener.load_balancer.load_balancer_dns_name}",
        )
