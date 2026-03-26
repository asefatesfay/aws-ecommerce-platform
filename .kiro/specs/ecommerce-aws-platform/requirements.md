# Requirements Document

## Introduction

This document defines the functional and non-functional requirements for the Ecommerce AWS Platform — a cloud-native, microservices-based ecommerce system built on AWS. The platform provides product catalog management, shopping cart, checkout and payments, order lifecycle management, user authentication, full-text search, personalized recommendations, inventory tracking, and an admin dashboard. Requirements are derived directly from the approved design document.

---

## Glossary

- **Auth_Service**: FastAPI microservice responsible for user registration, login, token refresh, and profile management via Amazon Cognito.
- **Catalog_Service**: FastAPI microservice responsible for product and category CRUD, image uploads, and cache management.
- **Cart_Service**: FastAPI microservice responsible for per-user shopping cart state stored in DynamoDB.
- **Order_Service**: FastAPI microservice responsible for order lifecycle management and state machine transitions.
- **Payment_Service**: FastAPI microservice responsible for Stripe PaymentIntent creation and webhook processing.
- **Search_Service**: FastAPI microservice responsible for full-text and faceted product search via OpenSearch.
- **Recommendation_Service**: FastAPI microservice responsible for personalized product recommendations via Amazon Personalize.
- **Inventory_Service**: FastAPI microservice responsible for real-time stock tracking and reservation.
- **Admin_Service**: FastAPI microservice restricted to admin users for dashboard metrics, reporting, and exports.
- **API_Gateway**: AWS API Gateway (REST) that routes requests to microservices and enforces Cognito JWT authorization.
- **Cognito**: Amazon Cognito User Pool used for authentication, JWT issuance, and group-based authorization.
- **Aurora**: Amazon Aurora PostgreSQL used as the primary relational database for transactional data.
- **DynamoDB**: Amazon DynamoDB used for cart and session data with key-value access patterns.
- **Redis**: Amazon ElastiCache Redis used for caching catalog pages, search results, recommendations, and sessions.
- **OpenSearch**: Amazon OpenSearch Service used for full-text product search, faceted filtering, and autocomplete.
- **SNS**: Amazon Simple Notification Service used for fan-out event publishing across services.
- **SQS**: Amazon Simple Queue Service used for reliable async task queues consumed by individual services.
- **EventBridge**: Amazon EventBridge used for scheduled jobs such as daily stock reconciliation.
- **Stripe**: External payment processor used for PaymentIntent creation and webhook-driven order confirmation.
- **SES**: Amazon Simple Email Service used for transactional email notifications.
- **Personalize**: Amazon Personalize used for ML-based personalized product recommendations.
- **CloudFront**: Amazon CloudFront CDN used to serve the Next.js frontend and static assets globally.
- **S3**: Amazon S3 used for static asset hosting, product image storage, and export file storage.
- **ECS_Fargate**: Amazon ECS with Fargate launch type used to run all FastAPI microservice containers.
- **ALB**: Application Load Balancer routing traffic from API Gateway and CloudFront to ECS Fargate tasks.
- **WAF**: AWS Web Application Firewall attached to CloudFront and API Gateway for rate limiting and injection protection.
- **Secrets_Manager**: AWS Secrets Manager used to store and inject secrets into ECS tasks at startup.
- **RDS_Proxy**: Amazon RDS Proxy used for Aurora connection pooling from ECS Fargate tasks.
- **Order**: A record representing a customer purchase, with a defined status and associated items, totals, and payment.
- **Cart**: A per-user collection of product items stored in DynamoDB with a 30-day TTL.
- **Reservation**: A temporary hold on inventory stock associated with a pending order.
- **PaymentIntent**: A Stripe object representing a payment transaction initiated server-side.
- **State_Machine**: The defined set of valid order status transitions enforced by the Order_Service.

---

## Requirements

### Requirement 1: User Authentication and Profile Management

**User Story:** As a customer, I want to register, log in, and manage my profile, so that I can access personalized features and track my orders securely.

#### Acceptance Criteria

1. WHEN a user submits a registration request with a valid email and password, THE Auth_Service SHALL create a new user account in Cognito and store extended profile data in Aurora.
2. WHEN a user submits valid credentials, THE Auth_Service SHALL return a JWT access token and refresh token issued by Cognito.
3. WHEN a user submits a valid refresh token, THE Auth_Service SHALL return a new JWT access token without requiring re-authentication.
4. WHEN a user requests their profile, THE Auth_Service SHALL return the profile data stored in Aurora for the authenticated user.
5. WHEN a user submits a profile update request, THE Auth_Service SHALL persist the updated fields in Aurora and return the updated profile.
6. IF a user submits an invalid or expired JWT to the API_Gateway, THEN THE API_Gateway SHALL return HTTP 401 Unauthorized.
7. WHEN a user's JWT access token expires and the frontend detects a 401 response, THE Auth_Service SHALL accept a valid refresh token and issue a new access token.
8. THE Auth_Service SHALL store the user's `cognito_sub` as a unique identifier linking the Cognito identity to the Aurora user record.
9. THE Auth_Service SHALL assign the role `"customer"` by default to all newly registered users.

---

### Requirement 2: Product Catalog Management

**User Story:** As an admin, I want to create, update, and delete products and categories, so that the storefront always reflects accurate and current inventory offerings.

#### Acceptance Criteria

1. WHEN an admin submits a create product request with valid fields, THE Catalog_Service SHALL persist the product in Aurora and return the created product detail.
2. WHEN an admin submits an update product request, THE Catalog_Service SHALL update the product in Aurora, publish a `product.updated` event to SNS, and return the updated product detail.
3. WHEN an admin deletes a product, THE Catalog_Service SHALL remove the product from Aurora and publish a `product.updated` event to SNS to trigger OpenSearch de-indexing.
4. WHEN a product image is uploaded, THE Catalog_Service SHALL store the image in S3 and return a CloudFront-served URL.
5. WHEN a product page is requested, THE Catalog_Service SHALL check Redis before querying Aurora, and cache the result in Redis with a TTL of 10 minutes on a cache miss.
6. WHEN a list of products is requested with pagination parameters, THE Catalog_Service SHALL return a paginated response containing at most `limit` products.
7. THE Catalog_Service SHALL enforce that `price` is greater than 0 for all products.
8. THE Catalog_Service SHALL enforce that `sku` is unique across all products.
9. THE Catalog_Service SHALL enforce that active products have at least one image URL.
10. WHEN a list of categories is requested, THE Catalog_Service SHALL return all available categories from Aurora.

---

### Requirement 3: Shopping Cart Management

**User Story:** As a customer, I want to add, update, and remove items in my cart, so that I can prepare my purchase before checkout.

#### Acceptance Criteria

1. WHEN a user requests their cart, THE Cart_Service SHALL return the current cart state from DynamoDB, using Redis as a read-through cache for sub-millisecond reads.
2. WHEN a user adds an item to the cart, THE Cart_Service SHALL validate product availability against the Inventory_Service before persisting the updated cart to DynamoDB.
3. IF a product is unavailable when a user attempts to add it to the cart, THEN THE Cart_Service SHALL reject the request and return an appropriate error response.
4. WHEN a user updates an item quantity in the cart, THE Cart_Service SHALL persist the updated cart to DynamoDB and return the updated cart state.
5. WHEN a user removes an item from the cart, THE Cart_Service SHALL remove the item from DynamoDB and return the updated cart state.
6. WHEN a user clears the cart, THE Cart_Service SHALL delete all items from the DynamoDB cart record.
7. THE Cart_Service SHALL store cart records in DynamoDB with a TTL of 30 days from the last update.
8. THE Cart_Service SHALL use the DynamoDB partition key `USER#<user_id>` and sort key `CART` for all cart records.

---

### Requirement 4: Order Lifecycle Management

**User Story:** As a customer, I want to place orders and track their status, so that I know when my purchases will arrive.

#### Acceptance Criteria

1. WHEN a checkout request is submitted with a non-empty cart and valid shipping address, THE Order_Service SHALL create a pending order in Aurora with price snapshots for all items.
2. THE Order_Service SHALL enforce that `order.total` equals `subtotal + tax + shipping_cost` for every order.
3. THE Order_Service SHALL enforce that each `OrderItem.subtotal` equals `unit_price * quantity`.
4. WHEN an order is created, THE Order_Service SHALL publish an `order.created` event to SNS.
5. WHEN a `payment.succeeded` event is consumed from SQS, THE Order_Service SHALL transition the order status to `confirmed` and publish an `order.confirmed` event to SNS.
6. WHEN a `payment.failed` event is consumed from SQS, THE Order_Service SHALL transition the order status to `cancelled` and publish an `order.cancelled` event to SNS.
7. WHEN an order status update is requested, THE Order_Service SHALL only allow transitions defined in the State_Machine and reject invalid transitions with HTTP 422.
8. THE Order_Service SHALL enforce the following State_Machine transitions: `pending` → `[confirmed, cancelled]`, `confirmed` → `[processing, cancelled]`, `processing` → `[shipped, cancelled]`, `shipped` → `[delivered]`, `delivered` → `[refunded]`, `cancelled` → `[]`, `refunded` → `[]`.
9. WHEN a user requests their order history, THE Order_Service SHALL return a paginated list of orders for that user from Aurora.
10. WHEN a user requests a specific order, THE Order_Service SHALL return the full order detail including items, totals, and current status.
11. WHEN an order is cancelled, THE Order_Service SHALL publish an `order.cancelled` event to SNS.
12. THE Order_Service SHALL store the `shipping_address` as an immutable JSONB snapshot at the time of order creation.

---

### Requirement 5: Payment Processing

**User Story:** As a customer, I want to pay for my order securely using a credit card, so that I can complete my purchase without exposing my card details to the platform.

#### Acceptance Criteria

1. WHEN a checkout request is received, THE Payment_Service SHALL create a Stripe PaymentIntent server-side and return the `client_secret` to the frontend.
2. THE Payment_Service SHALL never receive or store raw card data; card input SHALL be handled client-side by Stripe Elements.
3. WHEN a Stripe webhook event is received, THE Payment_Service SHALL verify the webhook signature using `STRIPE_WEBHOOK_SECRET` before processing.
4. IF a Stripe webhook signature verification fails, THEN THE Payment_Service SHALL reject the request with HTTP 400 and take no action.
5. WHEN a `payment_intent.succeeded` webhook is received, THE Payment_Service SHALL update the payment record status to `succeeded` and publish a `payment.succeeded` event to SNS.
6. WHEN a `payment_intent.payment_failed` webhook is received, THE Payment_Service SHALL update the payment record status to `failed` and publish a `payment.failed` event to SNS.
7. WHEN the same Stripe webhook event is delivered more than once, THE Payment_Service SHALL detect the duplicate via `stripe_payment_intent_id` and return HTTP 200 without re-processing.
8. WHEN a refund is requested, THE Payment_Service SHALL issue a refund via Stripe and update the payment record status to `refunded` or `partially_refunded`.
9. THE Payment_Service SHALL persist all payment records in Aurora for audit trail purposes.
10. THE Payment_Service SHALL store the `stripe_payment_intent_id` as a unique field on the payment record.

---

### Requirement 6: Product Search

**User Story:** As a customer, I want to search for products using keywords and filters, so that I can quickly find items that match my needs.

#### Acceptance Criteria

1. WHEN a search request is received with a non-empty query string, THE Search_Service SHALL execute a full-text query against OpenSearch and return ranked results with facets.
2. WHEN a search request is received, THE Search_Service SHALL check Redis for a cached result using a deterministic hash of `(query, filters, page, limit)` before querying OpenSearch.
3. WHEN a cache miss occurs, THE Search_Service SHALL store the OpenSearch result in Redis with a TTL of 5 minutes.
4. WHEN an autocomplete request is received, THE Search_Service SHALL return suggestions using the OpenSearch completion suggester.
5. WHEN a `product.updated` event is consumed from SQS, THE Search_Service SHALL re-index the product document in OpenSearch.
6. WHEN a product is deleted, THE Search_Service SHALL remove the product document from the OpenSearch index.
7. THE Search_Service SHALL enforce that `page >= 1` and `1 <= limit <= 100` for all search requests.
8. THE Search_Service SHALL enforce that `filters.price_min <= filters.price_max` when both are provided.
9. WHEN a search response is returned, THE Search_Service SHALL include `products`, `total_count`, `facets`, `page`, and `limit` fields.
10. THE Search_Service SHALL return at most `limit` products in any single search response.
11. IF OpenSearch is unavailable, THEN THE Search_Service SHALL return HTTP 503 with a `Retry-After` header.

---

### Requirement 7: Personalized Recommendations

**User Story:** As a customer, I want to see product recommendations tailored to my browsing and purchase history, so that I can discover relevant products more easily.

#### Acceptance Criteria

1. WHEN a recommendations request is received for a user, THE Recommendation_Service SHALL call Amazon Personalize to retrieve personalized item IDs and fetch product details from OpenSearch.
2. IF Amazon Personalize is unavailable or the user has no interaction history, THEN THE Recommendation_Service SHALL fall back to top-selling products ranked by OpenSearch.
3. WHEN a similar items request is received for a product, THE Recommendation_Service SHALL return related products using Amazon Personalize or OpenSearch similarity.
4. WHEN a user interaction event (view, add-to-cart, purchase) is received, THE Recommendation_Service SHALL record the event to the Amazon Personalize event tracker.
5. THE Recommendation_Service SHALL cache recommendation results in Redis per `user_id` with a TTL of 15 minutes.
6. THE Recommendation_Service SHALL enforce that `1 <= limit <= 50` for all recommendation requests.
7. THE Recommendation_Service SHALL return at most `limit` products in any recommendation response.

---

### Requirement 8: Inventory Management

**User Story:** As an operations manager, I want real-time stock tracking with automatic deduction on order confirmation, so that overselling is prevented and stock levels remain accurate.

#### Acceptance Criteria

1. WHEN a stock reservation request is received, THE Inventory_Service SHALL atomically decrease `quantity_available` and increase `quantity_reserved` using optimistic locking with a version field.
2. THE Inventory_Service SHALL enforce that `quantity_available` never goes below 0 at any point.
3. IF a concurrent update conflict is detected during reservation, THEN THE Inventory_Service SHALL retry the operation up to 3 times with a fresh inventory read before returning HTTP 409.
4. WHEN an `order.confirmed` event is consumed from SQS, THE Inventory_Service SHALL deduct the reserved quantity from `quantity_on_hand` and release the reservation.
5. WHEN an `order.cancelled` event is consumed from SQS, THE Inventory_Service SHALL release the stock reservation and restore `quantity_available`.
6. WHEN `quantity_available` falls below `reorder_threshold`, THE Inventory_Service SHALL publish an `inventory.low_stock` event to SNS.
7. WHEN a stock adjustment request is received, THE Inventory_Service SHALL update `quantity_on_hand` in Aurora and recalculate `quantity_available`.
8. WHEN a list of low-stock items is requested, THE Inventory_Service SHALL return all products where `quantity_available` is below the specified threshold.
9. THE Inventory_Service SHALL increment the `version` field on every write to support optimistic concurrency control.
10. WHERE EventBridge scheduled jobs are configured, THE Inventory_Service SHALL perform a daily stock reconciliation to detect and correct discrepancies.

---

### Requirement 9: Admin Dashboard and Reporting

**User Story:** As an admin, I want access to platform metrics, order management, and exportable reports, so that I can monitor business performance and manage operations.

#### Acceptance Criteria

1. WHEN an admin requests dashboard metrics, THE Admin_Service SHALL return aggregated order counts, revenue totals, and user counts from Aurora.
2. WHEN an admin requests a revenue report for a date range, THE Admin_Service SHALL return revenue data aggregated by the specified `start` and `end` dates.
3. WHEN an admin requests an order export, THE Admin_Service SHALL generate a CSV or Excel file, upload it to S3, and return a presigned URL for download.
4. WHEN an admin requests a list of all orders with filters, THE Admin_Service SHALL return a paginated list of orders matching the filter criteria.
5. WHEN an admin requests a list of users, THE Admin_Service SHALL return a paginated list of users from Aurora.
6. THE Admin_Service SHALL restrict all endpoints to users whose Cognito JWT contains the `"admins"` group claim.
7. IF a non-admin user attempts to access an Admin_Service endpoint, THEN THE API_Gateway SHALL return HTTP 403 Forbidden.

---

### Requirement 10: Event-Driven Messaging

**User Story:** As a platform engineer, I want reliable async event delivery between services, so that order processing, inventory updates, and notifications are decoupled and resilient.

#### Acceptance Criteria

1. WHEN the Order_Service publishes an `order.confirmed` event to SNS, THE SNS topic SHALL fan out the event to the Inventory_Service SQS queue and the SES notification queue.
2. WHEN the Payment_Service publishes a `payment.succeeded` event to SNS, THE SNS topic SHALL deliver the event to the Order_Service SQS queue.
3. WHEN the Catalog_Service publishes a `product.updated` event to SNS, THE SNS topic SHALL deliver the event to the Search_Service SQS queue for re-indexing.
4. THE SQS queues SHALL be configured with dead-letter queues to capture messages that fail processing after the maximum retry count.
5. WHEN an SQS message fails processing, THE consuming service SHALL retry delivery according to the SQS visibility timeout and redrive policy before routing to the dead-letter queue.
6. WHERE EventBridge scheduled rules are configured, THE EventBridge SHALL trigger the Inventory_Service daily reconciliation job and the Admin_Service report generation job on their configured schedules.

---

### Requirement 11: Frontend Delivery and Performance

**User Story:** As a customer, I want the storefront to load quickly from anywhere in the world, so that I have a responsive shopping experience.

#### Acceptance Criteria

1. THE CloudFront distribution SHALL serve the Next.js frontend build and all static assets from S3 edge locations globally.
2. THE CloudFront distribution SHALL set `Cache-Control: max-age=31536000, immutable` headers for content-hashed static assets.
3. THE S3 bucket containing static assets SHALL be private, with CloudFront as the only authorized reader via Origin Access Control.
4. WHEN a user navigates to the storefront, THE CloudFront distribution SHALL route API requests to the API_Gateway and static requests to S3.
5. THE Catalog_Service SHALL cache product catalog pages in Redis with a TTL of 10 minutes to reduce Aurora query load.
6. THE Search_Service SHALL cache search results in Redis with a TTL of 5 minutes to reduce OpenSearch query load.
7. THE Recommendation_Service SHALL cache recommendation results in Redis with a TTL of 15 minutes per user.

---

### Requirement 12: Security and Access Control

**User Story:** As a platform engineer, I want all services and data to be secured by default, so that customer data and payment information are protected.

#### Acceptance Criteria

1. THE API_Gateway SHALL require a valid Cognito JWT for all endpoints except `/health`, `/search`, and `/catalog` (public read).
2. THE Admin_Service SHALL verify the `cognito:groups` claim in the JWT contains `"admins"` before processing any request.
3. THE Payment_Service SHALL verify Stripe webhook signatures using `stripe.Webhook.construct_event()` before processing any webhook payload.
4. THE S3 bucket for product images SHALL deny all public access; CloudFront with Origin Access Control SHALL be the sole authorized reader.
5. THE ECS_Fargate tasks, Aurora, Redis, and OpenSearch SHALL run in private VPC subnets with no direct public internet access.
6. THE ALB and API_Gateway SHALL be the only components deployed in public subnets.
7. THE WAF SHALL be attached to CloudFront and API_Gateway to enforce rate limiting and protect against SQL injection and XSS attacks.
8. THE Secrets_Manager SHALL store all secrets including database passwords, Stripe API keys, and JWT secrets; THE ECS_Fargate tasks SHALL inject these secrets as environment variables at startup.
9. THE Aurora database SHALL be encrypted at rest using AWS KMS.
10. THE Redis cluster SHALL enforce TLS for all in-transit connections.
11. THE S3 buckets SHALL use SSE-S3 server-side encryption for all stored objects.

---

### Requirement 13: Infrastructure and Scalability

**User Story:** As a platform engineer, I want the platform to scale automatically under load and recover from failures, so that the system remains available during traffic spikes.

#### Acceptance Criteria

1. THE ECS_Fargate tasks SHALL scale automatically using target tracking policies on CPU utilization (70% target) and ALB request count per target.
2. THE Aurora database SHALL be deployed in a Multi-AZ configuration for high availability and automatic failover.
3. THE RDS_Proxy SHALL manage Aurora connection pooling to prevent connection exhaustion from ECS_Fargate ephemeral tasks.
4. THE DynamoDB tables SHALL use on-demand capacity mode to handle unpredictable traffic spikes without manual capacity planning.
5. THE SQS consumers SHALL process inventory deduction events in batches of up to 10 messages to reduce Aurora round trips.
6. THE OpenSearch domain SHALL be configured with dedicated master nodes for cluster stability.
7. WHEN an OpenSearch query fails due to a 5xx error, THE Search_Service SHALL apply exponential backoff retry logic using the `tenacity` library before returning an error.
8. THE ECS_Fargate tasks SHALL retrieve all configuration secrets from Secrets_Manager at startup and SHALL NOT store secrets in container images or environment variable definitions.

---

### Requirement 14: Observability and Error Handling

**User Story:** As a platform engineer, I want comprehensive error handling and monitoring, so that issues are detected and resolved quickly without impacting customers.

#### Acceptance Criteria

1. IF a checkout request contains items with insufficient stock, THEN THE Order_Service SHALL return HTTP 409 Conflict with a list of unavailable items and their current available quantities.
2. IF a Stripe `payment_intent.payment_failed` webhook is received, THEN THE Payment_Service SHALL publish a `payment.failed` event, THE Order_Service SHALL cancel the order, THE Inventory_Service SHALL release all stock reservations, and THE SES notification SHALL be sent to the customer.
3. IF the Inventory_Service fails to reserve stock after 3 retry attempts, THEN THE Inventory_Service SHALL return HTTP 409 to the caller without creating a reservation.
4. WHEN a CloudWatch alarm detects an OpenSearch cluster error, THE platform SHALL trigger an alert for operator review.
5. THE Catalog_Service SHALL fall back to Aurora-based product listing when OpenSearch is unavailable, returning results without full-text ranking or facets.
6. WHEN any microservice starts up, THE service SHALL verify connectivity to its required dependencies (Aurora, Redis, DynamoDB, OpenSearch) and expose a `/health` endpoint reflecting readiness status.

---

### Requirement 15: Shopping Assistant Agent

**User Story:** As a customer, I want a conversational AI assistant that can search products, manage my cart, and check my orders using natural language, so that I can shop without navigating multiple pages.

#### Acceptance Criteria

1. WHEN a customer sends a natural language message, THE Shopping_Assistant_Agent SHALL interpret the intent and call the appropriate tool (search_products, add_to_cart, get_cart, get_order_status, get_recommendations, check_stock).
2. THE Shopping_Assistant_Agent SHALL maintain conversation context across turns using AgentCore Memory (short-term session memory + long-term user preference memory).
3. WHEN a customer says "find me running shoes under $100", THE agent SHALL call search_products with the extracted query and price filter and return formatted results.
4. WHEN a customer says "add the first one to my cart", THE agent SHALL resolve the reference from conversation context and call add_to_cart.
5. WHEN a customer asks about order status, THE agent SHALL call get_order_status with the user's most recent order ID from memory.
6. THE Shopping_Assistant_Agent SHALL be deployed on AgentCore Runtime and exposed via a FastAPI Agent_Service at POST /agent/chat.
7. THE Agent_Service SHALL authenticate requests using the user's Cognito JWT and pass the user_id to AgentCore Identity for scoped tool access.
8. THE agent SHALL use AgentCore Gateway as an MCP server exposing all 9 microservice tools with Cognito-scoped authorization.
9. THE agent SHALL use AgentCore Observability to trace every tool call, latency, and model decision for debugging.
10. IF a tool call fails, THE agent SHALL gracefully inform the user and suggest an alternative action.

---

### Requirement 16: Ops Agent (Admin-Facing)

**User Story:** As an operations manager, I want an AI agent that can query platform data and generate operational reports using natural language, so that I can monitor the business without writing SQL or navigating dashboards.

#### Acceptance Criteria

1. WHEN an admin asks "show me orders stuck in processing for more than 24 hours", THE Ops_Agent SHALL query the Admin Service and return a formatted list with order IDs, customer names, and elapsed time.
2. WHEN an admin asks "which products are low on stock?", THE Ops_Agent SHALL call the Inventory Service low-stock endpoint and return a prioritized list.
3. WHEN an admin asks "generate a revenue summary for last week", THE Ops_Agent SHALL call the Admin revenue report endpoint and return a formatted summary with totals and daily breakdown.
4. THE Ops_Agent SHALL be restricted to users with the `"admins"` Cognito group claim — all tool calls SHALL be rejected with HTTP 403 for non-admin users.
5. THE Ops_Agent SHALL use AgentCore Memory to remember the admin's preferred report formats and frequently asked queries.
6. THE Ops_Agent SHALL be exposed at POST /agent/ops and share the same Agent_Service FastAPI app as the Shopping Assistant.
7. THE Ops_Agent SHALL use AgentCore Observability to log all admin queries and tool calls for audit purposes.
8. WHEN an admin asks to export data, THE Ops_Agent SHALL call the Admin export endpoint and return the presigned S3 download URL.

---

### Requirement 17: Price/Deal Agent

**User Story:** As a merchandising manager, I want an AI agent that monitors inventory velocity and suggests pricing actions, so that I can optimize revenue and reduce slow-moving stock.

#### Acceptance Criteria

1. THE Price_Deal_Agent SHALL run on a scheduled basis (EventBridge cron: daily at 08:00 UTC) to analyze inventory and sales data.
2. WHEN a product has been in stock for more than 30 days with fewer than 5 units sold, THE agent SHALL flag it as slow-moving and suggest a markdown percentage.
3. WHEN `quantity_available` falls below `reorder_threshold`, THE agent SHALL generate a restock recommendation with suggested reorder quantity.
4. THE agent SHALL publish pricing suggestions as `pricing.suggestion` events to SNS for admin review before any price changes are applied.
5. THE agent SHALL use AgentCore Memory to track historical pricing decisions and their outcomes (did the markdown increase sales?).
6. THE Price_Deal_Agent SHALL be triggered via EventBridge and run as an AgentCore Runtime async task.
7. WHEN the agent generates suggestions, THE Admin_Service SHALL store them in Aurora and surface them in the admin dashboard.
8. THE agent SHALL use Claude 3.5 Sonnet via Amazon Bedrock as the underlying model for reasoning about pricing strategy.

---

## Glossary (additions)

- **Shopping_Assistant_Agent**: AgentCore-powered conversational agent for customer-facing shopping assistance.
- **Ops_Agent**: AgentCore-powered admin-facing operational intelligence agent.
- **Price_Deal_Agent**: AgentCore-powered scheduled agent for pricing optimization and inventory analysis.
- **Agent_Service**: FastAPI microservice hosting the AgentCore agent endpoints.
- **AgentCore_Runtime**: Amazon Bedrock AgentCore Runtime for deploying and operating AI agents.
- **AgentCore_Memory**: AgentCore Memory service for short-term session and long-term user preference storage.
- **AgentCore_Gateway**: AgentCore Gateway acting as MCP server exposing microservice tools to agents.
- **AgentCore_Identity**: AgentCore Identity for mapping agent actions to user Cognito identities.
- **AgentCore_Observability**: AgentCore Observability for tracing agent decisions, tool calls, and latency.
