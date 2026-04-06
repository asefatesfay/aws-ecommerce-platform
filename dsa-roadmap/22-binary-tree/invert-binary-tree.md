# Invert Binary Tree

**Difficulty:** Easy
**Pattern:** DFS
**LeetCode:** #226

## Problem Statement

Given the root of a binary tree, invert the tree, and return its root. Inverting means swapping the left and right children of every node.

## Examples

### Example 1
**Input:** `root = [4,2,7,1,3,6,9]`
**Output:** `[4,7,2,9,6,3,1]`
**Explanation:** Every node's left and right children are swapped.

### Example 2
**Input:** `root = [2,1,3]`
**Output:** `[2,3,1]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** At each node, swap its left and right children. Then recursively invert both subtrees.

> 💡 **Hint 2:** The order doesn't matter — you can swap first then recurse, or recurse first then swap. Both produce the same result.

> 💡 **Hint 3:** BFS also works: process nodes level by level, swapping children at each node. Use a queue initialized with the root.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

Recursive: swap left and right children at each node, then recurse into both. Return the root after inversion.
