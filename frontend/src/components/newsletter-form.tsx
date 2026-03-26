'use client'

export function NewsletterForm() {
  return (
    <form
      className="flex flex-col sm:flex-row gap-2"
      onSubmit={(e) => e.preventDefault()}
    >
      <input
        type="email"
        placeholder="Enter your email address"
        className="flex-1 rounded-full border border-gray-600 bg-white px-4 py-2.5 text-sm text-[#0f1111] outline-none focus:border-[#ff9900] focus:ring-2 focus:ring-[#ff9900]/30 placeholder:text-gray-400"
      />
      <button
        type="submit"
        className="shrink-0 rounded-full bg-[#ffd814] hover:bg-[#f7ca00] border border-[#fcd200] px-6 py-2.5 text-sm font-bold text-[#0f1111] transition-colors"
      >
        Subscribe
      </button>
    </form>
  )
}
