# Maximum Difference Between Node and Ancestor

**Difficulty:** Medium
**Pattern:** DFS
**LeetCode:** #1026

## Problem Statement

Given the root of a binary tree, find the maximum value `v` for which there exist different nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`. A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

## Examples

### Example 1
**Input:** `root = [8,3,10,1,6,null,14,null,null,4,7,13]`
**Output:** `7`
**Explanation:** |8 - 1| = 7. The ancestor 8 and descendant 1 give the maximum difference.

### Example 2
**Input:** `root = [1,null,2,null,0,3]`
**Output:** `3`

## Constraints
- The number of nodes in the tree is in the range `[2, 5000]`
- `0 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** For any node, the maximum difference with one of its ancestors is either `node.val - min_ancestor` or `max_ancestor - node.val`. So track the running min and max values along the current root-to-node path.

> 💡 **Hint 2:** Pass `curr_min` and `curr_max` down through the DFS. At each node, update the global answer with `max(node.val - curr_min, curr_max - node.val)`, then recurse with updated min/max.

> 💡 **Hint 3:** At leaf nodes, return `max_ancestor - min_ancestor` — this is the maximum possible difference for any pair on this path. The answer is the max across all leaves.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS passing the running min and max values from root to current node. At each node, compute the max difference with any ancestor and update the global answer.
