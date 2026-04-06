# Binary Tree Maximum Path Sum

**Difficulty:** Hard
**Pattern:** DFS / Tree DP
**LeetCode:** #124

## Problem Statement

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root. Given the root of a binary tree, return the maximum path sum of any non-empty path.

## Examples

### Example 1
**Input:** `root = [1,2,3]`
**Output:** `6`
**Explanation:** The path 2→1→3 has sum 6.

### Example 2
**Input:** `root = [-10,9,20,null,null,15,7]`
**Output:** `42`
**Explanation:** The path 15→20→7 has sum 42.

## Constraints
- The number of nodes in the tree is in the range `[1, 3 * 10^4]`
- `-1000 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** For each node, the maximum path through it is `node.val + max(0, left_gain) + max(0, right_gain)`. The `max(0, ...)` handles negative subtrees — you'd rather not include them.

> 💡 **Hint 2:** The DFS function returns the maximum "gain" from this node going in one direction (either left or right, not both). This is `node.val + max(0, max(left_gain, right_gain))`. The path through the node (both directions) is only used to update the global answer.

> 💡 **Hint 3:** Use a global variable for the answer. At each node: compute `path_through = node.val + max(0, left) + max(0, right)`, update global max. Return `node.val + max(0, max(left, right))` as the single-direction gain.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS returning the max single-direction gain from each node. At each node, compute the path sum through it (both directions) and update the global maximum. Ignore negative subtrees by clamping gains to 0.
