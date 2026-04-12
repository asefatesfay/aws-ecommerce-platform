# AVL Tree

## What is it?
A **self-balancing Binary Search Tree** where the height difference between left and right subtrees (balance factor) is at most 1 for every node. Named after Adelson-Velsky and Landis (1962). Guarantees O(log N) for all operations in the **worst case** — unlike a plain BST which degrades to O(N) on sorted input.

## Visual Example
```
Insert 1, 2, 3 into a plain BST:
1
 \
  2       ← unbalanced! height=3, looks like a linked list
   \
    3

AVL detects imbalance at node 1 (balance factor = -2):
Perform LEFT ROTATION at node 1:
    2
   / \
  1   3   ← balanced! height=2

Insert 4, 5:
    2
   / \
  1   3
       \
        4
         \
          5   ← imbalance at node 3 (bf=-2), left rotate:
    2
   / \
  1   4
     / \
    3   5   ← balanced!
```

## Balance Factor
```
balance_factor(node) = height(left) - height(right)

-1, 0, +1 → balanced
-2 or +2  → needs rotation

4 rotation types:
1. Left-Left (LL):   right rotation
2. Right-Right (RR): left rotation
3. Left-Right (LR):  left rotate left child, then right rotate
4. Right-Left (RL):  right rotate right child, then left rotate
```

## Implementation

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # height of subtree rooted here

class AVLTree:
    """
    Self-balancing BST with O(log N) guaranteed for all operations.
    
    Example:
        avl = AVLTree()
        for v in [3, 1, 4, 1, 5, 9, 2, 6]:
            avl.insert(v)
        avl.inorder()  # sorted order
    """
    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        """Right rotation around y — O(1)"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x  # new root

    def _rotate_left(self, x):
        """Left rotation around x — O(1)"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y  # new root

    def _rebalance(self, node):
        """Rebalance node if needed — O(1)"""
        self._update_height(node)
        bf = self._balance_factor(node)

        # Left-Left: right rotate
        if bf > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)

        # Left-Right: left rotate left child, then right rotate
        if bf > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Right: left rotate
        if bf < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)

        # Right-Left: right rotate right child, then left rotate
        if bf < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # already balanced

    def insert(self, val):
        """O(log N)"""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # duplicate, ignore
        return self._rebalance(node)

    def delete(self, val):
        """O(log N)"""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Find inorder successor (smallest in right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return self._rebalance(node)

    def search(self, val):
        """O(log N)"""
        node = self.root
        while node:
            if val == node.val: return True
            node = node.left if val < node.val else node.right
        return False

    def inorder(self):
        result = []
        def dfs(n):
            if n:
                dfs(n.left)
                result.append(n.val)
                dfs(n.right)
        dfs(self.root)
        return result

    def __init__(self):
        self.root = None
```

## AVL vs Red-Black Tree

| Feature | AVL Tree | Red-Black Tree |
|---------|---------|----------------|
| Balance | Stricter (height diff ≤ 1) | Looser (2x height) |
| Search | Faster (shorter tree) | Slightly slower |
| Insert/Delete | More rotations | Fewer rotations |
| Best for | Read-heavy workloads | Write-heavy workloads |
| Used in | Databases (read-heavy) | Linux kernel, Java TreeMap |

## When to Use
- When you need guaranteed O(log N) BST operations
- Read-heavy workloads where search speed matters
- Understanding self-balancing concepts for interviews

## LeetCode Problems

---

### 1. Balance a Binary Search Tree — #1382 (Medium)

**Problem**: Given the root of a BST, return a balanced BST with the same node values. A balanced BST has a height difference of at most 1 between left and right subtrees for every node.

```
Input:
1
 \
  2
   \
    3
     \
      4
Output (one valid answer):
    2
   / \
  1   3
       \
        4
Or:
    3
   / \
  2   4
 /
1
```

**Hints**:
1. Inorder traversal of a BST gives a sorted array
2. Build a balanced BST from a sorted array: pick the middle element as root, recurse on left and right halves
3. This is exactly what AVL tree insertion achieves automatically

---

### 2. Count of Smaller Numbers After Self — #315 (Hard)

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

**Hints**:
1. Process from right to left; maintain a sorted structure (AVL/BST/BIT)
2. For each element, query how many elements already inserted are smaller
3. Then insert the current element
4. In Python, use `SortedList` from `sortedcontainers` for O(log N) insert and rank queries

---

### 3. Kth Largest Element in a Stream — #703 (Easy)

**Problem**: Design a class that finds the kth largest element in a stream. Initialize with k and an initial array. `add(val)` adds a new value and returns the kth largest.

```
Input:
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

Output: [null, 4, 5, 5, 8, 8]

Trace (k=3, initial=[4,5,8,2]):
Sorted: [2,4,5,8], 3rd largest = 4
add(3) → [2,3,4,5,8], 3rd largest = 4
add(5) → [2,3,4,5,5,8], 3rd largest = 5
add(10)→ [2,3,4,5,5,8,10], 3rd largest = 5
add(9) → [2,3,4,5,5,8,9,10], 3rd largest = 8
add(4) → [2,3,4,4,5,5,8,9,10], 3rd largest = 8
```

**Hints**:
1. Maintain a min-heap of size k
2. The root of the heap is always the kth largest element
3. On `add`: push to heap, pop if size > k; return `heap[0]`
