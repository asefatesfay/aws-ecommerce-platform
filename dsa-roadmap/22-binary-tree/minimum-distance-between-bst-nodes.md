# Minimum Distance Between BST Nodes

**Difficulty:** Easy
**Pattern:** BST Inorder Traversal
**LeetCode:** #783

## Problem Statement

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

## Examples

### Example 1
**Input:** `root = [4,2,6,1,3]`
**Output:** `1`
**Explanation:** Inorder: [1,2,3,4,6]. Minimum difference is |2-1| = 1.

### Example 2
**Input:** `root = [1,0,48,null,null,12,49]`
**Output:** `1`

## Constraints
- The number of nodes in the tree is in the range `[2, 100]`
- `0 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** In a BST, inorder traversal produces values in sorted order. The minimum difference between any two nodes must be between adjacent values in the sorted sequence.

> 💡 **Hint 2:** Do an inorder traversal and track the previous node's value. At each node, compute `current.val - prev_val` and update the minimum.

> 💡 **Hint 3:** Initialize `prev = -infinity` and `min_diff = infinity`. During inorder traversal, update `min_diff = min(min_diff, node.val - prev)`, then set `prev = node.val`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

Inorder traversal of the BST produces sorted values. Track the previous value and compute differences between consecutive nodes to find the minimum.
