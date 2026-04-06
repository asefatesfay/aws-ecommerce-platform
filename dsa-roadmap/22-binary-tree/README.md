# Binary Tree

Binary trees are hierarchical structures where each node has at most two children. Most tree problems reduce to a traversal (BFS or DFS) combined with some computation at each node.

## Core Traversals

- **Inorder (Left → Root → Right):** Produces sorted output for BSTs.
- **Preorder (Root → Left → Right):** Useful for serialization and copying.
- **Postorder (Left → Right → Root):** Useful when you need children's results before the parent.
- **Level-order (BFS):** Process nodes level by level using a queue.

## Key Patterns

### DFS with Return Values
Many problems ask you to compute something at each node using results from children. Return a value from each recursive call and combine at the parent.

```
def dfs(node):
    if not node: return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right, node.val)
```

### BFS Level-by-Level
Use a queue. At each level, snapshot the queue size first, then process exactly that many nodes.

```
queue = deque([root])
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        # process node
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

### Path Problems
For root-to-leaf paths, carry a running value down. For any-path problems (like path sum III), use prefix sums or a global variable updated during DFS.

### Tree Construction
Given two traversals (e.g., preorder + inorder), the first element of preorder is always the root. Find it in inorder to split left/right subtrees.

## When to Use BFS vs DFS

- **BFS:** Level-order output, minimum depth, right side view, anything "level-by-level"
- **DFS:** Path sums, tree height, subtree checks, serialization, anything requiring full subtree info

## Common Techniques

- **Null checks first:** Always handle `node is None` as the base case
- **Global variable trick:** For problems where the answer spans across the root (like diameter, max path sum), use a nonlocal/global variable updated during DFS
- **Morris traversal:** O(1) space inorder traversal (advanced)
- **Euler tour / flattening:** Convert tree to array for range queries

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Maximum Depth of Binary Tree](./maximum-depth-of-binary-tree.md) | Easy |
| [Average of Levels in Binary Tree](./average-of-levels-in-binary-tree.md) | Easy |
| [Binary Tree Level Order Traversal](./binary-tree-level-order-traversal.md) | Medium |
| [Binary Tree Right Side View](./binary-tree-right-side-view.md) | Medium |
| [Binary Tree Zigzag Level Order Traversal](./binary-tree-zigzag-level-order-traversal.md) | Medium |
| [Maximum Width of Binary Tree](./maximum-width-of-binary-tree.md) | Medium |
| [Check Completeness of a Binary Tree](./check-completeness-of-a-binary-tree.md) | Medium |
| [Binary Tree Preorder Traversal](./binary-tree-preorder-traversal.md) | Easy |
| [Same Tree](./same-tree.md) | Easy |
| [Symmetric Tree](./symmetric-tree.md) | Easy |
| [Binary Tree Paths](./binary-tree-paths.md) | Easy |
| [Convert Sorted Array to Binary Search Tree](./convert-sorted-array-to-binary-search-tree.md) | Easy |
| [Count Complete Tree Nodes](./count-complete-tree-nodes.md) | Easy |
| [Sum of Left Leaves](./sum-of-left-leaves.md) | Easy |
| [Subtree of Another Tree](./subtree-of-another-tree.md) | Easy |
| [Path Sum II](./path-sum-ii.md) | Medium |
| [Path Sum III](./path-sum-iii.md) | Medium |
| [Longest Univalue Path](./longest-univalue-path.md) | Medium |
| [Maximum Difference Between Node and Ancestor](./maximum-difference-between-node-and-ancestor.md) | Medium |
| [Construct Binary Tree from Preorder and Inorder Traversal](./construct-binary-tree-from-preorder-and-inorder-traversal.md) | Medium |
| [Construct Binary Tree from Inorder and Postorder Traversal](./construct-binary-tree-from-inorder-and-postorder-traversal.md) | Medium |
| [Serialize and Deserialize Binary Tree](./serialize-and-deserialize-binary-tree.md) | Hard |
| [Binary Tree Inorder Traversal](./binary-tree-inorder-traversal.md) | Easy |
| [Minimum Distance Between BST Nodes](./minimum-distance-between-bst-nodes.md) | Easy |
| [Validate Binary Search Tree](./validate-binary-search-tree.md) | Medium |
| [Kth Smallest Element in a BST](./kth-smallest-element-in-a-bst.md) | Medium |
| [Binary Search Tree Iterator](./binary-search-tree-iterator.md) | Medium |
| [Binary Tree Postorder Traversal](./binary-tree-postorder-traversal.md) | Easy |
| [Invert Binary Tree](./invert-binary-tree.md) | Easy |
| [Diameter of Binary Tree](./diameter-of-binary-tree.md) | Easy |
| [Balanced Binary Tree](./balanced-binary-tree.md) | Easy |
| [Delete Nodes and Return Forest](./delete-nodes-and-return-forest.md) | Medium |
| [Lowest Common Ancestor of a Binary Tree](./lowest-common-ancestor-of-a-binary-tree.md) | Medium |
| [Find Duplicate Subtrees](./find-duplicate-subtrees.md) | Medium |
| [Flatten Binary Tree to Linked List](./flatten-binary-tree-to-linked-list.md) | Medium |
| [Distribute Coins in Binary Tree](./distribute-coins-in-binary-tree.md) | Medium |
| [Count Good Nodes in Binary Tree](./count-good-nodes-in-binary-tree.md) | Medium |
| [Sum Root to Leaf Numbers](./sum-root-to-leaf-numbers.md) | Medium |
| [Binary Tree Maximum Path Sum](./binary-tree-maximum-path-sum.md) | Hard |
