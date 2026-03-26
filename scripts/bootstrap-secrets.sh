#!/bin/bash
# Bootstrap AWS Secrets Manager secrets for local development
# Uses LocalStack by default (AWS_ENDPOINT_URL=http://localhost:4566)

set -e

ENDPOINT=${AWS_ENDPOINT_URL:-http://localhost:4566}
REGION=${AWS_DEFAULT_REGION:-us-east-1}
ENV=${ENVIRONMENT:-dev}
PROJECT=${PROJECT:-ecommerce}

echo "Bootstrapping secrets for $PROJECT-$ENV..."

aws --endpoint-url=$ENDPOINT secretsmanager create-secret \
  --name "$PROJECT-$ENV/aurora/credentials" \
  --secret-string '{"username":"postgres","password":"postgres","host":"localhost","port":5432,"dbname":"ecommerce"}' \
  --region $REGION 2>/dev/null || echo "Secret already exists"

aws --endpoint-url=$ENDPOINT secretsmanager create-secret \
  --name "$PROJECT-$ENV/stripe/secret-key" \
  --secret-string "sk_test_placeholder" \
  --region $REGION 2>/dev/null || echo "Secret already exists"

aws --endpoint-url=$ENDPOINT secretsmanager create-secret \
  --name "$PROJECT-$ENV/stripe/webhook-secret" \
  --secret-string "whsec_placeholder" \
  --region $REGION 2>/dev/null || echo "Secret already exists"

echo "Done."
