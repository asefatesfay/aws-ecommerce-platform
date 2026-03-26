'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { CardElement, useStripe, useElements } from '@stripe/react-stripe-js'
import { useCartStore } from '@/store/cart'
import { checkout } from '@/lib/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { formatPrice } from '@/lib/utils'
import type { ShippingAddress } from '@/lib/api'

export default function CheckoutPage() {
  const router = useRouter()
  const stripe = useStripe()
  const elements = useElements()
  const { items, total, clearCart } = useCartStore()

  const [address, setAddress] = useState<ShippingAddress>({
    fullName: '',
    line1: '',
    line2: '',
    city: '',
    state: '',
    postalCode: '',
    country: 'US',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleChange = (field: keyof ShippingAddress) => (
    e: React.ChangeEvent<HTMLInputElement>
  ) => setAddress((prev) => ({ ...prev, [field]: e.target.value }))

  const handleCheckout = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!stripe || !elements) return

    setLoading(true)
    setError(null)

    try {
      const { clientSecret, orderId } = await checkout(address)

      const cardElement = elements.getElement(CardElement)
      if (!cardElement) throw new Error('Card element not found')

      const { error: stripeError, paymentIntent } = await stripe.confirmCardPayment(
        clientSecret,
        { payment_method: { card: cardElement } }
      )

      if (stripeError) {
        setError(stripeError.message ?? 'Payment failed')
        return
      }

      if (paymentIntent?.status === 'succeeded') {
        clearCart()
        router.push(`/orders/${orderId}`)
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Something went wrong')
    } finally {
      setLoading(false)
    }
  }

  if (items.length === 0) {
    return (
      <div className="mx-auto max-w-2xl px-6 py-20 text-center">
        <p className="text-gray-500">Your cart is empty.</p>
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-4xl px-6 py-10">
      <h1 className="text-2xl font-bold mb-8">Checkout</h1>

      <form onSubmit={handleCheckout} className="grid grid-cols-1 gap-8 lg:grid-cols-2">
        {/* Shipping */}
        <div className="space-y-5">
          <h2 className="font-semibold text-lg">Shipping Address</h2>
          <Input label="Full Name" required value={address.fullName} onChange={handleChange('fullName')} />
          <Input label="Address Line 1" required value={address.line1} onChange={handleChange('line1')} />
          <Input label="Address Line 2 (optional)" value={address.line2} onChange={handleChange('line2')} />
          <div className="grid grid-cols-2 gap-4">
            <Input label="City" required value={address.city} onChange={handleChange('city')} />
            <Input label="State" required value={address.state} onChange={handleChange('state')} />
          </div>
          <div className="grid grid-cols-2 gap-4">
            <Input label="Postal Code" required value={address.postalCode} onChange={handleChange('postalCode')} />
            <Input label="Country" required value={address.country} onChange={handleChange('country')} />
          </div>

          <h2 className="font-semibold text-lg pt-4">Payment</h2>
          <div className="rounded-lg border border-gray-300 px-3 py-3">
            <CardElement
              options={{
                style: {
                  base: { fontSize: '14px', color: '#111827', '::placeholder': { color: '#9ca3af' } },
                },
              }}
            />
          </div>
          {error && <p className="text-sm text-red-600">{error}</p>}
        </div>

        {/* Order summary */}
        <div className="rounded-xl border border-gray-200 p-6 h-fit space-y-4">
          <h2 className="font-semibold text-lg">Order Summary</h2>
          <ul className="space-y-3 text-sm">
            {items.map((item) => (
              <li key={item.productId} className="flex justify-between">
                <span className="text-gray-600 truncate mr-4">
                  {item.name} × {item.quantity}
                </span>
                <span className="font-medium shrink-0">
                  {formatPrice(item.unitPrice * item.quantity)}
                </span>
              </li>
            ))}
          </ul>
          <div className="border-t border-gray-200 pt-4 flex justify-between font-semibold">
            <span>Total</span>
            <span>{formatPrice(total())}</span>
          </div>
          <Button type="submit" className="w-full" size="lg" loading={loading} disabled={!stripe}>
            Pay {formatPrice(total())}
          </Button>
        </div>
      </form>
    </div>
  )
}
