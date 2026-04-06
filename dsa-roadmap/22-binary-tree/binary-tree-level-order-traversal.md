# Binary Tree Level Order Traversal

**Difficulty:** Medium
**Pattern:** BFS / Level Order Traversal
**LeetCode:** #102

## Problem Statement

Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `[[3],[9,20],[15,7]]`
**Explanation:** Level 0 has [3], level 1 has [9, 20], level 2 has [15, 7].

### Example 2
**Input:** `root = [1]`
**Output:** `[[1]]`

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`
- `-1000 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** Use a queue (deque). Start by enqueuing the root. Each iteration of the outer loop processes one complete level.

> 💡 **Hint 2:** Before processing a level, snapshot `level_size = len(queue)`. Then dequeue exactly `level_size` nodes, collecting their values into a list. Enqueue their children. Append the level list to your result.

> 💡 **Hint 3:** The key insight is that snapshotting the queue size before processing separates levels cleanly — you never mix nodes from different levels.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(w) where w is the maximum width of the tree

BFS with level-size snapshots: process exactly `len(queue)` nodes per iteration, collecting each level's values into a sublist before appending to the result.
