# Path Sum II

**Difficulty:** Medium
**Pattern:** DFS / Backtracking
**LeetCode:** #113

## Problem Statement

Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

## Examples

### Example 1
**Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]`, `targetSum = 22`
**Output:** `[[5,4,11,2],[5,8,4,5]]`
**Explanation:** 5+4+11+2=22 and 5+8+4+5=22.

### Example 2
**Input:** `root = [1,2,3]`, `targetSum = 5`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 5000]`
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Hints

> 💡 **Hint 1:** DFS with backtracking. Carry a running path list and the remaining sum. At each node, add it to the path and subtract its value from the remaining sum.

> 💡 **Hint 2:** At a leaf node, if `remaining == 0`, you've found a valid path. Append a copy of the current path to results (not the path itself — it will be modified later).

> 💡 **Hint 3:** After recursing into both children, pop the current node from the path (backtrack). This restores the path for other branches. The key is appending a copy (`path[:]`) when you find a solution.

## Approach

**Time Complexity:** O(n * h) where h is the height (copying paths)
**Space Complexity:** O(h) for the recursion stack and current path

DFS with backtracking: maintain a current path list, add node on entry, recurse into children, pop on exit. At leaves with remaining sum = 0, save a copy of the path.
