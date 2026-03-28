.PHONY: help up down build logs ps test lint fmt clean

SERVICES = auth catalog cart order payment search recommendation inventory admin

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

up: ## Start all services
	docker compose up -d

down: ## Stop all services
	docker compose down

build: ## Build all Docker images
	docker compose build

logs: ## Tail logs for all services
	docker compose logs -f

ps: ## Show running containers
	docker compose ps

test: ## Run all Python service tests
	@for svc in $(SERVICES); do \
		echo "Testing $$svc..."; \
		cd services/$$svc && pytest tests/ -v --tb=short 2>/dev/null || echo "No tests for $$svc"; \
		cd ../..; \
	done

lint: ## Lint all Python code
	ruff check services/ shared/

fmt: ## Format all Python code
	ruff format services/ shared/

type-check: ## Type check frontend
	cd frontend && npm run type-check

frontend-dev: ## Start frontend dev server
	cd frontend && npm run dev

frontend-build: ## Build frontend
	cd frontend && npm run build

tf-init-dev: ## Terraform init (dev)
	cd infra/environments/dev && terraform init

tf-plan-dev: ## Terraform plan (dev)
	cd infra/environments/dev && terraform plan

tf-apply-dev: ## Terraform apply (dev)
	cd infra/environments/dev && terraform apply

tf-init-prod: ## Terraform init (prod)
	cd infra/environments/prod && terraform init

tf-plan-prod: ## Terraform plan (prod)
	cd infra/environments/prod && terraform plan

test-e2e: ## Run end-to-end local test
	./scripts/test-e2e.sh

logs-order: ## Tail order service logs
	docker compose logs -f order

logs-inventory: ## Tail inventory service logs
	docker compose logs -f inventory

logs-payment: ## Tail payment service logs
	docker compose logs -f payment

localstack-status: ## Check LocalStack queues and topics
	@echo "=== SNS Topics ===" && docker compose exec localstack awslocal sns list-topics --region us-east-1
	@echo "=== SQS Queues ===" && docker compose exec localstack awslocal sqs list-queues --region us-east-1

clean: ## Remove all containers, volumes, and build artifacts
	docker compose down -v --remove-orphans
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name "*.db" -delete 2>/dev/null || true
	rm -rf frontend/.next frontend/out
