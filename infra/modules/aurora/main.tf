locals {
  full_name = "${var.project}-${var.environment}"
  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# ── KMS Key ───────────────────────────────────────────────────────────────────

resource "aws_kms_key" "aurora" {
  description             = "${local.full_name} Aurora encryption key"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  tags = merge(local.tags, { Name = "${local.full_name}-aurora-kms" })
}

resource "aws_kms_alias" "aurora" {
  name          = "alias/${local.full_name}-aurora"
  target_key_id = aws_kms_key.aurora.key_id
}

# ── Secrets Manager ───────────────────────────────────────────────────────────

resource "random_password" "db" {
  length           = 32
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

resource "aws_secretsmanager_secret" "db_credentials" {
  name                    = "${local.full_name}/aurora/credentials"
  description             = "Aurora PostgreSQL credentials for ${local.full_name}"
  recovery_window_in_days = 30
  kms_key_id              = aws_kms_key.aurora.arn

  tags = local.tags
}

resource "aws_secretsmanager_secret_version" "db_credentials" {
  secret_id = aws_secretsmanager_secret.db_credentials.id
  secret_string = jsonencode({
    username = var.db_username
    password = random_password.db.result
    host     = aws_rds_cluster.this.endpoint
    port     = 5432
    dbname   = var.db_name
  })
}

# ── Subnet Group ──────────────────────────────────────────────────────────────

resource "aws_db_subnet_group" "this" {
  name        = "${local.full_name}-aurora-subnet-group"
  description = "Aurora subnet group for ${local.full_name}"
  subnet_ids  = var.private_subnet_ids

  tags = merge(local.tags, { Name = "${local.full_name}-aurora-subnet-group" })
}

# ── Cluster Parameter Group ───────────────────────────────────────────────────

resource "aws_rds_cluster_parameter_group" "this" {
  name        = "${local.full_name}-aurora-pg15"
  family      = "aurora-postgresql15"
  description = "Aurora PostgreSQL 15 parameter group for ${local.full_name}"

  parameter {
    name  = "log_connections"
    value = "1"
  }

  parameter {
    name  = "log_disconnections"
    value = "1"
  }

  parameter {
    name  = "log_min_duration_statement"
    value = "1000"
  }

  tags = local.tags
}

# ── Aurora Cluster ────────────────────────────────────────────────────────────

resource "aws_rds_cluster" "this" {
  cluster_identifier              = "${local.full_name}-aurora"
  engine                          = "aurora-postgresql"
  engine_version                  = "15.4"
  database_name                   = var.db_name
  master_username                 = var.db_username
  master_password                 = random_password.db.result
  db_subnet_group_name            = aws_db_subnet_group.this.name
  vpc_security_group_ids          = [var.aurora_sg_id]
  db_cluster_parameter_group_name = aws_rds_cluster_parameter_group.this.name
  storage_encrypted               = true
  kms_key_id                      = aws_kms_key.aurora.arn
  deletion_protection             = true
  skip_final_snapshot             = false
  final_snapshot_identifier       = "${local.full_name}-aurora-final-snapshot"
  backup_retention_period         = 7
  preferred_backup_window         = "03:00-04:00"
  preferred_maintenance_window    = "sun:04:00-sun:05:00"
  enabled_cloudwatch_logs_exports = ["postgresql"]
  apply_immediately               = false

  tags = local.tags
}

# ── Cluster Instances ─────────────────────────────────────────────────────────

resource "aws_rds_cluster_instance" "this" {
  count                = var.instance_count
  identifier           = "${local.full_name}-aurora-${count.index == 0 ? "writer" : "reader-${count.index}"}"
  cluster_identifier   = aws_rds_cluster.this.id
  instance_class       = var.instance_class
  engine               = aws_rds_cluster.this.engine
  engine_version       = aws_rds_cluster.this.engine_version
  db_subnet_group_name = aws_db_subnet_group.this.name
  publicly_accessible  = false

  performance_insights_enabled          = true
  performance_insights_retention_period = 7
  monitoring_interval                   = 60
  monitoring_role_arn                   = aws_iam_role.rds_enhanced_monitoring.arn

  tags = merge(local.tags, {
    Name = "${local.full_name}-aurora-${count.index == 0 ? "writer" : "reader-${count.index}"}"
    Role = count.index == 0 ? "writer" : "reader"
  })
}

# ── Enhanced Monitoring Role ──────────────────────────────────────────────────

resource "aws_iam_role" "rds_enhanced_monitoring" {
  name = "${local.full_name}-rds-monitoring-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "monitoring.rds.amazonaws.com" }
    }]
  })

  tags = local.tags
}

resource "aws_iam_role_policy_attachment" "rds_enhanced_monitoring" {
  role       = aws_iam_role.rds_enhanced_monitoring.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole"
}

# ── RDS Proxy ─────────────────────────────────────────────────────────────────

resource "aws_iam_role" "rds_proxy" {
  name = "${local.full_name}-rds-proxy-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "rds.amazonaws.com" }
    }]
  })

  tags = local.tags
}

resource "aws_iam_role_policy" "rds_proxy_secrets" {
  name = "${local.full_name}-rds-proxy-secrets-policy"
  role = aws_iam_role.rds_proxy.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue"]
        Resource = [aws_secretsmanager_secret.db_credentials.arn]
      },
      {
        Effect   = "Allow"
        Action   = ["kms:Decrypt"]
        Resource = [aws_kms_key.aurora.arn]
        Condition = {
          StringEquals = {
            "kms:ViaService" = "secretsmanager.${data.aws_region.current.name}.amazonaws.com"
          }
        }
      }
    ]
  })
}

resource "aws_db_proxy" "this" {
  name                   = "${local.full_name}-rds-proxy"
  debug_logging          = false
  engine_family          = "POSTGRESQL"
  idle_client_timeout    = 1800
  require_tls            = true
  role_arn               = aws_iam_role.rds_proxy.arn
  vpc_security_group_ids = [var.aurora_sg_id]
  vpc_subnet_ids         = var.private_subnet_ids

  auth {
    auth_scheme = "SECRETS"
    description = "Aurora credentials"
    iam_auth    = "DISABLED"
    secret_arn  = aws_secretsmanager_secret.db_credentials.arn
  }

  tags = local.tags
}

resource "aws_db_proxy_default_target_group" "this" {
  db_proxy_name = aws_db_proxy.this.name

  connection_pool_config {
    connection_borrow_timeout    = 120
    max_connections_percent      = 100
    max_idle_connections_percent = 50
  }
}

resource "aws_db_proxy_target" "this" {
  db_cluster_identifier = aws_rds_cluster.this.id
  db_proxy_name         = aws_db_proxy.this.name
  target_group_name     = aws_db_proxy_default_target_group.this.name
}

data "aws_region" "current" {}
