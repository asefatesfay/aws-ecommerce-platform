# Count Good Nodes in Binary Tree

**Difficulty:** Medium
**Pattern:** DFS
**LeetCode:** #1448

## Problem Statement

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.val. Return the number of good nodes in the binary tree.

## Examples

### Example 1
**Input:** `root = [3,1,4,3,null,1,5]`
**Output:** `4`
**Explanation:** Good nodes: root (3), node 4, node 3 (left child of 1), node 5. Node 1 is not good because 3 > 1 on the path from root.

### Example 2
**Input:** `root = [3,3,null,4,2]`
**Output:** `3`
**Explanation:** Good nodes: root (3), node 3 (left child), node 4.

## Constraints
- The number of nodes in the binary tree is in the range `[1, 10^5]`
- Each node's value is between `-10^4` and `10^4`

## Hints

> 💡 **Hint 1:** A node is "good" if its value is ≥ the maximum value seen on the path from root to that node. Pass the running maximum down through the DFS.

> 💡 **Hint 2:** At each node, check if `node.val >= max_so_far`. If yes, it's a good node — increment the count. Then recurse with `max(max_so_far, node.val)` as the new maximum.

> 💡 **Hint 3:** The root is always a good node (no ancestors). Initialize `max_so_far = -infinity` or just `root.val` before the first call.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS passing the maximum value seen on the current root-to-node path. A node is good if its value ≥ the running max. Count good nodes and recurse with updated max.
