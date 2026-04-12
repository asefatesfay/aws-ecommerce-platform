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

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| Maximum Depth of Binary Tree (#104) | Easy | DFS height |
| Invert Binary Tree (#226) | Easy | Recursive swap |
| Symmetric Tree (#101) | Easy | Mirror check |
| Diameter of Binary Tree (#543) | Easy | Max left+right depth |
| Balanced Binary Tree (#110) | Easy | Height with -1 sentinel |
| Binary Tree Level Order Traversal (#102) | Medium | BFS |
| Binary Tree Right Side View (#199) | Medium | BFS last of each level |
| Path Sum II (#113) | Medium | DFS with path tracking |
| Path Sum III (#437) | Medium | Prefix sum + DFS |
| Lowest Common Ancestor (#236) | Medium | Post-order DFS |
| Binary Tree Maximum Path Sum (#124) | Hard | Post-order, max gain |
| Serialize and Deserialize Binary Tree (#297) | Hard | BFS/DFS encoding |
| Construct Tree from Preorder+Inorder (#105) | Medium | Divide and conquer |
