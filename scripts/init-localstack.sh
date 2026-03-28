#!/bin/bash
# Bootstrap LocalStack with SNS topics, SQS queues, DynamoDB table, and S3 bucket
# Runs automatically when LocalStack starts (mounted at /etc/localstack/init/ready.d/)

set -e

REGION="us-east-1"
PROJECT="ecommerce"
ENV="dev"
PREFIX="${PROJECT}-${ENV}"

echo "==> Bootstrapping LocalStack for ${PREFIX}..."

# ── SNS Topics ────────────────────────────────────────────────────────────────
echo "--> Creating SNS topics..."
for topic in order-events payment-events product-events inventory-events pricing-events; do
  awslocal sns create-topic \
    --name "${PREFIX}-${topic}" \
    --region $REGION \
    --output text --query 'TopicArn' | xargs -I{} echo "    Created: {}"
done

# ── SQS Queues + DLQs ─────────────────────────────────────────────────────────
echo "--> Creating SQS queues..."

create_queue_with_dlq() {
  local name=$1
  local dlq_name="${name}-dlq"

  # Create DLQ first
  DLQ_ARN=$(awslocal sqs create-queue \
    --queue-name "${PREFIX}-${dlq_name}" \
    --region $REGION \
    --output text --query 'QueueUrl' | \
    xargs -I{} awslocal sqs get-queue-attributes \
      --queue-url {} \
      --attribute-names QueueArn \
      --output text --query 'Attributes.QueueArn')

  # Create main queue with redrive policy
  awslocal sqs create-queue \
    --queue-name "${PREFIX}-${name}" \
    --region $REGION \
    --attributes "{\"RedrivePolicy\":\"{\\\"deadLetterTargetArn\\\":\\\"${DLQ_ARN}\\\",\\\"maxReceiveCount\\\":\\\"3\\\"}\"}" \
    --output text --query 'QueueUrl' | xargs -I{} echo "    Created: {}"
}

create_queue_with_dlq "inventory-order-confirmed-queue"
create_queue_with_dlq "order-payment-queue"
create_queue_with_dlq "search-product-queue"
create_queue_with_dlq "ses-notification-queue"

# ── SNS → SQS Subscriptions ───────────────────────────────────────────────────
echo "--> Wiring SNS → SQS subscriptions..."

subscribe_sns_to_sqs() {
  local topic_name=$1
  local queue_name=$2
  local filter_policy=$3

  TOPIC_ARN="arn:aws:sns:${REGION}:000000000000:${PREFIX}-${topic_name}"
  QUEUE_URL=$(awslocal sqs get-queue-url \
    --queue-name "${PREFIX}-${queue_name}" \
    --region $REGION \
    --output text --query 'QueueUrl')
  QUEUE_ARN=$(awslocal sqs get-queue-attributes \
    --queue-url "$QUEUE_URL" \
    --attribute-names QueueArn \
    --output text --query 'Attributes.QueueArn')

  if [ -n "$filter_policy" ]; then
    awslocal sns subscribe \
      --topic-arn "$TOPIC_ARN" \
      --protocol sqs \
      --notification-endpoint "$QUEUE_ARN" \
      --attributes "FilterPolicy=${filter_policy}" \
      --region $REGION \
      --output text --query 'SubscriptionArn' | xargs -I{} echo "    Subscribed: {}"
  else
    awslocal sns subscribe \
      --topic-arn "$TOPIC_ARN" \
      --protocol sqs \
      --notification-endpoint "$QUEUE_ARN" \
      --region $REGION \
      --output text --query 'SubscriptionArn' | xargs -I{} echo "    Subscribed: {}"
  fi

  # Allow SNS to send to SQS
  awslocal sqs set-queue-attributes \
    --queue-url "$QUEUE_URL" \
    --attributes "{\"Policy\":\"{\\\"Version\\\":\\\"2012-10-17\\\",\\\"Statement\\\":[{\\\"Effect\\\":\\\"Allow\\\",\\\"Principal\\\":{\\\"Service\\\":\\\"sns.amazonaws.com\\\"},\\\"Action\\\":\\\"sqs:SendMessage\\\",\\\"Resource\\\":\\\"${QUEUE_ARN}\\\"}]}\"}" \
    --region $REGION
}

# order.confirmed → inventory queue
subscribe_sns_to_sqs "order-events" "inventory-order-confirmed-queue" \
  '{"event_type":["order.confirmed"]}'

# payment events → order queue
subscribe_sns_to_sqs "payment-events" "order-payment-queue"

# product events → search queue
subscribe_sns_to_sqs "product-events" "search-product-queue"

# order.confirmed + order.cancelled → SES notification queue
subscribe_sns_to_sqs "order-events" "ses-notification-queue" \
  '{"event_type":["order.confirmed","order.cancelled"]}'

# ── DynamoDB Table (Cart) ─────────────────────────────────────────────────────
echo "--> Creating DynamoDB cart table..."
awslocal dynamodb create-table \
  --table-name "${PREFIX}-cart" \
  --attribute-definitions \
    AttributeName=PK,AttributeType=S \
    AttributeName=SK,AttributeType=S \
  --key-schema \
    AttributeName=PK,KeyType=HASH \
    AttributeName=SK,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST \
  --region $REGION \
  --output text --query 'TableDescription.TableName' | xargs -I{} echo "    Created: {}"

# ── S3 Bucket ─────────────────────────────────────────────────────────────────
echo "--> Creating S3 buckets..."
awslocal s3 mb "s3://${PREFIX}-product-images" --region $REGION
awslocal s3 mb "s3://${PREFIX}-exports" --region $REGION
echo "    Created: ${PREFIX}-product-images, ${PREFIX}-exports"

# ── Secrets Manager ───────────────────────────────────────────────────────────
echo "--> Creating Secrets Manager secrets..."
awslocal secretsmanager create-secret \
  --name "${PREFIX}/aurora/credentials" \
  --secret-string '{"username":"postgres","password":"postgres","host":"postgres","port":5432,"dbname":"ecommerce"}' \
  --region $REGION 2>/dev/null || echo "    Secret already exists"

awslocal secretsmanager create-secret \
  --name "${PREFIX}/stripe/secret-key" \
  --secret-string "sk_test_placeholder" \
  --region $REGION 2>/dev/null || echo "    Secret already exists"

echo ""
echo "==> LocalStack bootstrap complete!"
echo ""
echo "    SNS Topics:"
awslocal sns list-topics --region $REGION --output text --query 'Topics[].TopicArn'
echo ""
echo "    SQS Queues:"
awslocal sqs list-queues --region $REGION --output text --query 'QueueUrls[]'
