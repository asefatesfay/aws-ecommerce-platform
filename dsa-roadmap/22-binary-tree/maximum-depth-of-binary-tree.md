# Maximum Depth of Binary Tree

**Difficulty:** Easy
**Pattern:** DFS / BFS
**LeetCode:** #104

## Problem Statement

Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `3`
**Explanation:** The longest path is 3 → 20 → 15 (or 3 → 20 → 7), which has 3 nodes.

### Example 2
**Input:** `root = [1,null,2]`
**Output:** `2`

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** The depth of a tree is 1 + the maximum depth of its two subtrees. This is a natural recursive definition — the base case is a null node with depth 0.

> 💡 **Hint 2:** For BFS: use a queue and count how many levels you process. Each time you finish processing all nodes at the current level, increment your depth counter.

> 💡 **Hint 3:** Both DFS and BFS work here. DFS is 3 lines of code. BFS is slightly more code but gives you level-by-level control if needed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is the height (O(n) worst case for skewed tree, O(log n) for balanced)

Recursively return 1 + max(depth(left), depth(right)), with base case 0 for null nodes.
