variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "instance_type" {
  description = "OpenSearch data node instance type"
  type        = string
  default     = "t3.small.search"
}

variable "instance_count" {
  description = "Number of data nodes"
  type        = number
  default     = 1
}

variable "dedicated_master_enabled" {
  description = "Enable dedicated master nodes"
  type        = bool
  default     = false
}

variable "dedicated_master_type" {
  description = "Dedicated master node instance type"
  type        = string
  default     = "t3.small.search"
}

variable "dedicated_master_count" {
  description = "Number of dedicated master nodes"
  type        = number
  default     = 3
}

variable "ebs_volume_size" {
  description = "EBS volume size in GB"
  type        = number
  default     = 20
}

variable "private_subnet_ids" {
  description = "Private subnet IDs (use 1 for dev, 3 for prod)"
  type        = list(string)
}

variable "opensearch_sg_id" {
  description = "OpenSearch security group ID"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "ecs_task_role_arn" {
  description = "ECS task role ARN allowed to access OpenSearch"
  type        = string
}
