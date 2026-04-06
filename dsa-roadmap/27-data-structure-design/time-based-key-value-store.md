# Time Based Key-Value Store

**Difficulty:** Medium
**Pattern:** Hash Map + Binary Search
**LeetCode:** #981

## Problem Statement
Design a time-based key-value store that stores multiple values for the same key at different timestamps.
- `set(key, value, timestamp)` — stores the value at the given timestamp
- `get(key, timestamp)` — returns the value with the largest timestamp ≤ given timestamp, or "" if none

## Examples

### Example 1
**Input:** `set("foo","bar",1)`, `get("foo",1)` → `"bar"`, `get("foo",3)` → `"bar"`, `set("foo","bar2",4)`, `get("foo",4)` → `"bar2"`, `get("foo",5)` → `"bar2"`

## Constraints
- `1 <= key.length, value.length <= 100`
- `1 <= timestamp <= 10⁷`
- All timestamps in `set` are strictly increasing
- At most 2×10⁵ calls

## Hints

> 💡 **Hint 1:** Since timestamps in `set` are strictly increasing, each key maps to a sorted list of `(timestamp, value)` pairs.

> 💡 **Hint 2:** For `get`, binary search the list for the largest timestamp ≤ query timestamp using `bisect_right`.

> 💡 **Hint 3:** `bisect_right(timestamps, target) - 1` gives the index of the largest timestamp ≤ target. If index < 0, return "".

## Approach
**Time Complexity:** O(1) for set, O(log N) for get
**Space Complexity:** O(N)

Hash map of key → sorted list of (timestamp, value). Binary search on timestamps for each get query.
