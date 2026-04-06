# Subtree of Another Tree

**Difficulty:** Easy
**Pattern:** DFS / Tree Comparison
**LeetCode:** #572

## Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values as `subRoot` and `false` otherwise. A subtree of a binary tree `root` is a tree that consists of a node in `root` and all of this node's descendants.

## Examples

### Example 1
**Input:** `root = [3,4,5,1,2]`, `subRoot = [4,1,2]`
**Output:** `true`
**Explanation:** The subtree rooted at node 4 in root matches subRoot exactly.

### Example 2
**Input:** `root = [3,4,5,1,2,null,null,null,null,0]`, `subRoot = [4,1,2]`
**Output:** `false`
**Explanation:** Node 4 in root has an extra child (0), so it doesn't match subRoot.

## Constraints
- The number of nodes in the `root` tree is in the range `[1, 2000]`
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`
- `-10^4 <= root.val, subRoot.val <= 10^4`

## Hints

> 💡 **Hint 1:** Reuse the `isSameTree` function from #100. For each node in `root`, check if the subtree rooted there is identical to `subRoot`.

> 💡 **Hint 2:** The recursive structure is: `isSubtree(root, subRoot) = isSameTree(root, subRoot) OR isSubtree(root.left, subRoot) OR isSubtree(root.right, subRoot)`.

> 💡 **Hint 3:** For a more efficient approach, serialize both trees to strings and check if the subRoot string is a substring of the root string. Use a delimiter like "#" between values to avoid false matches (e.g., "12" vs "1" and "2").

## Approach

**Time Complexity:** O(m * n) where m and n are the sizes of the two trees
**Space Complexity:** O(h) for the recursion stack

For each node in root, check if the subtree rooted there equals subRoot using isSameTree. Return true if any match is found.
