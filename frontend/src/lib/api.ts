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
  createdAt: string
  items: Array<{
    productId: string
    name: string
    quantity: number
    unitPrice: number
  }>
  shippingAddress: ShippingAddress
}

export interface ShippingAddress {
  fullName: string
  line1: string
  line2?: string
  city: string
  state: string
  postalCode: string
  country: string
}

export interface CheckoutResponse {
  orderId: string
  clientSecret: string
}

// Products
export const searchProducts = (
  query: string,
  filters: Record<string, unknown> = {},
  page = 1,
  limit = 20
) =>
  fetcher<PaginatedResponse<Product>>(
    `/api/search?q=${encodeURIComponent(query)}&page=${page}&limit=${limit}&${buildFilterParams(filters)}`
  )

export const getProduct = (id: string) =>
  fetcher<Product>(`/api/products/${id}`)

export const listProducts = (page = 1, limit = 20, categoryId?: string) => {
  const params = new URLSearchParams({ page: String(page), limit: String(limit) })
  if (categoryId) params.set('categoryId', categoryId)
  return fetcher<PaginatedResponse<Product>>(`/api/products?${params}`)
}

// Cart
export const getCart = (userId: string) =>
  fetcher<{ items: Array<{ productId: string; quantity: number }> }>(
    `/api/cart/${userId}`
  )

export const addToCart = (
  userId: string,
  item: { productId: string; quantity: number; sku: string }
) =>
  fetch(`/api/cart/${userId}/items`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item),
  }).then((r) => r.json())

// Checkout
export const checkout = (shippingAddress: ShippingAddress) =>
  fetch('/api/checkout', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ shippingAddress }),
  }).then((r) => r.json() as Promise<CheckoutResponse>)

// Orders
export const getOrder = (orderId: string) =>
  fetcher<Order>(`/api/orders/${orderId}`)

export const listOrders = (page = 1, limit = 10) =>
  fetcher<PaginatedResponse<Order>>(`/api/orders?page=${page}&limit=${limit}`)

// Recommendations
export const getRecommendations = (userId: string, limit = 6) =>
  fetcher<Product[]>(`/api/recommendations/${userId}?limit=${limit}`)
