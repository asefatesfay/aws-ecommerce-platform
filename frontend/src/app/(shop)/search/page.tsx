import { Suspense } from 'react'
import SearchResults from './search-results'

export default function SearchPage() {
  return (
    <Suspense fallback={<div className="mx-auto max-w-7xl px-6 py-10 text-gray-500">Loading...</div>}>
      <SearchResults />
    </Suspense>
  )
}
