output "cloudfront_domain" {
  description = "CloudFront distribution domain name"
  value       = module.cloudfront.distribution_domain
}

output "api_gateway_url" {
  description = "API Gateway invoke URL"
  value       = module.api_gateway.invoke_url
}

output "aurora_proxy_endpoint" {
  description = "RDS Proxy endpoint"
  value       = module.aurora.proxy_endpoint
}

output "redis_endpoint" {
  description = "ElastiCache Redis primary endpoint"
  value       = module.elasticache.primary_endpoint
}

output "opensearch_endpoint" {
  description = "OpenSearch domain endpoint"
  value       = module.opensearch.domain_endpoint
}

output "cognito_user_pool_id" {
  description = "Cognito User Pool ID"
  value       = module.cognito.user_pool_id
}

output "cognito_client_id" {
  description = "Cognito User Pool Client ID"
  value       = module.cognito.client_id
}
