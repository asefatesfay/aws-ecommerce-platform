'use client'

import { useEffect } from 'react'
import { SWRConfig } from 'swr'
import { Elements } from '@stripe/react-stripe-js'
import { loadStripe } from '@stripe/stripe-js'
import { fetcher } from '@/lib/fetcher'
import { useCartStore } from '@/store/cart'
import { useAuthStore } from '@/store/auth'

const stripePromise = loadStripe(
  process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY ?? ''
)

export function Providers({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    useCartStore.persist.rehydrate()
    useAuthStore.persist.rehydrate()
  }, [])

  return (
    <SWRConfig
      value={{
        fetcher,
        shouldRetryOnError: false,
        revalidateOnFocus: false,
      }}
    >
      <Elements stripe={stripePromise}>{children}</Elements>
    </SWRConfig>
  )
}
