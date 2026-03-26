variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "azs" {
  description = "List of availability zones"
  type        = list(string)
}

variable "ecr_repository_url" {
  description = "Base ECR repository URL (without service suffix)"
  type        = string
}
