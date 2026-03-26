'use client'

import { useState } from 'react'
import Link from 'next/link'
import { ShoppingCart, User, MapPin, ChevronDown, Menu, X } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { useAuthStore } from '@/store/auth'
import { SearchBar } from '@/components/search/search-bar'
import { cn } from '@/lib/utils'

const CATEGORIES = [
  { label: 'All', slug: '' },
  { label: 'Electronics', slug: 'electronics' },
  { label: 'Clothing', slug: 'clothing' },
  { label: 'Sports', slug: 'sports' },
  { label: 'Home & Garden', slug: 'home-garden' },
  { label: 'Books', slug: 'books' },
  { label: "Today's Deals", slug: '' },
  { label: 'Customer Service', slug: '' },
  { label: 'Registry', slug: '' },
  { label: 'Gift Cards', slug: '' },
  { label: 'Sell', slug: '' },
]

export function Navbar() {
  const itemCount = useCartStore((s) => s.itemCount())
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated())
  const user = useAuthStore((s) => s.user)
  const [mobileOpen, setMobileOpen] = useState(false)

  const firstName = user?.fullName?.split(' ')[0] ?? 'Sign in'

  return (
    <header className="sticky top-0 z-50">
      {/* ── Top bar (navy) ─────────────────────────────────────────────── */}
      <div className="bg-[#131921] text-white">
        <div className="mx-auto flex max-w-[1500px] items-center gap-2 px-3 py-2">

          {/* Logo */}
          <Link
            href="/"
            className="flex items-center shrink-0 rounded border-2 border-transparent px-1 py-0.5 hover:border-white transition-colors"
          >
            <span className="text-2xl font-extrabold tracking-tight text-white leading-none">
              nexmart
            </span>
            <span className="text-[10px] text-[#ff9900] font-bold self-end mb-0.5">.com</span>
          </Link>

          {/* Deliver to */}
          <div className="hidden lg:flex flex-col shrink-0 px-2 py-0.5 rounded border-2 border-transparent hover:border-white cursor-pointer transition-colors">
            <span className="text-[11px] text-gray-300 leading-none">Deliver to</span>
            <div className="flex items-center gap-1">
              <MapPin className="h-3.5 w-3.5 text-white" />
              <span className="text-sm font-bold text-white leading-none">United States</span>
            </div>
          </div>

          {/* Search bar */}
          <div className="flex-1 min-w-0">
            <SearchBar />
          </div>

          {/* Account */}
          <Link
            href={isAuthenticated ? '/profile' : '/login'}
            className="hidden sm:flex flex-col shrink-0 px-2 py-0.5 rounded border-2 border-transparent hover:border-white transition-colors"
          >
            <span className="text-[11px] text-gray-300 leading-none">
              Hello, {firstName}
            </span>
            <div className="flex items-center gap-0.5">
              <span className="text-sm font-bold text-white leading-none">Account & Lists</span>
              <ChevronDown className="h-3 w-3 text-white" />
            </div>
          </Link>

          {/* Returns & Orders */}
          <Link
            href="/orders"
            className="hidden md:flex flex-col shrink-0 px-2 py-0.5 rounded border-2 border-transparent hover:border-white transition-colors"
          >
            <span className="text-[11px] text-gray-300 leading-none">Returns</span>
            <span className="text-sm font-bold text-white leading-none">& Orders</span>
          </Link>

          {/* Cart */}
          <Link
            href="/cart"
            className="flex items-end gap-1 shrink-0 px-2 py-0.5 rounded border-2 border-transparent hover:border-white transition-colors"
            aria-label={`Cart with ${itemCount} items`}
          >
            <div className="relative">
              <ShoppingCart className="h-8 w-8 text-white" />
              <span className="absolute -top-1 left-4 min-w-[18px] text-center text-sm font-bold text-[#ff9900] leading-none">
                {itemCount}
              </span>
            </div>
            <span className="hidden sm:block text-sm font-bold text-white leading-none mb-1">Cart</span>
          </Link>

          {/* Mobile menu toggle */}
          <button
            className="sm:hidden p-1 rounded border-2 border-transparent hover:border-white transition-colors"
            onClick={() => setMobileOpen((v) => !v)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* ── Nav bar (dark navy) ─────────────────────────────────────────── */}
      <div className="bg-[#232f3e] text-white">
        <div className="mx-auto flex max-w-[1500px] items-center gap-0 px-3 overflow-x-auto scrollbar-hide">
          {/* All menu */}
          <button className="flex items-center gap-1.5 shrink-0 px-3 py-2.5 text-sm font-bold hover:bg-white/10 rounded transition-colors border-2 border-transparent hover:border-white">
            <Menu className="h-4 w-4" />
            All
          </button>

          {CATEGORIES.slice(1).map((cat) => (
            <Link
              key={cat.label}
              href={cat.slug ? `/products?category=${cat.slug}` : '/products'}
              className="shrink-0 px-3 py-2.5 text-sm whitespace-nowrap hover:bg-white/10 rounded transition-colors border-2 border-transparent hover:border-white"
            >
              {cat.label}
            </Link>
          ))}
        </div>
      </div>

      {/* ── Mobile drawer ───────────────────────────────────────────────── */}
      {mobileOpen && (
        <div className="sm:hidden bg-white border-b border-gray-200 shadow-lg">
          <div className="px-4 py-3 space-y-1">
            {!isAuthenticated && (
              <Link
                href="/login"
                className="block w-full text-center rounded bg-[#ff9900] px-4 py-2 text-sm font-bold text-[#131921] hover:bg-[#e68a00] transition-colors mb-3"
                onClick={() => setMobileOpen(false)}
              >
                Sign in
              </Link>
            )}
            {CATEGORIES.map((cat) => (
              <Link
                key={cat.label}
                href={cat.slug ? `/products?category=${cat.slug}` : '/products'}
                className="block px-3 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded transition-colors"
                onClick={() => setMobileOpen(false)}
              >
                {cat.label}
              </Link>
            ))}
          </div>
        </div>
      )}
    </header>
  )
}
