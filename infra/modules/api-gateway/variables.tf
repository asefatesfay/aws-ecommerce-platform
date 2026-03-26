variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "alb_dns_name" {
  description = "ALB DNS name for HTTP_PROXY integration"
  type        = string
}

variable "cognito_user_pool_arn" {
  description = "Cognito User Pool ARN for the authorizer"
  type        = string
}

variable "stage_name" {
  description = "API Gateway stage name"
  type        = string
  default     = "v1"
}
