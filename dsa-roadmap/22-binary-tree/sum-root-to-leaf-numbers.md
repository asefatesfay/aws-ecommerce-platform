# Sum Root to Leaf Numbers

**Difficulty:** Medium
**Pattern:** DFS
**LeetCode:** #129

## Problem Statement

You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number. For example, the root-to-leaf path 1 → 2 → 3 represents the number 123. Return the total sum of all root-to-leaf numbers.

## Examples

### Example 1
**Input:** `root = [1,2,3]`
**Output:** `25`
**Explanation:** Path 1→2 = 12, path 1→3 = 13. Sum = 12 + 13 = 25.

### Example 2
**Input:** `root = [4,9,0,5,1]`
**Output:** `1026`
**Explanation:** Paths: 4→9→5 = 495, 4→9→1 = 491, 4→0 = 40. Sum = 495 + 491 + 40 = 1026.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`

## Hints

> 💡 **Hint 1:** Pass the current number being built down through the DFS. At each node, the new number is `current_num * 10 + node.val`.

> 💡 **Hint 2:** At a leaf node, return the current number — it represents the complete root-to-leaf number. At internal nodes, return the sum of results from left and right subtrees.

> 💡 **Hint 3:** Handle null nodes by returning 0. The recursion naturally sums all leaf numbers because each leaf returns its path number, and internal nodes sum their children's results.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS passing the running number (`current * 10 + node.val`). At leaves, return the number. At internal nodes, return the sum of left and right subtree results.
