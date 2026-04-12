# Doubly Linked List

## What is it?
A linked list where each node has pointers to both the **next** and **previous** nodes. This allows O(1) deletion of any node (given a reference to it) and O(1) insertion at both ends.

## Visual Example
```
None ← [1] ⇄ [2] ⇄ [3] ⇄ [4] → None
        ^head                ^tail

With sentinel nodes (simplifies edge cases):
[dummy_head] ⇄ [1] ⇄ [2] ⇄ [3] ⇄ [dummy_tail]

Insert after [2]:
[dummy_head] ⇄ [1] ⇄ [2] ⇄ [NEW] ⇄ [3] ⇄ [dummy_tail]

Remove [2]:
[dummy_head] ⇄ [1] ⇄ [3] ⇄ [dummy_tail]
(just update prev/next pointers — O(1) with node reference)
```

## Implementation

```python
class DNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None
        self.key = None  # used in LRU cache

class DoublyLinkedList:
    """
    Doubly linked list with sentinel head and tail.
    Sentinel nodes eliminate null checks for edge cases.
    """
    def __init__(self):
        self.head = DNode()  # dummy head (most recent end)
        self.tail = DNode()  # dummy tail (least recent end)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _insert_after(self, node, new_node):
        """Insert new_node immediately after node — O(1)"""
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def _remove(self, node):
        """Remove node from list — O(1) given node reference"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def append_front(self, val):
        """Add to front (after dummy head) — O(1)"""
        self._insert_after(self.head, DNode(val))

    def append_back(self, val):
        """Add to back (before dummy tail) — O(1)"""
        self._insert_after(self.tail.prev, DNode(val))

    def pop_front(self):
        """Remove and return front value — O(1)"""
        if self.size == 0:
            raise IndexError("Empty list")
        return self._remove(self.head.next).val

    def pop_back(self):
        """Remove and return back value — O(1)"""
        if self.size == 0:
            raise IndexError("Empty list")
        return self._remove(self.tail.prev).val

    def move_to_front(self, node):
        """Move existing node to front — O(1)"""
        self._remove(node)
        self._insert_after(self.head, node)
        self.size += 1  # _remove decremented, re-increment

    def __len__(self):
        return self.size

    def to_list(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.val)
            curr = curr.next
        return result
```

## Example Usage
```python
dll = DoublyLinkedList()
dll.append_back(1)
dll.append_back(2)
dll.append_back(3)
dll.append_front(0)
print(dll.to_list())   # [0, 1, 2, 3]

dll.pop_front()
print(dll.to_list())   # [1, 2, 3]

dll.pop_back()
print(dll.to_list())   # [1, 2]
print(len(dll))        # 2
```

## When to Use
- LRU Cache (O(1) move-to-front + O(1) remove-from-back)
- Browser history (forward/backward navigation)
- Text editor cursor movement
- Any situation needing O(1) deletion with node reference

## LeetCode Problems

---

### 1. LRU Cache — #146 (Medium)

**Problem**: Design a data structure that follows the Least Recently Used (LRU) cache eviction policy. Implement `get(key)` and `put(key, value)`, both in O(1).

```
Input:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],       [1,1],[2,2],[1],  [3,3],[2],  [4,4],[1],  [3],  [4]]

Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Trace (capacity=2):
put(1,1) → cache: {1:1}
put(2,2) → cache: {1:1, 2:2}
get(1)   → 1, moves 1 to most-recent: order [2,1]
put(3,3) → evict LRU=2, cache: {1:1, 3:3}
get(2)   → -1 (evicted)
put(4,4) → evict LRU=1, cache: {3:3, 4:4}
get(1)   → -1 (evicted)
get(3)   → 3
get(4)   → 4
```

**Hints**:
1. Hash map gives O(1) lookup; doubly linked list gives O(1) move-to-front and eviction
2. Use sentinel head/tail nodes to avoid null checks
3. Python shortcut: `OrderedDict` with `move_to_end` and `popitem(last=False)`

---

### 2. LFU Cache — #460 (Hard)

**Problem**: Design a data structure that follows the Least Frequently Used (LFU) cache eviction policy. Ties broken by LRU. Both `get` and `put` must be O(1).

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
2. Track `min_freq` — resets to 1 on every new insert
3. When a bucket empties and it was `min_freq`, increment `min_freq`

---

### 3. Design Linked List — #707 (Medium)

**Problem**: Design a linked list supporting: `get(index)`, `addAtHead(val)`, `addAtTail(val)`, `addAtIndex(index, val)`, `deleteAtIndex(index)`.

```
Input:
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],            [1],        [3],        [1,2],       [1],  [1],            [1]]

Output: [null, null, null, null, 2, null, 3]

Trace:
addAtHead(1) → list: 1
addAtTail(3) → list: 1 → 3
addAtIndex(1, 2) → list: 1 → 2 → 3
get(1) → 2
deleteAtIndex(1) → list: 1 → 3
get(1) → 3
```

**Hints**:
1. Use a dummy head node to simplify index-0 operations
2. For `addAtIndex(index, val)`: traverse to node at `index-1`, insert after it
3. Maintain a `size` counter to validate indices

---

### 4. Flatten a Multilevel Doubly Linked List — #430 (Medium)

**Problem**: A doubly linked list where some nodes have a `child` pointer to another doubly linked list. Flatten it so all nodes appear in a single-level list (depth-first order).

```
Input:
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5 ⇄ 6
        |
        7 ⇄ 8 ⇄ 9 ⇄ 10
                |
                11 ⇄ 12

Output: 1 ⇄ 2 ⇄ 3 ⇄ 7 ⇄ 8 ⇄ 11 ⇄ 12 ⇄ 9 ⇄ 10 ⇄ 4 ⇄ 5 ⇄ 6
```

**Hints**:
1. When you encounter a node with a child, insert the child list between current and current.next
2. Find the tail of the child list first, then reconnect pointers
3. Alternatively, use a stack to simulate DFS

---

### 5. All O`one Data Structure — #432 (Hard)

**Problem**: Design a data structure with O(1) `inc(key)`, `dec(key)`, `getMaxKey()`, `getMinKey()`.

```
Input:
["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
[[],      ["a"],["b"],[],         [],         ["b"],[],         []]

Output: [null, null, null, "a", "a", null, "b", "a"]

Trace:
inc("a") → {a:1}
inc("b") → {a:1, b:1}
getMaxKey() → "a" (or "b", both count=1)
getMinKey() → "a" (or "b")
inc("b") → {a:1, b:2}
getMaxKey() → "b" (count=2)
getMinKey() → "a" (count=1)
```

**Hints**:
1. Use a doubly linked list of count-buckets sorted by count
2. Each bucket holds a set of keys with that count
3. Head = max bucket, tail = min bucket — both accessible in O(1)

---

### 6. Design Browser History — #1472 (Medium)

**Problem**: Implement browser history with `visit(url)`, `back(steps)`, `forward(steps)`.

```
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Trace:
Start at "leetcode.com"
visit("google.com")   → history: leetcode → google (current)
visit("facebook.com") → history: leetcode → google → facebook (current)
visit("youtube.com")  → history: leetcode → google → facebook → youtube (current)
back(1)  → "facebook.com"
back(1)  → "google.com"
forward(1) → "facebook.com"
visit("linkedin.com") → clears forward history: leetcode → google → facebook → linkedin
forward(2) → "linkedin.com" (can't go forward, stay)
back(2)  → "google.com"
back(7)  → "leetcode.com" (can't go back more than available)
```

**Hints**:
1. Use a doubly linked list — current node is the "present"
2. `visit`: create new node after current, clear forward history
3. `back`/`forward`: move current pointer, clamped to list boundaries
