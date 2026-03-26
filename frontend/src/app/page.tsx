import Link from 'next/link'
import { ArrowRight, Truck } from 'lucide-react'
import { NewsletterForm } from '@/components/newsletter-form'

const CATEGORIES = [
  { emoji: '📱', label: 'Electronics', slug: 'electronics' },
  { emoji: '👕', label: 'Clothing', slug: 'clothing' },
  { emoji: '🏃', label: 'Sports', slug: 'sports' },
  { emoji: '🏠', label: 'Home & Garden', slug: 'home-garden' },
  { emoji: '📚', label: 'Books', slug: 'books' },
]

export default function HomePage() {
  return (
    <main className="bg-gray-50">
      {/* Hero */}
      <section className="bg-gradient-to-br from-indigo-600 to-purple-700 text-white">
        <div className="mx-auto max-w-7xl px-6 py-24 text-center">
          <span className="inline-block rounded-full bg-white/20 px-4 py-1 text-sm font-medium mb-6">
            New arrivals every week
          </span>
          <h1 className="text-5xl font-extrabold tracking-tight sm:text-6xl">
            Discover Amazing Products
          </h1>
          <p className="mt-5 text-xl text-indigo-100 max-w-2xl mx-auto">
            Shop thousands of products across every category — fast shipping, easy returns, unbeatable prices.
          </p>
          <div className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              href="/products"
              className="inline-flex items-center gap-2 rounded-xl bg-white px-8 py-3.5 text-base font-semibold text-indigo-600 shadow-lg hover:bg-indigo-50 transition-colors"
            >
              Shop Now
              <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              href="/products"
              className="inline-flex items-center gap-2 rounded-xl border-2 border-white/50 px-8 py-3.5 text-base font-semibold text-white hover:bg-white/10 transition-colors"
            >
              Browse Categories
            </Link>
          </div>
        </div>
      </section>

      {/* Category cards */}
      <section className="mx-auto max-w-7xl px-6 py-14">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Shop by Category</h2>
        <div className="flex gap-4 overflow-x-auto pb-2 scrollbar-hide">
          {CATEGORIES.map((cat) => (
            <Link
              key={cat.slug}
              href={`/products?category=${cat.slug}`}
              className="flex-shrink-0 flex flex-col items-center gap-3 rounded-2xl border border-gray-200 bg-white px-8 py-6 shadow-sm hover:shadow-md hover:border-indigo-200 hover:-translate-y-0.5 transition-all"
            >
              <span className="text-4xl">{cat.emoji}</span>
              <span className="text-sm font-semibold text-gray-700 whitespace-nowrap">{cat.label}</span>
            </Link>
          ))}
        </div>
      </section>

      {/* Featured products skeleton */}
      <section className="mx-auto max-w-7xl px-6 pb-14">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold text-gray-900">Featured Products</h2>
          <Link href="/products" className="text-sm font-medium text-indigo-600 hover:text-indigo-700 flex items-center gap-1">
            View all <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="rounded-2xl border border-gray-200 bg-white overflow-hidden animate-pulse">
              <div className="aspect-[4/3] bg-gray-200" />
              <div className="p-4 space-y-3">
                <div className="h-3 bg-gray-200 rounded w-1/3" />
                <div className="h-4 bg-gray-200 rounded w-3/4" />
                <div className="h-4 bg-gray-200 rounded w-1/2" />
                <div className="h-5 bg-gray-200 rounded w-1/4" />
                <div className="h-9 bg-gray-200 rounded-lg" />
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Free shipping banner */}
      <section className="bg-amber-400">
        <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-center gap-3">
          <Truck className="h-5 w-5 text-amber-900" />
          <p className="text-sm font-semibold text-amber-900">
            Free shipping on all orders over $50 — no code needed!
          </p>
        </div>
      </section>

      {/* Newsletter */}
      <section className="bg-white border-t border-gray-100">
        <div className="mx-auto max-w-2xl px-6 py-16 text-center">
          <h2 className="text-2xl font-bold text-gray-900">Stay in the loop</h2>
          <p className="mt-2 text-gray-500">Get the latest deals and new arrivals straight to your inbox.</p>
          <NewsletterForm />
        </div>
      </section>
    </main>
  )
}
