terraform {
  backend "s3" {
    bucket         = "ecommerce-terraform-state-<account_id>"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "ecommerce-terraform-locks"
  }
}
