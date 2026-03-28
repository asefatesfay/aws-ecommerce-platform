'use client'

import { useState } from 'react'
import useSWR from 'swr'
import { ChevronLeft, ChevronRight, SlidersHorizontal, X } from 'lucide-react'
import { listProducts } from '@/lib/api'
import { ProductGrid } from '@/components/products/product-grid'
import { cn } from '@/lib/utils'
import type { PaginatedResponse, Product } from '@/lib/api'

const LIMIT = 20

const CATEGORIES = [
  { label: 'Electronics', slug: 'electronics' },
  { label: 'Clothing', slug: 'clothing' },
  { label: 'Sports', slug: 'sports' },
  { label: 'Home & Garden', slug: 'home-garden' },
  { label: 'Books', slug: 'books' },
]

const SORT_OPTIONS = [
  { label: 'Relevance', value: 'relevance' },
  { label: 'Price: Low to High', value: 'price_asc' },
  { label: 'Price: High to Low', value: 'price_desc' },
  { label: 'Newest', value: 'newest' },
]

export default function ProductsPage() {
  const [page, setPage] = useState(1)
  const [selectedCategory, setSelectedCategory] = useState<string | undefined>()
  const [minPrice, setMinPrice] = useState('')
  const [maxPrice, setMaxPrice] = useState('')
  const [inStock, setInStock] = useState(false)
  const [sort, setSort] = useState('relevance')
  const [mobileFiltersOpen, setMobileFiltersOpen] = useState(false)

  const { data, isLoading } = useSWR<PaginatedResponse<Product>>(
    ['products', page, selectedCategory, sort],
    () => listProducts(page, LIMIT, selectedCategory)
  )

  const totalPages = data?.totalPages ?? 1

  const Filters = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-sm font-semibold text-gray-900 mb-3">Category</h3>
        <ul className="space-y-2">
          <li>
            <button
              onClick={() => { setSelectedCategory(undefined); setPage(1) }}
              className={cn('text-sm w-full text-left px-2 py-1 rounded-lg transition-colors',
                !selectedCategory ? 'bg-indigo-50 text-indigo-700 font-medium' : 'text-gray-600 hover:bg-gray-100')}
            >
              All Categories
            </button>
          </li>
          {CATEGORIES.map((cat) => (
            <li key={cat.slug}>
              <button
                onClick={() => { setSelectedCategory(cat.slug); setPage(1) }}
                className={cn('text-sm w-full text-left px-2 py-1 rounded-lg transition-colors',
                  selectedCategory === cat.slug ? 'bg-indigo-50 text-indigo-700 font-medium' : 'text-gray-600 hover:bg-gray-100')}
              >
                {cat.label}
              </button>
            </li>
          ))}
        </ul>
      </div>

      <div className="border-t border-gray-200 pt-5">
        <h3 className="text-sm font-semibold text-gray-900 mb-3">Price Range</h3>
        <div className="flex items-center gap-2">
          <input
            type="number"
            placeholder="Min"
            value={minPrice}
            onChange={(e) => setMinPrice(e.target.value)}
            className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
          />
          <span className="text-gray-400 text-sm">–</span>
          <input
            type="number"
            placeholder="Max"
            value={maxPrice}
            onChange={(e) => setMaxPrice(e.target.value)}
            className="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
          />
        </div>
      </div>

      <div className="border-t border-gray-200 pt-5">
        <label className="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            checked={inStock}
            onChange={(e) => setInStock(e.target.checked)}
            className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
          />
          <span className="text-sm text-gray-700">In Stock Only</span>
        </label>
      </div>
    </div>
  )

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-2 text-sm text-gray-500 mb-6">
          <a href="/" className="hover:text-indigo-600 transition-colors">Home</a>
          <span>/</span>
          <span className="text-gray-900 font-medium">Products</span>
        </nav>

        <div className="flex gap-8">
          {/* Desktop sidebar */}
          <aside className="hidden lg:block w-56 shrink-0">
            <div className="sticky top-24 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
              <h2 className="font-semibold text-gray-900 mb-5">Filters</h2>
              <Filters />
            </div>
          </aside>

          {/* Main content */}
          <div className="flex-1 min-w-0">
            {/* Toolbar */}
            <div className="flex items-center justify-between mb-6 gap-4">
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setMobileFiltersOpen(true)}
                  className="lg:hidden flex items-center gap-2 rounded-xl border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors shadow-sm"
                >
                  <SlidersHorizontal className="h-4 w-4" />
                  Filters
                </button>
                {data && (
                  <p className="text-sm text-gray-500">{data.total} products</p>
                )}
              </div>
              <select
                value={sort}
                onChange={(e) => setSort(e.target.value)}
                className="rounded-xl border border-gray-300 bg-white px-3 py-2 text-sm text-gray-700 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 shadow-sm"
              >
                {SORT_OPTIONS.map((opt) => (
                  <option key={opt.value} value={opt.value}>{opt.label}</option>
                ))}
              </select>
            </div>

            <ProductGrid products={data?.items ?? []} loading={isLoading} />

            {/* Pagination */}
            {totalPages > 1 && (
              <div className="mt-10 flex items-center justify-center gap-2">
                <button
                  onClick={() => setPage((p) => Math.max(1, p - 1))}
                  disabled={page === 1}
                  className="rounded-xl border border-gray-300 bg-white p-2 text-gray-600 hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed transition-colors shadow-sm"
                >
                  <ChevronLeft className="h-4 w-4" />
                </button>
                {Array.from({ length: Math.min(totalPages, 7) }, (_, i) => i + 1).map((p) => (
                  <button
                    key={p}
                    onClick={() => setPage(p)}
                    className={cn(
                      'h-9 w-9 rounded-xl text-sm font-medium transition-colors shadow-sm',
                      p === page
                        ? 'bg-indigo-600 text-white'
                        : 'border border-gray-300 bg-white text-gray-700 hover:bg-gray-50'
                    )}
                  >
                    {p}
                  </button>
                ))}
                <button
                  onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
                  disabled={page === totalPages}
                  className="rounded-xl border border-gray-300 bg-white p-2 text-gray-600 hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed transition-colors shadow-sm"
                >
                  <ChevronRight className="h-4 w-4" />
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Mobile filter modal */}
      {mobileFiltersOpen && (
        <div className="fixed inset-0 z-50 lg:hidden">
          <div className="absolute inset-0 bg-black/40" onClick={() => setMobileFiltersOpen(false)} />
          <div className="absolute bottom-0 left-0 right-0 rounded-t-2xl bg-white p-6 shadow-xl max-h-[80vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-5">
              <h2 className="font-semibold text-gray-900">Filters</h2>
              <button onClick={() => setMobileFiltersOpen(false)} className="rounded-lg p-1 text-gray-500 hover:bg-gray-100">
                <X className="h-5 w-5" />
              </button>
            </div>
            <Filters />
            <button
              onClick={() => setMobileFiltersOpen(false)}
              className="mt-6 w-full rounded-xl bg-indigo-600 py-3 text-sm font-semibold text-white hover:bg-indigo-700 transition-colors"
            >
              Apply Filters
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
