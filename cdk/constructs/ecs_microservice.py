from collections.abc import Mapping

from aws_cdk import Duration
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_logs as logs
from constructs import Construct


class EcsMicroservice(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        cluster: ecs.Cluster,
        image: ecs.ContainerImage,
        container_port: int,
        environment: Mapping[str, str] | None = None,
        cpu: int = 256,
        memory_mib: int = 512,
        desired_count: int = 1,
    ) -> None:
        super().__init__(scope, construct_id)

        service_name = construct_id.lower()

        task_definition = ecs.FargateTaskDefinition(
            self,
            "TaskDefinition",
            cpu=cpu,
            memory_limit_mib=memory_mib,
        )

        container = task_definition.add_container(
            "Container",
            image=image,
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix=service_name,
                log_retention=logs.RetentionDays.ONE_WEEK,
            ),
            environment=dict(environment or {}),
        )
        container.add_port_mappings(
            ecs.PortMapping(container_port=container_port),
        )

        self.service = ecs.FargateService(
            self,
            "Service",
            cluster=cluster,
            desired_count=desired_count,
            task_definition=task_definition,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
            min_healthy_percent=50,
            max_healthy_percent=200,
            assign_public_ip=False,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
        )

        scaling = self.service.auto_scale_task_count(
            min_capacity=1,
            max_capacity=3,
        )
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=60,
            scale_in_cooldown=Duration.seconds(60),
            scale_out_cooldown=Duration.seconds(60),
        )
