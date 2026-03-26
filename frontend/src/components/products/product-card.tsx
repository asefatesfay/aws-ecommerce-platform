'use client'

import Image from 'next/image'
import Link from 'next/link'
import { ShoppingCart, Star } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { formatPrice, cn } from '@/lib/utils'
import type { Product } from '@/lib/api'

interface ProductCardProps {
  product: Product
}

function StarRating() {
  return (
    <div className="flex items-center gap-0.5">
      {Array.from({ length: 5 }).map((_, i) => (
        <Star key={i} className="h-3.5 w-3.5 fill-gray-200 text-gray-200" />
      ))}
    </div>
  )
}

export function ProductCard({ product }: ProductCardProps) {
  const addItem = useCartStore((s) => s.addItem)
  const isOutOfStock = product.stock === 0
  const hasDiscount =
    product.compareAtPrice != null && product.compareAtPrice > product.price
  const discountPct = hasDiscount
    ? Math.round(
        ((product.compareAtPrice! - product.price) / product.compareAtPrice!) * 100
      )
    : 0

  const handleAddToCart = () => {
    if (isOutOfStock) return
    addItem({
      productId: product.id,
      sku: product.sku,
      name: product.name,
      unitPrice: product.price,
      quantity: 1,
      imageUrl: product.imageUrl,
    })
  }

  return (
    <div
      className={cn(
        'group relative flex flex-col rounded-2xl border border-gray-200 bg-white overflow-hidden',
        'shadow-sm hover:shadow-lg hover:-translate-y-0.5 transition-all duration-200'
      )}
    >
      {/* Image */}
      <Link href={`/products/${product.id}`} className="relative block aspect-[4/3] bg-gray-100 overflow-hidden">
        <Image
          src={product.imageUrl ?? '/placeholder-product.jpg'}
          alt={product.name}
          fill
          className={cn(
            'object-cover group-hover:scale-105 transition-transform duration-300',
            isOutOfStock && 'opacity-60'
          )}
          sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
        />

        {/* Discount badge */}
        {hasDiscount && (
          <span className="absolute top-2 left-2 rounded-md bg-red-500 px-2 py-0.5 text-xs font-bold text-white">
            {discountPct}% OFF
          </span>
        )}

        {/* Out of stock overlay */}
        {isOutOfStock && (
          <div className="absolute inset-0 flex items-center justify-center bg-gray-900/40">
            <span className="rounded-lg bg-white/90 px-3 py-1 text-sm font-semibold text-gray-700">
              Out of Stock
            </span>
          </div>
        )}
      </Link>

      {/* Content */}
      <div className="flex flex-col flex-1 p-4">
        {/* Brand */}
        <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Brand</p>

        {/* Name */}
        <Link href={`/products/${product.id}`} className="flex-1">
          <h3 className="text-sm font-semibold text-gray-900 line-clamp-2 hover:text-indigo-600 transition-colors leading-snug">
            {product.name}
          </h3>
        </Link>

        {/* Stars */}
        <div className="mt-2">
          <StarRating />
        </div>

        {/* Price */}
        <div className="mt-2 flex items-baseline gap-2">
          <span className="text-base font-bold text-gray-900">{formatPrice(product.price)}</span>
          {hasDiscount && (
            <span className="text-sm text-gray-400 line-through">
              {formatPrice(product.compareAtPrice!)}
            </span>
          )}
        </div>

        {/* Add to cart */}
        <button
          onClick={handleAddToCart}
          disabled={isOutOfStock}
          className={cn(
            'mt-3 flex w-full items-center justify-center gap-2 rounded-xl py-2.5 text-sm font-semibold transition-colors',
            isOutOfStock
              ? 'cursor-not-allowed bg-gray-100 text-gray-400'
              : 'bg-indigo-600 text-white hover:bg-indigo-700'
          )}
        >
          <ShoppingCart className="h-4 w-4" />
          {isOutOfStock ? 'Out of Stock' : 'Add to Cart'}
        </button>
      </div>
    </div>
  )
}
