'use client'

import { useState } from 'react'
import { useSearchParams } from 'next/navigation'
import useSWR from 'swr'
import { searchProducts } from '@/lib/api'
import { ProductGrid } from '@/components/products/product-grid'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import type { PaginatedResponse, Product } from '@/lib/api'

const PRICE_RANGES = [
  { label: 'Under $25', min: 0, max: 2500 },
  { label: '$25 – $50', min: 2500, max: 5000 },
  { label: '$50 – $100', min: 5000, max: 10000 },
  { label: 'Over $100', min: 10000, max: undefined },
]

export default function SearchPage() {
  const searchParams = useSearchParams()
  const q = searchParams.get('q') ?? ''
  const [page, setPage] = useState(1)
  const [minPrice, setMinPrice] = useState<number | undefined>()
  const [maxPrice, setMaxPrice] = useState<number | undefined>()

  const filters: Record<string, unknown> = {}
  if (minPrice !== undefined) filters.minPrice = minPrice
  if (maxPrice !== undefined) filters.maxPrice = maxPrice

  const { data, isLoading } = useSWR<PaginatedResponse<Product>>(
    q ? ['search', q, filters, page] : null,
    () => searchProducts(q, filters, page, 20)
  )

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-2xl font-bold mb-2">
        {q ? `Results for "${q}"` : 'Search Products'}
      </h1>
      {data && (
        <p className="text-sm text-gray-500 mb-8">{data.total} products found</p>
      )}

      <div className="flex gap-8">
        {/* Filters sidebar */}
        <aside className="hidden md:block w-56 shrink-0 space-y-6">
          <div>
            <h3 className="font-semibold text-gray-900 mb-3">Price Range</h3>
            <ul className="space-y-2">
              {PRICE_RANGES.map((r) => (
                <li key={r.label}>
                  <button
                    onClick={() => {
                      setMinPrice(r.min)
                      setMaxPrice(r.max)
                      setPage(1)
                    }}
                    className={`text-sm w-full text-left px-2 py-1 rounded hover:bg-gray-100 transition-colors ${
                      minPrice === r.min && maxPrice === r.max
                        ? 'text-primary font-medium'
                        : 'text-gray-600'
                    }`}
                  >
                    {r.label}
                  </button>
                </li>
              ))}
              <li>
                <button
                  onClick={() => { setMinPrice(undefined); setMaxPrice(undefined); setPage(1) }}
                  className="text-sm text-gray-400 hover:text-gray-700 px-2 py-1"
                >
                  Clear filter
                </button>
              </li>
            </ul>
          </div>
        </aside>

        {/* Results */}
        <div className="flex-1">
          <ProductGrid products={data?.items ?? []} loading={isLoading} />

          {(data?.totalPages ?? 0) > 1 && (
            <div className="mt-10 flex items-center justify-center gap-3">
              <Button variant="outline" size="sm" onClick={() => setPage((p) => p - 1)} disabled={page === 1}>
                Prev
              </Button>
              <span className="text-sm text-gray-600">Page {page} of {data?.totalPages}</span>
              <Button variant="outline" size="sm" onClick={() => setPage((p) => p + 1)} disabled={page === data?.totalPages}>
                Next
              </Button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
