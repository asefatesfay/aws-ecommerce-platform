# LFU Cache — Least Frequently Used

## What is it?

An LFU (Least Frequently Used) cache evicts the item that has been **accessed the fewest number of times** when capacity is exceeded. If there's a tie in frequency, it evicts the **least recently used** among those with the lowest frequency.

Both `get` and `put` must run in **O(1)** time.

---

## LRU vs LFU — Key Difference

```
LRU: evicts the item not used for the LONGEST TIME
LFU: evicts the item used the FEWEST TIMES

Example with capacity=2:
put(1,1), put(2,2), get(1), put(3,3)

LRU: evicts 2 (least recently used)
LFU: evicts 2 (freq[1]=2, freq[2]=1 → 2 is least frequent)

When to use LFU over LRU:
- When popular items should stay cached regardless of recency
- Database buffer pools (frequently accessed pages stay)
- CDN caching (popular content stays longer)
```

---

## The Core Challenge

The hard part is answering **"which item has the minimum frequency, and among those, which was used least recently?"** in O(1).

The naive approach — scan all items to find min frequency — is O(N). We need something smarter.

---

## Data Structures Needed

```
Three hash maps + doubly linked lists:

1. key_to_val:   {key → value}
   Purpose: O(1) value lookup

2. key_to_freq:  {key → frequency}
   Purpose: O(1) frequency lookup per key

3. freq_to_keys: {frequency → OrderedDict of keys}
   Purpose: O(1) access to all keys at a given frequency
            OrderedDict maintains insertion order → LRU tiebreaking

4. min_freq: integer
   Purpose: track current minimum frequency for O(1) eviction
```

---

## Visual Walkthrough

```
LFUCache(capacity=3)

Step 1: put(1, "a")
  key_to_val:  {1: "a"}
  key_to_freq: {1: 1}
  freq_to_keys: {1: OrderedDict([(1, None)])}
  min_freq: 1

Step 2: put(2, "b")
  key_to_val:  {1:"a", 2:"b"}
  key_to_freq: {1:1, 2:1}
  freq_to_keys: {1: OrderedDict([(1,None),(2,None)])}
  min_freq: 1

Step 3: put(3, "c")
  key_to_val:  {1:"a", 2:"b", 3:"c"}
  key_to_freq: {1:1, 2:1, 3:1}
  freq_to_keys: {1: OrderedDict([(1,None),(2,None),(3,None)])}
  min_freq: 1

Step 4: get(1)  → returns "a", freq[1] becomes 2
  key_to_freq: {1:2, 2:1, 3:1}
  freq_to_keys: {
    1: OrderedDict([(2,None),(3,None)]),  ← 1 removed from freq=1
    2: OrderedDict([(1,None)])            ← 1 added to freq=2
  }
  min_freq: 1  (still 1, keys 2 and 3 have freq=1)

Step 5: put(4, "d")  → capacity exceeded, must evict
  min_freq = 1
  freq_to_keys[1] = OrderedDict([(2,None),(3,None)])
  Evict FIRST item in freq=1 bucket → evict key 2 (LRU among freq=1)
  
  After eviction:
  key_to_val:  {1:"a", 3:"c", 4:"d"}
  key_to_freq: {1:2, 3:1, 4:1}
  freq_to_keys: {
    1: OrderedDict([(3,None),(4,None)]),
    2: OrderedDict([(1,None)])
  }
  min_freq: 1
```

---

## Why `min_freq` Can Only Increase by 1 on `put`

```
When we insert a new key, its frequency is always 1.
So min_freq = 1 after any new insertion.

When we access an existing key (get or put update):
  old_freq → old_freq + 1
  If old_freq == min_freq AND freq_to_keys[old_freq] is now empty:
    min_freq += 1  (the minimum just increased by 1)
  
This is why we can maintain min_freq in O(1).
```

---

## Implementation

```python
from collections import defaultdict, OrderedDict

class LFUCache:
    """
    O(1) get and put using three hash maps + OrderedDicts.
    
    Data structures:
    - key_to_val:   key → value
    - key_to_freq:  key → access frequency
    - freq_to_keys: frequency → OrderedDict{key: None} (insertion order = LRU order)
    - min_freq:     current minimum frequency
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_val = {}                          # key → value
        self.key_to_freq = {}                         # key → frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # freq → {key: None}

    def get(self, key: int) -> int:
        """
        Return value for key, or -1 if not found.
        Increments frequency of the key.
        O(1)
        """
        if key not in self.key_to_val:
            return -1
        self._increment_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        Evicts LFU item if at capacity.
        O(1)
        """
        if self.capacity <= 0:
            return

        if key in self.key_to_val:
            # Update existing key
            self.key_to_val[key] = value
            self._increment_freq(key)
        else:
            # Insert new key
            if self.size >= self.capacity:
                self._evict()
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1  # new key always has freq=1
            self.size += 1

    def _increment_freq(self, key: int) -> None:
        """
        Move key from its current frequency bucket to the next one.
        Update min_freq if the current bucket becomes empty.
        O(1)
        """
        freq = self.key_to_freq[key]
        # Remove from current frequency bucket
        del self.freq_to_keys[freq][key]
        # If this was the minimum frequency bucket and it's now empty, increment min_freq
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1
        # Add to next frequency bucket
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

    def _evict(self) -> None:
        """
        Remove the least frequently used item.
        Among ties, remove the least recently used (first in OrderedDict).
        O(1)
        """
        # Get the LRU key among minimum frequency items
        lfu_keys = self.freq_to_keys[self.min_freq]
        lfu_key, _ = lfu_keys.popitem(last=False)  # FIFO: remove oldest
        del self.key_to_val[lfu_key]
        del self.key_to_freq[lfu_key]
        self.size -= 1
```

---

## Step-by-Step Trace

```python
cache = LFUCache(2)

cache.put(1, 1)
# key_to_val:  {1:1}
# key_to_freq: {1:1}
# freq_to_keys:{1: {1}}
# min_freq: 1

cache.put(2, 2)
# key_to_val:  {1:1, 2:2}
# key_to_freq: {1:1, 2:1}
# freq_to_keys:{1: {1,2}}
# min_freq: 1

cache.get(1)  # returns 1
# key 1 freq: 1→2
# key_to_freq: {1:2, 2:1}
# freq_to_keys:{1:{2}, 2:{1}}
# min_freq: 1 (key 2 still has freq=1)

cache.put(3, 3)  # evict! capacity=2
# min_freq=1, freq_to_keys[1]={2} → evict key 2
# Insert key 3 with freq=1
# key_to_val:  {1:1, 3:3}
# key_to_freq: {1:2, 3:1}
# freq_to_keys:{1:{3}, 2:{1}}
# min_freq: 1

cache.get(2)  # returns -1 (evicted)
cache.get(3)  # returns 3
# key 3 freq: 1→2
# freq_to_keys:{1:{}, 2:{1,3}}
# min_freq: 2 (freq=1 bucket is now empty)

cache.put(4, 4)  # evict! capacity=2
# min_freq=2, freq_to_keys[2]={1,3} → evict key 1 (LRU among freq=2)
# Insert key 4 with freq=1
# key_to_val:  {3:3, 4:4}
# key_to_freq: {3:2, 4:1}
# freq_to_keys:{1:{4}, 2:{3}}
# min_freq: 1

cache.get(1)  # returns -1 (evicted)
cache.get(3)  # returns 3
cache.get(4)  # returns 4
```

---

## Alternative Implementation: Doubly Linked List

For interviews where you can't use `OrderedDict`, implement the frequency buckets manually using doubly linked lists:

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLL:
    """Doubly linked list with sentinel nodes."""
    def __init__(self):
        self.head = Node()  # dummy head (most recent)
        self.tail = Node()  # dummy tail (least recent)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        """Remove and return the LRU node (tail.prev)"""
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

    def is_empty(self):
        return self.size == 0


class LFUCacheManual:
    """LFU Cache using manual doubly linked lists — no OrderedDict."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}          # key → Node
        self.freq_to_list = defaultdict(DLL)  # freq → DLL

    def _update(self, node):
        """Move node to next frequency bucket."""
        freq = node.freq
        self.freq_to_list[freq].remove(node)
        if self.freq_to_list[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_list[node.freq].insert_front(node)

    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update(node)
        else:
            if self.size >= self.capacity:
                # Evict LFU (last node in min_freq list)
                evicted = self.freq_to_list[self.min_freq].remove_last()
                if evicted:
                    del self.key_to_node[evicted.key]
                    self.size -= 1
            node = Node(key, value)
            self.key_to_node[key] = node
            self.freq_to_list[1].insert_front(node)
            self.min_freq = 1
            self.size += 1
```

---

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| `get` | O(1) | — |
| `put` | O(1) | — |
| Total space | — | O(capacity) |

---

## LRU vs LFU Comparison

| Aspect | LRU | LFU |
|--------|-----|-----|
| Eviction policy | Least recently used | Least frequently used |
| Implementation | Hash map + DLL | 3 hash maps + OrderedDicts |
| Complexity | O(1) | O(1) |
| Handles recency | Yes | Only as tiebreaker |
| Handles frequency | No | Yes |
| Cold start problem | No | Yes (new items evicted quickly) |
| Best for | General caching | Stable access patterns |

---

## Common Mistakes

```python
# MISTAKE 1: Forgetting to update min_freq on new insert
def put(self, key, value):
    # ...
    self.min_freq = 1  # ← MUST reset to 1 for new keys!

# MISTAKE 2: Not handling the empty bucket case
def _increment_freq(self, key):
    freq = self.key_to_freq[key]
    del self.freq_to_keys[freq][key]
    if freq == self.min_freq and not self.freq_to_keys[freq]:
        self.min_freq += 1  # ← MUST check if bucket is empty!

# MISTAKE 3: Using regular dict instead of OrderedDict
# Regular dict doesn't guarantee insertion order for LRU tiebreaking
self.freq_to_keys = defaultdict(dict)       # WRONG
self.freq_to_keys = defaultdict(OrderedDict) # CORRECT
```

---

## Test Cases

```python
def test_lfu():
    # Basic test
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1      # freq[1]=2, freq[2]=1
    cache.put(3, 3)               # evict key 2 (min freq=1)
    assert cache.get(2) == -1     # evicted
    assert cache.get(3) == 3      # freq[3]=2
    cache.put(4, 4)               # evict key 1 (min freq=2, LRU=1)
    assert cache.get(1) == -1     # evicted
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Capacity 1
    cache2 = LFUCache(1)
    cache2.put(1, 1)
    cache2.put(2, 2)              # evict 1
    assert cache2.get(1) == -1
    assert cache2.get(2) == 2

    # Update existing key
    cache3 = LFUCache(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.put(1, 10)             # update key 1, freq[1]=2
    assert cache3.get(1) == 10
    cache3.put(3, 3)              # evict key 2 (min freq=1)
    assert cache3.get(2) == -1
    assert cache3.get(3) == 3

    print("All tests passed!")

test_lfu()
```

---

## LeetCode Problems

---

### 1. LFU Cache — #460 (Hard)

**Problem**

Design a data structure that follows the Least Frequently Used (LFU) cache eviction policy.

Implement the `LFUCache` class:
- `LFUCache(int capacity)` — initialize with positive capacity
- `int get(int key)` — return the value if key exists, else return `-1`
- `void put(int key, int value)` — insert or update the key. If at capacity, evict the least frequently used key before inserting. Ties broken by least recently used.

Both `get` and `put` must run in **O(1)** average time.

**Example**

```
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2],        [1,1], [2,2], [1],   [3,3], [2],   [3],   [4,4], [1],   [3],   [4]]

Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Trace:
LFUCache(2)
put(1,1) → {1:1}, freq[1]=1
put(2,2) → {1:1, 2:2}, freq[1]=1, freq[2]=1
get(1)   → 1, freq[1] becomes 2
put(3,3) → capacity full, min_freq=1, evict key 2 (only key with freq=1)
           → {1:1, 3:3}, freq[1]=2, freq[3]=1
get(2)   → -1 (evicted)
get(3)   → 3, freq[3] becomes 2
put(4,4) → capacity full, min_freq=2, both keys have freq=2
           → evict key 1 (LRU among freq=2, inserted before key 3)
           → {3:3, 4:4}, freq[3]=2, freq[4]=1
get(1)   → -1 (evicted)
get(3)   → 3
get(4)   → 4
```

**Constraints**
- `1 <= capacity <= 10^4`
- `0 <= key <= 10^5`
- `0 <= value <= 10^9`
- At most `2 * 10^5` calls to `get` and `put`

**How LFU applies**: This IS the LFU problem. The implementation above is the direct solution.

**Hints**
1. You need three maps: `key→value`, `key→freq`, `freq→ordered_keys`
2. `min_freq` resets to 1 every time you insert a new key
3. `min_freq` only increments when the current min bucket becomes empty after a `get`/`put` update
4. Use `OrderedDict` for each frequency bucket — `popitem(last=False)` gives you the LRU item in O(1)

---

### 2. LRU Cache — #146 (Medium)

**Problem**

Design a data structure that follows the Least Recently Used (LRU) cache eviction policy.

Implement the `LRUCache` class:
- `LRUCache(int capacity)` — initialize with positive capacity
- `int get(int key)` — return the value if key exists, else return `-1`. Marks key as most recently used.
- `void put(int key, int value)` — insert or update the key. If at capacity, evict the least recently used key first.

Both operations must run in **O(1)**.

**Example**

```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2],        [1,1], [2,2], [1],   [3,3], [2],   [4,4], [1],   [3],   [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Trace:
LRUCache(2)
put(1,1) → cache: [1]
put(2,2) → cache: [1, 2]  (2 is most recent)
get(1)   → 1, cache: [2, 1]  (1 moved to most recent)
put(3,3) → evict LRU=2, cache: [1, 3]
get(2)   → -1 (evicted)
put(4,4) → evict LRU=1, cache: [3, 4]
get(1)   → -1 (evicted)
get(3)   → 3
get(4)   → 4
```

**Constraints**
- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^4` calls to `get` and `put`

**How LFU applies**: LRU is simpler — you only track recency, not frequency. Think of it as LFU where every key has the same frequency. You only need one doubly linked list + one hash map.

**Key insight**: A doubly linked list maintains order (head = most recent, tail = least recent). The hash map gives O(1) access to any node so you can move it to the head in O(1).

**Hints**
1. Use a doubly linked list with sentinel head/tail nodes to avoid null checks
2. `get`: find node via hash map, move to head, return value
3. `put`: if key exists, update and move to head; if new, add to head and evict tail if over capacity
4. Python shortcut: `OrderedDict` with `move_to_end` and `popitem(last=False)` handles this in ~10 lines

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # mark as most recent
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict LRU (first item)
```

---

### 3. All O`one Data Structure — #432 (Hard)

**Problem**

Design a data structure to store string keys with counts, supporting:
- `inc(key)` — increment count of `key` by 1. If `key` doesn't exist, insert with count 1.
- `dec(key)` — decrement count of `key` by 1. If count reaches 0, remove the key.
- `getMaxKey()` — return any key with the maximum count. Return `""` if empty.
- `getMinKey()` — return any key with the minimum count. Return `""` if empty.

All operations must run in **O(1)** average time.

**Example**

```
Input:
["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
[[],      ["a"],["b"],  [],         [],        ["b"],  [],         []]

Output:
[null, null, null, "a", "a", null, "b", "a"]

Trace:
inc("a") → {a:1}
inc("b") → {a:1, b:1}
getMaxKey() → "a" (or "b", both have count=1)
getMinKey() → "a" (or "b", both have count=1)
inc("b") → {a:1, b:2}
getMaxKey() → "b" (count=2)
getMinKey() → "a" (count=1)
```

**Constraints**
- `1 <= key.length <= 10`
- `key` consists of lowercase English letters
- At most `5 * 10^4` calls to `inc`, `dec`, `getMaxKey`, `getMinKey`
- It's guaranteed that `dec` is called on an existing key

**How LFU applies**: This is essentially LFU's internal structure exposed as an API. You need the same `freq→keys` doubly linked list, but now you also need O(1) access to both the min AND max frequency nodes simultaneously.

**Key insight**: Use a doubly linked list of "count buckets" sorted by count. Each bucket holds a set of keys with that count. Maintain pointers to the head (max) and tail (min) of the list.

```
Bucket list (doubly linked):
[count=1: {a}] ↔ [count=2: {b}] ↔ [count=3: {c}]
     ↑ min                               ↑ max
```

**Hints**
1. Each node in the DLL represents a count value and holds a set of keys with that count
2. `inc(key)`: move key from its current bucket to `bucket.count + 1` (create if needed)
3. `dec(key)`: move key from its current bucket to `bucket.count - 1` (create if needed, remove if count=0)
4. After each move, delete the old bucket if it becomes empty
5. `getMaxKey()` → peek at head bucket's key set; `getMinKey()` → peek at tail bucket's key set

---

### 4. Maximum Frequency Stack — #895 (Hard)

**Problem**

Design a stack-like data structure that pushes and pops elements based on frequency.

Implement the `FreqStack` class:
- `FreqStack()` — construct an empty stack
- `void push(int val)` — push `val` onto the stack
- `int pop()` — remove and return the most frequently occurring element. If there's a tie, remove the element closest to the top of the stack (most recently pushed).

**Example**

```
Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
[[],         [5],   [7],   [5],   [7],   [4],   [5],   [],   [],   [],   []]

Output:
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Trace:
push(5) → freq[5]=1, group[1]=[5]
push(7) → freq[7]=1, group[1]=[5,7]
push(5) → freq[5]=2, group[2]=[5]
push(7) → freq[7]=2, group[2]=[5,7]
push(4) → freq[4]=1, group[1]=[5,7,4]
push(5) → freq[5]=3, group[3]=[5]
          max_freq = 3

pop()   → max_freq=3, group[3]=[5] → pop 5, freq[5]=2, max_freq stays 3? 
          No: group[3] is now empty → max_freq=2
          returns 5

pop()   → max_freq=2, group[2]=[5,7] → pop 7 (most recent), freq[7]=1
          returns 7

pop()   → max_freq=2, group[2]=[5] → pop 5, freq[5]=1, group[2] empty → max_freq=1
          returns 5

pop()   → max_freq=1, group[1]=[5,7,4] → pop 4 (most recent)
          returns 4
```

**Constraints**
- `0 <= val <= 10^9`
- At most `2 * 10^4` calls to `push` and `pop`
- It's guaranteed that `pop` is not called on an empty stack

**How LFU applies**: Same `freq→keys` mapping as LFU, but instead of evicting the LRU item, you pop the most recently pushed item (stack order, not queue order). The key difference from LFU:
- LFU: evict from the **front** of the freq bucket (oldest = LRU)
- FreqStack: pop from the **back** of the freq bucket (newest = most recent push)

**Hints**
1. Two maps: `freq[val]` = how many times val has been pushed; `group[freq]` = list of vals pushed at that frequency
2. Track `max_freq` — it only decreases when `group[max_freq]` becomes empty after a pop
3. `push(val)`: increment `freq[val]`, append to `group[freq[val]]`, update `max_freq`
4. `pop()`: pop last element from `group[max_freq]`, decrement its freq, if group is empty decrement `max_freq`

```python
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)       # val → frequency
        self.group = defaultdict(list)     # freq → stack of vals
        self.max_freq = 0

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
```

---

## Problem Comparison

| Problem | Core Idea | Eviction/Pop Order | Difficulty |
|---------|-----------|-------------------|------------|
| LFU Cache #460 | freq→ordered_keys, evict min freq LRU | min freq, then LRU | Hard |
| LRU Cache #146 | recency only, evict oldest | least recently used | Medium |
| All O`one #432 | freq buckets DLL, O(1) min+max | N/A (inc/dec API) | Hard |
| Max Freq Stack #895 | freq→stack, pop max freq newest | max freq, then LIFO | Hard |
