import Link from 'next/link'

const FOOTER_SECTIONS = [
  {
    title: 'Get to Know Us',
    links: [
      { label: 'About Nexmart', href: '#' },
      { label: 'Careers', href: '#' },
      { label: 'Press Releases', href: '#' },
      { label: 'Nexmart Science', href: '#' },
    ],
  },
  {
    title: 'Make Money with Us',
    links: [
      { label: 'Sell products on Nexmart', href: '#' },
      { label: 'Sell on Nexmart Business', href: '#' },
      { label: 'Become an Affiliate', href: '#' },
      { label: 'Advertise Your Products', href: '#' },
    ],
  },
  {
    title: 'Nexmart Payment Products',
    links: [
      { label: 'Nexmart Business Card', href: '#' },
      { label: 'Shop with Points', href: '#' },
      { label: 'Reload Your Balance', href: '#' },
      { label: 'Nexmart Currency Converter', href: '#' },
    ],
  },
  {
    title: 'Let Us Help You',
    links: [
      { label: 'Nexmart and COVID-19', href: '#' },
      { label: 'Your Account', href: '/profile' },
      { label: 'Your Orders', href: '/orders' },
      { label: 'Shipping Rates & Policies', href: '#' },
      { label: 'Returns & Replacements', href: '#' },
      { label: 'Manage Your Content', href: '#' },
      { label: 'Help', href: '#' },
    ],
  },
]

export function Footer() {
  return (
    <footer>
      {/* Back to top */}
      <button
        onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
        className="w-full bg-[#37475a] hover:bg-[#485769] text-white text-sm py-3 transition-colors"
      >
        Back to top
      </button>

      {/* Main footer links */}
      <div className="bg-[#232f3e] text-white">
        <div className="mx-auto max-w-[1500px] px-6 py-10">
          <div className="grid grid-cols-2 gap-8 sm:grid-cols-4">
            {FOOTER_SECTIONS.map((section) => (
              <div key={section.title}>
                <h3 className="text-sm font-bold text-white mb-3">{section.title}</h3>
                <ul className="space-y-2">
                  {section.links.map((link) => (
                    <li key={link.label}>
                      <Link
                        href={link.href}
                        className="text-xs text-gray-300 hover:text-white transition-colors"
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
      </div>

      {/* Logo + country selector */}
      <div className="bg-[#131921] border-t border-gray-700">
        <div className="mx-auto max-w-[1500px] px-6 py-6 flex flex-col items-center gap-4">
          <Link href="/" className="text-2xl font-extrabold text-white">
            nexmart<span className="text-[#ff9900]">.com</span>
          </Link>
          <div className="flex flex-wrap items-center justify-center gap-3">
            <button className="flex items-center gap-1.5 rounded border border-gray-600 px-3 py-1.5 text-xs text-gray-300 hover:border-gray-400 transition-colors">
              🌐 English
            </button>
            <button className="flex items-center gap-1.5 rounded border border-gray-600 px-3 py-1.5 text-xs text-gray-300 hover:border-gray-400 transition-colors">
              $ USD
            </button>
            <button className="flex items-center gap-1.5 rounded border border-gray-600 px-3 py-1.5 text-xs text-gray-300 hover:border-gray-400 transition-colors">
              🇺🇸 United States
            </button>
          </div>
        </div>
      </div>

      {/* Legal */}
      <div className="bg-[#131921] border-t border-gray-800">
        <div className="mx-auto max-w-[1500px] px-6 py-4 flex flex-wrap items-center justify-center gap-x-4 gap-y-1">
          {[
            'Conditions of Use',
            'Privacy Notice',
            'Your Ads Privacy Choices',
            'Interest-Based Ads',
            'Cookie Preferences',
          ].map((item) => (
            <Link key={item} href="#" className="text-xs text-gray-400 hover:text-gray-200 transition-colors">
              {item}
            </Link>
          ))}
          <span className="text-xs text-gray-500">
            © {new Date().getFullYear()}, Nexmart.com, Inc. or its affiliates
          </span>
        </div>
      </div>
    </footer>
  )
}
