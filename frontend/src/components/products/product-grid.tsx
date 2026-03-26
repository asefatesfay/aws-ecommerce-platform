import { ShoppingBag } from 'lucide-react'
import { ProductCard } from './product-card'
import type { Product } from '@/lib/api'

interface ProductGridProps {
  products: Product[]
  loading?: boolean
}

function SkeletonCard() {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white overflow-hidden animate-pulse">
      <div className="aspect-[4/3] bg-gray-200" />
      <div className="p-4 space-y-3">
        <div className="h-3 bg-gray-200 rounded w-1/4" />
        <div className="h-4 bg-gray-200 rounded w-3/4" />
        <div className="h-3 bg-gray-200 rounded w-1/2" />
        <div className="h-5 bg-gray-200 rounded w-1/3" />
        <div className="h-9 bg-gray-200 rounded-xl" />
      </div>
    </div>
  )
}

export function ProductGrid({ products, loading }: ProductGridProps) {
  if (loading) {
    return (
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        {Array.from({ length: 8 }).map((_, i) => (
          <SkeletonCard key={i} />
        ))}
      </div>
    )
  }

  if (products.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20 text-center">
        <ShoppingBag className="h-16 w-16 text-gray-200 mb-4" />
        <h3 className="text-lg font-semibold text-gray-700">No products found</h3>
        <p className="mt-1 text-sm text-gray-400">Try adjusting your filters or search query.</p>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  )
}
