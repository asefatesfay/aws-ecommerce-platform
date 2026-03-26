terraform {
  required_version = ">= 1.7.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project
      Environment = var.environment
      ManagedBy   = "terraform"
    }
  }
}

locals {
  full_name = "${var.project}-${var.environment}"

  services = {
    auth           = { port = 8001 }
    catalog        = { port = 8002 }
    cart           = { port = 8003 }
    order          = { port = 8004 }
    payment        = { port = 8005 }
    search         = { port = 8006 }
    recommendation = { port = 8007 }
    inventory      = { port = 8008 }
    admin          = { port = 8009 }
  }
}

# ── VPC ───────────────────────────────────────────────────────────────────────

module "vpc" {
  source = "../../modules/vpc"

  project            = var.project
  environment        = var.environment
  vpc_cidr           = "10.0.0.0/16"
  azs                = var.azs
  single_nat_gateway = true
}

# ── ECS Cluster ───────────────────────────────────────────────────────────────

resource "aws_ecs_cluster" "main" {
  name = "${local.full_name}-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_ecs_cluster_capacity_providers" "main" {
  cluster_name       = aws_ecs_cluster.main.name
  capacity_providers = ["FARGATE", "FARGATE_SPOT"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}

# ── IAM Roles ─────────────────────────────────────────────────────────────────

resource "aws_iam_role" "ecs_execution" {
  name = "${local.full_name}-ecs-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_iam_role_policy_attachment" "ecs_execution_managed" {
  role       = aws_iam_role.ecs_execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy" "ecs_execution_secrets" {
  name = "${local.full_name}-ecs-execution-secrets"
  role = aws_iam_role.ecs_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue", "kms:Decrypt"]
        Resource = ["*"]
      }
    ]
  })
}

resource "aws_iam_role" "ecs_task" {
  name = "${local.full_name}-ecs-task-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_iam_role_policy" "ecs_task_permissions" {
  name = "${local.full_name}-ecs-task-permissions"
  role = aws_iam_role.ecs_task.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sns:Publish",
          "sqs:SendMessage",
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes",
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem",
          "dynamodb:Query",
          "dynamodb:Scan",
          "secretsmanager:GetSecretValue",
          "kms:Decrypt",
          "kms:GenerateDataKey",
          "es:ESHttp*",
          "xray:PutTraceSegments",
          "xray:PutTelemetryRecords",
          "cloudwatch:PutMetricData",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
        ]
        Resource = ["*"]
      }
    ]
  })
}

# ── ALB ───────────────────────────────────────────────────────────────────────

resource "aws_alb" "main" {
  name               = "${local.full_name}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [module.vpc.alb_sg_id]
  subnets            = module.vpc.public_subnet_ids

  enable_deletion_protection = false
  enable_http2               = true

  access_logs {
    bucket  = aws_s3_bucket.alb_logs.bucket
    prefix  = "alb"
    enabled = true
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket" "alb_logs" {
  bucket        = "${local.full_name}-alb-logs"
  force_destroy = true

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket_public_access_block" "alb_logs" {
  bucket                  = aws_s3_bucket.alb_logs.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

data "aws_elb_service_account" "main" {}

resource "aws_s3_bucket_policy" "alb_logs" {
  bucket = aws_s3_bucket.alb_logs.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = data.aws_elb_service_account.main.arn }
        Action    = "s3:PutObject"
        Resource  = "${aws_s3_bucket.alb_logs.arn}/alb/AWSLogs/*"
      }
    ]
  })
}

# HTTP → HTTPS redirect
resource "aws_alb_listener" "http" {
  load_balancer_arn = aws_alb.main.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "redirect"
    redirect {
      port        = "443"
      protocol    = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}

# HTTPS listener — default 404
resource "aws_alb_listener" "https" {
  load_balancer_arn = aws_alb.main.arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-TLS13-1-2-2021-06"
  certificate_arn   = aws_acm_certificate.this.arn

  default_action {
    type = "fixed-response"
    fixed_response {
      content_type = "application/json"
      message_body = "{\"error\": \"not found\"}"
      status_code  = "404"
    }
  }
}

# Self-signed cert placeholder — replace with ACM cert in real deployment
resource "aws_acm_certificate" "this" {
  domain_name       = "${local.full_name}.example.com"
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# ── ALB Target Groups (one per service) ───────────────────────────────────────

resource "aws_alb_target_group" "services" {
  for_each = local.services

  name        = "${local.full_name}-${each.key}-tg"
  port        = each.value.port
  protocol    = "HTTP"
  vpc_id      = module.vpc.vpc_id
  target_type = "ip"

  health_check {
    enabled             = true
    healthy_threshold   = 2
    unhealthy_threshold = 3
    timeout             = 5
    interval            = 30
    path                = "/health"
    matcher             = "200"
  }

  deregistration_delay = 30

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
    Service     = each.key
  }
}

# ALB listener rules — route by path prefix /service-name/*
resource "aws_alb_listener_rule" "services" {
  for_each = local.services

  listener_arn = aws_alb_listener.https.arn
  priority     = 100 + index(keys(local.services), each.key)

  action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.services[each.key].arn
  }

  condition {
    path_pattern {
      values = ["/${each.key}/*", "/${each.key}"]
    }
  }
}

# ── DynamoDB (Cart / Sessions) ────────────────────────────────────────────────

resource "aws_dynamodb_table" "cart" {
  name         = "${local.full_name}-cart"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "PK"
  range_key    = "SK"

  attribute {
    name = "PK"
    type = "S"
  }

  attribute {
    name = "SK"
    type = "S"
  }

  ttl {
    attribute_name = "ttl"
    enabled        = true
  }

  point_in_time_recovery {
    enabled = true
  }

  server_side_encryption {
    enabled = true
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# ── Modules ───────────────────────────────────────────────────────────────────

module "aurora" {
  source = "../../modules/aurora"

  project            = var.project
  environment        = var.environment
  db_name            = "ecommerce"
  db_username        = "dbadmin"
  instance_class     = "db.t3.medium"
  instance_count     = 1
  private_subnet_ids = module.vpc.private_subnet_ids
  aurora_sg_id       = module.vpc.aurora_sg_id
  vpc_id             = module.vpc.vpc_id
}

module "elasticache" {
  source = "../../modules/elasticache"

  project            = var.project
  environment        = var.environment
  node_type          = "cache.t3.micro"
  num_cache_nodes    = 1
  private_subnet_ids = module.vpc.private_subnet_ids
  redis_sg_id        = module.vpc.redis_sg_id
}

module "opensearch" {
  source = "../../modules/opensearch"

  project                  = var.project
  environment              = var.environment
  instance_type            = "t3.small.search"
  instance_count           = 1
  dedicated_master_enabled = false
  ebs_volume_size          = 20
  private_subnet_ids       = module.vpc.private_subnet_ids
  opensearch_sg_id         = module.vpc.opensearch_sg_id
  vpc_id                   = module.vpc.vpc_id
  ecs_task_role_arn        = aws_iam_role.ecs_task.arn
}

module "cognito" {
  source = "../../modules/cognito"

  project       = var.project
  environment   = var.environment
  callback_urls = ["https://localhost:3000/auth/callback"]
  logout_urls   = ["https://localhost:3000"]
}

module "messaging" {
  source = "../../modules/messaging"

  project     = var.project
  environment = var.environment
}

module "waf_regional" {
  source = "../../modules/waf"

  project         = var.project
  environment     = var.environment
  scope           = "REGIONAL"
  api_gateway_arn = "${module.api_gateway.execution_arn}/${module.api_gateway.stage_name}/*/*"
}

module "api_gateway" {
  source = "../../modules/api-gateway"

  project               = var.project
  environment           = var.environment
  alb_dns_name          = aws_alb.main.dns_name
  cognito_user_pool_arn = module.cognito.user_pool_arn
  stage_name            = "v1"
}

module "cloudfront" {
  source = "../../modules/cloudfront"

  project         = var.project
  environment     = var.environment
  api_gateway_url = module.api_gateway.invoke_url
  price_class     = "PriceClass_100"
}

# ── ECS Services ──────────────────────────────────────────────────────────────

module "ecs_auth" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "auth"
  container_image      = "${var.ecr_repository_url}/auth:latest"
  container_port       = 8001
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["auth"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT          = var.environment
    COGNITO_USER_POOL_ID = module.cognito.user_pool_id
    COGNITO_CLIENT_ID    = module.cognito.client_id
  }

  secrets = {
    DB_SECRET_ARN = module.aurora.secret_arn
  }
}

module "ecs_catalog" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "catalog"
  container_image      = "${var.ecr_repository_url}/catalog:latest"
  container_port       = 8002
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["catalog"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT          = var.environment
    REDIS_HOST           = module.elasticache.primary_endpoint
    REDIS_PORT           = "6379"
    SNS_PRODUCT_TOPIC    = module.messaging.product_events_topic_arn
  }

  secrets = {
    DB_SECRET_ARN = module.aurora.secret_arn
  }
}

module "ecs_cart" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "cart"
  container_image      = "${var.ecr_repository_url}/cart:latest"
  container_port       = 8003
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["cart"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT      = var.environment
    DYNAMODB_TABLE   = aws_dynamodb_table.cart.name
    REDIS_HOST       = module.elasticache.primary_endpoint
    REDIS_PORT       = "6379"
  }
}

module "ecs_order" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "order"
  container_image      = "${var.ecr_repository_url}/order:latest"
  container_port       = 8004
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["order"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT           = var.environment
    SNS_ORDER_TOPIC       = module.messaging.order_events_topic_arn
    SQS_ORDER_PAYMENT_URL = module.messaging.order_payment_queue_url
  }

  secrets = {
    DB_SECRET_ARN = module.aurora.secret_arn
  }
}

module "ecs_payment" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "payment"
  container_image      = "${var.ecr_repository_url}/payment:latest"
  container_port       = 8005
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["payment"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT             = var.environment
    SNS_PAYMENT_TOPIC       = module.messaging.payment_events_topic_arn
  }

  secrets = {
    DB_SECRET_ARN          = module.aurora.secret_arn
    STRIPE_SECRET_KEY      = "arn:aws:secretsmanager:${var.aws_region}:*:secret:${local.full_name}/stripe/secret-key"
    STRIPE_WEBHOOK_SECRET  = "arn:aws:secretsmanager:${var.aws_region}:*:secret:${local.full_name}/stripe/webhook-secret"
  }
}

module "ecs_search" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "search"
  container_image      = "${var.ecr_repository_url}/search:latest"
  container_port       = 8006
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["search"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT           = var.environment
    OPENSEARCH_ENDPOINT   = module.opensearch.domain_endpoint
    REDIS_HOST            = module.elasticache.primary_endpoint
    REDIS_PORT            = "6379"
    SQS_SEARCH_QUEUE_URL  = module.messaging.search_product_queue_url
  }
}

module "ecs_recommendation" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "recommendation"
  container_image      = "${var.ecr_repository_url}/recommendation:latest"
  container_port       = 8007
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["recommendation"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT         = var.environment
    OPENSEARCH_ENDPOINT = module.opensearch.domain_endpoint
    REDIS_HOST          = module.elasticache.primary_endpoint
    REDIS_PORT          = "6379"
  }
}

module "ecs_inventory" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "inventory"
  container_image      = "${var.ecr_repository_url}/inventory:latest"
  container_port       = 8008
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["inventory"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT                    = var.environment
    SNS_INVENTORY_TOPIC            = module.messaging.inventory_events_topic_arn
    SQS_INVENTORY_ORDER_QUEUE_URL  = module.messaging.inventory_order_queue_url
  }

  secrets = {
    DB_SECRET_ARN = module.aurora.secret_arn
  }
}

module "ecs_admin" {
  source = "../../modules/ecs-service"

  project              = var.project
  environment          = var.environment
  service_name         = "admin"
  container_image      = "${var.ecr_repository_url}/admin:latest"
  container_port       = 8009
  cpu                  = 256
  memory               = 512
  desired_count        = 1
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  ecs_sg_id            = module.vpc.ecs_sg_id
  alb_target_group_arn = aws_alb_target_group.services["admin"].arn
  cluster_arn          = aws_ecs_cluster.main.arn
  execution_role_arn   = aws_iam_role.ecs_execution.arn
  task_role_arn        = aws_iam_role.ecs_task.arn

  environment_variables = {
    ENVIRONMENT          = var.environment
    COGNITO_USER_POOL_ID = module.cognito.user_pool_id
    ADMINS_GROUP         = module.cognito.admins_group_name
  }

  secrets = {
    DB_SECRET_ARN = module.aurora.secret_arn
  }
}

# ── CloudWatch Alarms ─────────────────────────────────────────────────────────

resource "aws_cloudwatch_metric_alarm" "alb_5xx" {
  alarm_name          = "${local.full_name}-alb-5xx-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "HTTPCode_ELB_5XX_Count"
  namespace           = "AWS/ApplicationELB"
  period              = 60
  statistic           = "Sum"
  threshold           = 10
  alarm_description   = "ALB 5XX error rate too high"
  treat_missing_data  = "notBreaching"

  dimensions = {
    LoadBalancer = aws_alb.main.arn_suffix
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_cloudwatch_metric_alarm" "aurora_cpu" {
  alarm_name          = "${local.full_name}-aurora-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 3
  metric_name         = "CPUUtilization"
  namespace           = "AWS/RDS"
  period              = 60
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Aurora CPU utilization too high"
  treat_missing_data  = "notBreaching"

  dimensions = {
    DBClusterIdentifier = "${local.full_name}-aurora"
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_cloudwatch_metric_alarm" "redis_cpu" {
  alarm_name          = "${local.full_name}-redis-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 3
  metric_name         = "EngineCPUUtilization"
  namespace           = "AWS/ElastiCache"
  period              = 60
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Redis CPU utilization too high"
  treat_missing_data  = "notBreaching"

  dimensions = {
    ReplicationGroupId = "${local.full_name}-redis"
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_cloudwatch_metric_alarm" "dlq_messages" {
  for_each = {
    inventory = module.messaging.inventory_order_queue_arn
    payment   = module.messaging.order_payment_queue_arn
    search    = module.messaging.search_product_queue_arn
    ses       = module.messaging.ses_notification_queue_arn
  }

  alarm_name          = "${local.full_name}-dlq-${each.key}-messages"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ApproximateNumberOfMessagesVisible"
  namespace           = "AWS/SQS"
  period              = 300
  statistic           = "Sum"
  threshold           = 0
  alarm_description   = "Messages in ${each.key} DLQ"
  treat_missing_data  = "notBreaching"

  dimensions = {
    QueueName = "${local.full_name}-${each.key}-dlq"
  }

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
