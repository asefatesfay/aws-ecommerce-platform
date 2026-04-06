# Diameter of Binary Tree

**Difficulty:** Easy
**Pattern:** DFS / Tree DP
**LeetCode:** #543

## Problem Statement

Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5]`
**Output:** `3`
**Explanation:** The longest path is 4→2→1→3 or 5→2→1→3, with 3 edges.

### Example 2
**Input:** `root = [1,2]`
**Output:** `1`

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** The diameter through any node equals `left_height + right_height` (the longest path going through that node). The answer is the maximum of this across all nodes.

> 💡 **Hint 2:** Write a DFS that returns the height of a subtree. At each node, update a global `max_diameter` with `left_height + right_height`. Return `1 + max(left_height, right_height)` as the height.

> 💡 **Hint 3:** The key insight: the diameter doesn't have to pass through the root. By computing the diameter at every node and tracking the global max, you cover all possible paths.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS returning subtree height. At each node, update global max with `left_height + right_height`. The diameter is the maximum sum of left and right heights across all nodes.
