'use client'

import Image from 'next/image'
import Link from 'next/link'
import { Minus, Plus, Trash2, ShoppingBag, ArrowLeft, Truck } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { formatPrice } from '@/lib/utils'

const SHIPPING_THRESHOLD = 5000 // $50.00 in cents
const SHIPPING_COST = 999       // $9.99 in cents
const TAX_RATE = 0.08

export default function CartPage() {
  const { items, updateItem, removeItem, total } = useCartStore()

  const subtotal = total()
  const shipping = subtotal >= SHIPPING_THRESHOLD ? 0 : SHIPPING_COST
  const tax = Math.round(subtotal * TAX_RATE)
  const orderTotal = subtotal + shipping + tax

  if (items.length === 0) {
    return (
      <div className="bg-gray-50 min-h-screen">
        <div className="mx-auto max-w-2xl px-6 py-24 text-center">
          <ShoppingBag className="mx-auto h-20 w-20 text-gray-200 mb-6" />
          <h1 className="text-2xl font-bold text-gray-900 mb-2">Your cart is empty</h1>
          <p className="text-gray-500 mb-8">Looks like you haven&apos;t added anything yet.</p>
          <Link
            href="/products"
            className="inline-flex items-center gap-2 rounded-xl bg-indigo-600 px-8 py-3.5 text-sm font-semibold text-white hover:bg-indigo-700 transition-colors"
          >
            <ShoppingBag className="h-4 w-4" />
            Shop Now
          </Link>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
        <h1 className="text-2xl font-bold text-gray-900 mb-8">Shopping Cart</h1>

        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3">
          {/* Cart items */}
          <div className="lg:col-span-2 space-y-4">
            {items.map((item) => (
              <div
                key={item.productId}
                className="flex gap-4 rounded-2xl border border-gray-200 bg-white p-4 shadow-sm"
              >
                {/* Thumbnail */}
                <Link href={`/products/${item.productId}`} className="relative h-24 w-24 shrink-0 rounded-xl overflow-hidden bg-gray-100">
                  <Image
                    src={item.imageUrl ?? '/placeholder-product.jpg'}
                    alt={item.name}
                    fill
                    className="object-cover"
                    sizes="96px"
                  />
                </Link>

                {/* Info */}
                <div className="flex flex-1 min-w-0 flex-col justify-between">
                  <div>
                    <Link
                      href={`/products/${item.productId}`}
                      className="font-semibold text-gray-900 hover:text-indigo-600 line-clamp-2 transition-colors text-sm"
                    >
                      {item.name}
                    </Link>
                    <p className="text-xs text-gray-400 mt-0.5">SKU: {item.sku}</p>
                  </div>

                  <div className="flex items-center gap-3 mt-3">
                    {/* Quantity stepper */}
                    <div className="flex items-center rounded-xl border border-gray-300 bg-gray-50 overflow-hidden">
                      <button
                        onClick={() => updateItem(item.productId, item.quantity - 1)}
                        className="px-2.5 py-1.5 text-gray-600 hover:bg-gray-200 transition-colors"
                        aria-label="Decrease quantity"
                      >
                        <Minus className="h-3.5 w-3.5" />
                      </button>
                      <span className="w-8 text-center text-sm font-semibold text-gray-900">
                        {item.quantity}
                      </span>
                      <button
                        onClick={() => updateItem(item.productId, item.quantity + 1)}
                        className="px-2.5 py-1.5 text-gray-600 hover:bg-gray-200 transition-colors"
                        aria-label="Increase quantity"
                      >
                        <Plus className="h-3.5 w-3.5" />
                      </button>
                    </div>

                    {/* Remove */}
                    <button
                      onClick={() => removeItem(item.productId)}
                      className="rounded-lg p-1.5 text-gray-400 hover:bg-red-50 hover:text-red-500 transition-colors"
                      aria-label="Remove item"
                    >
                      <Trash2 className="h-4 w-4" />
                    </button>
                  </div>
                </div>

                {/* Price */}
                <div className="text-right shrink-0">
                  <p className="font-bold text-gray-900">{formatPrice(item.unitPrice * item.quantity)}</p>
                  <p className="text-xs text-gray-400 mt-0.5">{formatPrice(item.unitPrice)} each</p>
                </div>
              </div>
            ))}

            <Link
              href="/products"
              className="inline-flex items-center gap-2 text-sm font-medium text-indigo-600 hover:text-indigo-700 transition-colors mt-2"
            >
              <ArrowLeft className="h-4 w-4" />
              Continue Shopping
            </Link>
          </div>

          {/* Order summary */}
          <div className="lg:col-span-1">
            <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm sticky top-24">
              <h2 className="text-lg font-bold text-gray-900 mb-5">Order Summary</h2>

              <div className="space-y-3 text-sm">
                <div className="flex justify-between text-gray-600">
                  <span>Subtotal ({items.reduce((s, i) => s + i.quantity, 0)} items)</span>
                  <span className="font-medium text-gray-900">{formatPrice(subtotal)}</span>
                </div>
                <div className="flex justify-between text-gray-600">
                  <span>Shipping</span>
                  <span className={shipping === 0 ? 'font-medium text-green-600' : 'font-medium text-gray-900'}>
                    {shipping === 0 ? 'Free' : formatPrice(shipping)}
                  </span>
                </div>
                <div className="flex justify-between text-gray-600">
                  <span>Tax (8%)</span>
                  <span className="font-medium text-gray-900">{formatPrice(tax)}</span>
                </div>
              </div>

              {shipping > 0 && (
                <div className="mt-4 flex items-center gap-2 rounded-xl bg-amber-50 border border-amber-200 px-3 py-2.5">
                  <Truck className="h-4 w-4 text-amber-600 shrink-0" />
                  <p className="text-xs text-amber-700">
                    Add {formatPrice(SHIPPING_THRESHOLD - subtotal)} more for free shipping
                  </p>
                </div>
              )}

              <div className="mt-5 border-t border-gray-200 pt-4 flex justify-between">
                <span className="font-bold text-gray-900">Total</span>
                <span className="text-xl font-bold text-gray-900">{formatPrice(orderTotal)}</span>
              </div>

              <Link
                href="/checkout"
                className="mt-5 flex w-full items-center justify-center rounded-xl bg-indigo-600 py-3.5 text-sm font-semibold text-white hover:bg-indigo-700 transition-colors"
              >
                Proceed to Checkout
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
