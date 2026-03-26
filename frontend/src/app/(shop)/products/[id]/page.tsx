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
    <div className="bg-white min-h-screen">
      <div className="mx-auto max-w-[1500px] px-4 py-4 sm:px-6">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-1 text-xs text-[#007185] mb-4 flex-wrap">
          <Link href="/" className="hover:text-[#c45500] hover:underline">Home</Link>
          <span className="text-gray-400">›</span>
          <Link href="/products" className="hover:text-[#c45500] hover:underline">Products</Link>
          <span className="text-gray-400">›</span>
          <span className="text-gray-600 line-clamp-1">{product.name}</span>
        </nav>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-[auto_1fr_300px]">
          {/* Image gallery */}
          <div className="lg:w-80 space-y-2">
            <div className="relative aspect-square border border-gray-200 bg-white overflow-hidden">
              <Image
                src={images[selectedImage]}
                alt={product.name}
                fill
                className="object-contain p-4"
                sizes="(max-width: 1024px) 100vw, 320px"
                priority
              />
              {hasDiscount && (
                <span className="absolute top-2 left-2 bg-[#cc0c39] text-white text-xs font-bold px-1.5 py-0.5 rounded-sm">
                  -{discountPct}%
                </span>
              )}
            </div>
            {images.length > 1 && (
              <div className="flex gap-2 overflow-x-auto">
                {images.map((img, i) => (
                  <button
                    key={i}
                    onClick={() => setSelectedImage(i)}
                    className={cn(
                      'relative h-14 w-14 shrink-0 border-2 overflow-hidden transition-all',
                      i === selectedImage ? 'border-[#c45500]' : 'border-gray-200 hover:border-gray-400'
                    )}
                  >
                    <Image src={img} alt="" fill className="object-contain p-1" sizes="56px" />
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Product details */}
          <div className="space-y-3">
            <h1 className="text-xl font-medium text-[#0f1111] leading-snug">{product.name}</h1>

            {/* Brand */}
            <p className="text-sm">
              <span className="text-gray-500">Brand: </span>
              <span className="text-[#007185] hover:text-[#c45500] cursor-pointer">Brand Name</span>
            </p>

            {/* Stars */}
            <div className="flex items-center gap-2 border-b border-gray-200 pb-3">
              <div className="flex items-center">
                {Array.from({ length: 5 }).map((_, i) => (
                  <Star key={i} className={cn('h-4 w-4', i < 4 ? 'fill-[#ff9900] text-[#ff9900]' : 'fill-gray-200 text-gray-200')} />
                ))}
              </div>
              <span className="text-sm text-[#007185] hover:text-[#c45500] cursor-pointer">1,284 ratings</span>
              <span className="text-gray-300">|</span>
              <span className="text-sm text-[#007185] hover:text-[#c45500] cursor-pointer">Search this page</span>
            </div>

            {/* Price */}
            <div className="border-b border-gray-200 pb-3">
              {hasDiscount && (
                <div className="flex items-baseline gap-2 mb-1">
                  <span className="text-sm text-gray-500">List Price:</span>
                  <span className="text-sm text-gray-500 line-through">{formatPrice(product.compareAtPrice!)}</span>
                  <span className="text-sm text-[#cc0c39]">-{discountPct}%</span>
                </div>
              )}
              <div className="flex items-baseline gap-1">
                <span className="text-sm text-[#cc0c39] align-super">$</span>
                <span className="text-3xl font-medium text-[#cc0c39]">{Math.floor(product.price)}</span>
                <span className="text-sm text-[#cc0c39] align-super">
                  {String(Math.round((product.price % 1) * 100)).padStart(2, '0')}
                </span>
              </div>
              <p className="text-xs text-gray-500 mt-1">
                FREE Returns &nbsp;|&nbsp;{' '}
                <span className="text-[#007185]">FREE delivery</span> on orders over $25
              </p>
            </div>

            {/* Description */}
            <div>
              <h3 className="text-sm font-bold text-[#0f1111] mb-2">About this item</h3>
              <p className="text-sm text-[#0f1111] leading-relaxed">{product.description}</p>
            </div>

            {/* Attributes */}
            <div className="border border-gray-200">
              <table className="w-full text-sm">
                <tbody>
                  <tr className="border-b border-gray-100 bg-[#f3f3f3]">
                    <td className="px-3 py-2 font-medium text-[#0f1111] w-1/3">SKU</td>
                    <td className="px-3 py-2 text-[#0f1111]">{product.sku}</td>
                  </tr>
                  <tr className="border-b border-gray-100">
                    <td className="px-3 py-2 font-medium text-[#0f1111] bg-[#f3f3f3]">Category</td>
                    <td className="px-3 py-2 text-[#0f1111]">{product.categoryId}</td>
                  </tr>
                  <tr className="bg-[#f3f3f3]">
                    <td className="px-3 py-2 font-medium text-[#0f1111]">Availability</td>
                    <td className="px-3 py-2 text-[#0f1111]">{product.stock > 0 ? `${product.stock} in stock` : 'Out of stock'}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          {/* Buy box (right column) */}
          <div className="border border-gray-200 rounded p-4 h-fit space-y-3 bg-white">
            {/* Price */}
            <div className="flex items-baseline gap-1">
              <span className="text-sm text-[#cc0c39] align-super">$</span>
              <span className="text-2xl font-medium text-[#cc0c39]">{Math.floor(product.price)}</span>
              <span className="text-sm text-[#cc0c39] align-super">
                {String(Math.round((product.price % 1) * 100)).padStart(2, '0')}
              </span>
            </div>

            {/* Delivery */}
            <div className="text-sm">
              <p className="text-[#007185] font-medium">FREE delivery</p>
              <p className="text-[#0f1111]">
                <span className="font-bold">Tomorrow</span> if you order within{' '}
                <span className="text-[#cc0c39] font-bold">12 hrs 30 mins</span>
              </p>
            </div>

            {/* Stock */}
            <p className={cn('text-sm font-medium', isOutOfStock ? 'text-[#cc0c39]' : 'text-[#007600]')}>
              {isOutOfStock ? 'Currently unavailable' : 'In Stock'}
            </p>

            {/* Quantity */}
            {!isOutOfStock && (
              <div className="flex items-center gap-2">
                <label className="text-sm text-[#0f1111]">Qty:</label>
                <select
                  value={quantity}
                  onChange={(e) => setQuantity(Number(e.target.value))}
                  className="border border-gray-300 rounded bg-[#f0f2f2] px-2 py-1 text-sm text-[#0f1111] focus:outline-none focus:border-[#e77600] focus:ring-2 focus:ring-[#e77600]/30"
                >
                  {Array.from({ length: Math.min(product.stock, 10) }, (_, i) => i + 1).map((n) => (
                    <option key={n} value={n}>{n}</option>
                  ))}
                </select>
              </div>
            )}

            {/* Add to cart */}
            <button
              onClick={handleAddToCart}
              disabled={isOutOfStock}
              className={cn(
                'w-full rounded-full py-2 text-sm font-medium border transition-colors',
                isOutOfStock
                  ? 'cursor-not-allowed bg-gray-100 text-gray-400 border-gray-200'
                  : 'bg-[#ffd814] border-[#fcd200] text-[#0f1111] hover:bg-[#f7ca00]'
              )}
            >
              Add to Cart
            </button>

            {/* Buy now */}
            <button
              disabled={isOutOfStock}
              className={cn(
                'w-full rounded-full py-2 text-sm font-medium border transition-colors',
                isOutOfStock
                  ? 'cursor-not-allowed bg-gray-100 text-gray-400 border-gray-200'
                  : 'bg-[#ffa41c] border-[#ff8f00] text-[#0f1111] hover:bg-[#fa8900]'
              )}
            >
              Buy Now
            </button>

            {/* Secure transaction */}
            <p className="text-xs text-gray-500 text-center">
              🔒 Secure transaction
            </p>

            <div className="border-t border-gray-200 pt-3 space-y-1 text-xs text-[#0f1111]">
              <div className="flex justify-between">
                <span className="text-gray-500">Ships from</span>
                <span>Nexmart</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Sold by</span>
                <span className="text-[#007185]">Nexmart</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Returns</span>
                <span className="text-[#007185]">Eligible for Return</span>
              </div>
            </div>
          </div>
        </div>

        {/* Recommendations */}
        {recommendations && recommendations.length > 0 && (
          <section className="mt-8 bg-white p-4">
            <h2 className="text-lg font-bold text-[#0f1111] mb-4">Customers who viewed this also viewed</h2>
            <ProductGrid products={recommendations} />
          </section>
        )}
      </div>
    </div>
  )
}
