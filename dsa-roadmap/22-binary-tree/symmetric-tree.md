# Symmetric Tree

**Difficulty:** Easy
**Pattern:** DFS / Tree Comparison
**LeetCode:** #101

## Problem Statement

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Examples

### Example 1
**Input:** `root = [1,2,2,3,4,4,3]`
**Output:** `true`
**Explanation:** The tree is symmetric: left subtree mirrors right subtree.

### Example 2
**Input:** `root = [1,2,2,null,3,null,3]`
**Output:** `false`
**Explanation:** The right child of the left 2 is 3, but the left child of the right 2 is null — not a mirror.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** A tree is symmetric if its left subtree is a mirror of its right subtree. Write a helper `isMirror(left, right)` that checks if two subtrees are mirrors of each other.

> 💡 **Hint 2:** Two subtrees are mirrors if: both are null (True), one is null (False), their root values are equal AND `isMirror(left.left, right.right)` AND `isMirror(left.right, right.left)`. Notice the cross-comparison: left's left with right's right.

> 💡 **Hint 3:** For the iterative approach, use a queue initialized with (root.left, root.right). Each iteration dequeues a pair and enqueues (left.left, right.right) and (left.right, right.left).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for recursion stack

Helper function `isMirror(left, right)` recursively checks that outer pairs (left.left, right.right) and inner pairs (left.right, right.left) match.
