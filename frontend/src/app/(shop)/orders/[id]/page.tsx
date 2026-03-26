'use client'

import { useParams } from 'next/navigation'
import useSWR from 'swr'
import Image from 'next/image'
import { CheckCircle, Clock, Package, Truck } from 'lucide-react'
import { getOrder } from '@/lib/api'
import { Badge } from '@/components/ui/badge'
import { formatPrice } from '@/lib/utils'
import type { Order } from '@/lib/api'

const TIMELINE = [
  { key: 'pending', label: 'Order Placed', icon: Clock },
  { key: 'processing', label: 'Processing', icon: Package },
  { key: 'shipped', label: 'Shipped', icon: Truck },
  { key: 'delivered', label: 'Delivered', icon: CheckCircle },
]

const ORDER_STATUS_INDEX: Record<string, number> = {
  pending: 0,
  processing: 1,
  shipped: 2,
  delivered: 3,
}

export default function OrderDetailPage() {
  const { id } = useParams<{ id: string }>()
  const { data: order, isLoading } = useSWR<Order>(
    id ? ['order', id] : null,
    () => getOrder(id)
  )

  if (isLoading) {
    return (
      <div className="mx-auto max-w-3xl px-6 py-10 space-y-6 animate-pulse">
        <div className="h-8 bg-gray-200 rounded w-1/3" />
        <div className="h-24 bg-gray-100 rounded-xl" />
        <div className="h-48 bg-gray-100 rounded-xl" />
      </div>
    )
  }

  if (!order) return <div className="p-10 text-center text-gray-500">Order not found.</div>

  const currentStep = ORDER_STATUS_INDEX[order.status] ?? 0

  return (
    <div className="mx-auto max-w-3xl px-6 py-10 space-y-8">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold">Order #{order.id.slice(-8).toUpperCase()}</h1>
        <Badge variant={order.status === 'delivered' ? 'success' : order.status === 'cancelled' ? 'destructive' : 'primary'}>
          {order.status}
        </Badge>
      </div>

      {/* Status timeline */}
      {order.status !== 'cancelled' && (
        <div className="flex items-center gap-0">
          {TIMELINE.map((step, i) => {
            const Icon = step.icon
            const done = i <= currentStep
            return (
              <div key={step.key} className="flex items-center flex-1 last:flex-none">
                <div className="flex flex-col items-center gap-1">
                  <div className={`rounded-full p-2 ${done ? 'bg-primary text-white' : 'bg-gray-100 text-gray-400'}`}>
                    <Icon className="h-4 w-4" />
                  </div>
                  <span className={`text-xs ${done ? 'text-primary font-medium' : 'text-gray-400'}`}>
                    {step.label}
                  </span>
                </div>
                {i < TIMELINE.length - 1 && (
                  <div className={`flex-1 h-0.5 mb-5 ${i < currentStep ? 'bg-primary' : 'bg-gray-200'}`} />
                )}
              </div>
            )
          })}
        </div>
      )}

      {/* Items */}
      <div className="rounded-xl border border-gray-200 divide-y divide-gray-100">
        {order.items.map((item) => (
          <div key={item.productId} className="flex items-center justify-between px-5 py-4">
            <div>
              <p className="font-medium text-gray-900">{item.name}</p>
              <p className="text-sm text-gray-500">Qty: {item.quantity}</p>
            </div>
            <span className="font-semibold">{formatPrice(item.unitPrice * item.quantity)}</span>
          </div>
        ))}
        <div className="flex justify-between px-5 py-4 font-semibold">
          <span>Total</span>
          <span>{formatPrice(order.total)}</span>
        </div>
      </div>

      {/* Shipping address */}
      <div className="rounded-xl border border-gray-200 p-5">
        <h2 className="font-semibold mb-3">Shipping Address</h2>
        <address className="not-italic text-sm text-gray-600 space-y-0.5">
          <p>{order.shippingAddress.fullName}</p>
          <p>{order.shippingAddress.line1}</p>
          {order.shippingAddress.line2 && <p>{order.shippingAddress.line2}</p>}
          <p>
            {order.shippingAddress.city}, {order.shippingAddress.state}{' '}
            {order.shippingAddress.postalCode}
          </p>
          <p>{order.shippingAddress.country}</p>
        </address>
      </div>
    </div>
  )
}
