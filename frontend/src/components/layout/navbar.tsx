'use client'

import Link from 'next/link'
import { ShoppingCart, User } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { useAuthStore } from '@/store/auth'
import { SearchBar } from '@/components/search/search-bar'

export function Navbar() {
  const itemCount = useCartStore((s) => s.itemCount())
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated())

  return (
    <header className="sticky top-0 z-50 border-b border-gray-200 bg-white/95 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center gap-4 px-6 py-3">
        {/* Logo */}
        <Link href="/" className="text-xl font-bold text-primary shrink-0">
          Shop
        </Link>

        {/* Search */}
        <div className="flex-1 max-w-xl">
          <SearchBar />
        </div>

        {/* Actions */}
        <nav className="flex items-center gap-3 shrink-0">
          <Link href="/cart" className="relative p-2 text-gray-600 hover:text-primary transition-colors">
            <ShoppingCart className="h-5 w-5" />
            {itemCount > 0 && (
              <span className="absolute -top-0.5 -right-0.5 flex h-4 w-4 items-center justify-center rounded-full bg-primary text-[10px] font-bold text-white">
                {itemCount > 99 ? '99+' : itemCount}
              </span>
            )}
          </Link>

          {isAuthenticated ? (
            <Link href="/profile" className="p-2 text-gray-600 hover:text-primary transition-colors">
              <User className="h-5 w-5" />
            </Link>
          ) : (
            <Link
              href="/login"
              className="rounded-lg bg-primary px-4 py-1.5 text-sm font-medium text-white hover:bg-primary-dark transition-colors"
            >
              Login
            </Link>
          )}
        </nav>
      </div>
    </header>
  )
}
