# Balanced Binary Tree

**Difficulty:** Easy
**Pattern:** DFS / Tree DP
**LeetCode:** #110

## Problem Statement

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one in which the left and right subtrees of every node differ in height by no more than 1.

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `true`
**Explanation:** Left subtree height = 1, right subtree height = 2. Difference = 1 ≤ 1.

### Example 2
**Input:** `root = [1,2,2,3,3,null,null,4,4]`
**Output:** `false`
**Explanation:** The left subtree has height 3, right has height 1. Difference = 2 > 1.

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`
- `-10^4 <= Node.val <= 10^4`

## Hints

> 💡 **Hint 1:** A naive approach checks balance at each node by computing heights separately — this is O(n^2). Instead, compute height and check balance in a single DFS pass.

> 💡 **Hint 2:** Write a DFS that returns the height of a subtree, or -1 if the subtree is unbalanced. At each node: get left and right heights. If either is -1, or `|left - right| > 1`, return -1. Otherwise return `1 + max(left, right)`.

> 💡 **Hint 3:** The tree is balanced if and only if the DFS returns a non-negative value (not -1). Using -1 as a sentinel for "unbalanced" lets you short-circuit early without a separate boolean.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS returning height or -1 (unbalanced sentinel). At each node, if either child returns -1 or heights differ by more than 1, propagate -1 upward.
