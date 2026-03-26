import Link from 'next/link'

export default function HomePage() {
  return (
    <main>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary to-primary-dark text-white py-24 px-6 text-center">
        <h1 className="text-5xl font-bold mb-4">Welcome to Shop</h1>
        <p className="text-xl mb-8 opacity-90">Discover amazing products at great prices.</p>
        <Link
          href="/products"
          className="inline-block bg-white text-primary font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition-colors"
        >
          Shop Now
        </Link>
      </section>

      {/* Featured products placeholder */}
      <section className="max-w-7xl mx-auto px-6 py-16">
        <h2 className="text-2xl font-bold mb-8">Featured Products</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="rounded-xl border border-gray-200 bg-gray-50 h-64 animate-pulse" />
          ))}
        </div>
      </section>
    </main>
  )
}
