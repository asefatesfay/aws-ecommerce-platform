# Treap

## What is it?
A **randomized BST** that combines a **tree** (BST property on keys) with a **heap** (heap property on random priorities). The random priorities ensure the tree stays balanced with high probability, giving O(log N) expected time for all operations — without the complex rotation logic of AVL or Red-Black trees.

## Visual Example
```
Each node has: (key, priority)
BST property: keys ordered left < root < right
Heap property: parent priority > children priorities

Insert (3,91), (1,73), (4,65), (1,58), (5,97), (9,26), (2,53):

After all insertions (max-heap on priority):
         (5,97)
        /      \
     (3,91)   (9,26)
     /    \
  (1,73) (4,65)
      \
     (2,53)

BST check: 1<3<5, 4<5, 9>5 ✓
Heap check: 97>91>73>53, 97>26 ✓
```

## Why Random Priorities Work
```
With random priorities, the expected height is O(log N).
The probability that any node becomes the root is 1/N.
This gives the same distribution as a random BST,
which has expected height O(log N).

No need for complex rebalancing — just maintain heap property
through rotations when inserting/deleting.
```

## Implementation

```python
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()  # random priority
        self.left = None
        self.right = None
        self.size = 1  # subtree size for order statistics

class Treap:
    """
    Randomized BST with O(log N) expected time for all operations.
    Simpler than AVL/RB trees, supports split/merge efficiently.
    
    Example:
        t = Treap()
        for v in [5, 3, 7, 1, 4, 6, 8]:
            t.insert(v)
        t.inorder()  # [1, 3, 4, 5, 6, 7, 8]
        t.kth_smallest(3)  # 4 (3rd smallest)
    """
    def __init__(self):
        self.root = None

    def _size(self, node):
        return node.size if node else 0

    def _update(self, node):
        if node:
            node.size = 1 + self._size(node.left) + self._size(node.right)

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update(x)
        self._update(y)
        return y

    def _insert(self, node, key):
        if not node:
            return TreapNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert(node.right, key)
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        self._update(node)
        return node

    def insert(self, key):
        """O(log N) expected"""
        self.root = self._insert(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Rotate down until leaf, then remove
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            if node.left.priority > node.right.priority:
                node = self._rotate_right(node)
                node.right = self._delete(node.right, key)
            else:
                node = self._rotate_left(node)
                node.left = self._delete(node.left, key)
        self._update(node)
        return node

    def delete(self, key):
        """O(log N) expected"""
        self.root = self._delete(self.root, key)

    def search(self, key):
        """O(log N) expected"""
        node = self.root
        while node:
            if key == node.key: return True
            node = node.left if key < node.key else node.right
        return False

    def kth_smallest(self, k):
        """Find k-th smallest element (1-indexed) — O(log N) expected"""
        node = self.root
        while node:
            left_size = self._size(node.left)
            if k == left_size + 1:
                return node.key
            elif k <= left_size:
                node = node.left
            else:
                k -= left_size + 1
                node = node.right
        return None

    def rank(self, key):
        """Count elements less than key — O(log N) expected"""
        count = 0
        node = self.root
        while node:
            if key <= node.key:
                node = node.left
            else:
                count += 1 + self._size(node.left)
                node = node.right
        return count

    def inorder(self):
        result = []
        def dfs(n):
            if n:
                dfs(n.left)
                result.append(n.key)
                dfs(n.right)
        dfs(self.root)
        return result
```

## Example Usage
```python
t = Treap()
for v in [5, 3, 7, 1, 4, 6, 8]:
    t.insert(v)

print(t.inorder())          # [1, 3, 4, 5, 6, 7, 8]
print(t.kth_smallest(3))    # 4
print(t.rank(5))            # 3 (three elements less than 5: 1,3,4)
print(t.search(6))          # True
t.delete(5)
print(t.inorder())          # [1, 3, 4, 6, 7, 8]
```

## Treap vs AVL vs Red-Black

| Feature | Treap | AVL | Red-Black |
|---------|-------|-----|-----------|
| Balance | Probabilistic | Deterministic | Deterministic |
| Implementation | Simple | Complex | Very complex |
| Worst case | O(N) (rare) | O(log N) | O(log N) |
| Split/Merge | O(log N) | Hard | Hard |
| Use case | Competitive programming | Read-heavy | Write-heavy |

## When to Use
- Competitive programming (simpler than AVL/RB)
- When you need split/merge operations
- Order statistics (k-th element, rank)
- When probabilistic guarantees are acceptable

## LeetCode Problems

---

### 1. Count of Smaller Numbers After Self — #315 (Hard)

**Problem**: Given an integer array, return a count array where `count[i]` is the number of elements to the right of `nums[i]` that are smaller than `nums[i]`.

```
Input:  [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Explanation:
5: [2,1] are smaller to the right → 2
2: [1] is smaller to the right → 1
6: [1] is smaller to the right → 1
1: nothing to the right → 0
```

**Treap connection**: Process from right to left. Insert each element into a treap. Use `rank(num)` to count how many elements already in the treap are smaller.

**Hints**:
1. Process right to left; for each element, query how many inserted elements are smaller
2. Use treap's `rank(key)` = count of elements less than key
3. In Python, use `SortedList` from `sortedcontainers` for the same effect

---

### 2. Kth Largest Element in a Stream — #703 (Easy)

**Problem**: Design a class that finds the kth largest element in a stream. `add(val)` adds a new value and returns the kth largest.

```
Input:
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

Output: [null, 4, 5, 5, 8, 8]

Trace (k=3, initial=[4,5,8,2]):
Initial sorted: [2,4,5,8], 3rd largest = 4
add(3) → [2,3,4,5,8], 3rd largest = 4
add(5) → [2,3,4,5,5,8], 3rd largest = 5
add(10)→ 3rd largest = 5
add(9) → 3rd largest = 8
add(4) → 3rd largest = 8
```

**Treap connection**: A treap with order statistics can answer "kth largest" in O(log N). In practice, a min-heap of size k is simpler.

**Hints**:
1. Maintain a min-heap of size k
2. On `add`: push to heap, pop if size > k
3. `heap[0]` is always the kth largest

---

### 3. My Calendar I — #729 (Medium)

**Problem**: Implement a calendar where you can book events `[start, end)`. A booking is successful if it doesn't overlap with any existing booking.

```
Input:
["MyCalendar","book","book","book"]
[[],          [10,20],[15,25],[20,30]]

Output: [null, true, false, true]

Trace:
book(10,20) → no conflicts → true
book(15,25) → overlaps [10,20] → false
book(20,30) → no overlap → true
```

**Treap connection**: A treap (or any sorted BST) can store booked intervals sorted by start time, enabling O(log N) overlap checks.

**Hints**:
1. Store intervals sorted by start time
2. For new `[s, e)`: find the largest start ≤ s and check if it ends after s; find the smallest start > s and check if it starts before e
3. In Python, use `SortedList` for O(log N) insert and neighbor lookup
