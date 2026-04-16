import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subscriptions
from aws_cdk import aws_sqs as sqs
from constructs import Construct

from stacks.config import ProjectSettings


class MessagingStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self,
            "OrderEventsTopic",
            topic_name=f"{settings.name_prefix}-order-events",
        )

        queue = sqs.Queue(
            self,
            "OrderEventsQueue",
            queue_name=f"{settings.name_prefix}-order-events-consumer",
        )

        topic.add_subscription(subscriptions.SqsSubscription(queue))

        CfnOutput(self, "OrderEventsTopicArn", value=topic.topic_arn)
        CfnOutput(self, "OrderEventsQueueUrl", value=queue.queue_url)
