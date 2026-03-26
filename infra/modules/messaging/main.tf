locals {
  full_name = "${var.project}-${var.environment}"
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# ── SNS Topics ────────────────────────────────────────────────────────────────

resource "aws_sns_topic" "order_events" {
  name              = "${local.full_name}-order-events"
  kms_master_key_id = "alias/aws/sns"

  tags = local.tags
}

resource "aws_sns_topic" "payment_events" {
  name              = "${local.full_name}-payment-events"
  kms_master_key_id = "alias/aws/sns"

  tags = local.tags
}

resource "aws_sns_topic" "product_events" {
  name              = "${local.full_name}-product-events"
  kms_master_key_id = "alias/aws/sns"

  tags = local.tags
}

resource "aws_sns_topic" "inventory_events" {
  name              = "${local.full_name}-inventory-events"
  kms_master_key_id = "alias/aws/sns"

  tags = local.tags
}

# ── SQS Dead-Letter Queues ────────────────────────────────────────────────────

resource "aws_sqs_queue" "inventory_order_confirmed_dlq" {
  name                      = "${local.full_name}-inventory-order-confirmed-dlq"
  message_retention_seconds = 1209600 # 14 days
  kms_master_key_id         = "alias/aws/sqs"

  tags = local.tags
}

resource "aws_sqs_queue" "order_payment_dlq" {
  name                      = "${local.full_name}-order-payment-dlq"
  message_retention_seconds = 1209600
  kms_master_key_id         = "alias/aws/sqs"

  tags = local.tags
}

resource "aws_sqs_queue" "search_product_dlq" {
  name                      = "${local.full_name}-search-product-dlq"
  message_retention_seconds = 1209600
  kms_master_key_id         = "alias/aws/sqs"

  tags = local.tags
}

resource "aws_sqs_queue" "ses_notification_dlq" {
  name                      = "${local.full_name}-ses-notification-dlq"
  message_retention_seconds = 1209600
  kms_master_key_id         = "alias/aws/sqs"

  tags = local.tags
}

# ── SQS Main Queues ───────────────────────────────────────────────────────────

resource "aws_sqs_queue" "inventory_order_confirmed" {
  name                       = "${local.full_name}-inventory-order-confirmed-queue"
  visibility_timeout_seconds = 300
  message_retention_seconds  = 86400
  kms_master_key_id          = "alias/aws/sqs"

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.inventory_order_confirmed_dlq.arn
    maxReceiveCount     = 3
  })

  tags = local.tags
}

resource "aws_sqs_queue" "order_payment" {
  name                       = "${local.full_name}-order-payment-queue"
  visibility_timeout_seconds = 300
  message_retention_seconds  = 86400
  kms_master_key_id          = "alias/aws/sqs"

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.order_payment_dlq.arn
    maxReceiveCount     = 3
  })

  tags = local.tags
}

resource "aws_sqs_queue" "search_product" {
  name                       = "${local.full_name}-search-product-queue"
  visibility_timeout_seconds = 300
  message_retention_seconds  = 86400
  kms_master_key_id          = "alias/aws/sqs"

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.search_product_dlq.arn
    maxReceiveCount     = 3
  })

  tags = local.tags
}

resource "aws_sqs_queue" "ses_notification" {
  name                       = "${local.full_name}-ses-notification-queue"
  visibility_timeout_seconds = 300
  message_retention_seconds  = 86400
  kms_master_key_id          = "alias/aws/sqs"

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.ses_notification_dlq.arn
    maxReceiveCount     = 3
  })

  tags = local.tags
}

# ── SQS Redrive Allow Policies (DLQs) ────────────────────────────────────────

resource "aws_sqs_queue_redrive_allow_policy" "inventory_order_confirmed_dlq" {
  queue_url = aws_sqs_queue.inventory_order_confirmed_dlq.url

  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue"
    sourceQueueArns   = [aws_sqs_queue.inventory_order_confirmed.arn]
  })
}

resource "aws_sqs_queue_redrive_allow_policy" "order_payment_dlq" {
  queue_url = aws_sqs_queue.order_payment_dlq.url

  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue"
    sourceQueueArns   = [aws_sqs_queue.order_payment.arn]
  })
}

resource "aws_sqs_queue_redrive_allow_policy" "search_product_dlq" {
  queue_url = aws_sqs_queue.search_product_dlq.url

  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue"
    sourceQueueArns   = [aws_sqs_queue.search_product.arn]
  })
}

resource "aws_sqs_queue_redrive_allow_policy" "ses_notification_dlq" {
  queue_url = aws_sqs_queue.ses_notification_dlq.url

  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue"
    sourceQueueArns   = [aws_sqs_queue.ses_notification.arn]
  })
}

# ── SNS → SQS Subscriptions ───────────────────────────────────────────────────

resource "aws_sns_topic_subscription" "inventory_order_confirmed" {
  topic_arn = aws_sns_topic.order_events.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.inventory_order_confirmed.arn

  filter_policy = jsonencode({
    event_type = ["order.confirmed"]
  })
}

resource "aws_sns_topic_subscription" "order_payment" {
  topic_arn = aws_sns_topic.payment_events.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.order_payment.arn
}

resource "aws_sns_topic_subscription" "search_product" {
  topic_arn = aws_sns_topic.product_events.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.search_product.arn
}

resource "aws_sns_topic_subscription" "ses_notification" {
  topic_arn = aws_sns_topic.order_events.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.ses_notification.arn

  filter_policy = jsonencode({
    event_type = ["order.confirmed", "order.cancelled"]
  })
}

# ── SNS Topic Policies ────────────────────────────────────────────────────────

resource "aws_sns_topic_policy" "order_events" {
  arn = aws_sns_topic.order_events.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPublish"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.order_events.arn
      }
    ]
  })
}

resource "aws_sns_topic_policy" "payment_events" {
  arn = aws_sns_topic.payment_events.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPublish"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.payment_events.arn
      }
    ]
  })
}

resource "aws_sns_topic_policy" "product_events" {
  arn = aws_sns_topic.product_events.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPublish"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.product_events.arn
      }
    ]
  })
}

resource "aws_sns_topic_policy" "inventory_events" {
  arn = aws_sns_topic.inventory_events.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPublish"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.inventory_events.arn
      }
    ]
  })
}

# ── SQS Queue Policies (allow SNS) ───────────────────────────────────────────

resource "aws_sqs_queue_policy" "inventory_order_confirmed" {
  queue_url = aws_sqs_queue.inventory_order_confirmed.url

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSNS"
        Effect = "Allow"
        Principal = { Service = "sns.amazonaws.com" }
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.inventory_order_confirmed.arn
        Condition = {
          ArnEquals = { "aws:SourceArn" = aws_sns_topic.order_events.arn }
        }
      }
    ]
  })
}

resource "aws_sqs_queue_policy" "order_payment" {
  queue_url = aws_sqs_queue.order_payment.url

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSNS"
        Effect = "Allow"
        Principal = { Service = "sns.amazonaws.com" }
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.order_payment.arn
        Condition = {
          ArnEquals = { "aws:SourceArn" = aws_sns_topic.payment_events.arn }
        }
      }
    ]
  })
}

resource "aws_sqs_queue_policy" "search_product" {
  queue_url = aws_sqs_queue.search_product.url

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSNS"
        Effect = "Allow"
        Principal = { Service = "sns.amazonaws.com" }
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.search_product.arn
        Condition = {
          ArnEquals = { "aws:SourceArn" = aws_sns_topic.product_events.arn }
        }
      }
    ]
  })
}

resource "aws_sqs_queue_policy" "ses_notification" {
  queue_url = aws_sqs_queue.ses_notification.url

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowSNS"
        Effect = "Allow"
        Principal = { Service = "sns.amazonaws.com" }
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.ses_notification.arn
        Condition = {
          ArnEquals = { "aws:SourceArn" = aws_sns_topic.order_events.arn }
        }
      }
    ]
  })
}

# ── EventBridge Rules ─────────────────────────────────────────────────────────

resource "aws_cloudwatch_event_rule" "daily_inventory_reconciliation" {
  name                = "${local.full_name}-daily-inventory-reconciliation"
  description         = "Trigger daily inventory reconciliation at 02:00 UTC"
  schedule_expression = "cron(0 2 * * ? *)"
  state               = "ENABLED"

  tags = local.tags
}

resource "aws_cloudwatch_event_rule" "daily_admin_report" {
  name                = "${local.full_name}-daily-admin-report"
  description         = "Trigger daily admin report generation at 06:00 UTC"
  schedule_expression = "cron(0 6 * * ? *)"
  state               = "ENABLED"

  tags = local.tags
}

resource "aws_cloudwatch_event_target" "daily_inventory_reconciliation" {
  rule      = aws_cloudwatch_event_rule.daily_inventory_reconciliation.name
  target_id = "inventory-reconciliation-sns"
  arn       = aws_sns_topic.inventory_events.arn

  input = jsonencode({
    event_type = "inventory.reconciliation.scheduled"
    source     = "eventbridge"
  })
}

resource "aws_cloudwatch_event_target" "daily_admin_report" {
  rule      = aws_cloudwatch_event_rule.daily_admin_report.name
  target_id = "admin-report-sns"
  arn       = aws_sns_topic.inventory_events.arn

  input = jsonencode({
    event_type = "admin.report.scheduled"
    source     = "eventbridge"
  })
}

resource "aws_sns_topic_policy" "inventory_events_eventbridge" {
  arn = aws_sns_topic.inventory_events.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowPublish"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.inventory_events.arn
      },
      {
        Sid    = "AllowEventBridge"
        Effect = "Allow"
        Principal = {
          Service = "events.amazonaws.com"
        }
        Action   = "SNS:Publish"
        Resource = aws_sns_topic.inventory_events.arn
      }
    ]
  })
}
