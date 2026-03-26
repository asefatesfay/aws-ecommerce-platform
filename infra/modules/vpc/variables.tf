variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name (dev, prod)"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "azs" {
  description = "List of availability zones (exactly 2)"
  type        = list(string)
  validation {
    condition     = length(var.azs) == 2
    error_message = "Exactly 2 availability zones must be provided."
  }
}

variable "single_nat_gateway" {
  description = "Use a single NAT gateway (dev) vs one per AZ (prod)"
  type        = bool
  default     = false
}
