# AWS CDK Starter

This directory contains a Python AWS CDK scaffold for the ecommerce platform.

Terraform under `../infra` stays in the repository. CDK is the new deployment path only for the environments and resources that you explicitly decide CDK owns.

## What This Starter Includes

- Shared CDK context for project and environment naming
- `NetworkStack` with VPC, ECS cluster, and an internet-facing ALB
- `ApplicationStack` with one ECR repository and one ECS Fargate service per microservice
- `FrontendStack` with S3 and CloudFront for the storefront
- `DataStack`, `IdentityStack`, and `MessagingStack` as starter platform stacks you can extend next

## Current Scope

This is a starting point, not a full parity rewrite of the Terraform estate. It intentionally focuses on the deployment shape first:

- ECS cluster and services
- image repositories
- ALB path routing
- frontend hosting

You can extend it next with Aurora, ElastiCache, OpenSearch, Cognito authorizers, Secrets Manager wiring, and HTTPS certificates.

## New To CDK?

If this is your first time with AWS CDK, start here:

- [CDK-BASICS-TUTORIAL.md](CDK-BASICS-TUTORIAL.md)

## Deployment Diagram

```mermaid
flowchart TB
	GH[GitHub Actions Deploy Workflow] --> CDK[CDK App app.py]
	CDK --> NS[NetworkStack]
	CDK --> AS[ApplicationStack]
	CDK --> FS[FrontendStack]
	CDK --> DS[DataStack Starter]
	CDK --> IS[IdentityStack Starter]
	CDK --> MS[MessagingStack Starter]

	subgraph AWS[AWS Environment]
		NS --> VPC[VPC]
		NS --> ECS[ECS Cluster]
		NS --> ALB[Application Load Balancer]

		AS --> ECR[ECR Repositories]
		AS --> SVC1[auth Service]
		AS --> SVC2[catalog Service]
		AS --> SVC3[cart Service]
		AS --> SVC4[order Service]
		AS --> SVC5[payment Service]
		AS --> SVC6[search Service]
		AS --> SVC7[recommendation Service]
		AS --> SVC8[inventory Service]
		AS --> SVC9[admin Service]

		ECS --> SVC1
		ECS --> SVC2
		ECS --> SVC3
		ECS --> SVC4
		ECS --> SVC5
		ECS --> SVC6
		ECS --> SVC7
		ECS --> SVC8
		ECS --> SVC9

		ECR --> SVC1
		ECR --> SVC2
		ECR --> SVC3
		ECR --> SVC4
		ECR --> SVC5
		ECR --> SVC6
		ECR --> SVC7
		ECR --> SVC8
		ECR --> SVC9

		ALB --> SVC1
		ALB --> SVC2
		ALB --> SVC3
		ALB --> SVC4
		ALB --> SVC5
		ALB --> SVC6
		ALB --> SVC7
		ALB --> SVC8
		ALB --> SVC9

		FS --> S3[S3 Frontend Bucket]
		FS --> CF[CloudFront Distribution]
		S3 --> CF
	end

	User[Browser User] --> CF
	User --> ALB
```

## Bootstrap

```bash
cd cdk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap aws://ACCOUNT_ID/us-east-1
```

## Synthesize

```bash
cd cdk
cdk synth
```

## Deploy

```bash
cd cdk
cdk deploy --all
```

## Useful Context Overrides

```bash
cdk synth -c project=ecommerce -c environment=dev -c service_image_tag=latest
cdk deploy -c environment=sandbox -c aws_region=us-east-1
```

## Ownership Rule

Keep the ownership boundary simple:

- Terraform can remain in the repository for learning and comparison.
- CDK should be the deployment authority for any environment where the pipeline runs `cdk deploy`.
- Do not let Terraform and CDK both manage the same named resource in the same AWS environment.
