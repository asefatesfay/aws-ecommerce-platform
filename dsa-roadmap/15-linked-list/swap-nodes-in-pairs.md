# Swap Nodes in Pairs

**Difficulty:** Medium
**Pattern:** Linked List Manipulation
**LeetCode:** #24

## Problem Statement

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

## Examples

### Example 1
**Input:** `head = [1,2,3,4]`
**Output:** `[2,1,4,3]`

### Example 2
**Input:** `head = []`
**Output:** `[]`

### Example 3
**Input:** `head = [1]`
**Output:** `[1]`

## Constraints
- The number of nodes in the list is in the range `[0, 100]`
- `0 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Use a dummy head. Process pairs of nodes at a time.

> 💡 **Hint 2:** For each pair (first, second): set `prev.next = second`, `first.next = second.next`, `second.next = first`. Then advance prev to first (which is now the second in the pair).

> 💡 **Hint 3:** Recursive approach: swap the first two nodes, then recursively swap the rest and connect.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) iterative, O(n) recursive

Dummy head + iterative pair swapping. For each pair, rewire three pointers. Advance to the next pair.
