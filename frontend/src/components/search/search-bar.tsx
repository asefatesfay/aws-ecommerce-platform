'use client'

import { useState, useEffect, useRef, useCallback } from 'react'
import { useRouter } from 'next/navigation'
import { Search, X } from 'lucide-react'
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
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const inputRef = useRef<HTMLInputElement>(null)

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

  return (
    <div className="relative w-full">
      <form onSubmit={handleSubmit} className="relative">
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
          className="w-full rounded-full border border-gray-300 bg-gray-50 py-2.5 pl-10 pr-10 text-sm outline-none focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-500/20 transition-all"
          aria-label="Search products"
          aria-autocomplete="list"
          aria-expanded={open}
        />
        {query && (
          <button
            type="button"
            onClick={handleClear}
            className="absolute right-3.5 top-1/2 -translate-y-1/2 rounded-full p-0.5 text-gray-400 hover:text-gray-600 transition-colors"
            aria-label="Clear search"
          >
            <X className="h-3.5 w-3.5" />
          </button>
        )}
      </form>

      {open && suggestions.length > 0 && (
        <ul
          role="listbox"
          className="absolute top-full mt-1.5 w-full rounded-2xl border border-gray-200 bg-white shadow-xl z-50 overflow-hidden py-1"
        >
          {suggestions.map((s, i) => (
            <li key={s.id} role="option" aria-selected={i === activeIndex}>
              <button
                className={cn(
                  'flex w-full items-center gap-3 px-4 py-2.5 text-left text-sm transition-colors',
                  i === activeIndex ? 'bg-indigo-50 text-indigo-700' : 'text-gray-700 hover:bg-gray-50'
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
