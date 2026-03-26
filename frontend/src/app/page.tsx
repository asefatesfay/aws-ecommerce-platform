import Link from 'next/link'
import { ChevronRight } from 'lucide-react'
import { NewsletterForm } from '@/components/newsletter-form'

const CATEGORIES = [
  { emoji: '📱', label: 'Electronics', slug: 'electronics', bg: 'bg-blue-50' },
  { emoji: '👕', label: 'Clothing', slug: 'clothing', bg: 'bg-pink-50' },
  { emoji: '🏃', label: 'Sports & Outdoors', slug: 'sports', bg: 'bg-green-50' },
  { emoji: '🏠', label: 'Home & Garden', slug: 'home-garden', bg: 'bg-yellow-50' },
  { emoji: '📚', label: 'Books', slug: 'books', bg: 'bg-orange-50' },
  { emoji: '🎮', label: 'Gaming', slug: 'electronics', bg: 'bg-purple-50' },
  { emoji: '💄', label: 'Beauty', slug: 'clothing', bg: 'bg-red-50' },
  { emoji: '🐾', label: 'Pet Supplies', slug: '', bg: 'bg-teal-50' },
]

const DEALS = [
  { label: 'Up to 50% off Electronics', sub: 'Limited time deal', color: 'bg-[#cc0c39]' },
  { label: 'New Arrivals in Clothing', sub: 'Shop the latest styles', color: 'bg-[#007185]' },
  { label: 'Sports & Outdoors Sale', sub: 'Save on top brands', color: 'bg-[#007600]' },
  { label: 'Home Essentials', sub: 'Refresh your space', color: 'bg-[#c45500]' },
]

export default function HomePage() {
  return (
    <div className="bg-[#eaeded] min-h-screen">
      {/* Hero banner */}
      <div className="relative bg-gradient-to-b from-[#c9e4f0] to-[#eaeded] overflow-hidden">
        <div className="mx-auto max-w-[1500px] px-4 py-8">
          <div className="text-center py-8">
            <p className="text-sm text-gray-600 mb-2">Shop smarter with AI-powered search</p>
            <h1 className="text-3xl font-bold text-[#0f1111] mb-4">
              Welcome to Nexmart
            </h1>
            <p className="text-gray-600 mb-6 max-w-xl mx-auto">
              Millions of products. Fast delivery. Powered by AI.
            </p>
            <Link
              href="/products"
              className="inline-block bg-[#ffd814] hover:bg-[#f7ca00] text-[#0f1111] font-medium px-8 py-2.5 rounded-full border border-[#fcd200] transition-colors text-sm"
            >
              Shop Now
            </Link>
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-[1500px] px-4 py-4 space-y-4">

        {/* Deal cards row */}
        <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
          {DEALS.map((deal) => (
            <Link
              key={deal.label}
              href="/products"
              className="bg-white p-4 hover:shadow-md transition-shadow group"
            >
              <div className={`${deal.color} text-white text-xs font-bold px-2 py-0.5 rounded-sm inline-block mb-2`}>
                Deal
              </div>
              <div className="aspect-square bg-gray-100 mb-3 flex items-center justify-center">
                <div className="w-16 h-16 bg-gray-200 rounded animate-pulse" />
              </div>
              <p className="text-sm font-medium text-[#0f1111] line-clamp-2 group-hover:text-[#c45500] transition-colors">
                {deal.label}
              </p>
              <p className="text-xs text-[#cc0c39] mt-0.5">{deal.sub}</p>
              <p className="text-xs text-[#007185] mt-2 group-hover:text-[#c45500] transition-colors">
                See all deals <ChevronRight className="inline h-3 w-3" />
              </p>
            </Link>
          ))}
        </div>

        {/* Shop by category */}
        <div className="bg-white p-4">
          <h2 className="text-lg font-bold text-[#0f1111] mb-4">Shop by Category</h2>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4 lg:grid-cols-8">
            {CATEGORIES.map((cat) => (
              <Link
                key={cat.slug + cat.label}
                href={cat.slug ? `/products?category=${cat.slug}` : '/products'}
                className="flex flex-col items-center gap-2 group"
              >
                <div className={`${cat.bg} w-full aspect-square rounded flex items-center justify-center text-3xl group-hover:opacity-80 transition-opacity`}>
                  {cat.emoji}
                </div>
                <span className="text-xs text-center text-[#0f1111] font-medium group-hover:text-[#c45500] transition-colors leading-tight">
                  {cat.label}
                </span>
              </Link>
            ))}
          </div>
        </div>

        {/* Featured products */}
        <div className="bg-white p-4">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-bold text-[#0f1111]">Featured Products</h2>
            <Link href="/products" className="text-sm text-[#007185] hover:text-[#c45500] hover:underline transition-colors">
              See all deals
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
            {Array.from({ length: 6 }).map((_, i) => (
              <div key={i} className="animate-pulse">
                <div className="aspect-square bg-gray-200 mb-2" />
                <div className="h-3 bg-gray-200 rounded mb-1" />
                <div className="h-3 bg-gray-200 rounded w-2/3 mb-1" />
                <div className="h-4 bg-gray-200 rounded w-1/2" />
              </div>
            ))}
          </div>
        </div>

        {/* Sign in prompt (Amazon-style) */}
        <div className="bg-white p-6 text-center">
          <h2 className="text-lg font-bold text-[#0f1111] mb-2">Sign in for the best experience</h2>
          <p className="text-sm text-gray-600 mb-4">Get personalized recommendations, track orders, and more.</p>
          <Link
            href="/login"
            className="inline-block bg-[#ffd814] hover:bg-[#f7ca00] text-[#0f1111] font-medium px-8 py-2 rounded-full border border-[#fcd200] transition-colors text-sm"
          >
            Sign in
          </Link>
          <p className="text-xs text-gray-500 mt-3">
            New customer?{' '}
            <Link href="/register" className="text-[#007185] hover:text-[#c45500] hover:underline">
              Start here
            </Link>
          </p>
        </div>

        {/* Newsletter */}
        <div className="bg-white p-6 text-center">
          <h2 className="text-base font-bold text-[#0f1111] mb-1">Stay up to date</h2>
          <p className="text-sm text-gray-500 mb-4">Get deals, new arrivals, and more in your inbox.</p>
          <NewsletterForm />
        </div>

      </div>
    </div>
  )
}
