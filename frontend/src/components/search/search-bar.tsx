'use client'

import { useState, useEffect, useRef, useCallback } from 'react'
import { useRouter } from 'next/navigation'
import { Search, X, Camera } from 'lucide-react'
import { cn } from '@/lib/utils'

interface Suggestion {
  id: string
  name: string
}

export function SearchBar() {
  const router = useRouter()
  const [query, setQuery] = useState('')
  const [suggestions, setSuggestions] = useState<Suggestion[]>([])
  const [open, setOpen] = useState(false)
  const [activeIndex, setActiveIndex] = useState(-1)
  const [visualSearching, setVisualSearching] = useState(false)
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const fetchSuggestions = useCallback(async (q: string) => {
    try {
      const res = await fetch(`/api/search/autocomplete?q=${encodeURIComponent(q)}`)
      if (res.ok) {
        const data = await res.json()
        setSuggestions(data.suggestions ?? [])
        setOpen(true)
        setActiveIndex(-1)
      }
    } catch {
      // silently ignore
    }
  }, [])

  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current)
    if (query.trim().length < 2) {
      setSuggestions([])
      setOpen(false)
      return
    }
    debounceRef.current = setTimeout(() => fetchSuggestions(query), 300)
    return () => {
      if (debounceRef.current) clearTimeout(debounceRef.current)
    }
  }, [query, fetchSuggestions])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    const q = activeIndex >= 0 ? suggestions[activeIndex]?.name ?? query : query
    if (q.trim()) {
      setOpen(false)
      router.push(`/search?q=${encodeURIComponent(q.trim())}`)
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (!open || suggestions.length === 0) return
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setActiveIndex((i) => Math.min(i + 1, suggestions.length - 1))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setActiveIndex((i) => Math.max(i - 1, -1))
    } else if (e.key === 'Escape') {
      setOpen(false)
      setActiveIndex(-1)
    }
  }

  const handleClear = () => {
    setQuery('')
    setSuggestions([])
    setOpen(false)
    inputRef.current?.focus()
  }

  const handleVisualSearch = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setVisualSearching(true)
    try {
      const formData = new FormData()
      formData.append('file', file)
      const res = await fetch('/api/search/visual', { method: 'POST', body: formData })
      if (res.ok) {
        const data = await res.json()
        const attrs = data.extracted_attributes as Record<string, string>
        const attrQuery = Object.values(attrs).filter(Boolean).join(' ')
        router.push(`/search?q=${encodeURIComponent(attrQuery)}&visual=1`)
      } else {
        const err = await res.json().catch(() => ({ detail: 'Visual search failed' }))
        alert(err.detail ?? 'Visual search failed')
      }
    } catch {
      alert('Visual search failed. Please try again.')
    } finally {
      setVisualSearching(false)
      // Reset file input so the same file can be re-selected
      if (fileInputRef.current) fileInputRef.current.value = ''
    }
  }

  return (
    <div className="relative w-full">
      <form onSubmit={handleSubmit} className="relative flex w-full">
        <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none" />
        <input
          ref={inputRef}
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => suggestions.length > 0 && setOpen(true)}
          onBlur={() => setTimeout(() => setOpen(false), 150)}
          onKeyDown={handleKeyDown}
          placeholder="Search products..."
          className="w-full rounded-l-md border-0 bg-white py-2.5 pl-10 pr-10 text-sm text-[#0f1111] outline-none focus:ring-2 focus:ring-[#ff9900] placeholder:text-gray-400"
          aria-label="Search products"
          aria-autocomplete="list"
          aria-expanded={open}
        />
        {query && (
          <button
            type="button"
            onClick={handleClear}
            className="absolute right-12 top-1/2 -translate-y-1/2 rounded-full p-0.5 text-gray-400 hover:text-gray-600 transition-colors"
            aria-label="Clear search"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        )}
        {/* Visual search button */}
        <button
          type="button"
          onClick={() => fileInputRef.current?.click()}
          disabled={visualSearching}
          className="absolute right-[52px] top-1/2 -translate-y-1/2 p-1 text-gray-400 hover:text-[#ff9900] transition-colors"
          aria-label="Search by image"
          title="Search by image"
        >
          <Camera className={cn('h-4 w-4', visualSearching && 'animate-pulse text-[#ff9900]')} />
        </button>
        {/* Orange search button */}
        <button
          type="submit"
          className="shrink-0 rounded-r-md bg-[#febd69] hover:bg-[#f3a847] px-4 py-2.5 transition-colors"
          aria-label="Search"
        >
          <Search className="h-5 w-5 text-[#131921]" />
        </button>
      </form>

      {/* Hidden file input for visual search */}
      <input
        ref={fileInputRef}
        type="file"
        accept="image/jpeg,image/png,image/webp"
        className="hidden"
        onChange={handleVisualSearch}
        aria-hidden="true"
      />

      {open && suggestions.length > 0 && (
        <ul
          role="listbox"
          className="absolute top-full mt-0.5 w-full rounded border border-gray-300 bg-white shadow-xl z-50 overflow-hidden py-1"
        >
          {suggestions.map((s, i) => (
            <li key={s.id} role="option" aria-selected={i === activeIndex}>
              <button
                className={cn(
                  'flex w-full items-center gap-3 px-4 py-2 text-left text-sm transition-colors',
                  i === activeIndex ? 'bg-[#eaf4fe]' : 'text-[#0f1111] hover:bg-gray-100'
                )}
                onMouseDown={() => {
                  router.push(`/products/${s.id}`)
                  setOpen(false)
                }}
              >
                <Search className="h-3.5 w-3.5 shrink-0 text-gray-400" />
                {s.name}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
