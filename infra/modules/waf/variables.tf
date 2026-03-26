variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "scope" {
  description = "WAF scope: CLOUDFRONT or REGIONAL"
  type        = string
  validation {
    condition     = contains(["CLOUDFRONT", "REGIONAL"], var.scope)
    error_message = "scope must be CLOUDFRONT or REGIONAL."
  }
}

variable "api_gateway_arn" {
  description = "API Gateway stage ARN for WAF association (REGIONAL only)"
  type        = string
  default     = ""
}
