# ── SNS Topic ARNs ────────────────────────────────────────────────────────────

output "order_events_topic_arn" {
  description = "ARN of the order-events SNS topic"
  value       = aws_sns_topic.order_events.arn
}

output "payment_events_topic_arn" {
  description = "ARN of the payment-events SNS topic"
  value       = aws_sns_topic.payment_events.arn
}

output "product_events_topic_arn" {
  description = "ARN of the product-events SNS topic"
  value       = aws_sns_topic.product_events.arn
}

output "inventory_events_topic_arn" {
  description = "ARN of the inventory-events SNS topic"
  value       = aws_sns_topic.inventory_events.arn
}

# ── SQS Queue ARNs ────────────────────────────────────────────────────────────

output "inventory_order_queue_arn" {
  description = "ARN of the inventory-order-confirmed SQS queue"
  value       = aws_sqs_queue.inventory_order_confirmed.arn
}

output "inventory_order_queue_url" {
  description = "URL of the inventory-order-confirmed SQS queue"
  value       = aws_sqs_queue.inventory_order_confirmed.url
}

output "order_payment_queue_arn" {
  description = "ARN of the order-payment SQS queue"
  value       = aws_sqs_queue.order_payment.arn
}

output "order_payment_queue_url" {
  description = "URL of the order-payment SQS queue"
  value       = aws_sqs_queue.order_payment.url
}

output "search_product_queue_arn" {
  description = "ARN of the search-product SQS queue"
  value       = aws_sqs_queue.search_product.arn
}

output "search_product_queue_url" {
  description = "URL of the search-product SQS queue"
  value       = aws_sqs_queue.search_product.url
}

output "ses_notification_queue_arn" {
  description = "ARN of the ses-notification SQS queue"
  value       = aws_sqs_queue.ses_notification.arn
}

output "ses_notification_queue_url" {
  description = "URL of the ses-notification SQS queue"
  value       = aws_sqs_queue.ses_notification.url
}
