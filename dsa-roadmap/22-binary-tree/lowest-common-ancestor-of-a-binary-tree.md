# Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium
**Pattern:** DFS / LCA
**LeetCode:** #236

## Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q`. The LCA is defined as the lowest node in the tree that has both `p` and `q` as descendants (a node can be a descendant of itself).

## Examples

### Example 1
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`
**Output:** `3`
**Explanation:** Node 3 is the LCA of 5 and 1.

### Example 2
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 4`
**Output:** `5`
**Explanation:** Node 5 is the LCA of 5 and 4 (5 is an ancestor of itself).

## Constraints
- The number of nodes in the tree is in the range `[2, 10^5]`
- All node values are unique
- `p != q`
- Both `p` and `q` exist in the tree

## Hints

> 💡 **Hint 1:** The LCA is the first node where p and q "split" — one is in the left subtree and one is in the right. Or the node itself is p or q (since a node is its own ancestor).

> 💡 **Hint 2:** DFS: if the current node is null, p, or q — return it. Recurse left and right. If both return non-null, the current node is the LCA. If only one returns non-null, that's the LCA.

> 💡 **Hint 3:** The logic: `left = lca(root.left, p, q)`, `right = lca(root.right, p, q)`. If both are non-null, return root. Otherwise return whichever is non-null (or null if both are null).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS returning the LCA candidate. If both subtrees return non-null results, the current node is the LCA. Otherwise propagate the non-null result upward.
