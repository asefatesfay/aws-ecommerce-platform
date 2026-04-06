# Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium
**Pattern:** BFS / Level Order Traversal
**LeetCode:** #103

## Problem Statement

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level, and so on).

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `[[3],[20,9],[15,7]]`
**Explanation:** Level 0: left-to-right → [3]. Level 1: right-to-left → [20, 9]. Level 2: left-to-right → [15, 7].

### Example 2
**Input:** `root = [1]`
**Output:** `[[1]]`

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Start with standard BFS level-order traversal. The only difference is that on odd-numbered levels you reverse the collected list before appending.

> 💡 **Hint 2:** Track a boolean `left_to_right` that flips after each level. When it's False, reverse the current level's list (or use a deque and append to front vs back).

> 💡 **Hint 3:** Using a deque for each level is more efficient than reversing: on left-to-right levels, append to the right; on right-to-left levels, appendleft. This avoids the O(w) reversal cost.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(w) where w is the maximum width

BFS level-order with a direction flag: collect each level normally, then reverse the list on odd levels (or use a deque with conditional appendleft).
