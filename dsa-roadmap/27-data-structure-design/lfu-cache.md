# LFU Cache

**Difficulty:** Hard
**Pattern:** Hash Map + Frequency Buckets
**LeetCode:** #460

## Problem Statement
Design a Least Frequently Used (LFU) cache. When capacity is exceeded, evict the least frequently used item. If there's a tie, evict the least recently used among them.
- `get(key)` — return value or -1, increment frequency
- `put(key, value)` — insert/update, increment frequency, evict if needed

Both O(1).

## Examples

### Example 1
**Input:** `LFUCache(2)`, `put(1,1)`, `put(2,2)`, `get(1)` → `1` (freq[1]=2), `put(3,3)` (evicts key 2, freq=1), `get(2)` → `-1`, `get(3)` → `3`, `put(4,4)` (evicts key 3, freq=1), `get(1)` → `1`, `get(3)` → `-1`, `get(4)` → `4`

## Constraints
- `0 <= capacity <= 10⁴`
- At most 10⁵ calls

## Hints

> 💡 **Hint 1:** Maintain three hash maps: `key→value`, `key→freq`, and `freq→OrderedDict of keys`. Also track `min_freq`.

> 💡 **Hint 2:** On access, move the key from `freq[k]` bucket to `freq[k+1]` bucket. Update `min_freq` if the old bucket is now empty.

> 💡 **Hint 3:** On eviction, remove the oldest key from `freq[min_freq]` bucket (use OrderedDict for O(1) oldest access).

## Approach
**Time Complexity:** O(1) for all operations
**Space Complexity:** O(capacity)

Three maps + min_freq tracker. Frequency buckets use OrderedDict to maintain insertion order for LRU tiebreaking.
