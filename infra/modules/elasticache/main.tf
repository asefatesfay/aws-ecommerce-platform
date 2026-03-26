locals {
  full_name = "${var.project}-${var.environment}"
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_elasticache_subnet_group" "this" {
  name        = "${local.full_name}-redis-subnet-group"
  description = "Redis subnet group for ${local.full_name}"
  subnet_ids  = var.private_subnet_ids

  tags = local.tags
}

resource "aws_elasticache_replication_group" "this" {
  replication_group_id       = "${local.full_name}-redis"
  description                = "Redis cluster for ${local.full_name}"
  node_type                  = var.node_type
  num_cache_clusters         = var.num_cache_nodes
  parameter_group_name       = "default.redis7"
  engine_version             = "7.1"
  port                       = 6379
  subnet_group_name          = aws_elasticache_subnet_group.this.name
  security_group_ids         = [var.redis_sg_id]
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  automatic_failover_enabled = var.num_cache_nodes > 1 ? true : false
  multi_az_enabled           = var.num_cache_nodes > 1 ? true : false
  snapshot_retention_limit   = 1
  snapshot_window            = "05:00-06:00"
  maintenance_window         = "sun:06:00-sun:07:00"
  apply_immediately          = false

  log_delivery_configuration {
    destination      = aws_cloudwatch_log_group.redis_slow.name
    destination_type = "cloudwatch-logs"
    log_format       = "text"
    log_type         = "slow-log"
  }

  tags = local.tags
}

resource "aws_cloudwatch_log_group" "redis_slow" {
  name              = "/elasticache/${local.full_name}/slow-log"
  retention_in_days = 14

  tags = local.tags
}
