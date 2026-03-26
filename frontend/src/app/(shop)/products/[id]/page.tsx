'use client'

import { useState } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { useParams } from 'next/navigation'
import useSWR from 'swr'
import { ShoppingCart, Star, Minus, Plus, Zap } from 'lucide-react'
import { getProduct, getRecommendations } from '@/lib/api'
import { useCartStore } from '@/store/cart'
import { ProductGrid } from '@/components/products/product-grid'
import { formatPrice, cn } from '@/lib/utils'
import type { Product } from '@/lib/api'

export default function ProductDetailPage() {
  const { id } = useParams<{ id: string }>()
  const { data: product, isLoading } = useSWR<Product>(
    id ? ['product', id] : null,
    () => getProduct(id)
  )
  const { data: recommendations } = useSWR<Product[]>(
    id ? ['recommendations', id] : null,
    () => getRecommendations(id, 6)
  )

  const addItem = useCartStore((s) => s.addItem)
  const [selectedImage, setSelectedImage] = useState(0)
  const [quantity, setQuantity] = useState(1)

  if (isLoading) {
    return (
      <div className="mx-auto max-w-7xl px-6 py-10 animate-pulse">
        <div className="h-4 bg-gray-200 rounded w-48 mb-8" />
        <div className="grid grid-cols-1 gap-10 md:grid-cols-2">
          <div className="space-y-3">
            <div className="aspect-square rounded-2xl bg-gray-200" />
            <div className="flex gap-2">
              {Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="h-16 w-16 rounded-lg bg-gray-200" />
              ))}
            </div>
          </div>
          <div className="space-y-4">
            <div className="h-4 bg-gray-200 rounded w-1/4" />
            <div className="h-8 bg-gray-200 rounded w-3/4" />
            <div className="h-6 bg-gray-200 rounded w-1/3" />
            <div className="h-24 bg-gray-200 rounded" />
            <div className="h-12 bg-gray-200 rounded-xl" />
          </div>
        </div>
      </div>
    )
  }

  if (!product) {
    return (
      <div className="flex flex-col items-center justify-center py-24 text-center">
        <p className="text-lg font-semibold text-gray-700">Product not found.</p>
        <Link href="/products" className="mt-4 text-sm text-indigo-600 hover:underline">
          Back to products
        </Link>
      </div>
    )
  }

  const images = product.images?.length ? product.images : [product.imageUrl ?? '/placeholder-product.jpg']
  const isOutOfStock = product.stock === 0
  const hasDiscount = product.compareAtPrice != null && product.compareAtPrice > product.price
  const discountPct = hasDiscount
    ? Math.round(((product.compareAtPrice! - product.price) / product.compareAtPrice!) * 100)
    : 0

  const handleAddToCart = () => {
    addItem({
      productId: product.id,
      sku: product.sku,
      name: product.name,
      unitPrice: product.price,
      quantity,
      imageUrl: product.imageUrl,
    })
  }

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-2 text-sm text-gray-500 mb-8">
          <Link href="/" className="hover:text-indigo-600 transition-colors">Home</Link>
          <span>/</span>
          <Link href="/products" className="hover:text-indigo-600 transition-colors">Products</Link>
          <span>/</span>
          <span className="text-gray-900 font-medium line-clamp-1">{product.name}</span>
        </nav>

        <div className="grid grid-cols-1 gap-10 lg:grid-cols-2">
          {/* Image gallery */}
          <div className="space-y-3">
            <div className="relative aspect-square rounded-2xl overflow-hidden bg-white border border-gray-200 shadow-sm">
              <Image
                src={images[selectedImage]}
                alt={product.name}
                fill
                className="object-cover"
                sizes="(max-width: 1024px) 100vw, 50vw"
                priority
              />
              {hasDiscount && (
                <span className="absolute top-3 left-3 rounded-lg bg-red-500 px-2.5 py-1 text-sm font-bold text-white">
                  {discountPct}% OFF
                </span>
              )}
            </div>
            {images.length > 1 && (
              <div className="flex gap-2 overflow-x-auto pb-1">
                {images.map((img, i) => (
                  <button
                    key={i}
                    onClick={() => setSelectedImage(i)}
                    className={cn(
                      'relative h-16 w-16 shrink-0 rounded-xl overflow-hidden border-2 transition-all',
                      i === selectedImage
                        ? 'border-indigo-600 shadow-md'
                        : 'border-gray-200 hover:border-gray-400'
                    )}
                  >
                    <Image src={img} alt="" fill className="object-cover" sizes="64px" />
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Product details */}
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-gray-400 uppercase tracking-wide mb-1">Brand</p>
              <h1 className="text-3xl font-extrabold text-gray-900 leading-tight">{product.name}</h1>
            </div>

            {/* Stars */}
            <div className="flex items-center gap-1">
              {Array.from({ length: 5 }).map((_, i) => (
                <Star key={i} className="h-4 w-4 fill-gray-200 text-gray-200" />
              ))}
              <span className="ml-2 text-sm text-gray-400">No reviews yet</span>
            </div>

            {/* Price */}
            <div className="flex items-baseline gap-3">
              <span className="text-3xl font-bold text-gray-900">{formatPrice(product.price)}</span>
              {hasDiscount && (
                <span className="text-xl text-gray-400 line-through">{formatPrice(product.compareAtPrice!)}</span>
              )}
              {hasDiscount && (
                <span className="rounded-lg bg-red-100 px-2 py-0.5 text-sm font-semibold text-red-600">
                  Save {discountPct}%
                </span>
              )}
            </div>

            {/* Stock indicator */}
            <div className="flex items-center gap-2">
              <span
                className={cn(
                  'h-2.5 w-2.5 rounded-full',
                  isOutOfStock ? 'bg-red-500' : 'bg-green-500'
                )}
              />
              <span className={cn('text-sm font-medium', isOutOfStock ? 'text-red-600' : 'text-green-600')}>
                {isOutOfStock ? 'Out of Stock' : `In Stock${product.stock < 10 ? ` — only ${product.stock} left` : ''}`}
              </span>
            </div>

            {/* Quantity selector */}
            {!isOutOfStock && (
              <div className="flex items-center gap-3">
                <span className="text-sm font-medium text-gray-700">Quantity</span>
                <div className="flex items-center rounded-xl border border-gray-300 bg-white overflow-hidden">
                  <button
                    onClick={() => setQuantity((q) => Math.max(1, q - 1))}
                    className="px-3 py-2 text-gray-600 hover:bg-gray-100 transition-colors"
                  >
                    <Minus className="h-4 w-4" />
                  </button>
                  <span className="w-10 text-center text-sm font-semibold">{quantity}</span>
                  <button
                    onClick={() => setQuantity((q) => Math.min(product.stock, q + 1))}
                    className="px-3 py-2 text-gray-600 hover:bg-gray-100 transition-colors"
                  >
                    <Plus className="h-4 w-4" />
                  </button>
                </div>
              </div>
            )}

            {/* CTA buttons */}
            <div className="flex flex-col sm:flex-row gap-3 pt-1">
              <button
                onClick={handleAddToCart}
                disabled={isOutOfStock}
                className={cn(
                  'flex flex-1 items-center justify-center gap-2 rounded-xl py-3.5 text-base font-semibold transition-colors',
                  isOutOfStock
                    ? 'cursor-not-allowed bg-gray-100 text-gray-400'
                    : 'bg-indigo-600 text-white hover:bg-indigo-700'
                )}
              >
                <ShoppingCart className="h-5 w-5" />
                Add to Cart
              </button>
              <button
                disabled={isOutOfStock}
                className={cn(
                  'flex flex-1 items-center justify-center gap-2 rounded-xl border-2 py-3.5 text-base font-semibold transition-colors',
                  isOutOfStock
                    ? 'cursor-not-allowed border-gray-200 text-gray-400'
                    : 'border-indigo-600 text-indigo-600 hover:bg-indigo-50'
                )}
              >
                <Zap className="h-5 w-5" />
                Buy Now
              </button>
            </div>

            {/* Description */}
            <div className="border-t border-gray-200 pt-5">
              <h3 className="text-sm font-semibold text-gray-900 mb-2">Description</h3>
              <p className="text-sm text-gray-600 leading-relaxed">{product.description}</p>
            </div>

            {/* Attributes table */}
            <div className="rounded-xl border border-gray-200 bg-white overflow-hidden">
              <table className="w-full text-sm">
                <tbody>
                  <tr className="border-b border-gray-100">
                    <td className="px-4 py-2.5 font-medium text-gray-500 bg-gray-50 w-1/3">SKU</td>
                    <td className="px-4 py-2.5 text-gray-700">{product.sku}</td>
                  </tr>
                  <tr className="border-b border-gray-100">
                    <td className="px-4 py-2.5 font-medium text-gray-500 bg-gray-50">Category</td>
                    <td className="px-4 py-2.5 text-gray-700">{product.categoryId}</td>
                  </tr>
                  <tr>
                    <td className="px-4 py-2.5 font-medium text-gray-500 bg-gray-50">Availability</td>
                    <td className="px-4 py-2.5 text-gray-700">{product.stock > 0 ? `${product.stock} units` : 'Out of stock'}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* Recommendations */}
        {recommendations && recommendations.length > 0 && (
          <section className="mt-16">
            <h2 className="text-2xl font-bold text-gray-900 mb-6">You might also like</h2>
            <ProductGrid products={recommendations} />
          </section>
        )}
      </div>
    </div>
  )
}
