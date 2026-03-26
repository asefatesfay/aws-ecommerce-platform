'use client'

import Image from 'next/image'
import Link from 'next/link'
import { Star } from 'lucide-react'
import { useCartStore } from '@/store/cart'
import { formatPrice, cn } from '@/lib/utils'
import type { Product } from '@/lib/api'

interface ProductCardProps {
  product: Product
}

function StarRating({ rating = 4.2, count = 1284 }: { rating?: number; count?: number }) {
  const full = Math.floor(rating)
  const half = rating % 1 >= 0.5
  return (
    <div className="flex items-center gap-1">
      <div className="flex items-center">
        {Array.from({ length: 5 }).map((_, i) => (
          <Star
            key={i}
            className={cn(
              'h-3.5 w-3.5',
              i < full
                ? 'fill-[#ff9900] text-[#ff9900]'
                : i === full && half
                ? 'fill-[#ff9900]/50 text-[#ff9900]'
                : 'fill-gray-200 text-gray-200'
            )}
          />
        ))}
      </div>
      <span className="text-xs text-[#007185] hover:text-[#c45500] cursor-pointer">
        {count.toLocaleString()}
      </span>
    </div>
  )
}

export function ProductCard({ product }: ProductCardProps) {
  const addItem = useCartStore((s) => s.addItem)
  const isOutOfStock = product.stock === 0
  const hasDiscount = product.compareAtPrice != null && product.compareAtPrice > product.price
  const discountPct = hasDiscount
    ? Math.round(((product.compareAtPrice! - product.price) / product.compareAtPrice!) * 100)
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
    <div className="group flex flex-col bg-white border border-gray-200 hover:shadow-md transition-shadow duration-200 overflow-hidden">
      {/* Image */}
      <Link href={`/products/${product.id}`} className="relative block aspect-square bg-white overflow-hidden p-4">
        <Image
          src={product.imageUrl ?? '/placeholder-product.jpg'}
          alt={product.name}
          fill
          className={cn(
            'object-contain group-hover:scale-105 transition-transform duration-300 p-2',
            isOutOfStock && 'opacity-50'
          )}
          sizes="(max-width: 640px) 50vw, (max-width: 1024px) 33vw, 20vw"
        />
        {hasDiscount && (
          <span className="absolute top-2 left-2 bg-[#cc0c39] text-white text-xs font-bold px-1.5 py-0.5 rounded-sm">
            -{discountPct}%
          </span>
        )}
        {isOutOfStock && (
          <div className="absolute inset-0 flex items-center justify-center bg-white/60">
            <span className="text-sm font-semibold text-gray-500">Out of Stock</span>
          </div>
        )}
      </Link>

      {/* Content */}
      <div className="flex flex-col flex-1 px-3 pb-3">
        {/* Name */}
        <Link href={`/products/${product.id}`}>
          <h3 className="text-sm text-gray-800 line-clamp-2 hover:text-[#c45500] transition-colors leading-snug mb-1">
            {product.name}
          </h3>
        </Link>

        {/* Stars */}
        <StarRating />

        {/* Price */}
        <div className="mt-1.5">
          {hasDiscount && (
            <div className="flex items-baseline gap-1.5">
              <span className="text-xs text-gray-500">List:</span>
              <span className="text-xs text-gray-500 line-through">{formatPrice(product.compareAtPrice!)}</span>
            </div>
          )}
          <div className="flex items-baseline gap-1">
            <span className="text-xs text-gray-700 align-super text-[10px]">$</span>
            <span className="text-xl font-medium text-gray-900 leading-none">
              {Math.floor(product.price)}
            </span>
            <span className="text-xs text-gray-700 align-super text-[10px]">
              {String(Math.round((product.price % 1) * 100)).padStart(2, '0')}
            </span>
          </div>
          {hasDiscount && (
            <span className="text-xs text-[#cc0c39] font-medium">
              Save {discountPct}% ({formatPrice(product.compareAtPrice! - product.price)})
            </span>
          )}
        </div>

        {/* Prime badge */}
        <div className="mt-1 flex items-center gap-1">
          <span className="text-[11px] font-bold text-[#00a8e1]">prime</span>
          <span className="text-[11px] text-gray-500">FREE Delivery</span>
        </div>

        {/* Stock */}
        {!isOutOfStock && product.stock < 10 && (
          <p className="text-xs text-[#cc0c39] mt-1">Only {product.stock} left in stock</p>
        )}

        {/* Add to cart */}
        <button
          onClick={handleAddToCart}
          disabled={isOutOfStock}
          className={cn(
            'mt-2 w-full rounded-full py-1.5 text-sm font-medium border transition-colors',
            isOutOfStock
              ? 'cursor-not-allowed bg-gray-100 text-gray-400 border-gray-200'
              : 'bg-[#ffd814] border-[#fcd200] text-[#0f1111] hover:bg-[#f7ca00]'
          )}
        >
          {isOutOfStock ? 'Currently unavailable' : 'Add to cart'}
        </button>
      </div>
    </div>
  )
}
