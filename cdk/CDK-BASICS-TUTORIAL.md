# AWS CDK Basics Tutorial (Python)

This guide is for first-time AWS CDK users working in this repository.

Goal: help you understand the CDK flow end-to-end and safely deploy without deleting the Terraform folder.

## 1. What CDK Is

AWS CDK lets you define AWS infrastructure in code (Python in this project).

Instead of writing CloudFormation JSON/YAML directly, you write Python classes and CDK converts them into CloudFormation templates.

Basic mental model:

- App: the entry point (`app.py`)
- Stack: a deployable unit (for example `NetworkStack`, `ApplicationStack`)
- Construct: reusable building block inside stacks

## 2. Repository Rule You Are Using

In this repo, keep `infra/` (Terraform) for learning/reference.

CDK is the deployment authority only for environments/resources you deploy with `cdk deploy`.

Do not let Terraform and CDK manage the same named resource in the same AWS environment.

## 3. One-Time Setup

From repo root:

```bash
cd cdk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install -g aws-cdk
```

Check CDK CLI:

```bash
cdk --version
```

## 4. Configure AWS Access

Make sure your AWS credentials are configured in your shell.

```bash
aws sts get-caller-identity
```

If this command fails, configure AWS CLI credentials first.

## 5. Bootstrap Your AWS Account (One-Time Per Account/Region)

Bootstrapping creates CDK support resources in your account.

```bash
cd cdk
cdk bootstrap aws://ACCOUNT_ID/us-east-1
```

Replace `ACCOUNT_ID` with your account number.

## 6. Understand the CDK Workflow

You will mostly use four commands:

1. `cdk synth`: compile CDK code into CloudFormation templates
2. `cdk diff`: preview infrastructure changes
3. `cdk deploy`: apply changes
4. `cdk destroy`: delete stack resources (careful)

Typical loop:

```bash
cd cdk
cdk synth
cdk diff
cdk deploy --all
```

## 7. Use Context Values

This project uses context values for environment naming and image tags.

Examples:

```bash
cd cdk
cdk synth -c project=ecommerce -c environment=dev -c service_image_tag=latest
cdk deploy -c project=ecommerce -c environment=sandbox -c aws_region=us-east-1 --all
```

Tip: keep a dedicated CDK environment name like `sandbox` while learning.

## 8. Safe First Deploy Plan

Start with a cautious plan:

1. Synthesize all stacks.
2. Diff one stack.
3. Deploy one non-critical stack.
4. Verify in AWS Console.
5. Deploy remaining stacks.

Example:

```bash
cd cdk
cdk synth
cdk diff NetworkStack
cdk deploy NetworkStack
```

Then continue with application/frontend stacks.

## 9. First Practical Exercise: Deploy Only NetworkStack

Use this as your first hands-on lab.

### Step A: Prepare a safe learning environment name

```bash
cd cdk
export CDK_ENV=sandbox
export AWS_REGION=us-east-1
```

### Step B: Synthesize only network resources

```bash
cdk synth \
	-c project=ecommerce \
	-c environment=$CDK_ENV \
	-c aws_region=$AWS_REGION \
	NetworkStack
```

Expected result: CDK prints a synthesized CloudFormation template for `NetworkStack` with no runtime errors.

### Step C: Preview exactly what will change

```bash
cdk diff \
	-c project=ecommerce \
	-c environment=$CDK_ENV \
	-c aws_region=$AWS_REGION \
	NetworkStack
```

Expected result: additions for VPC, ECS cluster, and ALB resources.

### Step D: Deploy only NetworkStack

```bash
cdk deploy \
	-c project=ecommerce \
	-c environment=$CDK_ENV \
	-c aws_region=$AWS_REGION \
	NetworkStack
```

### Step E: Verify in AWS Console

Check these resources in region `us-east-1`:

1. CloudFormation stack for `NetworkStack` status is `CREATE_COMPLETE`.
2. VPC exists with expected subnets.
3. ECS cluster exists and is active.
4. ALB exists and is internet-facing.

### Step F: Validate outputs from CLI

```bash
aws cloudformation describe-stacks \
	--stack-name NetworkStack \
	--region $AWS_REGION
```

If your stack name is environment-prefixed by CDK, run this first and use the exact generated stack name:

```bash
aws cloudformation list-stacks \
	--region $AWS_REGION \
	--stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

### Step G: Roll back if needed

If you are done testing and want to remove only this stack:

```bash
cdk destroy \
	-c project=ecommerce \
	-c environment=$CDK_ENV \
	-c aws_region=$AWS_REGION \
	NetworkStack
```

## 10. Update and Redeploy

After code changes in `stacks/` or `constructs/`:

```bash
cd cdk
cdk diff
cdk deploy --all
```

CDK only updates resources that changed.

## 11. Common Errors and Fixes

`No credentials`:
- Run `aws sts get-caller-identity` and fix AWS auth.

`Toolkit stack not found`:
- Run bootstrap again for the same account/region.

`Already exists` resource conflicts:
- Usually means naming collision with existing resources.
- Use a different context/environment name (for example `sandbox`).

`AccessDenied` on deploy:
- Your IAM user/role lacks required permissions.
- Use a deployment role with CloudFormation, IAM pass role, ECS/ECR, networking permissions.

## 12. Clean Up (When Needed)

To remove deployed CDK stacks:

```bash
cd cdk
cdk destroy --all
```

Run this only for environments you intentionally want to remove.

## 13. Suggested Next Learning Steps

1. Add Secrets Manager parameters to service task definitions.
2. Add HTTPS with ACM + ALB/CloudFront certificates.
3. Add a pipeline stage running `cdk synth` and `cdk deploy`.
4. Add alarms and dashboards for ECS services.

You now have the basic CDK workflow and safety model needed to start shipping with CDK in this repository.
