# Binary Tree Postorder Traversal

**Difficulty:** Easy
**Pattern:** DFS / Tree Traversal
**LeetCode:** #145

## Problem Statement

Given the root of a binary tree, return the postorder traversal of its nodes' values. Postorder visits: Left → Right → Root.

## Examples

### Example 1
**Input:** `root = [1,null,2,3]`
**Output:** `[3,2,1]`

### Example 2
**Input:** `root = []`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Recursive solution: recurse left, recurse right, append root.val. This is the most natural approach.

> 💡 **Hint 2:** Iterative trick: postorder (L→R→Root) is the reverse of a modified preorder (Root→R→L). Do a preorder traversal but push left before right (so right is processed first), then reverse the result.

> 💡 **Hint 3:** True iterative postorder without reversal: use a stack and track the previously visited node. Only visit a node when both its children have been visited (or it has no children).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

Recursive: left → right → root. Iterative shortcut: reverse of (root → right → left) traversal, which is a simple preorder variant.
