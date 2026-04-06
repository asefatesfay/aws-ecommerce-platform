# Design HashMap

**Difficulty:** Easy
**Pattern:** Hash Table Design
**LeetCode:** #706

## Problem Statement

Design a HashMap without using any built-in hash table libraries. Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object with an empty map
- `void put(int key, int value)` inserts a (key, value) pair into the HashMap. If the key already exists, update the corresponding value.
- `int get(int key)` returns the value to which the specified key is mapped, or `-1` if this map contains no mapping for the key.
- `void remove(int key)` removes the key and its corresponding value if the map contains the mapping for the key.

## Examples

### Example 1
**Input:** `["MyHashMap","put","put","get","get","put","get","remove","get"]` with args `[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]`
**Output:** `[null,null,null,1,-1,null,1,null,-1]`

## Constraints
- `0 <= key, value <= 10^6`
- At most `10^4` calls will be made to `put`, `get`, and `remove`

## Hints

> 💡 **Hint 1:** Use an array of buckets. The hash function maps a key to a bucket index. Each bucket holds a list of (key, value) pairs to handle collisions.

> 💡 **Hint 2:** Choose a prime number of buckets (e.g., 1009) to reduce collisions. The hash function is simply `key % num_buckets`.

> 💡 **Hint 3:** For each operation, compute the bucket index, then linearly search the bucket's list for the key. For `put`, update if found or append if not. For `remove`, delete the matching pair.

## Approach

**Time Complexity:** O(n/k) average per operation, where n = number of keys, k = number of buckets
**Space Complexity:** O(n + k)

Array of linked lists (chaining). Hash function: `key % bucket_count`. Each operation hashes to a bucket, then scans the bucket's list.
