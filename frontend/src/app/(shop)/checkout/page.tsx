'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { CardElement, useStripe, useElements } from '@stripe/react-stripe-js'
import { useCartStore } from '@/store/cart'
import { useAuthStore } from '@/store/auth'
import { createOrder, createPaymentIntent } from '@/lib/api'
import { formatPrice, cn } from '@/lib/utils'
import { Lock, Truck } from 'lucide-react'

const TAX_RATE = 0.08
const SHIPPING_THRESHOLD = 50
const SHIPPING_COST = 9.99

export default function CheckoutPage() {
  const router = useRouter()
  const stripe = useStripe()
  const elements = useElements()
  const { items, total, clearCart } = useCartStore()
  const user = useAuthStore((s) => s.user)

  const [address, setAddress] = useState({
    full_name: user?.fullName ?? '',
    street: '',
    city: '',
    state: '',
    postal_code: '',
    country: 'US',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [step, setStep] = useState<'form' | 'processing' | 'done'>('form')

  const subtotal = total()
  const shipping = subtotal >= SHIPPING_THRESHOLD ? 0 : SHIPPING_COST
  const tax = Math.round(subtotal * TAX_RATE * 100) / 100
  const orderTotal = subtotal + shipping + tax

  const handleChange = (field: keyof typeof address) =>
    (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) =>
      setAddress((prev) => ({ ...prev, [field]: e.target.value }))

  const handleCheckout = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!stripe || !elements || items.length === 0) return

    setLoading(true)
    setError(null)
    setStep('processing')

    try {
      const userId = user?.id ?? 'guest-' + Date.now()

      // Step 1: Create order
      const order = await createOrder({
        items: items.map((i) => ({
          product_id: i.productId,
          sku: i.sku,
          name: i.name,
          unit_price: i.unitPrice,
          quantity: i.quantity,
        })),
        shipping_address: address,
      }, userId)

      if (!order.id) throw new Error('Order creation failed')

      // Step 2: Create payment intent
      const { clientSecret } = await createPaymentIntent(order.id, orderTotal)

      // Step 3: Confirm payment with Stripe
      const cardElement = elements.getElement(CardElement)
      if (!cardElement) throw new Error('Card element not found')

      const { error: stripeError, paymentIntent } = await stripe.confirmCardPayment(
        clientSecret,
        { payment_method: { card: cardElement } }
      )

      if (stripeError) {
        setError(stripeError.message ?? 'Payment failed')
        setStep('form')
        return
      }

      if (paymentIntent?.status === 'succeeded') {
        clearCart()
        setStep('done')
        router.push(`/orders/${order.id}`)
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Something went wrong. Please try again.')
      setStep('form')
    } finally {
      setLoading(false)
    }
  }

  if (items.length === 0) {
    return (
      <div className="bg-[#eaeded] min-h-screen flex items-center justify-center">
        <div className="bg-white p-8 text-center max-w-sm w-full">
          <p className="text-[#0f1111] mb-4">Your cart is empty.</p>
          <a href="/products" className="text-[#007185] hover:text-[#c45500] hover:underline text-sm">
            Continue shopping
          </a>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-[#eaeded] min-h-screen">
      <div className="mx-auto max-w-5xl px-4 py-6">
        {/* Header */}
        <div className="flex items-center gap-2 mb-6">
          <a href="/" className="text-xl font-extrabold text-[#131921]">nexmart</a>
          <span className="text-gray-400 text-sm">/ Checkout</span>
        </div>

        <form onSubmit={handleCheckout} className="grid grid-cols-1 gap-4 lg:grid-cols-[1fr_320px]">
          {/* Left column */}
          <div className="space-y-4">
            {/* Shipping address */}
            <div className="bg-white p-5 border border-gray-200">
              <h2 className="text-lg font-bold text-[#0f1111] mb-4">1. Shipping address</h2>
              <div className="space-y-3">
                <div>
                  <label className="block text-xs font-medium text-[#0f1111] mb-1">Full name</label>
                  <input
                    required
                    value={address.full_name}
                    onChange={handleChange('full_name')}
                    className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                  />
                </div>
                <div>
                  <label className="block text-xs font-medium text-[#0f1111] mb-1">Street address</label>
                  <input
                    required
                    value={address.street}
                    onChange={handleChange('street')}
                    className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                  />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-medium text-[#0f1111] mb-1">City</label>
                    <input
                      required
                      value={address.city}
                      onChange={handleChange('city')}
                      className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-[#0f1111] mb-1">State</label>
                    <input
                      required
                      value={address.state}
                      onChange={handleChange('state')}
                      className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                    />
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-medium text-[#0f1111] mb-1">ZIP code</label>
                    <input
                      required
                      value={address.postal_code}
                      onChange={handleChange('postal_code')}
                      className="w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-[#0f1111] mb-1">Country</label>
                    <select
                      value={address.country}
                      onChange={handleChange('country')}
                      className="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-[#f0f2f2] focus:outline-none focus:border-[#e77600]"
                    >
                      <option value="US">United States</option>
                      <option value="CA">Canada</option>
                      <option value="GB">United Kingdom</option>
                      <option value="AU">Australia</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>

            {/* Payment */}
            <div className="bg-white p-5 border border-gray-200">
              <h2 className="text-lg font-bold text-[#0f1111] mb-4">2. Payment method</h2>
              <div className="border border-gray-300 rounded px-3 py-3 bg-white">
                <CardElement
                  options={{
                    style: {
                      base: {
                        fontSize: '14px',
                        color: '#0f1111',
                        '::placeholder': { color: '#9ca3af' },
                      },
                    },
                  }}
                />
              </div>
              {error && (
                <p className="mt-2 text-sm text-[#cc0c39] bg-[#fff3f3] border border-[#cc0c39]/20 rounded px-3 py-2">
                  {error}
                </p>
              )}
              <div className="flex items-center gap-1.5 mt-3 text-xs text-gray-500">
                <Lock className="h-3 w-3" />
                <span>Secure payment — your card details are encrypted</span>
              </div>
            </div>
          </div>

          {/* Right column — order summary */}
          <div className="space-y-4">
            <div className="bg-white p-5 border border-gray-200">
              <button
                type="submit"
                disabled={loading || !stripe}
                className={cn(
                  'w-full rounded-full py-3 text-sm font-bold border transition-colors mb-4',
                  loading || !stripe
                    ? 'bg-gray-200 text-gray-400 border-gray-200 cursor-not-allowed'
                    : 'bg-[#ffd814] border-[#fcd200] text-[#0f1111] hover:bg-[#f7ca00]'
                )}
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="h-4 w-4 border-2 border-gray-400 border-t-transparent rounded-full animate-spin" />
                    {step === 'processing' ? 'Processing...' : 'Loading...'}
                  </span>
                ) : (
                  `Place your order — ${formatPrice(orderTotal)}`
                )}
              </button>

              <p className="text-xs text-gray-500 text-center mb-4">
                By placing your order, you agree to our{' '}
                <a href="#" className="text-[#007185] hover:underline">Terms of Service</a>
              </p>

              <h3 className="text-base font-bold text-[#0f1111] mb-3">Order Summary</h3>

              <div className="space-y-2 text-sm">
                <div className="flex justify-between text-[#0f1111]">
                  <span>Items ({items.reduce((s, i) => s + i.quantity, 0)}):</span>
                  <span>{formatPrice(subtotal)}</span>
                </div>
                <div className="flex justify-between text-[#0f1111]">
                  <span>Shipping:</span>
                  <span className={shipping === 0 ? 'text-[#007600]' : ''}>
                    {shipping === 0 ? 'FREE' : formatPrice(shipping)}
                  </span>
                </div>
                <div className="flex justify-between text-[#0f1111]">
                  <span>Tax (8%):</span>
                  <span>{formatPrice(tax)}</span>
                </div>
                <div className="border-t border-gray-200 pt-2 flex justify-between font-bold text-[#cc0c39] text-base">
                  <span>Order total:</span>
                  <span>{formatPrice(orderTotal)}</span>
                </div>
              </div>

              {shipping > 0 && (
                <div className="mt-3 flex items-center gap-2 text-xs text-[#007185] bg-[#f0f9ff] border border-[#007185]/20 rounded px-3 py-2">
                  <Truck className="h-3.5 w-3.5 shrink-0" />
                  <span>Add {formatPrice(SHIPPING_THRESHOLD - subtotal)} more for FREE shipping</span>
                </div>
              )}
            </div>

            {/* Items list */}
            <div className="bg-white p-4 border border-gray-200">
              <h3 className="text-sm font-bold text-[#0f1111] mb-3">Items in your order</h3>
              <ul className="space-y-3">
                {items.map((item) => (
                  <li key={item.productId} className="flex gap-3 text-xs">
                    <div className="h-12 w-12 shrink-0 bg-gray-100 rounded overflow-hidden">
                      {item.imageUrl && (
                        // eslint-disable-next-line @next/next/no-img-element
                        <img src={item.imageUrl} alt={item.name} className="h-full w-full object-contain p-1" />
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-[#0f1111] line-clamp-2 leading-snug">{item.name}</p>
                      <p className="text-gray-500 mt-0.5">Qty: {item.quantity}</p>
                    </div>
                    <span className="font-medium text-[#0f1111] shrink-0">
                      {formatPrice(item.unitPrice * item.quantity)}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </form>
      </div>
    </div>
  )
}
