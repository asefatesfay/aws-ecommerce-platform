# Validate Binary Search Tree

**Difficulty:** Medium
**Pattern:** DFS with Bounds
**LeetCode:** #98

## Problem Statement

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: the left subtree of a node contains only nodes with keys less than the node's key; the right subtree contains only nodes with keys greater than the node's key; both the left and right subtrees must also be BSTs.

## Examples

### Example 1
**Input:** `root = [2,1,3]`
**Output:** `true`

### Example 2
**Input:** `root = [5,1,4,null,null,3,6]`
**Output:** `false`
**Explanation:** Node 4 is in the right subtree of 5, but 4 < 5. Also, node 3 is in the right subtree of 4 but 3 < 4.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Don't just check that each node is greater than its left child and less than its right child — that's not sufficient. The node [5,1,4,null,null,3,6] fails because 3 is in the right subtree of 5 but 3 < 5.

> 💡 **Hint 2:** Pass valid bounds `(min_val, max_val)` down through the recursion. Every node must satisfy `min_val < node.val < max_val`. When going left, update the upper bound to `node.val`. When going right, update the lower bound.

> 💡 **Hint 3:** Initialize with `(-infinity, +infinity)`. For the left child of node with value 5: bounds become `(-inf, 5)`. For the right child: bounds become `(5, +inf)`. Use `float('-inf')` and `float('inf')` to handle edge cases.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS with valid range `(min, max)` passed down. Each node must be strictly within its range. Going left tightens the upper bound; going right tightens the lower bound.
