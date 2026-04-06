# Maximum Width of Binary Tree

**Difficulty:** Medium
**Pattern:** BFS with Node Indexing
**LeetCode:** #662

## Problem Statement

Given the root of a binary tree, return the maximum width of the given tree. The width of one level is defined as the length between the leftmost and rightmost non-null nodes, including the null nodes between them. The answer is guaranteed to fit in a 32-bit signed integer.

## Examples

### Example 1
**Input:** `root = [1,3,2,5,3,null,9]`
**Output:** `4`
**Explanation:** The third level has nodes 5, 3, null, 9. Width = index(9) - index(5) + 1 = 4.

### Example 2
**Input:** `root = [1,3,2,5,null,null,9,6,null,7]`
**Output:** `7`

## Constraints
- The number of nodes in the tree is in the range `[1, 3000]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Assign each node an index like a heap array: root = 0, left child of node i = 2*i, right child = 2*i + 1. The width of a level is `rightmost_index - leftmost_index + 1`.

> 💡 **Hint 2:** Do BFS and carry the index alongside each node. At each level, the width is `last_index - first_index + 1`.

> 💡 **Hint 3:** Indices can grow exponentially (2^depth), causing overflow. Normalize at each level by subtracting the leftmost index of that level from all indices. This keeps numbers small without changing relative widths.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(w) where w is the maximum width

BFS carrying (node, index) pairs. At each level, width = last_index - first_index + 1. Normalize indices at each level to prevent overflow.
