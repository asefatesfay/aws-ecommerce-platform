import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from constructs import Construct

from stacks.config import ProjectSettings


class NetworkStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "Vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            max_azs=2,
            nat_gateways=1,
        )

        self.cluster = ecs.Cluster(
            self,
            "Cluster",
            cluster_name=f"{settings.name_prefix}-cluster",
            vpc=self.vpc,
            container_insights=True,
        )

        self.load_balancer = elbv2.ApplicationLoadBalancer(
            self,
            "LoadBalancer",
            load_balancer_name=f"{settings.name_prefix}-alb",
            vpc=self.vpc,
            internet_facing=True,
        )

        self.http_listener = self.load_balancer.add_listener(
            "HttpListener",
            port=80,
            open=True,
            default_action=elbv2.ListenerAction.fixed_response(
                404,
                content_type="application/json",
                message_body='{"message":"Route not configured"}',
            ),
        )

        CfnOutput(
            self,
            "AlbDnsName",
            value=self.load_balancer.load_balancer_dns_name,
        )
