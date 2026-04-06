# Palindrome Linked List

**Difficulty:** Easy
**Pattern:** Fast/Slow Pointers + Reversal
**LeetCode:** #234

## Problem Statement

Given the head of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

## Examples

### Example 1
**Input:** `head = [1,2,2,1]`
**Output:** `true`

### Example 2
**Input:** `head = [1,2]`
**Output:** `false`

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`
- `0 <= Node.val <= 9`

## Hints

> 💡 **Hint 1:** Find the middle of the list using fast/slow pointers.

> 💡 **Hint 2:** Reverse the second half of the list in-place.

> 💡 **Hint 3:** Compare the first half with the reversed second half node by node. Optionally restore the list afterward.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Find middle with fast/slow, reverse second half, compare both halves. Optionally restore the list.
