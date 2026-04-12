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

---

### 1. LRU Cache — #146 (Medium)

**Problem**: Design a data structure that follows the Least Recently Used (LRU) cache eviction policy. Implement `get(key)` (returns value or -1) and `put(key, value)` (inserts/updates, evicts LRU if at capacity). Both must be O(1).

```
Input:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],       [1,1],[2,2],[1],  [3,3],[2],  [4,4],[1],  [3],  [4]]

Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Trace (capacity=2):
put(1,1) → {1:1}
put(2,2) → {1:1, 2:2}
get(1)   → 1, order: [2→1] (1 is now most recent)
put(3,3) → evict 2 (LRU), {1:1, 3:3}
get(2)   → -1 (evicted)
put(4,4) → evict 1 (LRU), {3:3, 4:4}
get(1)   → -1 (evicted)
get(3)   → 3
get(4)   → 4
```

**Hints**:
1. Hash map for O(1) lookup; doubly linked list for O(1) move-to-front and eviction
2. Use sentinel head/tail nodes to avoid null checks
3. Python shortcut: `OrderedDict` with `move_to_end(key)` and `popitem(last=False)`

---

### 2. LFU Cache — #460 (Hard)

**Problem**: Design a data structure following the Least Frequently Used (LFU) cache policy. Ties broken by LRU. Both `get` and `put` must be O(1).

```
Input:
["LFUCache","put","put","get","put","get","get","put","get","get","get"]
[[2],       [1,1],[2,2],[1],  [3,3],[2],  [3],  [4,4],[1],  [3],  [4]]

Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Trace (capacity=2):
put(1,1) → freq[1]=1
put(2,2) → freq[2]=1
get(1)   → 1, freq[1]=2
put(3,3) → evict key 2 (min_freq=1, only key with freq=1)
get(2)   → -1 (evicted)
get(3)   → 3, freq[3]=2
put(4,4) → evict key 1 (min_freq=2, key 1 is LRU among freq=2)
get(1)   → -1 (evicted)
get(3)   → 3
get(4)   → 4
```

**Hints**:
1. Three maps: `key→val`, `key→freq`, `freq→OrderedDict(keys)`
2. `min_freq` resets to 1 on every new insert
3. When a frequency bucket empties and it was `min_freq`, increment `min_freq`

---

### 3. Design In-Memory File System — #588 (Hard)

**Problem**: Implement a file system with `ls(path)`, `mkdir(path)`, `addContentToFile(filePath, content)`, `readContentFromFile(filePath)`.

```
Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],          ["/"],["/a/b/c"],["a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output: [null, [], null, null, ["a"], "hello"]

Trace:
ls("/")                    → []  (empty root)
mkdir("/a/b/c")            → creates directories a, b, c
addContentToFile("/a/b/c/d","hello") → creates file d with content "hello"
ls("/")                    → ["a"]  (only top-level entry)
readContentFromFile("/a/b/c/d") → "hello"
```

**Hints**:
1. Use a trie where each node represents a directory or file
2. Each node stores: children (dict), is_file (bool), content (str)
3. `ls` on a file returns `[filename]`; on a directory returns sorted children names
