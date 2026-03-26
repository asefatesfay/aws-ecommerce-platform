locals {
  full_name = "${var.project}-${var.environment}"
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_wafv2_web_acl" "this" {
  name        = "${local.full_name}-waf-${lower(var.scope)}"
  description = "WAF Web ACL for ${local.full_name} (${var.scope})"
  scope       = var.scope

  default_action {
    allow {}
  }

  # AWS Managed Common Rule Set
  rule {
    name     = "AWSManagedRulesCommonRuleSet"
    priority = 10

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${local.full_name}-common-rules"
      sampled_requests_enabled   = true
    }
  }

  # AWS Managed Known Bad Inputs Rule Set
  rule {
    name     = "AWSManagedRulesKnownBadInputsRuleSet"
    priority = 20

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesKnownBadInputsRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${local.full_name}-known-bad-inputs"
      sampled_requests_enabled   = true
    }
  }

  # AWS Managed SQLi Rule Set
  rule {
    name     = "AWSManagedRulesSQLiRuleSet"
    priority = 30

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesSQLiRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${local.full_name}-sqli-rules"
      sampled_requests_enabled   = true
    }
  }

  # Rate limiting: 2000 requests per 5 minutes per IP
  rule {
    name     = "RateLimitPerIP"
    priority = 40

    action {
      block {}
    }

    statement {
      rate_based_statement {
        limit              = 2000
        aggregate_key_type = "IP"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${local.full_name}-rate-limit"
      sampled_requests_enabled   = true
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "${local.full_name}-waf"
    sampled_requests_enabled   = true
  }

  tags = local.tags
}

# Associate WAF with API Gateway stage (REGIONAL only)
resource "aws_wafv2_web_acl_association" "api_gateway" {
  count        = var.scope == "REGIONAL" && var.api_gateway_arn != "" ? 1 : 0
  resource_arn = var.api_gateway_arn
  web_acl_arn  = aws_wafv2_web_acl.this.arn
}

# CloudWatch log group for WAF
resource "aws_cloudwatch_log_group" "waf" {
  # WAF log group name must start with "aws-waf-logs-"
  name              = "aws-waf-logs-${local.full_name}-${lower(var.scope)}"
  retention_in_days = 30

  tags = local.tags
}

resource "aws_wafv2_web_acl_logging_configuration" "this" {
  log_destination_configs = [aws_cloudwatch_log_group.waf.arn]
  resource_arn            = aws_wafv2_web_acl.this.arn
}
