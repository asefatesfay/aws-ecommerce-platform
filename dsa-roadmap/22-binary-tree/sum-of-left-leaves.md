# Sum of Left Leaves

**Difficulty:** Easy
**Pattern:** DFS
**LeetCode:** #404

## Problem Statement

Given the root of a binary tree, return the sum of all left leaves.

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `24`
**Explanation:** Left leaves are 9 and 15. Sum = 9 + 15 = 24.

### Example 2
**Input:** `root = [1]`
**Output:** `0`
**Explanation:** No left leaves exist.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`
- `-1000 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** You need to know whether a node is a left child or a right child. Pass a boolean `is_left` down through the recursion.

> 💡 **Hint 2:** A node is a "left leaf" if it has no children AND it was reached as a left child. When `is_left=True` and the node has no children, add its value to the sum.

> 💡 **Hint 3:** Recurse: `dfs(node.left, is_left=True)` and `dfs(node.right, is_left=False)`. Sum the results. The root itself is never a left leaf regardless of its children.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS passing an `is_left` flag. When a leaf node is reached with `is_left=True`, return its value; otherwise return 0. Sum results from both subtrees.
