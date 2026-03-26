locals {
  full_name   = "${var.project}-${var.environment}"
  domain_name = "${var.project}-${var.environment}-search"
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

resource "aws_opensearch_domain" "this" {
  domain_name    = local.domain_name
  engine_version = "OpenSearch_2.11"

  cluster_config {
    instance_type            = var.instance_type
    instance_count           = var.instance_count
    dedicated_master_enabled = var.dedicated_master_enabled
    dedicated_master_type    = var.dedicated_master_enabled ? var.dedicated_master_type : null
    dedicated_master_count   = var.dedicated_master_enabled ? var.dedicated_master_count : null
    zone_awareness_enabled   = var.instance_count > 1 ? true : false

    dynamic "zone_awareness_config" {
      for_each = var.instance_count > 1 ? [1] : []
      content {
        availability_zone_count = min(var.instance_count, 3)
      }
    }
  }

  ebs_options {
    ebs_enabled = true
    volume_type = "gp3"
    volume_size = var.ebs_volume_size
  }

  vpc_options {
    subnet_ids         = slice(var.private_subnet_ids, 0, min(var.instance_count, length(var.private_subnet_ids)))
    security_group_ids = [var.opensearch_sg_id]
  }

  encrypt_at_rest {
    enabled = true
  }

  node_to_node_encryption {
    enabled = true
  }

  domain_endpoint_options {
    enforce_https       = true
    tls_security_policy = "Policy-Min-TLS-1-2-2019-07"
  }

  advanced_security_options {
    enabled                        = false
    anonymous_auth_enabled         = true
    internal_user_database_enabled = false
  }

  log_publishing_options {
    cloudwatch_log_group_arn = aws_cloudwatch_log_group.opensearch.arn
    log_type                 = "INDEX_SLOW_LOGS"
  }

  log_publishing_options {
    cloudwatch_log_group_arn = aws_cloudwatch_log_group.opensearch.arn
    log_type                 = "SEARCH_SLOW_LOGS"
  }

  tags = local.tags
}

resource "aws_cloudwatch_log_group" "opensearch" {
  name              = "/opensearch/${local.full_name}"
  retention_in_days = 14

  tags = local.tags
}

resource "aws_cloudwatch_log_resource_policy" "opensearch" {
  policy_name = "${local.full_name}-opensearch-log-policy"

  policy_document = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "es.amazonaws.com"
      }
      Action = [
        "logs:PutLogEvents",
        "logs:PutLogEventsBatch",
        "logs:CreateLogStream"
      ]
      Resource = "${aws_cloudwatch_log_group.opensearch.arn}:*"
    }]
  })
}

resource "aws_opensearch_domain_policy" "this" {
  domain_name = aws_opensearch_domain.this.domain_name

  access_policies = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = var.ecs_task_role_arn }
        Action    = "es:*"
        Resource  = "${aws_opensearch_domain.this.arn}/*"
      }
    ]
  })
}
