# Red-Black Tree

## What is it?
A self-balancing BST where each node is colored **red or black**. Less strictly balanced than AVL trees — allows up to 2x height difference — but requires fewer rotations on insert/delete, making it faster for write-heavy workloads.

## Red-Black Properties
```
1. Every node is RED or BLACK
2. Root is BLACK
3. Every leaf (NULL) is BLACK
4. If a node is RED, both children are BLACK (no two consecutive reds)
5. All paths from any node to its descendant NULL leaves have the same number of BLACK nodes (black-height)

These rules guarantee: height ≤ 2 * log(N+1)
```

## Visual Example
```
Insert 7, 3, 18, 10, 22, 8, 11, 26:

        7(B)
       /    \
     3(B)   18(R)
            /   \
          10(B) 22(B)
          / \     \
        8(R) 11(R) 26(R)

Black-height = 2 for all paths ✓
No consecutive reds ✓
```

## Rotations and Recoloring
```
When inserting a RED node causes a violation:

Case 1: Uncle is RED → recolor parent, uncle to BLACK, grandparent to RED
Case 2: Uncle is BLACK, node is inner child → rotate parent
Case 3: Uncle is BLACK, node is outer child → rotate grandparent + recolor
```

## Implementation

```python
class RBNode:
    RED = True
    BLACK = False

    def __init__(self, val):
        self.val = val
        self.color = RBNode.RED  # new nodes are always red
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """
    Red-Black Tree with O(log N) guaranteed insert, delete, search.
    Used in: Python's sortedcontainers, Java TreeMap, Linux CFS scheduler.
    
    Note: Full implementation is complex. This shows the core structure
    and key operations. In practice, use sortedcontainers.SortedList.
    """
    def __init__(self):
        self.NIL = RBNode(None)   # sentinel NIL node
        self.NIL.color = RBNode.BLACK
        self.root = self.NIL

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, val):
        """O(log N)"""
        node = RBNode(val)
        node.left = node.right = self.NIL

        # Standard BST insert
        parent = None
        curr = self.root
        while curr != self.NIL:
            parent = curr
            if node.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        # Fix red-black violations
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == RBNode.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RBNode.RED:
                    # Case 1: uncle is red → recolor
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: node is right child → rotate left
                        node = node.parent
                        self._rotate_left(node)
                    # Case 3: node is left child → rotate right
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._rotate_right(node.parent.parent)
            else:
                # Mirror cases (parent is right child)
                uncle = node.parent.parent.left
                if uncle.color == RBNode.RED:
                    node.parent.color = RBNode.BLACK
                    uncle.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = RBNode.BLACK
                    node.parent.parent.color = RBNode.RED
                    self._rotate_left(node.parent.parent)
        self.root.color = RBNode.BLACK

    def search(self, val):
        """O(log N)"""
        curr = self.root
        while curr != self.NIL:
            if val == curr.val: return True
            curr = curr.left if val < curr.val else curr.right
        return False

    def inorder(self):
        result = []
        def dfs(node):
            if node != self.NIL:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)
        dfs(self.root)
        return result


# In practice, use Python's sortedcontainers (backed by sorted list of lists)
from sortedcontainers import SortedList

sl = SortedList([3, 1, 4, 1, 5, 9])
sl.add(2)
print(sl)           # SortedList([1, 1, 2, 3, 4, 5, 9])
print(sl[0])        # 1 (minimum)
print(sl[-1])       # 9 (maximum)
sl.remove(4)
print(sl.bisect_left(3))  # index of first element >= 3
```

## Real-World Uses
- **Linux kernel**: Completely Fair Scheduler (CFS) uses RB tree for process scheduling
- **Java**: `TreeMap`, `TreeSet`
- **C++ STL**: `std::map`, `std::set`
- **Python**: `sortedcontainers.SortedList` (approximation)
- **Nginx**: timer management

## When to Use
- Need sorted order + O(log N) insert/delete/search
- Write-heavy workloads (fewer rotations than AVL)
- When you need `floor()`, `ceiling()`, `rank()` operations

## LeetCode Problems

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| My Calendar I (#729) | Medium | Sorted set / interval tree |
| My Calendar II (#731) | Medium | Sorted set |
| Count of Smaller Numbers After Self (#315) | Hard | Sorted structure |
| Sliding Window Median (#480) | Hard | Two sorted sets |
| Find K-th Smallest Pair Distance (#719) | Hard | Sorted structure |
