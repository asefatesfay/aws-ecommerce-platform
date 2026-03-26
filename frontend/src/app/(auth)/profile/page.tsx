'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { useAuthStore } from '@/store/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent, CardHeader, CardFooter } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

export default function ProfilePage() {
  const router = useRouter()
  const { user, logout } = useAuthStore()
  const [saving, setSaving] = useState(false)
  const [success, setSuccess] = useState(false)
  const [form, setForm] = useState({
    fullName: user?.fullName ?? '',
    email: user?.email ?? '',
  })

  if (!user) {
    router.replace('/login')
    return null
  }

  const handleChange = (field: keyof typeof form) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setForm((prev) => ({ ...prev, [field]: e.target.value }))

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault()
    setSaving(true)
    try {
      await fetch('/api/users/me', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      setSuccess(true)
      setTimeout(() => setSuccess(false), 3000)
    } finally {
      setSaving(false)
    }
  }

  const handleLogout = () => {
    logout()
    router.push('/')
  }

  return (
    <div className="mx-auto max-w-2xl px-6 py-10 space-y-6">
      <h1 className="text-2xl font-bold">My Profile</h1>

      <Card>
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-lg">
              {user.fullName.charAt(0).toUpperCase()}
            </div>
            <div>
              <p className="font-semibold text-gray-900">{user.fullName}</p>
              <p className="text-sm text-gray-500">{user.email}</p>
            </div>
            <Badge variant="primary" className="ml-auto">{user.role}</Badge>
          </div>
        </CardHeader>
        <CardContent>
          <form id="profile-form" onSubmit={handleSave} className="space-y-4">
            <Input
              id="fullName"
              label="Full Name"
              value={form.fullName}
              onChange={handleChange('fullName')}
            />
            <Input
              id="email"
              label="Email"
              type="email"
              value={form.email}
              onChange={handleChange('email')}
            />
            {success && <p className="text-sm text-green-600">Profile updated successfully.</p>}
          </form>
        </CardContent>
        <CardFooter className="justify-between">
          <Button variant="ghost" onClick={handleLogout}>
            Sign Out
          </Button>
          <Button type="submit" form="profile-form" loading={saving}>
            Save Changes
          </Button>
        </CardFooter>
      </Card>
    </div>
  )
}
