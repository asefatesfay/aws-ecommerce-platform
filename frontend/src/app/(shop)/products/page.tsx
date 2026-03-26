'use client'

import { useState } from 'react'
import useSWR from 'swr'
import { ChevronLeft, ChevronRight } from 'lucide-react'
import { listProducts } from '@/lib/api'
import { ProductGrid } from '@/components/products/product-grid'
import { Button } from '@/components/ui/button'
import type { PaginatedResponse, Product } from '@/lib/api'

const LIMIT = 20

export default function ProductsPage() {
  const [page, setPage] = useState(1)
  const { data, isLoading } = useSWR<PaginatedResponse<Product>>(
    ['products', page],
    () => listProducts(page, LIMIT)
  )

  const totalPages = data?.totalPages ?? 1

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <h1 className="text-2xl font-bold mb-8">All Products</h1>
      <ProductGrid products={data?.items ?? []} loading={isLoading} />

      {totalPages > 1 && (
        <div className="mt-10 flex items-center justify-center gap-3">
          <Button
            variant="outline"
            size="sm"
            onClick={() => setPage((p) => Math.max(1, p - 1))}
            disabled={page === 1}
          >
            <ChevronLeft className="h-4 w-4" />
            Prev
          </Button>
          <span className="text-sm text-gray-600">
            Page {page} of {totalPages}
          </span>
          <Button
            variant="outline"
            size="sm"
            onClick={() => setPage((p) => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
          >
            Next
            <ChevronRight className="h-4 w-4" />
          </Button>
        </div>
      )}
    </div>
  )
}
