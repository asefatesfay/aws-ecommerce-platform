variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "api_gateway_url" {
  description = "API Gateway invoke URL (without trailing slash)"
  type        = string
}

variable "price_class" {
  description = "CloudFront price class"
  type        = string
  default     = "PriceClass_100"
}

variable "waf_web_acl_arn" {
  description = "WAF Web ACL ARN to attach (must be CLOUDFRONT scope, us-east-1)"
  type        = string
  default     = ""
}
