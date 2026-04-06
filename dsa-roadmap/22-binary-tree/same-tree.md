# Same Tree

**Difficulty:** Easy
**Pattern:** DFS / Tree Comparison
**LeetCode:** #100

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Examples

### Example 1
**Input:** `p = [1,2,3]`, `q = [1,2,3]`
**Output:** `true`

### Example 2
**Input:** `p = [1,2]`, `q = [1,null,2]`
**Output:** `false`
**Explanation:** Same values but different structure — 2 is a left child in p but a right child in q.

## Constraints
- The number of nodes in both trees is in the range `[0, 100]`
- `-10^4 <= Node.val <= 10^4`

## Hints

> 💡 **Hint 1:** Recurse on both trees simultaneously. At each step, compare the current nodes of both trees.

> 💡 **Hint 2:** There are four cases: both null (return True), one null and one not (return False), both non-null with different values (return False), both non-null with same value (recurse on children).

> 💡 **Hint 3:** The recursive call is: `p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`. Short-circuit evaluation handles the null cases first.

## Approach

**Time Complexity:** O(n) where n is the number of nodes in the smaller tree
**Space Complexity:** O(h) for the recursion stack

Simultaneous DFS on both trees: compare values at each node and recurse on both left and right pairs.
