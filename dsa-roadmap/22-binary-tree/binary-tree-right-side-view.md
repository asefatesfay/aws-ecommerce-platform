# Binary Tree Right Side View

**Difficulty:** Medium
**Pattern:** BFS / Level Order Traversal
**LeetCode:** #199

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

## Examples

### Example 1
**Input:** `root = [1,2,3,null,5,null,4]`
**Output:** `[1,3,4]`
**Explanation:** From the right side you see 1 (level 0), 3 (level 1, rightmost), 4 (level 2, rightmost).

### Example 2
**Input:** `root = [1,null,3]`
**Output:** `[1,3]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** The "right side view" is simply the last node at each level. Do a level-order BFS and record the last node you process at each level.

> 💡 **Hint 2:** Alternatively, do DFS visiting right children before left children. The first time you reach a new depth, that node is the rightmost one visible.

> 💡 **Hint 3:** For the DFS approach, track the current depth and the result list size. When `depth == len(result)`, you're visiting a new level for the first time — append the node's value.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for DFS, O(w) for BFS

BFS: process each level, take the last node's value. Or DFS right-first: the first node encountered at each depth is the rightmost visible node.
