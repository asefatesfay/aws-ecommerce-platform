'use client'

import { useState } from 'react'
import Link from 'next/link'
import useSWR from 'swr'
import { listOrders } from '@/lib/api'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { formatPrice } from '@/lib/utils'
import type { PaginatedResponse, Order } from '@/lib/api'

const statusVariant: Record<string, 'default' | 'primary' | 'success' | 'warning' | 'destructive'> = {
  pending: 'warning',
  processing: 'primary',
  shipped: 'primary',
  delivered: 'success',
  cancelled: 'destructive',
}

export default function OrdersPage() {
  const [page, setPage] = useState(1)
  const { data, isLoading } = useSWR<PaginatedResponse<Order>>(
    ['orders', page],
    () => listOrders(page, 10)
  )

  return (
    <div className="mx-auto max-w-3xl px-6 py-10">
      <h1 className="text-2xl font-bold mb-8">Order History</h1>

      {isLoading && (
        <div className="space-y-4">
          {Array.from({ length: 3 }).map((_, i) => (
            <div key={i} className="h-24 rounded-xl bg-gray-100 animate-pulse" />
          ))}
        </div>
      )}

      {!isLoading && data?.items.length === 0 && (
        <div className="text-center py-16 text-gray-500">
          <p>No orders yet.</p>
          <Link href="/products" className="mt-4 inline-block">
            <Button variant="outline">Start Shopping</Button>
          </Link>
        </div>
      )}

      <ul className="space-y-4">
        {data?.items.map((order) => (
          <li key={order.id}>
            <Link
              href={`/orders/${order.id}`}
              className="flex items-center justify-between rounded-xl border border-gray-200 p-5 hover:border-primary transition-colors"
            >
              <div>
                <p className="font-medium text-gray-900">Order #{order.id.slice(-8).toUpperCase()}</p>
                <p className="text-sm text-gray-500 mt-0.5">
                  {new Date(order.createdAt).toLocaleDateString()} · {order.items.length} item(s)
                </p>
              </div>
              <div className="flex items-center gap-4">
                <Badge variant={statusVariant[order.status] ?? 'default'}>
                  {order.status}
                </Badge>
                <span className="font-semibold">{formatPrice(order.total)}</span>
              </div>
            </Link>
          </li>
        ))}
      </ul>

      {(data?.totalPages ?? 0) > 1 && (
        <div className="mt-8 flex justify-center gap-3">
          <Button variant="outline" size="sm" onClick={() => setPage((p) => p - 1)} disabled={page === 1}>Prev</Button>
          <span className="text-sm text-gray-600 self-center">Page {page} of {data?.totalPages}</span>
          <Button variant="outline" size="sm" onClick={() => setPage((p) => p + 1)} disabled={page === data?.totalPages}>Next</Button>
        </div>
      )}
    </div>
  )
}
