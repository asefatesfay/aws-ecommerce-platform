output "cluster_endpoint" {
  description = "Aurora cluster writer endpoint"
  value       = aws_rds_cluster.this.endpoint
}

output "reader_endpoint" {
  description = "Aurora cluster reader endpoint"
  value       = aws_rds_cluster.this.reader_endpoint
}

output "proxy_endpoint" {
  description = "RDS Proxy endpoint"
  value       = aws_db_proxy.this.endpoint
}

output "secret_arn" {
  description = "Secrets Manager ARN for DB credentials"
  value       = aws_secretsmanager_secret.db_credentials.arn
}

output "kms_key_arn" {
  description = "KMS key ARN used for Aurora encryption"
  value       = aws_kms_key.aurora.arn
}
