# Binary Tree

## What is it?
A hierarchical data structure where each node has at most two children (left and right). The topmost node is the root. Nodes with no children are leaves.

## Visual Example
```
        1          ← root
       / \
      2   3
     / \   \
    4   5   6
   /
  7

Inorder  (L→Root→R): 7,4,2,5,1,3,6
Preorder (Root→L→R): 1,2,4,7,5,3,6
Postorder(L→R→Root): 7,4,5,2,6,3,1
Level order:         1,2,3,4,5,6,7

Height = 4 (longest path from root to leaf)
```

## Implementation

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    # ── Traversals ──────────────────────────────────────────────────────────

    def inorder(self, node=None):
        """Left → Root → Right — O(N). Gives sorted order for BST."""
        if node is None and not hasattr(self, '_started'):
            node = self.root
        result = []
        def dfs(n):
            if n:
                dfs(n.left)
                result.append(n.val)
                dfs(n.right)
        dfs(self.root)
        return result

    def preorder(self, node=None):
        """Root → Left → Right — O(N). Used to copy/serialize tree."""
        result = []
        def dfs(n):
            if n:
                result.append(n.val)
                dfs(n.left)
                dfs(n.right)
        dfs(self.root)
        return result

    def postorder(self, node=None):
        """Left → Right → Root — O(N). Used to delete tree."""
        result = []
        def dfs(n):
            if n:
                dfs(n.left)
                dfs(n.right)
                result.append(n.val)
        dfs(self.root)
        return result

    def level_order(self):
        """BFS level by level — O(N). Returns list of levels."""
        if not self.root:
            return []
        result, queue = [], deque([self.root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result

    # ── Properties ──────────────────────────────────────────────────────────

    def height(self, node=None):
        """Max depth from node — O(N)"""
        if node is None:
            node = self.root
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self):
        """Check if height-balanced (|left_h - right_h| <= 1) — O(N)"""
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1: return -1
            right = check(node.right)
            if right == -1: return -1
            if abs(left - right) > 1: return -1
            return 1 + max(left, right)
        return check(self.root) != -1

    def diameter(self):
        """Longest path between any two nodes — O(N)"""
        self._max_diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self._max_diameter = max(self._max_diameter, left + right)
            return 1 + max(left, right)
        depth(self.root)
        return self._max_diameter

    def lowest_common_ancestor(self, root, p, q):
        """LCA of nodes p and q — O(N)"""
        if not root or root == p or root == q:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root  # p and q are in different subtrees
        return left or right

    def max_path_sum(self):
        """Maximum path sum (any path) — O(N)"""
        self._max_sum = float('-inf')
        def gain(node):
            if not node:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            self._max_sum = max(self._max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)
        gain(self.root)
        return self._max_sum
```

## Example Usage
```python
# Build tree:    1
#               / \
#              2   3
#             / \
#            4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

bt = BinaryTree()
bt.root = root

print(bt.inorder())      # [4, 2, 5, 1, 3]
print(bt.preorder())     # [1, 2, 4, 5, 3]
print(bt.level_order())  # [[1], [2, 3], [4, 5]]
print(bt.height())       # 3
print(bt.diameter())     # 3 (path: 4→2→1→3 or 5→2→1→3)
print(bt.is_balanced())  # True
```

## When to Use
- Hierarchical data (file systems, org charts)
- Expression trees (compilers)
- Decision trees (ML)
- Base for BST, heap, trie

## LeetCode Problems

---

### 1. Maximum Depth of Binary Tree — #104 (Easy)

**Problem**: Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root to a leaf).

```
Input:
    3
   / \
  9  20
     / \
    15   7
Output: 3

Input: [1, null, 2]
Output: 2

Input: []
Output: 0
```

**Hints**:
1. `depth(node) = 1 + max(depth(left), depth(right))`
2. Base case: `depth(None) = 0`
3. Alternatively, BFS and count levels

---

### 2. Invert Binary Tree — #226 (Easy)

**Problem**: Given the root of a binary tree, invert the tree (mirror it), and return its root.

```
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**Hints**:
1. Swap left and right children at every node
2. Recursively invert both subtrees
3. `node.left, node.right = invert(node.right), invert(node.left)`

---

### 3. Symmetric Tree — #101 (Easy)

**Problem**: Given the root of a binary tree, check whether it is a mirror of itself (symmetric around its center).

```
Input:
    1
   / \
  2   2
 / \ / \
3  4 4  3
Output: true

Input:
    1
   / \
  2   2
   \   \
    3    3
Output: false
```

**Hints**:
1. A tree is symmetric if its left and right subtrees are mirrors
2. Two trees are mirrors if: their roots are equal, and left.left mirrors right.right, and left.right mirrors right.left
3. Use recursion or BFS with pairs of nodes

---

### 4. Diameter of Binary Tree — #543 (Easy)

**Problem**: Given the root of a binary tree, return the length of the diameter (the longest path between any two nodes — the path may or may not pass through the root). Length = number of edges.

```
Input:
      1
     / \
    2   3
   / \
  4   5
Output: 3
Path: 4 → 2 → 1 → 3  (or 5 → 2 → 1 → 3)

Input: [1, 2]
Output: 1
```

**Hints**:
1. For each node, diameter through it = `depth(left) + depth(right)`
2. Track the global maximum during the depth calculation
3. Return `1 + max(depth(left), depth(right))` from the depth function

---

### 5. Binary Tree Level Order Traversal — #102 (Medium)

**Problem**: Return the level-order traversal of a binary tree's values as a list of lists (each inner list = one level).

```
Input:
    3
   / \
  9  20
     / \
    15   7
Output: [[3], [9, 20], [15, 7]]
```

**Hints**:
1. BFS with a queue; process all nodes at the current level before moving to the next
2. Use `len(queue)` at the start of each level to know how many nodes to process

---

### 6. Binary Tree Right Side View — #199 (Medium)

**Problem**: Given the root of a binary tree, imagine standing on the right side. Return the values of the nodes you can see (one per level, rightmost node).

```
Input:
    1
   / \
  2   3
   \   \
    5   4
Output: [1, 3, 4]

Input: [1, null, 3]
Output: [1, 3]
```

**Hints**:
1. BFS level by level; the last node in each level is visible from the right
2. Alternatively, DFS — visit right child before left, record the first node at each depth

---

### 7. Path Sum II — #113 (Medium)

**Problem**: Given the root of a binary tree and a target sum, return all root-to-leaf paths where the sum of node values equals the target.

```
Input: target = 22
        5
       / \
      4   8
     /   / \
    11  13   4
   /  \     / \
  7    2   5   1

Output: [[5,4,11,2], [5,8,4,5]]
```

**Hints**:
1. DFS with a running path and remaining sum
2. At a leaf, if `remaining == leaf.val`, add the current path to results
3. Backtrack by removing the last element after returning from recursion

---

### 8. Lowest Common Ancestor of a Binary Tree — #236 (Medium)

**Problem**: Given a binary tree and two nodes `p` and `q`, find their lowest common ancestor (LCA) — the deepest node that has both p and q as descendants (a node can be a descendant of itself).

```
Input:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
p=5, q=1 → Output: 3
p=5, q=4 → Output: 5  (5 is an ancestor of 4)
```

**Hints**:
1. If `root` is None, p, or q — return root
2. Recurse left and right
3. If both sides return non-null, current node is the LCA
4. Otherwise return whichever side is non-null

---

### 9. Binary Tree Maximum Path Sum — #124 (Hard)

**Problem**: A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. The path does not need to pass through the root. Return the maximum sum of any path.

```
Input:
    1
   / \
  2   3
Output: 6  (path: 2 → 1 → 3)

Input:
   -10
   /  \
  9   20
      / \
     15   7
Output: 42  (path: 15 → 20 → 7)
```

**Hints**:
1. For each node, the max path through it = `node.val + max(0, left_gain) + max(0, right_gain)`
2. Track the global max across all nodes
3. Return `node.val + max(0, left_gain, right_gain)` upward (can only extend one side)

---

### 10. Serialize and Deserialize Binary Tree — #297 (Hard)

**Problem**: Design an algorithm to serialize a binary tree to a string and deserialize that string back to the tree.

```
Input:
    1
   / \
  2   3
     / \
    4   5

Serialized: "1,2,null,null,3,4,null,null,5,null,null"
Deserialized: same tree structure
```

**Hints**:
1. Preorder DFS: serialize as `val,left,right` with "null" for missing nodes
2. Deserialize by splitting on comma and using a queue/index to consume tokens
3. Alternatively, use BFS (level-order) serialization
