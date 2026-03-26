import { useAuthStore } from '@/store/auth'

async function refreshAccessToken(): Promise<string | null> {
  const { refreshToken, setTokens, logout } = useAuthStore.getState()
  if (!refreshToken) return null

  try {
    const res = await fetch('/api/auth/refresh', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refreshToken }),
    })
    if (!res.ok) {
      logout()
      return null
    }
    const data = await res.json()
    setTokens(data.accessToken, data.refreshToken ?? refreshToken)
    return data.accessToken as string
  } catch {
    logout()
    return null
  }
}

export async function fetcher<T = unknown>(url: string): Promise<T> {
  const { accessToken } = useAuthStore.getState()

  const headers: HeadersInit = { 'Content-Type': 'application/json' }
  if (accessToken) headers['Authorization'] = `Bearer ${accessToken}`

  let res = await fetch(url, { headers })

  if (res.status === 401) {
    const newToken = await refreshAccessToken()
    if (newToken) {
      res = await fetch(url, {
        headers: { ...headers, Authorization: `Bearer ${newToken}` },
      })
    }
  }

  if (!res.ok) {
    const error = new Error(`API error: ${res.status}`)
    throw error
  }

  return res.json() as Promise<T>
}
