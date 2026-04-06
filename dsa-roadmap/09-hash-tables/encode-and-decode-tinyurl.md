# Encode and Decode TinyURL

**Difficulty:** Medium
**Pattern:** Hash Map / Design
**LeetCode:** #535

## Problem Statement

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a short URL.

Implement the `Solution` class:
- `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.
- `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the input to `decode` is a URL returned by `encode`.

## Examples

### Example 1
**Input:** `url = "https://leetcode.com/problems/design-tinyurl"`
**Output:** `encode` returns a short URL, `decode` returns the original URL

## Constraints
- `1 <= url.length <= 10^4`
- `url` is guaranteed to be a valid URL

## Hints

> 💡 **Hint 1:** You need a bidirectional mapping: long URL ↔ short URL. Use two HashMaps.

> 💡 **Hint 2:** For the short URL, generate a unique key. Options: auto-incrementing integer, random string, hash of the URL.

> 💡 **Hint 3:** A simple approach: use a counter as the key. `encode` maps longUrl → "http://tinyurl.com/{counter}" and stores the reverse mapping. `decode` looks up the counter in the reverse map.

## Approach

**Time Complexity:** O(1) for both encode and decode
**Space Complexity:** O(n) for n URLs

Two HashMaps: one from long URL to short code, one from short code to long URL. Generate unique codes with a counter or random string.
