# Reverse Nodes in k-Group

**Difficulty:** Hard
**Pattern:** Linked List / Reversal
**LeetCode:** #25

## Problem Statement

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`, `k = 2`
**Output:** `[2,1,4,3,5]`

### Example 2
**Input:** `head = [1,2,3,4,5]`, `k = 3`
**Output:** `[3,2,1,4,5]`

## Constraints
- The number of nodes in the list is `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** First check if there are at least k nodes remaining. If not, leave them as is.

> 💡 **Hint 2:** Reverse the next k nodes. Connect the reversed group to the previous group and to the next group.

> 💡 **Hint 3:** Recursively (or iteratively) process the remaining list after the reversed group.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n/k) recursive, O(1) iterative

Check k nodes exist, reverse them, connect to previous tail and recurse/iterate on the rest.
