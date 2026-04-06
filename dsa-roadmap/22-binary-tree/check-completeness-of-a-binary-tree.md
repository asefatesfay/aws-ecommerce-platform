# Check Completeness of a Binary Tree

**Difficulty:** Medium
**Pattern:** BFS
**LeetCode:** #958

## Problem Statement

Given the root of a binary tree, determine if it is a complete binary tree. In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5,6]`
**Output:** `true`
**Explanation:** All levels are full except the last, and the last level's nodes are left-aligned.

### Example 2
**Input:** `root = [1,2,3,4,5,null,7]`
**Output:** `false`
**Explanation:** Node 7 is in the right subtree of level 2, but there's a null gap before it.

## Constraints
- The number of nodes in the tree is in the range `[1, 100]`
- `1 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** Do a BFS. Once you encounter a null node, every subsequent node in the BFS queue must also be null. If you see a non-null node after a null, the tree is not complete.

> 💡 **Hint 2:** Enqueue children even if they are null (enqueue None). Use a flag `found_null` that becomes True when you first dequeue a None. If you then dequeue a non-None node, return False.

> 💡 **Hint 3:** Alternatively, use the heap-index trick: in a complete tree of n nodes, all indices should be in range [1, n]. If any node has index > n, it's not complete.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(w) where w is the maximum width

BFS with null-tracking: once a null is dequeued, set a flag. Any subsequent non-null node means the tree is incomplete.
