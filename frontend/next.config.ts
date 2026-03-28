import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: process.env.NEXT_PUBLIC_CLOUDFRONT_DOMAIN?.replace('https://', '') ?? 'cdn.example.com',
      },
      {
        protocol: 'https',
        hostname: '*.cloudfront.net',
      },
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
    ],
  },
  async rewrites() {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://nginx'
    return [
      { source: '/auth/:path*',            destination: `${apiUrl}/auth/:path*` },
      { source: '/catalog/:path*',         destination: `${apiUrl}/catalog/:path*` },
      { source: '/cart/:path*',            destination: `${apiUrl}/cart/:path*` },
      { source: '/orders/:path*',          destination: `${apiUrl}/orders/:path*` },
      { source: '/payments/:path*',        destination: `${apiUrl}/payments/:path*` },
      { source: '/search/:path*',          destination: `${apiUrl}/search/:path*` },
      { source: '/search',                 destination: `${apiUrl}/search` },
      { source: '/recommendations/:path*', destination: `${apiUrl}/recommendations/:path*` },
      { source: '/inventory/:path*',       destination: `${apiUrl}/inventory/:path*` },
      { source: '/admin/:path*',           destination: `${apiUrl}/admin/:path*` },
    ]
  },
}

export default nextConfig
