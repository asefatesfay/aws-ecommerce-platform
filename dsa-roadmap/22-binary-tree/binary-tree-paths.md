# Binary Tree Paths

**Difficulty:** Easy
**Pattern:** DFS / Root-to-Leaf Paths
**LeetCode:** #257

## Problem Statement

Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.

## Examples

### Example 1
**Input:** `root = [1,2,3,null,5]`
**Output:** `["1->2->5","1->3"]`
**Explanation:** Paths: 1→2→5 and 1→3.

### Example 2
**Input:** `root = [1]`
**Output:** `["1"]`

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** DFS with a running path string. Pass the current path down as you recurse. When you reach a leaf (no children), add the path to your result list.

> 💡 **Hint 2:** Build the path by appending `"->" + str(node.val)` at each step. At the root, start with just `str(root.val)`. At a leaf, append the current path to results.

> 💡 **Hint 3:** Since strings are immutable, passing the path string down doesn't cause backtracking issues — each recursive call gets its own copy. Alternatively, use a list and join at leaves, then pop on the way back up.

## Approach

**Time Complexity:** O(n * h) where h is the height (path string construction)
**Space Complexity:** O(h) for the recursion stack

DFS carrying the current path string. At each leaf node, append the complete path to the result list.
