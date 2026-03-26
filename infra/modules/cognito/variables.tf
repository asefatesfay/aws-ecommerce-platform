variable "project" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "callback_urls" {
  description = "Allowed callback URLs for the Cognito app client"
  type        = list(string)
}

variable "logout_urls" {
  description = "Allowed logout URLs for the Cognito app client"
  type        = list(string)
}
