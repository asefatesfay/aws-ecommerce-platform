'use client'

import { useState, useRef, useEffect, useCallback } from 'react'
import { useAuthStore } from '@/store/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

const QUICK_ACTIONS = [
  { label: 'Find deals 🔥', message: 'Show me the best deals available right now' },
  { label: 'Track my order 📦', message: 'What is the status of my most recent order?' },
  { label: "What's new? ✨", message: 'Show me the newest products added to the store' },
  { label: 'View my cart 🛒', message: 'Show me what is currently in my cart' },
]

export function ChatWidget() {
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [sessionId, setSessionId] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { accessToken } = useAuthStore()

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  const sendMessage = useCallback(
    async (text: string) => {
      if (!text.trim() || loading) return

      const userMsg: Message = { role: 'user', content: text }
      setMessages((prev) => [...prev, userMsg])
      setInput('')
      setLoading(true)

      try {
        const res = await fetch('/api/agent/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
          },
          body: JSON.stringify({ message: text, session_id: sessionId }),
        })

        if (!res.ok) throw new Error(`HTTP ${res.status}`)

        // Handle SSE streaming if content-type is event-stream, else parse JSON
        const contentType = res.headers.get('content-type') ?? ''
        if (contentType.includes('text/event-stream')) {
          const reader = res.body?.getReader()
          const decoder = new TextDecoder()
          let reply = ''
          setMessages((prev) => [...prev, { role: 'assistant', content: '' }])

          while (reader) {
            const { done, value } = await reader.read()
            if (done) break
            const chunk = decoder.decode(value)
            for (const line of chunk.split('\n')) {
              if (line.startsWith('data: ')) {
                try {
                  const data = JSON.parse(line.slice(6))
                  if (data.token) {
                    reply += data.token
                    setMessages((prev) => {
                      const updated = [...prev]
                      updated[updated.length - 1] = { role: 'assistant', content: reply }
                      return updated
                    })
                  }
                  if (data.session_id) setSessionId(data.session_id)
                } catch {
                  // ignore parse errors on SSE lines
                }
              }
            }
          }
        } else {
          const data = await res.json()
          if (data.session_id) setSessionId(data.session_id)
          setMessages((prev) => [...prev, { role: 'assistant', content: data.reply }])
        }
      } catch (err) {
        setMessages((prev) => [
          ...prev,
          { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' },
        ])
      } finally {
        setLoading(false)
      }
    },
    [loading, sessionId, accessToken],
  )

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    sendMessage(input)
  }

  return (
    <>
      {/* Floating trigger button */}
      <button
        onClick={() => setOpen((v) => !v)}
        aria-label="Open shopping assistant"
        className="fixed bottom-6 right-6 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-indigo-600 text-white shadow-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition-colors"
      >
        {open ? (
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        ) : (
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
          </svg>
        )}
      </button>

      {/* Slide-over panel */}
      {open && (
        <div
          role="dialog"
          aria-label="Shopping assistant"
          className="fixed bottom-24 right-6 z-50 flex w-96 max-w-[calc(100vw-1.5rem)] flex-col rounded-2xl bg-white shadow-2xl border border-gray-200 overflow-hidden"
          style={{ height: '520px' }}
        >
          {/* Header */}
          <div className="flex items-center justify-between bg-indigo-600 px-4 py-3">
            <div className="flex items-center gap-2">
              <span className="text-lg" aria-hidden="true">🛍️</span>
              <span className="font-semibold text-white text-sm">Shopping Assistant</span>
            </div>
            <button
              onClick={() => setOpen(false)}
              aria-label="Close assistant"
              className="text-indigo-200 hover:text-white transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto px-4 py-3 space-y-3 bg-gray-50">
            {messages.length === 0 && (
              <p className="text-center text-sm text-gray-400 mt-8">
                Hi! How can I help you shop today?
              </p>
            )}
            {messages.map((msg, i) => (
              <div
                key={i}
                className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-[80%] rounded-2xl px-3 py-2 text-sm leading-relaxed ${
                    msg.role === 'user'
                      ? 'bg-indigo-600 text-white rounded-br-sm'
                      : 'bg-white text-gray-800 border border-gray-200 rounded-bl-sm shadow-sm'
                  }`}
                >
                  {msg.content}
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start">
                <div className="bg-white border border-gray-200 rounded-2xl rounded-bl-sm px-3 py-2 shadow-sm">
                  <span className="flex gap-1 items-center">
                    <span className="h-2 w-2 rounded-full bg-gray-400 animate-bounce [animation-delay:-0.3s]" />
                    <span className="h-2 w-2 rounded-full bg-gray-400 animate-bounce [animation-delay:-0.15s]" />
                    <span className="h-2 w-2 rounded-full bg-gray-400 animate-bounce" />
                  </span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Quick actions */}
          {messages.length === 0 && (
            <div className="flex flex-wrap gap-2 px-4 py-2 bg-gray-50 border-t border-gray-100">
              {QUICK_ACTIONS.map((action) => (
                <button
                  key={action.label}
                  onClick={() => sendMessage(action.message)}
                  className="rounded-full border border-indigo-200 bg-white px-3 py-1 text-xs text-indigo-700 hover:bg-indigo-50 transition-colors"
                >
                  {action.label}
                </button>
              ))}
            </div>
          )}

          {/* Input */}
          <form onSubmit={handleSubmit} className="flex gap-2 border-t border-gray-200 bg-white px-3 py-3">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask me anything..."
              disabled={loading}
              className="flex-1 text-sm"
              aria-label="Message input"
            />
            <Button
              type="submit"
              disabled={loading || !input.trim()}
              size="sm"
              className="bg-indigo-600 hover:bg-indigo-700 text-white px-3"
              aria-label="Send message"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </Button>
          </form>
        </div>
      )}
    </>
  )
}
