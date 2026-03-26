import Link from 'next/link'
import Image from 'next/image'
import { ChevronRight, Star, Truck, RotateCcw, Shield, Headphones, Zap, TrendingUp, Gift } from 'lucide-react'
import { NewsletterForm } from '@/components/newsletter-form'

// ── Mock data ──────────────────────────────────────────────────────────────

const HERO_SLIDES = [
  {
    id: 1,
    title: 'Next-Gen Electronics',
    subtitle: 'Up to 40% off on the latest gadgets',
    cta: 'Shop Electronics',
    href: '/products?category=electronics',
    bg: 'from-[#131921] to-[#232f3e]',
    accent: '#ff9900',
    image: 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=800&q=80',
    badge: "Today's Deal",
  },
  {
    id: 2,
    title: 'Summer Fashion',
    subtitle: 'New arrivals — fresh styles for every occasion',
    cta: 'Shop Clothing',
    href: '/products?category=clothing',
    bg: 'from-[#1a1a2e] to-[#16213e]',
    accent: '#febd69',
    image: 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&q=80',
    badge: 'New Arrivals',
  },
]

const FEATURED_PRODUCTS = [
  {
    id: '1',
    name: 'Sony WH-1000XM5 Wireless Headphones',
    price: 279.99,
    originalPrice: 399.99,
    rating: 4.8,
    reviews: 12847,
    image: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&q=80',
    badge: "Best Seller",
    prime: true,
  },
  {
    id: '2',
    name: 'Apple Watch Series 9 GPS 45mm',
    price: 399.00,
    originalPrice: 429.00,
    rating: 4.7,
    reviews: 8234,
    image: 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400&q=80',
    badge: '#1 Best Seller',
    prime: true,
  },
  {
    id: '3',
    name: 'Nike Air Max 270 Running Shoes',
    price: 89.99,
    originalPrice: 150.00,
    rating: 4.6,
    reviews: 5621,
    image: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&q=80',
    badge: 'Limited Deal',
    prime: true,
  },
  {
    id: '4',
    name: 'Kindle Paperwhite 16GB Waterproof',
    price: 139.99,
    originalPrice: 159.99,
    rating: 4.9,
    reviews: 23451,
    image: 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&q=80',
    badge: "Amazon's Choice",
    prime: true,
  },
  {
    id: '5',
    name: 'Instant Pot Duo 7-in-1 Electric Pressure Cooker',
    price: 59.99,
    originalPrice: 99.99,
    rating: 4.7,
    reviews: 45123,
    image: 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=400&q=80',
    badge: 'Deal of the Day',
    prime: true,
  },
  {
    id: '6',
    name: 'Levi\'s 501 Original Fit Jeans',
    price: 49.99,
    originalPrice: 69.50,
    rating: 4.5,
    reviews: 9876,
    image: 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&q=80',
    badge: null,
    prime: true,
  },
  {
    id: '7',
    name: 'Dyson V15 Detect Cordless Vacuum',
    price: 549.99,
    originalPrice: 699.99,
    rating: 4.8,
    reviews: 3421,
    image: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80',
    badge: 'Top Pick',
    prime: true,
  },
  {
    id: '8',
    name: 'The Psychology of Money — Hardcover',
    price: 18.99,
    originalPrice: 28.00,
    rating: 4.9,
    reviews: 67234,
    image: 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=400&q=80',
    badge: null,
    prime: true,
  },
]

const CATEGORIES = [
  {
    label: 'Electronics',
    slug: 'electronics',
    image: 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=300&q=80',
    count: '50,000+ items',
  },
  {
    label: 'Clothing',
    slug: 'clothing',
    image: 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=300&q=80',
    count: '120,000+ items',
  },
  {
    label: 'Sports & Outdoors',
    slug: 'sports',
    image: 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=300&q=80',
    count: '35,000+ items',
  },
  {
    label: 'Home & Garden',
    slug: 'home-garden',
    image: 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=300&q=80',
    count: '80,000+ items',
  },
  {
    label: 'Books',
    slug: 'books',
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=300&q=80',
    count: '200,000+ items',
  },
  {
    label: 'Beauty',
    slug: 'clothing',
    image: 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=300&q=80',
    count: '45,000+ items',
  },
]

const DEALS_OF_DAY = [
  {
    id: 'd1',
    name: 'JBL Charge 5 Portable Speaker',
    price: 99.95,
    originalPrice: 179.95,
    discount: 44,
    image: 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300&q=80',
    timeLeft: '8h 23m',
    claimed: 67,
  },
  {
    id: 'd2',
    name: 'Yoga Mat Premium Non-Slip',
    price: 24.99,
    originalPrice: 49.99,
    discount: 50,
    image: 'https://images.unsplash.com/photo-1601925228008-f5e4c5e5e5e5?w=300&q=80',
    timeLeft: '12h 45m',
    claimed: 43,
  },
  {
    id: 'd3',
    name: 'Nespresso Vertuo Coffee Machine',
    price: 119.00,
    originalPrice: 199.00,
    discount: 40,
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=300&q=80',
    timeLeft: '5h 10m',
    claimed: 82,
  },
  {
    id: 'd4',
    name: 'Anker 65W USB-C Charger',
    price: 25.99,
    originalPrice: 45.99,
    discount: 43,
    image: 'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=300&q=80',
    timeLeft: '3h 55m',
    claimed: 91,
  },
]

const TRUST_BADGES = [
  { icon: Truck, title: 'Free Delivery', desc: 'On orders over $25' },
  { icon: RotateCcw, title: 'Easy Returns', desc: '30-day return policy' },
  { icon: Shield, title: 'Secure Payment', desc: '100% protected' },
  { icon: Headphones, title: '24/7 Support', desc: 'Always here to help' },
]

// ── Helpers ────────────────────────────────────────────────────────────────

function StarRating({ rating, count }: { rating: number; count: number }) {
  return (
    <div className="flex items-center gap-1">
      <div className="flex">
        {Array.from({ length: 5 }).map((_, i) => (
          <Star
            key={i}
            className={`h-3 w-3 ${i < Math.floor(rating) ? 'fill-[#ff9900] text-[#ff9900]' : 'fill-gray-200 text-gray-200'}`}
          />
        ))}
      </div>
      <span className="text-xs text-[#007185]">{count.toLocaleString()}</span>
    </div>
  )
}

function PriceDisplay({ price, original }: { price: number; original?: number }) {
  const discount = original ? Math.round(((original - price) / original) * 100) : 0
  return (
    <div>
      {original && (
        <div className="flex items-center gap-1 text-xs text-gray-500">
          <span>List: <span className="line-through">${original.toFixed(2)}</span></span>
          {discount > 0 && <span className="text-[#cc0c39] font-medium">-{discount}%</span>}
        </div>
      )}
      <div className="flex items-baseline gap-0.5">
        <span className="text-xs text-[#cc0c39] align-super leading-none">$</span>
        <span className="text-xl font-medium text-[#cc0c39] leading-none">{Math.floor(price)}</span>
        <span className="text-xs text-[#cc0c39] align-super leading-none">
          {String(Math.round((price % 1) * 100)).padStart(2, '0')}
        </span>
      </div>
    </div>
  )
}

// ── Page ───────────────────────────────────────────────────────────────────

export default function HomePage() {
  return (
    <div className="bg-[#eaeded]">

      {/* ── Hero Banner ──────────────────────────────────────────────────── */}
      <div className={`relative bg-gradient-to-r ${HERO_SLIDES[0].bg} overflow-hidden`}>
        <div className="mx-auto max-w-[1500px] px-4">
          <div className="grid grid-cols-1 md:grid-cols-2 items-center min-h-[400px] gap-8 py-12">
            <div className="text-white z-10">
              <span
                className="inline-block text-xs font-bold px-2 py-1 rounded-sm mb-4"
                style={{ backgroundColor: HERO_SLIDES[0].accent, color: '#131921' }}
              >
                {HERO_SLIDES[0].badge}
              </span>
              <h1 className="text-4xl md:text-5xl font-extrabold leading-tight mb-3">
                {HERO_SLIDES[0].title}
              </h1>
              <p className="text-lg text-gray-300 mb-6">{HERO_SLIDES[0].subtitle}</p>
              <Link
                href={HERO_SLIDES[0].href}
                className="inline-flex items-center gap-2 bg-[#ffd814] hover:bg-[#f7ca00] text-[#131921] font-bold px-8 py-3 rounded-full transition-colors text-sm"
              >
                {HERO_SLIDES[0].cta}
                <ChevronRight className="h-4 w-4" />
              </Link>
            </div>
            <div className="relative h-64 md:h-80">
              <Image
                src={HERO_SLIDES[0].image}
                alt="Electronics"
                fill
                className="object-cover rounded-xl opacity-80"
                sizes="(max-width: 768px) 100vw, 50vw"
                priority
              />
            </div>
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-[1500px] px-4 py-4 space-y-4">

        {/* ── Trust badges ─────────────────────────────────────────────── */}
        <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
          {TRUST_BADGES.map(({ icon: Icon, title, desc }) => (
            <div key={title} className="bg-white flex items-center gap-3 p-4">
              <div className="shrink-0 w-10 h-10 rounded-full bg-[#fff3cd] flex items-center justify-center">
                <Icon className="h-5 w-5 text-[#ff9900]" />
              </div>
              <div>
                <p className="text-sm font-bold text-[#0f1111]">{title}</p>
                <p className="text-xs text-gray-500">{desc}</p>
              </div>
            </div>
          ))}
        </div>

        {/* ── Deals of the Day ─────────────────────────────────────────── */}
        <div className="bg-white p-4">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <Zap className="h-5 w-5 text-[#cc0c39]" />
              <h2 className="text-xl font-bold text-[#0f1111]">Deals of the Day</h2>
              <span className="text-sm text-[#cc0c39] font-medium">Ends in 08:23:45</span>
            </div>
            <Link href="/products" className="text-sm text-[#007185] hover:text-[#c45500] hover:underline flex items-center gap-1">
              See all deals <ChevronRight className="h-3.5 w-3.5" />
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
            {DEALS_OF_DAY.map((deal) => (
              <Link key={deal.id} href="/products" className="group border border-gray-200 hover:shadow-md transition-shadow overflow-hidden">
                <div className="relative aspect-square bg-gray-50 overflow-hidden">
                  <Image
                    src={deal.image}
                    alt={deal.name}
                    fill
                    className="object-cover group-hover:scale-105 transition-transform duration-300"
                    sizes="(max-width: 640px) 50vw, 25vw"
                  />
                  <span className="absolute top-2 left-2 bg-[#cc0c39] text-white text-xs font-bold px-1.5 py-0.5 rounded-sm">
                    -{deal.discount}%
                  </span>
                </div>
                <div className="p-3">
                  <p className="text-xs text-[#0f1111] line-clamp-2 mb-2 group-hover:text-[#c45500] transition-colors">
                    {deal.name}
                  </p>
                  <PriceDisplay price={deal.price} original={deal.originalPrice} />
                  {/* Progress bar */}
                  <div className="mt-2">
                    <div className="flex justify-between text-xs text-gray-500 mb-1">
                      <span className="text-[#cc0c39] font-medium">{deal.claimed}% claimed</span>
                      <span>{deal.timeLeft} left</span>
                    </div>
                    <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-[#cc0c39] rounded-full"
                        style={{ width: `${deal.claimed}%` }}
                      />
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* ── Shop by Category ─────────────────────────────────────────── */}
        <div className="bg-white p-4">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-bold text-[#0f1111]">Shop by Category</h2>
            <Link href="/products" className="text-sm text-[#007185] hover:text-[#c45500] hover:underline flex items-center gap-1">
              All categories <ChevronRight className="h-3.5 w-3.5" />
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
            {CATEGORIES.map((cat) => (
              <Link
                key={cat.slug + cat.label}
                href={`/products?category=${cat.slug}`}
                className="group overflow-hidden border border-gray-200 hover:shadow-md transition-shadow"
              >
                <div className="relative aspect-[4/3] overflow-hidden">
                  <Image
                    src={cat.image}
                    alt={cat.label}
                    fill
                    className="object-cover group-hover:scale-105 transition-transform duration-300"
                    sizes="(max-width: 640px) 50vw, (max-width: 1024px) 33vw, 16vw"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
                  <div className="absolute bottom-0 left-0 right-0 p-2">
                    <p className="text-white text-xs font-bold">{cat.label}</p>
                    <p className="text-gray-300 text-[10px]">{cat.count}</p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* ── Featured Products ─────────────────────────────────────────── */}
        <div className="bg-white p-4">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <TrendingUp className="h-5 w-5 text-[#ff9900]" />
              <h2 className="text-xl font-bold text-[#0f1111]">Best Sellers</h2>
            </div>
            <Link href="/products" className="text-sm text-[#007185] hover:text-[#c45500] hover:underline flex items-center gap-1">
              See all <ChevronRight className="h-3.5 w-3.5" />
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-8">
            {FEATURED_PRODUCTS.map((product) => (
              <Link key={product.id} href="/products" className="group border border-gray-200 hover:shadow-md transition-shadow overflow-hidden flex flex-col">
                <div className="relative aspect-square bg-white overflow-hidden p-3">
                  <Image
                    src={product.image}
                    alt={product.name}
                    fill
                    className="object-contain p-2 group-hover:scale-105 transition-transform duration-300"
                    sizes="(max-width: 640px) 50vw, (max-width: 1024px) 33vw, 12vw"
                  />
                  {product.badge && (
                    <span className="absolute top-1 left-1 bg-[#cc0c39] text-white text-[10px] font-bold px-1 py-0.5 rounded-sm">
                      {product.badge}
                    </span>
                  )}
                </div>
                <div className="p-2 flex flex-col flex-1">
                  <p className="text-xs text-[#0f1111] line-clamp-2 mb-1 group-hover:text-[#c45500] transition-colors leading-snug">
                    {product.name}
                  </p>
                  <StarRating rating={product.rating} count={product.reviews} />
                  <div className="mt-1">
                    <PriceDisplay price={product.price} original={product.originalPrice} />
                  </div>
                  {product.prime && (
                    <p className="text-[10px] text-[#00a8e1] font-bold mt-0.5">prime</p>
                  )}
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* ── Second hero banner ───────────────────────────────────────── */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="relative bg-gradient-to-r from-[#1a1a2e] to-[#16213e] overflow-hidden min-h-[200px] flex items-center">
            <div className="absolute inset-0">
              <Image
                src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80"
                alt="Fashion"
                fill
                className="object-cover opacity-30"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
            </div>
            <div className="relative z-10 p-6 text-white">
              <p className="text-xs font-bold text-[#febd69] mb-1">NEW SEASON</p>
              <h3 className="text-2xl font-extrabold mb-2">Summer Fashion</h3>
              <p className="text-sm text-gray-300 mb-4">Fresh styles, unbeatable prices</p>
              <Link
                href="/products?category=clothing"
                className="inline-flex items-center gap-1 bg-white text-[#131921] text-sm font-bold px-5 py-2 rounded-full hover:bg-gray-100 transition-colors"
              >
                Shop Now <ChevronRight className="h-3.5 w-3.5" />
              </Link>
            </div>
          </div>

          <div className="relative bg-gradient-to-r from-[#0d1b2a] to-[#1b263b] overflow-hidden min-h-[200px] flex items-center">
            <div className="absolute inset-0">
              <Image
                src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&q=80"
                alt="Sports"
                fill
                className="object-cover opacity-30"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
            </div>
            <div className="relative z-10 p-6 text-white">
              <p className="text-xs font-bold text-[#ff9900] mb-1">FLASH SALE</p>
              <h3 className="text-2xl font-extrabold mb-2">Sports & Fitness</h3>
              <p className="text-sm text-gray-300 mb-4">Up to 50% off top brands</p>
              <Link
                href="/products?category=sports"
                className="inline-flex items-center gap-1 bg-[#ffd814] text-[#131921] text-sm font-bold px-5 py-2 rounded-full hover:bg-[#f7ca00] transition-colors"
              >
                Shop Now <ChevronRight className="h-3.5 w-3.5" />
              </Link>
            </div>
          </div>
        </div>

        {/* ── Gift ideas ───────────────────────────────────────────────── */}
        <div className="bg-white p-4">
          <div className="flex items-center gap-2 mb-4">
            <Gift className="h-5 w-5 text-[#cc0c39]" />
            <h2 className="text-xl font-bold text-[#0f1111]">Gift Ideas</h2>
          </div>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {[
              { label: 'Under $25', image: 'https://images.unsplash.com/photo-1513201099705-a9746e1e201f?w=300&q=80', href: '/products' },
              { label: 'Under $50', image: 'https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=300&q=80', href: '/products' },
              { label: 'Under $100', image: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300&q=80', href: '/products' },
              { label: 'Luxury Gifts', image: 'https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=300&q=80', href: '/products' },
            ].map((item) => (
              <Link key={item.label} href={item.href} className="group relative overflow-hidden aspect-square">
                <Image
                  src={item.image}
                  alt={item.label}
                  fill
                  className="object-cover group-hover:scale-105 transition-transform duration-300"
                  sizes="(max-width: 640px) 50vw, 25vw"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent" />
                <div className="absolute bottom-0 left-0 right-0 p-3">
                  <p className="text-white font-bold text-sm">{item.label}</p>
                  <p className="text-[#febd69] text-xs group-hover:underline">Shop now →</p>
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* ── Sign in / Account prompt ─────────────────────────────────── */}
        <div className="bg-white p-6">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="text-xl font-bold text-[#0f1111] mb-2">
              Sign in for a personalized experience
            </h2>
            <p className="text-sm text-gray-500 mb-5">
              Get AI-powered recommendations, track your orders, and access exclusive deals.
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Link
                href="/login"
                className="inline-block bg-[#ffd814] hover:bg-[#f7ca00] text-[#0f1111] font-bold px-8 py-2.5 rounded-full border border-[#fcd200] transition-colors text-sm"
              >
                Sign in
              </Link>
              <Link
                href="/register"
                className="inline-block bg-white hover:bg-gray-50 text-[#0f1111] font-medium px-8 py-2.5 rounded-full border border-gray-300 transition-colors text-sm"
              >
                Create account
              </Link>
            </div>
          </div>
        </div>

        {/* ── Newsletter ───────────────────────────────────────────────── */}
        <div className="bg-[#232f3e] p-6 text-center">
          <h2 className="text-lg font-bold text-white mb-1">Stay ahead of the deals</h2>
          <p className="text-sm text-gray-400 mb-4">
            Get exclusive offers, new arrivals, and AI-curated picks in your inbox.
          </p>
          <div className="max-w-md mx-auto">
            <NewsletterForm />
          </div>
        </div>

      </div>
    </div>
  )
}
