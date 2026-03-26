variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "ecommerce"
}

variable "db_username" {
  description = "Master DB username"
  type        = string
  default     = "dbadmin"
}

variable "instance_class" {
  description = "Aurora instance class"
  type        = string
  default     = "db.t3.medium"
}

variable "instance_count" {
  description = "Number of Aurora instances (1 = writer only, 2 = writer + reader)"
  type        = number
  default     = 1
}

variable "private_subnet_ids" {
  description = "Private subnet IDs for Aurora"
  type        = list(string)
}

variable "aurora_sg_id" {
  description = "Aurora security group ID"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}
