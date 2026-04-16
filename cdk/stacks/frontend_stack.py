import aws_cdk as cdk
from aws_cdk import CfnOutput
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3 as s3
from constructs import Construct

from stacks.config import ProjectSettings


class FrontendStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        settings: ProjectSettings,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        site_bucket = s3.Bucket(
            self,
            "SiteBucket",
            bucket_name=f"{settings.name_prefix}-frontend-assets",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
        )

        distribution = cloudfront.Distribution(
            self,
            "Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(site_bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
            price_class=cloudfront.PriceClass[settings.frontend_price_class],
        )

        CfnOutput(self, "FrontendBucketName", value=site_bucket.bucket_name)
        CfnOutput(self, "CloudFrontDomainName", value=distribution.distribution_domain_name)