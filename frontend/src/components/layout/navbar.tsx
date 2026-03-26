'use client'

import { useState } from 'react'
import Link from 'next/link'
import { ShoppingBag, ShoppingCart, User, Menu, X, ChevronDown } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { useAuthStore } from '@/store/auth'
import { SearchBar } from '@/components/search/search-bar'
import { cn } from '@/lib/utils'

const CATEGORIES = [
  { label: 'Electronics', slug: 'electronics' },
  { label: 'Clothing', slug: 'clothing' },
  { label: 'Sports', slug: 'sports' },
  { label: 'Home & Garden', slug: 'home-garden' },
  { label: 'Books', slug: 'books' },
]

export function Navbar() {
  const itemCount = useCartStore((s) => s.itemCount())
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated())
  const user = useAuthStore((s) => s.user)
  const [mobileOpen, setMobileOpen] = useState(false)
  const [categoriesOpen, setCategoriesOpen] = useState(false)

  return (
    <header className="sticky top-0 z-50 bg-white shadow-sm">
      {/* Main bar */}
      <div className="mx-auto flex max-w-7xl items-center gap-4 px-4 py-3 sm:px-6">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-1.5 shrink-0">
          <ShoppingBag className="h-6 w-6 text-indigo-600" />
          <span className="text-xl font-extrabold tracking-tight text-indigo-600">NEXMART</span>
        </Link>

        {/* Search — hidden on mobile, shown on sm+ */}
        <div className="hidden sm:flex flex-1 max-w-2xl">
          <SearchBar />
        </div>

        {/* Right actions */}
        <nav className="flex items-center gap-1 shrink-0 ml-auto sm:ml-0">
          {/* Categories dropdown — desktop */}
          <div className="relative hidden md:block">
            <button
              onClick={() => setCategoriesOpen((v) => !v)}
              onBlur={() => setTimeout(() => setCategoriesOpen(false), 150)}
              className="flex items-center gap-1 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 transition-colors"
            >
              Categories
              <ChevronDown className={cn('h-4 w-4 transition-transform', categoriesOpen && 'rotate-180')} />
            </button>
            {categoriesOpen && (
              <div className="absolute right-0 top-full mt-1 w-48 rounded-xl border border-gray-100 bg-white shadow-lg py-1 z-50">
                {CATEGORIES.map((cat) => (
                  <Link
                    key={cat.slug}
                    href={`/products?category=${cat.slug}`}
                    className="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                    onClick={() => setCategoriesOpen(false)}
                  >
                    {cat.label}
                  </Link>
                ))}
              </div>
            )}
          </div>

          {/* Cart */}
          <Link
            href="/cart"
            className="relative p-2 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-indigo-600 transition-colors"
            aria-label="Cart"
          >
            <ShoppingCart className="h-5 w-5" />
            {itemCount > 0 && (
              <span className="absolute -top-0.5 -right-0.5 flex h-4 w-4 items-center justify-center rounded-full bg-indigo-600 text-[10px] font-bold text-white">
                {itemCount > 99 ? '99+' : itemCount}
              </span>
            )}
          </Link>

          {/* Auth */}
          {isAuthenticated ? (
            <Link
              href="/profile"
              className="flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 transition-colors"
            >
              <User className="h-4 w-4" />
              <span className="hidden sm:inline">{user?.fullName?.split(' ')[0] ?? 'Profile'}</span>
            </Link>
          ) : (
            <Link
              href="/login"
              className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700 transition-colors"
            >
              Login
            </Link>
          )}

          {/* Mobile hamburger */}
          <button
            className="ml-1 p-2 rounded-lg text-gray-600 hover:bg-gray-100 transition-colors sm:hidden"
            onClick={() => setMobileOpen((v) => !v)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </nav>
      </div>

      {/* Mobile search */}
      <div className="sm:hidden px-4 pb-3">
        <SearchBar />
      </div>

      {/* Category bar — desktop only */}
      <div className="hidden md:block border-t border-gray-100 bg-gray-50">
        <div className="mx-auto flex max-w-7xl items-center gap-1 px-6 py-1.5">
          {CATEGORIES.map((cat) => (
            <Link
              key={cat.slug}
              href={`/products?category=${cat.slug}`}
              className="rounded-md px-3 py-1 text-sm text-gray-600 hover:bg-white hover:text-indigo-600 hover:shadow-sm transition-all"
            >
              {cat.label}
            </Link>
          ))}
        </div>
      </div>

      {/* Mobile drawer */}
      {mobileOpen && (
        <div className="sm:hidden border-t border-gray-100 bg-white shadow-lg">
          <div className="px-4 py-3 space-y-1">
            <p className="text-xs font-semibold uppercase tracking-wider text-gray-400 px-2 mb-2">Categories</p>
            {CATEGORIES.map((cat) => (
              <Link
                key={cat.slug}
                href={`/products?category=${cat.slug}`}
                className="block rounded-lg px-3 py-2 text-sm text-gray-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                onClick={() => setMobileOpen(false)}
              >
                {cat.label}
              </Link>
            ))}
            <div className="border-t border-gray-100 pt-2 mt-2">
              <Link
                href="/products"
                className="block rounded-lg px-3 py-2 text-sm text-gray-700 hover:bg-gray-50 transition-colors"
                onClick={() => setMobileOpen(false)}
              >
                All Products
              </Link>
              {!isAuthenticated && (
                <Link
                  href="/register"
                  className="block rounded-lg px-3 py-2 text-sm text-gray-700 hover:bg-gray-50 transition-colors"
                  onClick={() => setMobileOpen(false)}
                >
                  Create Account
                </Link>
              )}
            </div>
          </div>
        </div>
      )}
    </header>
  )
}
