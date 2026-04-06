# LRU Cache

**Difficulty:** Medium
**Pattern:** Hash Map + Doubly Linked List
**LeetCode:** #146

## Problem Statement
Design a data structure that follows the Least Recently Used (LRU) cache eviction policy.
- `get(key)` — return the value if key exists, else -1. Mark as recently used.
- `put(key, value)` — insert or update. If capacity is exceeded, evict the least recently used item.

Both operations must run in O(1) average time.

## Examples

### Example 1
**Input:** `LRUCache(2)`, `put(1,1)`, `put(2,2)`, `get(1)` → `1`, `put(3,3)` (evicts key 2), `get(2)` → `-1`, `get(3)` → `3`

### Example 2
**Input:** `LRUCache(1)`, `put(2,1)`, `get(2)` → `1`, `put(3,2)` (evicts key 2), `get(2)` → `-1`, `get(3)` → `2`

## Constraints
- `1 <= capacity <= 3000`
- `0 <= key, value <= 10⁴`
- At most 3×10⁴ calls to `get` and `put`

## Hints

> 💡 **Hint 1:** Use a hash map for O(1) key lookup. Use a doubly linked list to track access order — most recent at head, least recent at tail.

> 💡 **Hint 2:** On `get`: move the accessed node to the head. On `put`: add to head; if over capacity, remove from tail.

> 💡 **Hint 3:** Use sentinel head and tail nodes to simplify edge cases (no null checks needed for empty list).

## Approach
**Time Complexity:** O(1) for both get and put
**Space Complexity:** O(capacity)

Hash map maps keys to doubly linked list nodes. List maintains order: head = most recent, tail = least recent. Move-to-front on access, remove-from-tail on eviction.
