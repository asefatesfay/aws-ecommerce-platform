#!/bin/bash
# End-to-end local test script
# Tests the full flow: register → browse → add to cart → checkout → simulate payment → verify order confirmed
# Usage: ./scripts/test-e2e.sh

set -e

BASE="http://localhost"
PASS=0
FAIL=0

green() { echo -e "\033[32m✓ $1\033[0m"; PASS=$((PASS+1)); }
red()   { echo -e "\033[31m✗ $1\033[0m"; FAIL=$((FAIL+1)); }
blue()  { echo -e "\033[34m→ $1\033[0m"; }
bold()  { echo -e "\033[1m$1\033[0m"; }

check() {
  local desc=$1
  local status=$2
  local expected=$3
  if [ "$status" -eq "$expected" ]; then
    green "$desc (HTTP $status)"
  else
    red "$desc (expected $expected, got $status)"
  fi
}

bold "═══════════════════════════════════════════"
bold " Nexmart End-to-End Local Test"
bold "═══════════════════════════════════════════"
echo ""

# ── 1. Health checks ──────────────────────────────────────────────────────────
bold "1. Health Checks"
for svc in auth catalog cart order payment search recommendation inventory admin; do
  port_map=("auth:8001" "catalog:8002" "cart:8003" "order:8004" "payment:8005" "search:8006" "recommendation:8007" "inventory:8008" "admin:8009")
  port=8000
  for p in "${port_map[@]}"; do
    if [[ "$p" == "$svc:"* ]]; then
      port="${p#*:}"
    fi
  done
  status=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:${port}/health" 2>/dev/null || echo "000")
  check "$svc health" "$status" 200
done
echo ""

# ── 2. Register user ──────────────────────────────────────────────────────────
bold "2. User Registration"
USER_EMAIL="testuser_$(date +%s)@example.com"
REGISTER_RESP=$(curl -s -X POST "$BASE/auth/register" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$USER_EMAIL\",\"password\":\"Test1234!\",\"full_name\":\"Test User\"}")
USER_ID=$(echo "$REGISTER_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id',''))" 2>/dev/null || echo "")
if [ -n "$USER_ID" ]; then
  green "Registered user: $USER_EMAIL (id: $USER_ID)"
else
  red "Registration failed: $REGISTER_RESP"
  USER_ID="test-user-$(date +%s)"
fi
echo ""

# ── 3. Browse catalog ─────────────────────────────────────────────────────────
bold "3. Browse Catalog"
CATALOG_RESP=$(curl -s "$BASE/catalog/products?limit=5")
PRODUCT_COUNT=$(echo "$CATALOG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('total',0))" 2>/dev/null || echo "0")
FIRST_PRODUCT_ID=$(echo "$CATALOG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); items=d.get('items',[]); print(items[0]['id'] if items else '')" 2>/dev/null || echo "")
FIRST_PRODUCT_SKU=$(echo "$CATALOG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); items=d.get('items',[]); print(items[0]['sku'] if items else '')" 2>/dev/null || echo "")
FIRST_PRODUCT_PRICE=$(echo "$CATALOG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); items=d.get('items',[]); print(items[0]['price'] if items else '9.99')" 2>/dev/null || echo "9.99")
FIRST_PRODUCT_NAME=$(echo "$CATALOG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); items=d.get('items',[]); print(items[0]['name'] if items else 'Test Product')" 2>/dev/null || echo "Test Product")

if [ "$PRODUCT_COUNT" -gt 0 ] 2>/dev/null; then
  green "Found $PRODUCT_COUNT products. Using: $FIRST_PRODUCT_NAME ($FIRST_PRODUCT_SKU)"
else
  red "No products found in catalog"
fi
echo ""

# ── 4. Search ─────────────────────────────────────────────────────────────────
bold "4. Search"
SEARCH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/search?q=headphones")
check "Search for 'headphones'" "$SEARCH_STATUS" 200
echo ""

# ── 5. Check inventory ────────────────────────────────────────────────────────
bold "5. Inventory Check"
if [ -n "$FIRST_PRODUCT_SKU" ]; then
  INV_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/inventory/$FIRST_PRODUCT_SKU")
  check "Stock check for $FIRST_PRODUCT_SKU" "$INV_STATUS" 200
fi
echo ""

# ── 6. Add to cart ────────────────────────────────────────────────────────────
bold "6. Cart Operations"
CART_RESP=$(curl -s -X POST "$BASE/cart/$USER_ID/items" \
  -H "Content-Type: application/json" \
  -d "{\"product_id\":\"$FIRST_PRODUCT_ID\",\"quantity\":2,\"sku\":\"$FIRST_PRODUCT_SKU\",\"name\":\"$FIRST_PRODUCT_NAME\",\"unit_price\":$FIRST_PRODUCT_PRICE,\"image_url\":\"\"}")
CART_ITEM_COUNT=$(echo "$CART_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('items',[])))" 2>/dev/null || echo "0")
if [ "$CART_ITEM_COUNT" -gt 0 ] 2>/dev/null; then
  green "Added to cart. Cart has $CART_ITEM_COUNT item(s)"
else
  red "Add to cart failed: $CART_RESP"
fi

GET_CART_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/cart/$USER_ID")
check "Get cart" "$GET_CART_STATUS" 200
echo ""

# ── 7. Create order ───────────────────────────────────────────────────────────
bold "7. Order Creation"
ORDER_RESP=$(curl -s -X POST "$BASE/orders" \
  -H "Content-Type: application/json" \
  -H "X-User-Id: $USER_ID" \
  -d "{
    \"items\": [{
      \"product_id\": \"$FIRST_PRODUCT_ID\",
      \"sku\": \"$FIRST_PRODUCT_SKU\",
      \"name\": \"$FIRST_PRODUCT_NAME\",
      \"unit_price\": $FIRST_PRODUCT_PRICE,
      \"quantity\": 1
    }],
    \"shipping_address\": {
      \"full_name\": \"Test User\",
      \"street\": \"123 Main St\",
      \"city\": \"Seattle\",
      \"state\": \"WA\",
      \"country\": \"US\",
      \"postal_code\": \"98101\"
    }
  }")
ORDER_ID=$(echo "$ORDER_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('id',''))" 2>/dev/null || echo "")
ORDER_STATUS=$(echo "$ORDER_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status',''))" 2>/dev/null || echo "")
if [ -n "$ORDER_ID" ]; then
  green "Order created: $ORDER_ID (status: $ORDER_STATUS)"
else
  red "Order creation failed: $ORDER_RESP"
fi
echo ""

# ── 8. Create payment intent ──────────────────────────────────────────────────
bold "8. Payment"
if [ -n "$ORDER_ID" ]; then
  ORDER_TOTAL=$(echo "$ORDER_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('total',0))" 2>/dev/null || echo "0")
  PAYMENT_RESP=$(curl -s -X POST "$BASE/payments/intent" \
    -H "Content-Type: application/json" \
    -d "{\"order_id\":\"$ORDER_ID\",\"amount\":$ORDER_TOTAL,\"currency\":\"usd\"}")
  PAYMENT_ID=$(echo "$PAYMENT_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('payment_id',''))" 2>/dev/null || echo "")
  CLIENT_SECRET=$(echo "$PAYMENT_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('client_secret',''))" 2>/dev/null || echo "")
  if [ -n "$PAYMENT_ID" ]; then
    green "Payment intent created: $PAYMENT_ID"
    blue "  client_secret: ${CLIENT_SECRET:0:30}..."
  else
    red "Payment intent failed: $PAYMENT_RESP"
  fi

  # Simulate payment success (dev-only endpoint)
  if [ -n "$PAYMENT_ID" ]; then
    blue "Simulating payment success..."
    SIM_RESP=$(curl -s -X POST "$BASE/payments/$PAYMENT_ID/simulate-success")
    SIM_STATUS=$(echo "$SIM_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status',''))" 2>/dev/null || echo "")
    if [ "$SIM_STATUS" = "succeeded" ]; then
      green "Payment simulated as succeeded"
    else
      red "Payment simulation failed: $SIM_RESP"
    fi
  fi
fi
echo ""

# ── 9. Verify order confirmed (after SQS consumer processes) ──────────────────
bold "9. Order Status Verification (waiting for SQS consumer...)"
if [ -n "$ORDER_ID" ]; then
  sleep 3  # Give SQS consumer time to process
  FINAL_ORDER=$(curl -s "$BASE/orders/$ORDER_ID" -H "X-User-Id: $USER_ID")
  FINAL_STATUS=$(echo "$FINAL_ORDER" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status',''))" 2>/dev/null || echo "")
  if [ "$FINAL_STATUS" = "confirmed" ]; then
    green "Order $ORDER_ID is now: $FINAL_STATUS ✓ (SQS consumer worked!)"
  else
    red "Order status is '$FINAL_STATUS' (expected 'confirmed') — SQS consumer may not be running"
  fi
fi
echo ""

# ── 10. List orders ───────────────────────────────────────────────────────────
bold "10. Order History"
ORDERS_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/orders" -H "X-User-Id: $USER_ID")
check "List orders for user" "$ORDERS_STATUS" 200
echo ""

# ── Summary ───────────────────────────────────────────────────────────────────
bold "═══════════════════════════════════════════"
bold " Results: $PASS passed, $FAIL failed"
bold "═══════════════════════════════════════════"
echo ""
echo "Service URLs:"
echo "  Frontend:       http://localhost"
echo "  Auth:           http://localhost:8001/docs"
echo "  Catalog:        http://localhost:8002/docs"
echo "  Cart:           http://localhost:8003/docs"
echo "  Order:          http://localhost:8004/docs"
echo "  Payment:        http://localhost:8005/docs"
echo "  Search:         http://localhost:8006/docs"
echo "  Recommendation: http://localhost:8007/docs"
echo "  Inventory:      http://localhost:8008/docs"
echo "  Admin:          http://localhost:8009/docs"
echo "  LocalStack:     http://localhost:4566"
echo ""

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
