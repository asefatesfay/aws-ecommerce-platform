'use client'

import { useState } from 'react'
import useSWR from 'swr'
import { ChevronLeft, ChevronRight } from 'lucide-react'
import { listProducts } from '@/lib/api'
import { ProductGrid } from '@/components/products/product-grid'
import type { PaginatedResponse, Product } from '@/lib/api'

export default function ProductsPage() {
  const [page, setPage] = useState(1)
  const { data, isLoading } = useSWR<PaginatedResponse<Product>>(
    ['products', page],
    () => listProducts(page, 20)
  )

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-2xl font-bold mb-8">All Products</h1>
      <ProductGrid products={data?.items ?? []} loading={isLoading} />
      {(data?.totalPages ?? 0) > 1 && (
        <div className="mt-10 flex items-center justify-center gap-3">
          <button onClick={() => setPage(p => p - 1)} disabled={page === 1}>
            <ChevronLeft className="h-4 w-4" />
          </button>
          <span>Page {page} of {data?.totalPages}</span>
          <button onClick={() => setPage(p => p + 1)} disabled={page === data?.totalPages}>
            <ChevronRight className="h-4 w-4" />
          </button>
        </div>
      )}
    </div>
  )
}
