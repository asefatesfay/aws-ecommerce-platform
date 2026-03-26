output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "alb_sg_id" {
  description = "ALB security group ID"
  value       = aws_security_group.alb.id
}

output "ecs_sg_id" {
  description = "ECS security group ID"
  value       = aws_security_group.ecs.id
}

output "aurora_sg_id" {
  description = "Aurora security group ID"
  value       = aws_security_group.aurora.id
}

output "redis_sg_id" {
  description = "Redis security group ID"
  value       = aws_security_group.redis.id
}

output "opensearch_sg_id" {
  description = "OpenSearch security group ID"
  value       = aws_security_group.opensearch.id
}
