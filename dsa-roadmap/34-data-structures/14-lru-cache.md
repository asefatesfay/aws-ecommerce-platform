# LRU Cache

## What is it?
A cache that evicts the **Least Recently Used** item when capacity is exceeded. Combines a **hash map** (O(1) lookup) with a **doubly linked list** (O(1) move-to-front and eviction).

## Visual Example
```
LRUCache(capacity=3)

put(1,1): [1]
put(2,2): [2,1]       ← 2 is most recent
put(3,3): [3,2,1]
get(1):   [1,3,2]     ← 1 moved to front (recently used)
put(4,4): [4,1,3]     ← 2 evicted (least recently used)
get(2):   -1          ← 2 was evicted
get(3):   [3,4,1]     ← 3 moved to front
put(5,5): [5,3,4]     ← 1 evicted

Structure:
  head ⇄ [most_recent] ⇄ ... ⇄ [least_recent] ⇄ tail
  hash_map: {key → node}
```

## Implementation

```python
from collections import OrderedDict

class LRUCache:
    """
    O(1) get and put using Python's OrderedDict.
    OrderedDict maintains insertion order and supports move_to_end.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """O(1) — return value and mark as recently used"""
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # most recent = end
        return self.cache[key]

    def put(self, key, value):
        """O(1) — insert/update and evict LRU if needed"""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict LRU (front)


class LRUCacheManual:
    """
    Manual implementation with doubly linked list + hash map.
    Shows the underlying mechanism clearly.
    """
    class _Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key → Node
        # Sentinel nodes eliminate edge case checks
        self.head = self._Node()  # dummy head (most recent side)
        self.tail = self._Node()  # dummy tail (least recent side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from list — O(1)"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        """Insert node right after head — O(1)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = self._Node(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev  # least recently used
            self._remove(lru)
            del self.cache[lru.key]
```

## Example Usage
```python
cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
print(cache.get(1))   # 1 (moves 1 to front)
cache.put(4, 4)       # evicts 2 (LRU)
print(cache.get(2))   # -1 (evicted)
print(cache.get(3))   # 3
print(cache.get(4))   # 4

# Manual implementation
cache2 = LRUCacheManual(2)
cache2.put(1, 1)
cache2.put(2, 2)
print(cache2.get(1))  # 1
cache2.put(3, 3)      # evicts 2
print(cache2.get(2))  # -1
```

## When to Use
- Web browser cache
- Database query cache
- CPU cache simulation
- Any "evict least recently used" scenario

## LeetCode Problems

| Problem | Difficulty | Notes |
|---------|-----------|-------|
| LRU Cache (#146) | Medium | Direct implementation |
| LFU Cache (#460) | Hard | Frequency-based eviction |
| Design In-Memory File System (#588) | Hard | Cache + trie |
| All O`one Data Structure (#432) | Hard | Similar DLL technique |
