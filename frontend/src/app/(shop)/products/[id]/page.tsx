'use client'

import { useState } from 'react'
import Image from 'next/image'
import { useParams } from 'next/navigation'
import useSWR from 'swr'
import { ShoppingCart } from 'lucide-react'
import { getProduct, getRecommendations } from '@/lib/api'
import { useCartStore } from '@/store/cart'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { ProductGrid } from '@/components/products/product-grid'
import { formatPrice } from '@/lib/utils'
import type { Product } from '@/lib/api'

export default function ProductDetailPage() {
  const { id } = useParams<{ id: string }>()
  const { data: product, isLoading } = useSWR<Product>(
    id ? ['product', id] : null,
    () => getProduct(id)
  )
  const { data: recommendations } = useSWR<Product[]>(
    id ? ['recommendations', id] : null,
    () => getRecommendations(id, 4)
  )

  const addItem = useCartStore((s) => s.addItem)
  const [selectedImage, setSelectedImage] = useState(0)

  if (isLoading) {
    return (
      <div className="mx-auto max-w-7xl px-6 py-10">
        <div className="grid grid-cols-1 gap-10 md:grid-cols-2 animate-pulse">
          <div className="aspect-square rounded-xl bg-gray-200" />
          <div className="space-y-4">
            <div className="h-8 bg-gray-200 rounded w-3/4" />
            <div className="h-6 bg-gray-200 rounded w-1/4" />
            <div className="h-24 bg-gray-200 rounded" />
          </div>
        </div>
      </div>
    )
  }

  if (!product) return <div className="p-10 text-center text-gray-500">Product not found.</div>

  const images = product.images?.length ? product.images : [product.imageUrl]

  return (
    <div className="mx-auto max-w-7xl px-6 py-10">
      <div className="grid grid-cols-1 gap-10 md:grid-cols-2">
        {/* Image gallery */}
        <div className="space-y-3">
          <div className="relative aspect-square rounded-xl overflow-hidden bg-gray-100">
            <Image
              src={images[selectedImage]}
              alt={product.name}
              fill
              className="object-cover"
              sizes="(max-width: 768px) 100vw, 50vw"
              priority
            />
          </div>
          {images.length > 1 && (
            <div className="flex gap-2 overflow-x-auto">
              {images.map((img, i) => (
                <button
                  key={i}
                  onClick={() => setSelectedImage(i)}
                  className={`relative h-16 w-16 shrink-0 rounded-lg overflow-hidden border-2 transition-colors ${
                    i === selectedImage ? 'border-primary' : 'border-transparent'
                  }`}
                >
                  <Image src={img} alt="" fill className="object-cover" sizes="64px" />
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Details */}
        <div className="space-y-5">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{product.name}</h1>
            <div className="mt-3 flex items-center gap-3">
              <span className="text-2xl font-semibold">{formatPrice(product.price)}</span>
              {product.compareAtPrice && product.compareAtPrice > product.price && (
                <span className="text-lg text-gray-400 line-through">
                  {formatPrice(product.compareAtPrice)}
                </span>
              )}
              {product.stock === 0 ? (
                <Badge variant="destructive">Out of Stock</Badge>
              ) : product.stock < 10 ? (
                <Badge variant="warning">Only {product.stock} left</Badge>
              ) : (
                <Badge variant="success">In Stock</Badge>
              )}
            </div>
          </div>

          <p className="text-gray-600 leading-relaxed">{product.description}</p>

          <Button
            size="lg"
            className="w-full sm:w-auto"
            disabled={product.stock === 0}
            onClick={() =>
              addItem({
                productId: product.id,
                sku: product.sku,
                name: product.name,
                unitPrice: product.price,
                quantity: 1,
                imageUrl: product.imageUrl,
              })
            }
          >
            <ShoppingCart className="mr-2 h-5 w-5" />
            Add to Cart
          </Button>
        </div>
      </div>

      {/* Recommendations */}
      {recommendations && recommendations.length > 0 && (
        <section className="mt-16">
          <h2 className="text-xl font-bold mb-6">You might also like</h2>
          <ProductGrid products={recommendations} />
        </section>
      )}
    </div>
  )
}
