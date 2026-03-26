import Link from 'next/link'
import { Twitter, Github, Instagram } from 'lucide-react'

const LINKS = {
  Shop: [
    { label: 'All Products', href: '/products' },
    { label: 'Electronics', href: '/products?category=electronics' },
    { label: 'Clothing', href: '/products?category=clothing' },
    { label: 'Sports', href: '/products?category=sports' },
    { label: 'Home & Garden', href: '/products?category=home-garden' },
  ],
  Account: [
    { label: 'Login', href: '/login' },
    { label: 'Register', href: '/register' },
    { label: 'My Orders', href: '/orders' },
    { label: 'Profile', href: '/profile' },
  ],
  Support: [
    { label: 'FAQ', href: '#' },
    { label: 'Contact Us', href: '#' },
    { label: 'Shipping Info', href: '#' },
    { label: 'Returns', href: '#' },
  ],
  Company: [
    { label: 'About Us', href: '#' },
    { label: 'Privacy Policy', href: '#' },
    { label: 'Terms of Service', href: '#' },
    { label: 'Careers', href: '#' },
  ],
}

export function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-300">
      {/* Main content */}
      <div className="mx-auto max-w-7xl px-6 py-14">
        <div className="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-5">
          {/* Brand column */}
          <div className="lg:col-span-1">
            <Link href="/" className="text-2xl font-extrabold tracking-tight text-white">
              NEXMART
            </Link>
            <p className="mt-3 text-sm text-gray-400 leading-relaxed">
              Discover amazing products at unbeatable prices. Shop smarter, live better.
            </p>
            <div className="mt-5 flex items-center gap-3">
              <a
                href="#"
                aria-label="Twitter"
                className="rounded-lg p-2 text-gray-400 hover:bg-gray-800 hover:text-white transition-colors"
              >
                <Twitter className="h-4 w-4" />
              </a>
              <a
                href="#"
                aria-label="GitHub"
                className="rounded-lg p-2 text-gray-400 hover:bg-gray-800 hover:text-white transition-colors"
              >
                <Github className="h-4 w-4" />
              </a>
              <a
                href="#"
                aria-label="Instagram"
                className="rounded-lg p-2 text-gray-400 hover:bg-gray-800 hover:text-white transition-colors"
              >
                <Instagram className="h-4 w-4" />
              </a>
            </div>
          </div>

          {/* Link columns */}
          {(Object.entries(LINKS) as [string, { label: string; href: string }[]][]).map(([section, links]) => (
            <div key={section}>
              <h3 className="text-sm font-semibold uppercase tracking-wider text-white mb-4">
                {section}
              </h3>
              <ul className="space-y-2.5">
                {links.map((link) => (
                  <li key={link.label}>
                    <Link
                      href={link.href}
                      className="text-sm text-gray-400 hover:text-white transition-colors"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>

      {/* Bottom bar */}
      <div className="border-t border-gray-800">
        <div className="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-6 py-5 sm:flex-row">
          <p className="text-xs text-gray-500">
            &copy; {new Date().getFullYear()} NEXMART. All rights reserved.
          </p>
          <div className="flex items-center gap-2">
            <span className="text-xs text-gray-500">We accept:</span>
            <span className="rounded border border-gray-700 bg-gray-800 px-2 py-0.5 text-xs font-semibold text-gray-300">
              VISA
            </span>
            <span className="rounded border border-gray-700 bg-gray-800 px-2 py-0.5 text-xs font-semibold text-gray-300">
              Mastercard
            </span>
            <span className="rounded border border-gray-700 bg-gray-800 px-2 py-0.5 text-xs font-semibold text-gray-300">
              Stripe
            </span>
          </div>
        </div>
      </div>
    </footer>
  )
}
