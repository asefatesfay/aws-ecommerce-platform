'use client'

import { useState } from 'react'
import { X } from 'lucide-react'
import { Navbar } from '@/components/layout/navbar'
import { Footer } from '@/components/layout/footer'

export default function ShopLayout({ children }: { children: React.ReactNode }) {
  const [announcementVisible, setAnnouncementVisible] = useState(true)

  return (
    <div className="flex min-h-screen flex-col">
      {/* Announcement bar */}
      {announcementVisible && (
        <div className="relative bg-amber-400 px-4 py-2.5 text-center">
          <p className="text-sm font-medium text-amber-900">
            🎉 Free shipping on orders over $50 &nbsp;|&nbsp; Use code{' '}
            <span className="font-bold">WELCOME10</span> for 10% off your first order
          </p>
          <button
            onClick={() => setAnnouncementVisible(false)}
            className="absolute right-3 top-1/2 -translate-y-1/2 rounded-lg p-1 text-amber-800 hover:bg-amber-500 transition-colors"
            aria-label="Dismiss announcement"
          >
            <X className="h-4 w-4" />
          </button>
        </div>
      )}

      <Navbar />
      <main className="flex-1">{children}</main>
      <Footer />
    </div>
  )
}
