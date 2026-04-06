# Binary Tree Preorder Traversal

**Difficulty:** Easy
**Pattern:** DFS / Tree Traversal
**LeetCode:** #144

## Problem Statement

Given the root of a binary tree, return the preorder traversal of its nodes' values. Preorder visits: Root → Left → Right.

## Examples

### Example 1
**Input:** `root = [1,null,2,3]`
**Output:** `[1,2,3]`
**Explanation:** Visit root (1), then right subtree root (2), then its left child (3).

### Example 2
**Input:** `root = []`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Recursive solution: append root.val, recurse left, recurse right. Base case: null node returns nothing.

> 💡 **Hint 2:** Iterative solution: use a stack. Push root. While stack is non-empty: pop a node, append its value, push right child then left child (right first so left is processed first).

> 💡 **Hint 3:** The iterative approach pushes right before left because a stack is LIFO — pushing right first means left gets popped and processed first, maintaining the Root → Left → Right order.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is the height of the tree

Recursive DFS: visit root, recurse left, recurse right. Iterative: stack-based with right-before-left push order.
