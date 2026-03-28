import { fetcher } from './fetcher'
import { buildFilterParams } from './utils'

export interface Product {
  id: string
  name: string
  description: string
  price: number
  compareAtPrice?: number
  imageUrl: string
  images?: string[]
  sku: string
  categoryId: string
  stock: number
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  limit: number
  totalPages: number
}

export interface Order {
  id: string
  status: string
  total: number
  subtotal: number
  tax: number
  shippingCost: number
  createdAt: string
  updatedAt: string
  items: Array<{
    id: string
    productId: string
    name: string
    sku: string
    quantity: number
    unitPrice: number
    subtotal: number
  }>
  shippingAddress: ShippingAddress
  fraudScore?: number
}

export interface ShippingAddress {
  fullName: string
  street: string
  city: string
  state: string
  postalCode: string
  country: string
}

export interface PaymentIntentResponse {
  paymentId: string
  clientSecret: string
  amount: number
  currency: string
}

// ── Products ──────────────────────────────────────────────────────────────────

export const searchProducts = (
  query: string,
  filters: Record<string, unknown> = {},
  page = 1,
  limit = 20
) =>
  fetcher<PaginatedResponse<Product>>(
    `/search?q=${encodeURIComponent(query)}&page=${page}&limit=${limit}&${buildFilterParams(filters)}`
  )

export const getProduct = (id: string) =>
  fetcher<Product>(`/catalog/products/${id}`)

export const listProducts = (page = 1, limit = 20, categoryId?: string) => {
  const params = new URLSearchParams({ page: String(page), limit: String(limit) })
  if (categoryId) params.set('categoryId', categoryId)
  return fetcher<PaginatedResponse<Product>>(`/catalog/products?${params}`)
}

export const listCategories = () =>
  fetcher<Array<{ id: string; name: string; slug: string }>>('/catalog/categories')

// ── Cart ──────────────────────────────────────────────────────────────────────

export const getCart = (userId: string) =>
  fetcher<{ items: Array<{ productId: string; quantity: number }>; total: number }>(
    `/cart/${userId}`
  )

export const addToCart = (
  userId: string,
  item: { product_id: string; quantity: number; sku: string; name: string; unit_price: number; image_url: string }
) =>
  fetch(`/cart/${userId}/items`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item),
  }).then((r) => r.json())

export const removeFromCart = (userId: string, itemId: string) =>
  fetch(`/cart/${userId}/items/${itemId}`, { method: 'DELETE' }).then((r) => r.json())

export const clearCart = (userId: string) =>
  fetch(`/cart/${userId}`, { method: 'DELETE' })

// ── Orders ────────────────────────────────────────────────────────────────────

export interface CreateOrderPayload {
  items: Array<{
    product_id: string
    sku: string
    name: string
    unit_price: number
    quantity: number
  }>
  shipping_address: {
    full_name: string
    street: string
    city: string
    state: string
    country: string
    postal_code: string
  }
  notes?: string
}

export const createOrder = (payload: CreateOrderPayload, userId: string) =>
  fetch('/orders', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-User-Id': userId },
    body: JSON.stringify(payload),
  }).then((r) => r.json() as Promise<Order>)

export const getOrder = (orderId: string, userId: string) =>
  fetcher<Order>(`/orders/${orderId}`, { 'X-User-Id': userId })

export const listOrders = (page = 1, limit = 10, userId = '') =>
  fetcher<PaginatedResponse<Order>>(
    `/orders?page=${page}&limit=${limit}`,
    { 'X-User-Id': userId }
  )

export const cancelOrder = (orderId: string) =>
  fetch(`/orders/${orderId}/cancel`, { method: 'POST' }).then((r) => r.json())

// ── Payments ──────────────────────────────────────────────────────────────────

export const createPaymentIntent = (orderId: string, amount: number) =>
  fetch('/payments/intent', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ order_id: orderId, amount, currency: 'usd' }),
  }).then((r) => r.json() as Promise<PaymentIntentResponse>)

// ── Recommendations ───────────────────────────────────────────────────────────

export const getRecommendations = (userId: string, limit = 6) =>
  fetcher<Product[]>(`/recommendations/${userId}?limit=${limit}`)

export const getSimilarItems = (productId: string, limit = 6) =>
  fetcher<Product[]>(`/recommendations/similar/${productId}?limit=${limit}`)
