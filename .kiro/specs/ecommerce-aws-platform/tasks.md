# Implementation Plan: Ecommerce AWS Platform

## Overview

Incremental implementation of a cloud-native ecommerce platform using FastAPI (Python) microservices, Next.js frontend, and AWS managed services. Tasks are ordered to build shared infrastructure first, then individual services, then integration wiring.

## Tasks

- [x] 1. Project scaffolding and shared infrastructure
  - Create monorepo directory structure: `services/{auth,catalog,cart,order,payment,search,recommendation,inventory,admin}`, `frontend/`, `infra/`
  - Create shared `pyproject.toml` / `requirements.txt` with FastAPI, SQLAlchemy 2.0 async, asyncpg, boto3, aioboto3, redis, opensearch-py, stripe, pydantic v2, alembic, tenacity, hypothesis, pytest-asyncio
  - Implement shared `app/db.py` (async SQLAlchemy engine + session factory), `app/cache.py` (async Redis pool), `app/settings.py` (Pydantic BaseSettings reading from env/Secrets Manager)
  - Implement shared `app/events/publisher.py` SNS publish helper
  - Implement shared FastAPI lifespan bootstrap (`app/main.py` template) with startup dependency checks and `/health` endpoint
  - _Requirements: 13.8, 14.6_

- [ ] 2. Database schema and migrations
  - [ ] 2.1 Define SQLAlchemy ORM models for `users`, `addresses`, `products`, `categories`, `orders`, `order_items`, `payments`, `inventory` tables with all fields, constraints, and relationships from the data models
    - Include `version` column on `inventory` for optimistic locking
    - Include JSONB columns: `shipping_address` on orders, `attributes` on products, `metadata` on payments
    - _Requirements: 1.8, 2.7, 2.8, 4.2, 4.3, 4.12, 5.9, 5.10, 8.9_
  - [ ]* 2.2 Write property test for Order total mathematical invariant
    - **Property 11: Order Total Mathematical Invariant**
    - **Validates: Requirements 4.2, 4.3**
  - [ ]* 2.3 Write property test for Inventory availability invariant
    - **Property 23: Inventory Availability Invariant**
    - **Validates: Requirements 8.1, 8.2, 8.9**
  - [ ] 2.4 Create Alembic migration for initial schema
    - _Requirements: 2.1, 4.1, 5.9, 8.1_

- [ ] 3. Auth Service
  - [ ] 3.1 Implement `AuthRouter` with `POST /auth/register`, `POST /auth/login`, `POST /auth/refresh`, `GET /auth/profile`, `PATCH /auth/profile`
    - Delegate registration and login to Cognito User Pools via boto3 `cognito-idp`
    - Store extended profile in Aurora `users` table with `cognito_sub` as unique FK
    - Assign `role = "customer"` on registration
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.8, 1.9_
  - [ ]* 3.2 Write property test for User registration round-trip
    - **Property 1: User Registration Round-Trip**
    - **Validates: Requirements 1.1, 1.4, 1.8, 1.9**
  - [ ]* 3.3 Write property test for Token refresh round-trip
    - **Property 2: Token Refresh Round-Trip**
    - **Validates: Requirements 1.3, 1.7**
  - [ ]* 3.4 Write property test for Profile update round-trip
    - **Property 3: Profile Update Round-Trip**
    - **Validates: Requirements 1.5**
  - [ ]* 3.5 Write unit tests for invalid JWT rejection at API Gateway authorizer level
    - **Property 4: Invalid JWT Rejection**
    - **Validates: Requirements 1.6, 12.1**

- [ ] 4. Checkpoint — Auth Service
  - Ensure all Auth Service tests pass, ask the user if questions arise.

- [ ] 5. Catalog Service
  - [ ] 5.1 Implement `CatalogRouter` with `GET /catalog/products`, `GET /catalog/products/{id}`, `POST /catalog/products`, `PUT /catalog/products/{id}`, `DELETE /catalog/products/{id}`, `POST /catalog/products/{id}/images`, `GET /catalog/categories`
    - Enforce `price > 0`, unique `sku`, and at least one image for active products
    - Cache product pages in Redis with TTL 10 min; invalidate on update/delete
    - Upload images to S3 and return CloudFront URL
    - Publish `product.updated` event to SNS on create, update, and delete
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10_
  - [ ]* 5.2 Write property test for Product CRUD round-trip
    - **Property 5: Product CRUD Round-Trip**
    - **Validates: Requirements 2.1, 2.2, 2.3**
  - [ ]* 5.3 Write property test for Product validation invariants
    - **Property 6: Product Validation Invariants**
    - **Validates: Requirements 2.7, 2.8, 2.9**
  - [ ]* 5.4 Write property test for Pagination upper bound
    - **Property 7: Pagination Upper Bound**
    - **Validates: Requirements 2.6, 4.9, 6.10, 7.7, 9.4**
  - [ ]* 5.5 Write property test for Cache-then-store round-trip
    - **Property 8: Cache-Then-Store Round-Trip**
    - **Validates: Requirements 2.5, 6.2, 6.3, 7.5**

- [ ] 6. Cart Service
  - [ ] 6.1 Implement `CartRouter` with `GET /cart/{user_id}`, `POST /cart/{user_id}/items`, `PUT /cart/{user_id}/items/{item_id}`, `DELETE /cart/{user_id}/items/{item_id}`, `DELETE /cart/{user_id}`
    - Store cart in DynamoDB with PK `USER#<user_id>`, SK `CART`, TTL 30 days
    - Cache active carts in Redis as read-through layer
    - Validate product availability against Inventory Service before adding items
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8_
  - [ ]* 6.2 Write property test for Cart mutation round-trip
    - **Property 9: Cart Mutation Round-Trip**
    - **Validates: Requirements 3.1, 3.4, 3.5, 3.6**
  - [ ]* 6.3 Write property test for Cart DynamoDB structure invariant
    - **Property 10: Cart DynamoDB Structure Invariant**
    - **Validates: Requirements 3.7, 3.8**

- [ ] 7. Inventory Service
  - [ ] 7.1 Implement `InventoryRouter` with `GET /inventory/{product_id}`, `POST /inventory/reserve`, `DELETE /inventory/reservations/{id}`, `PATCH /inventory/{product_id}/adjust`, `GET /inventory/low-stock`
    - Implement optimistic locking with `version` field and `SELECT FOR UPDATE` on reserve
    - Retry up to 3 times on `OptimisticLockError` before returning HTTP 409
    - Publish `inventory.low_stock` event to SNS when `quantity_available < reorder_threshold`
    - _Requirements: 8.1, 8.2, 8.3, 8.6, 8.7, 8.8, 8.9_
  - [ ] 7.2 Implement SQS consumer for `order.confirmed` events — deduct reserved stock from `quantity_on_hand`
    - Process in batches of up to 10 messages
    - _Requirements: 8.4, 13.5_
  - [ ] 7.3 Implement SQS consumer for `order.cancelled` events — release reservation and restore `quantity_available`
    - _Requirements: 8.5_
  - [ ] 7.4 Implement EventBridge-triggered daily stock reconciliation handler
    - _Requirements: 8.10_
  - [ ]* 7.5 Write property test for Inventory availability invariant
    - **Property 23: Inventory Availability Invariant**
    - **Validates: Requirements 8.1, 8.2, 8.9**
  - [ ]* 7.6 Write property test for Reservation and release round-trip
    - **Property 24: Reservation and Release Round-Trip**
    - **Validates: Requirements 8.4, 8.5**
  - [ ]* 7.7 Write property test for Concurrent reservation retry and failure
    - **Property 27: Concurrent Reservation Retry and Failure**
    - **Validates: Requirements 8.3, 14.3**
  - [ ]* 7.8 Write property test for Low-stock threshold and listing
    - **Property 25: Low-Stock Threshold and Listing**
    - **Validates: Requirements 8.6, 8.8**
  - [ ]* 7.9 Write property test for Inventory adjustment correctness
    - **Property 26: Inventory Adjustment Correctness**
    - **Validates: Requirements 8.7**
  - [ ]* 7.10 Write property test for SQS batch processing completeness
    - **Property 32: SQS Batch Processing Completeness**
    - **Validates: Requirements 13.5**

- [ ] 8. Checkpoint — Inventory Service
  - Ensure all Inventory Service tests pass, ask the user if questions arise.

- [ ] 9. Order Service
  - [ ] 9.1 Implement `OrderRouter` with `POST /orders`, `GET /orders/{id}`, `GET /orders` (paginated), `PATCH /orders/{id}/status`, `POST /orders/{id}/cancel`
    - Enforce state machine transitions from `ORDER_STATE_MACHINE`; reject invalid transitions with HTTP 422
    - Persist `shipping_address` as immutable JSONB snapshot
    - Publish `order.created`, `order.confirmed`, `order.cancelled` events to SNS
    - Return HTTP 409 with unavailable items list when stock is insufficient at checkout
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 14.1_
  - [ ] 9.2 Implement SQS consumer for `payment.succeeded` events — transition order to `confirmed`
    - _Requirements: 4.5_
  - [ ] 9.3 Implement SQS consumer for `payment.failed` events — transition order to `cancelled`
    - _Requirements: 4.6_
  - [ ]* 9.4 Write property test for Order state machine validity
    - **Property 12: Order State Machine Validity**
    - **Validates: Requirements 4.7, 4.8**
  - [ ]* 9.5 Write property test for Order creation round-trip with immutable snapshot
    - **Property 13: Order Creation Round-Trip with Immutable Snapshot**
    - **Validates: Requirements 4.1, 4.12**
  - [ ]* 9.6 Write property test for Checkout insufficient stock response
    - **Property 30: Checkout Insufficient Stock Response**
    - **Validates: Requirements 14.1**
  - [ ]* 9.7 Write property test for Pagination upper bound (orders)
    - **Property 7: Pagination Upper Bound**
    - **Validates: Requirements 4.9**

- [ ] 10. Payment Service
  - [ ] 10.1 Implement `PaymentRouter` with `POST /payments/intent`, `POST /payments/webhook`, `GET /payments/{id}`, `POST /payments/{id}/refund`
    - Create Stripe PaymentIntent server-side; never receive raw card data
    - Verify webhook signature with `stripe.Webhook.construct_event()` before processing; return HTTP 400 on failure
    - Detect duplicate webhooks via `stripe_payment_intent_id` uniqueness; return HTTP 200 without re-processing
    - Publish `payment.succeeded` / `payment.failed` events to SNS
    - Persist all payment records in Aurora
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10_
  - [ ]* 10.2 Write property test for Webhook idempotency
    - **Property 15: Webhook Idempotency**
    - **Validates: Requirements 5.7**
  - [ ]* 10.3 Write property test for Webhook signature rejection
    - **Property 16: Webhook Signature Rejection**
    - **Validates: Requirements 5.3, 5.4**
  - [ ]* 10.4 Write property test for Payment record persistence and uniqueness
    - **Property 17: Payment Record Persistence and Uniqueness**
    - **Validates: Requirements 5.9, 5.10**
  - [ ]* 10.5 Write property test for SNS event publishing on order and payment transitions
    - **Property 14: SNS Event Publishing on Order and Payment Transitions**
    - **Validates: Requirements 4.4, 4.5, 4.6, 4.11, 5.5, 5.6**

- [ ] 11. Checkpoint — Order and Payment Services
  - Ensure all Order and Payment Service tests pass, ask the user if questions arise.

- [ ] 12. Search Service
  - [ ] 12.1 Implement `SearchRouter` with `GET /search`, `GET /search/autocomplete`
    - Execute full-text + faceted OpenSearch queries
    - Cache results in Redis with TTL 5 min using deterministic hash of `(query, filters, page, limit)`
    - Enforce `page >= 1`, `1 <= limit <= 100`, `price_min <= price_max`
    - Return HTTP 503 with `Retry-After` header when OpenSearch is unavailable
    - Apply exponential backoff retry via `tenacity` on OpenSearch 5xx errors
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.7, 6.8, 6.9, 6.10, 6.11, 13.7_
  - [ ] 12.2 Implement `index_product` and `delete_product_index` functions and SQS consumer for `product.updated` events
    - Build product document using `build_product_document` including `suggest` field for autocomplete
    - _Requirements: 6.5, 6.6_
  - [ ]* 12.3 Write property test for Search response structure
    - **Property 18: Search Response Structure**
    - **Validates: Requirements 6.1, 6.9, 6.10**
  - [ ]* 12.4 Write property test for Search input validation
    - **Property 19: Search Input Validation**
    - **Validates: Requirements 6.7, 6.8**
  - [ ]* 12.5 Write property test for Search index synchronization
    - **Property 20: Search Index Synchronization**
    - **Validates: Requirements 6.5, 6.6**
  - [ ]* 12.6 Write property test for Search retry on OpenSearch failure
    - **Property 33: Search Retry on OpenSearch Failure**
    - **Validates: Requirements 13.7**

- [ ] 13. Recommendation Service
  - [ ] 13.1 Implement `RecommendationRouter` with `GET /recommendations/{user_id}`, `GET /recommendations/similar/{product_id}`, `POST /recommendations/events`
    - Call Amazon Personalize `GetRecommendations`; fall back to OpenSearch popularity ranking when unavailable or no history
    - Cache results in Redis per `user_id` with TTL 15 min
    - Enforce `1 <= limit <= 50`
    - Record user interaction events to Personalize event tracker
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7_
  - [ ]* 13.2 Write property test for Recommendation fallback
    - **Property 21: Recommendation Fallback**
    - **Validates: Requirements 7.2**
  - [ ]* 13.3 Write property test for Recommendation limit enforcement
    - **Property 22: Recommendation Limit Enforcement**
    - **Validates: Requirements 7.6, 7.7**

- [ ] 14. Admin Service
  - [ ] 14.1 Implement `AdminRouter` with `GET /admin/metrics`, `GET /admin/orders`, `POST /admin/orders/export`, `GET /admin/users`, `GET /admin/revenue`
    - Aggregate metrics from Aurora (order counts, revenue totals, user counts)
    - Generate CSV/Excel export, upload to S3, return presigned URL
    - Verify `cognito:groups` contains `"admins"` on every request; return HTTP 403 otherwise
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7_
  - [ ]* 14.2 Write property test for Admin authorization enforcement
    - **Property 28: Admin Authorization Enforcement**
    - **Validates: Requirements 9.6, 9.7**
  - [ ]* 14.3 Write property test for Revenue report date filter
    - **Property 29: Revenue Report Date Filter**
    - **Validates: Requirements 9.2**
  - [ ]* 14.4 Write property test for Pagination upper bound (admin orders and users)
    - **Property 7: Pagination Upper Bound**
    - **Validates: Requirements 9.4, 9.5**

- [ ] 15. Checkpoint — Search, Recommendation, and Admin Services
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 16. Next.js frontend
  - [ ] 16.1 Scaffold Next.js 14 App Router project with Tailwind CSS, Zustand for cart state, SWR for data fetching, and `@stripe/stripe-js` + Stripe Elements
    - Configure `next.config.js` to proxy `/api/*` to API Gateway
    - _Requirements: 11.1, 11.4_
  - [ ] 16.2 Implement product catalog pages: product listing with pagination, product detail page, category filter
    - Fetch from Catalog Service via SWR with `dedupingInterval`
    - _Requirements: 2.6, 11.1_
  - [ ] 16.3 Implement search page with `SearchBar` component, faceted filters, and autocomplete
    - _Requirements: 6.1, 6.4_
  - [ ] 16.4 Implement cart UI with Zustand store: add, update, remove, clear actions
    - _Requirements: 3.1, 3.4, 3.5, 3.6_
  - [ ] 16.5 Implement checkout page with Stripe Elements card input and `handleCheckout` flow
    - Call backend to create order + PaymentIntent, confirm payment client-side, redirect to confirmation page
    - _Requirements: 5.1, 5.2_
  - [ ] 16.6 Implement auth pages: register, login, profile; handle JWT storage and 401 → token refresh flow
    - _Requirements: 1.1, 1.2, 1.3, 1.7_
  - [ ] 16.7 Implement order history and order detail pages
    - _Requirements: 4.9, 4.10_
  - [ ] 16.8 Implement recommendations widget on product detail and home pages
    - _Requirements: 7.1, 7.3_

- [ ] 17. Infrastructure as Code (AWS CDK or Terraform)
  - [ ] 17.1 Define VPC with public subnets (ALB, NAT Gateway) and private subnets (ECS, Aurora, Redis, OpenSearch, DynamoDB)
    - _Requirements: 12.5, 12.6_
  - [ ] 17.2 Define ECS Fargate task definitions and services for all 9 microservices with Secrets Manager secret injection and target tracking auto-scaling (CPU 70%)
    - _Requirements: 13.1, 13.8_
  - [ ] 17.3 Define Aurora PostgreSQL Multi-AZ cluster with KMS encryption at rest and RDS Proxy
    - _Requirements: 12.9, 13.2, 13.3_
  - [ ] 17.4 Define ElastiCache Redis cluster with TLS enforced; DynamoDB table with on-demand capacity and TTL attribute
    - _Requirements: 12.10, 13.4_
  - [ ] 17.5 Define OpenSearch domain with dedicated master nodes; SNS topics and SQS queues with dead-letter queues and redrive policies; EventBridge scheduled rules
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 13.6_
  - [ ] 17.6 Define CloudFront distribution with S3 Origin Access Control, `Cache-Control: max-age=31536000, immutable` for hashed assets, and API Gateway origin for `/api/*`
    - _Requirements: 11.1, 11.2, 11.3, 11.4_
  - [ ] 17.7 Define API Gateway REST API with Cognito authorizer, WAF association, and route mappings to ALB
    - _Requirements: 12.1, 12.7_
  - [ ] 17.8 Define Cognito User Pool with customer and admins groups; Secrets Manager secrets for DB, Stripe, and JWT
    - _Requirements: 12.2, 12.8_

- [ ] 18. Integration wiring and end-to-end checkout flow
  - [ ] 18.1 Wire SNS topic subscriptions to SQS queues: `order.confirmed` → Inventory SQS + SES queue; `payment.succeeded` → Order SQS; `product.updated` → Search SQS
    - _Requirements: 10.1, 10.2, 10.3_
  - [ ] 18.2 Implement SES email notification handler consuming from SES SQS queue — send order confirmation and payment failure emails
    - _Requirements: 14.2_
  - [ ] 18.3 Implement `checkout` orchestration in Order Service: validate cart → reserve stock → create order → create PaymentIntent, returning HTTP 409 with unavailable items on stock failure
    - _Requirements: 4.1, 14.1_
  - [ ] 18.4 Implement Catalog Service fallback to Aurora when OpenSearch is unavailable
    - _Requirements: 14.5_
  - [ ] 18.5 Implement CloudWatch alarm for OpenSearch cluster errors
    - _Requirements: 14.4_
  - [ ]* 18.6 Write integration tests for end-to-end checkout flow using docker-compose with LocalStack, PostgreSQL, Redis, and OpenSearch
    - Test: cart → order creation → payment webhook → inventory deduction → email notification
    - _Requirements: 4.1, 4.5, 8.4, 10.1_
  - [ ]* 18.7 Write property test for Catalog fallback on OpenSearch unavailability
    - **Property 31: Catalog Fallback on OpenSearch Unavailability**
    - **Validates: Requirements 14.5**

- [ ] 19. Final checkpoint — Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP
- Each task references specific requirements for traceability
- Property tests use the `hypothesis` library; integration tests use `pytest-asyncio` with LocalStack
- Checkpoints ensure incremental validation before moving to the next service group
- The design uses Python/FastAPI for all backend services and Next.js 14 for the frontend

- [ ] 20. Agent Service — Shopping Assistant
  - [ ] 20.1 Create `services/agent/` directory with `app/main.py`, `app/routers/agent.py`, `app/tools/shopping.py`, `app/tools/ops.py`, `app/tools/pricing.py`, `requirements.txt`, `Dockerfile`
  - [ ] 20.2 Implement `POST /agent/chat` endpoint — accepts `{ message, session_id }`, authenticates via Cognito JWT, invokes AgentCore Runtime with Shopping Assistant agent config
  - [ ] 20.3 Implement AgentCore tool handlers in `app/tools/shopping.py` — each tool calls the corresponding microservice via HTTP (search, cart, orders, recommendations, inventory)
  - [ ] 20.4 Configure AgentCore Memory for session (TTL 1h) and long-term user preferences
  - [ ] 20.5 Configure AgentCore Gateway as MCP server with all 6 shopping tools
  - [ ] 20.6 Configure AgentCore Identity to scope tool calls to the authenticated user's Cognito sub
  - [ ] 20.7 Add `/health` endpoint and Dockerfile for ECS Fargate deployment
  - _Requirements: 15.1–15.10_

- [ ] 21. Agent Service — Ops Agent
  - [ ] 21.1 Implement `POST /agent/ops` endpoint — admin-only (verify `admins` Cognito group), invokes AgentCore Runtime with Ops Agent config
  - [ ] 21.2 Implement Ops Agent tool handlers in `app/tools/ops.py` — get_stuck_orders, get_low_stock_items, get_revenue_report, get_dashboard_metrics, export_orders
  - [ ] 21.3 Configure AgentCore Memory for admin long-term preferences (report formats, date ranges)
  - [ ] 21.4 Configure AgentCore Observability to log all admin queries for audit trail
  - _Requirements: 16.1–16.8_

- [ ] 22. Agent Service — Price/Deal Agent
  - [ ] 22.1 Implement `POST /agent/pricing/run` endpoint — triggered by EventBridge daily at 08:00 UTC
  - [ ] 22.2 Implement pricing tool handlers in `app/tools/pricing.py` — get_slow_moving_products, suggest_markdown, get_restock_recommendations, publish_pricing_suggestion
  - [ ] 22.3 Implement SNS publisher for `pricing.suggestion` events
  - [ ] 22.4 Add `pricing_suggestions` table to Aurora for storing agent suggestions
  - [ ] 22.5 Add EventBridge rule `daily-pricing-agent` (cron: `0 8 * * ? *`) in Terraform messaging module
  - _Requirements: 17.1–17.8_

- [ ] 23. Frontend — Chat Widget
  - [ ] 23.1 Create `frontend/src/components/chat/chat-widget.tsx` — floating button + slide-over panel
  - [ ] 23.2 Implement SSE streaming for agent responses using `EventSource`
  - [ ] 23.3 Add quick action chips: "Find deals", "Track my order", "What's new?", "My cart"
  - [ ] 23.4 Add admin chat panel at `/admin/ops` using the Ops Agent endpoint
  - [ ] 23.5 Add chat widget to shop layout (visible on all shop pages)
  - _Requirements: 15.6, 16.6_

- [ ] 24. Semantic/Vector Search
  - [ ] 24.1 Update OpenSearch index mapping to add `embedding` field (knn_vector, 1024 dims, cosine similarity)
  - [ ] 24.2 Update `build_product_document()` in Search Service to call Bedrock Titan Embeddings and include vector in document
  - [ ] 24.3 Update `search_products()` to embed the query and execute hybrid BM25 + k-NN search
  - [ ] 24.4 Add fallback to keyword-only search when Bedrock embedding call fails
  - _Requirements: 18.1–18.7_

- [ ] 25. Visual Search
  - [ ] 25.1 Add `POST /search/visual` endpoint to Search Service — accepts multipart image upload
  - [ ] 25.2 Implement Claude Vision call to extract product attributes from uploaded image
  - [ ] 25.3 Construct search query from extracted attributes and execute hybrid search
  - [ ] 25.4 Add visual search button to frontend search bar
  - _Requirements: 19.1–19.6_

- [ ] 26. AI Product Description Generator
  - [ ] 26.1 Add `POST /catalog/products/{productId}/generate-description` endpoint to Catalog Service
  - [ ] 26.2 Implement Bedrock Claude call with product description prompt template
  - [ ] 26.3 Add `POST /catalog/products/{productId}/apply-description` endpoint to apply generated content
  - [ ] 26.4 Add "Generate Description" button to admin product edit UI
  - _Requirements: 20.1–20.6_

- [ ] 27. Order Fraud Detection
  - [ ] 27.1 Implement `app/fraud.py` in Order Service with rule-based scorer (local dev) and Bedrock Claude scorer (production)
  - [ ] 27.2 Integrate fraud scoring into order creation flow — call before PaymentIntent creation
  - [ ] 27.3 Add `fraud_score` and `fraud_signals` JSONB fields to orders table
  - [ ] 27.4 Implement `under_review` order status and admin SNS notification for medium-risk orders
  - _Requirements: 21.1–21.8_
