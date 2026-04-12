# Skip List

## What is it?
A probabilistic data structure that allows O(log N) average search, insert, and delete — like a balanced BST but much simpler to implement. It uses **multiple layers of linked lists** where higher layers skip over more elements, acting as "express lanes."

## Visual Example
```
Elements: 1, 3, 5, 7, 9, 12, 15

Level 3: 1 ─────────────────────────── 15
Level 2: 1 ──────── 5 ──────── 9 ───── 15
Level 1: 1 ── 3 ── 5 ── 7 ── 9 ── 12 ─ 15
Level 0: 1 ── 3 ── 5 ── 7 ── 9 ── 12 ─ 15  (base list, all elements)

Search for 9:
  Start at top-left (Level 3, node 1)
  1 < 9, move right → 15 > 9, drop down to Level 2
  Level 2: 1 < 9, move right → 5 < 9, move right → 9 = 9, FOUND!
  
  Only 3 comparisons instead of 7!
```

## Why It Works
```
Each node is promoted to the next level with probability P (usually 0.5).
Expected number of nodes at level k: N * P^k
Expected height: log_{1/P}(N)
Expected search time: O(log N)

The randomness ensures balance without complex rotations.
```

## Implementation

```python
import random

class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)  # pointers for each level

class SkipList:
    """
    Probabilistic sorted data structure.
    O(log N) average for search, insert, delete.
    
    Example:
        sl = SkipList()
        for v in [3, 1, 5, 7, 2]:
            sl.insert(v)
        sl.search(5)   # True
        sl.search(4)   # False
        sl.delete(3)
        sl.to_list()   # [1, 2, 5, 7]
    """
    MAX_LEVEL = 16
    P = 0.5  # probability of promoting to next level

    def __init__(self):
        self.head = SkipNode(float('-inf'), self.MAX_LEVEL)
        self.level = 0  # current max level in use

    def _random_level(self):
        """Generate random level for new node"""
        level = 0
        while random.random() < self.P and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target):
        """O(log N) average"""
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def insert(self, val):
        """O(log N) average"""
        # Find update positions at each level
        update = [None] * (self.MAX_LEVEL + 1)
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr

        new_level = self._random_level()
        # If new level exceeds current, update head pointers
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level

        new_node = SkipNode(val, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, val):
        """O(log N) average"""
        update = [None] * (self.MAX_LEVEL + 1)
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]
        if curr and curr.val == val:
            for i in range(self.level + 1):
                if update[i].forward[i] != curr:
                    break
                update[i].forward[i] = curr.forward[i]
            # Reduce level if top levels are empty
            while self.level > 0 and not self.head.forward[self.level]:
                self.level -= 1

    def to_list(self):
        """Return all elements in sorted order"""
        result = []
        curr = self.head.forward[0]
        while curr:
            result.append(curr.val)
            curr = curr.forward[0]
        return result

    def floor(self, val):
        """Largest element <= val — O(log N)"""
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val <= val:
                curr = curr.forward[i]
        return curr.val if curr != self.head else None

    def ceiling(self, val):
        """Smallest element >= val — O(log N)"""
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr.val if curr else None
```

## Example Usage
```python
sl = SkipList()
for v in [5, 3, 7, 1, 4, 6, 8]:
    sl.insert(v)

print(sl.to_list())    # [1, 3, 4, 5, 6, 7, 8]
print(sl.search(5))    # True
print(sl.search(2))    # False
print(sl.floor(5))     # 5
print(sl.ceiling(5))   # 5
print(sl.floor(4.5))   # 4
print(sl.ceiling(4.5)) # 5

sl.delete(5)
print(sl.to_list())    # [1, 3, 4, 6, 7, 8]
```

## Skip List vs BST

| Feature | Skip List | AVL/RB Tree |
|---------|----------|-------------|
| Implementation | Simple | Complex |
| Balance | Probabilistic | Deterministic |
| Worst case | O(N) (rare) | O(log N) |
| Cache performance | Poor (pointers) | Poor (pointers) |
| Concurrent access | Easier to make lock-free | Harder |
| Used in | Redis ZSet, LevelDB | Java TreeMap |

## Real-World Uses
- **Redis**: Sorted Sets (ZSet) use skip lists
- **LevelDB/RocksDB**: MemTable uses skip list
- **Apache Lucene**: Term dictionary

## LeetCode Problems

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| Design Skiplist (#1206) | Hard | Direct implementation |
| My Calendar I (#729) | Medium | Sorted structure |
| Count of Smaller Numbers After Self (#315) | Hard | Sorted structure |
