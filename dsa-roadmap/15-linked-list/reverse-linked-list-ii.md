# Reverse Linked List II

**Difficulty:** Medium
**Pattern:** Linked List Manipulation
**LeetCode:** #92

## Problem Statement

Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`, `left = 2`, `right = 4`
**Output:** `[1,4,3,2,5]`

### Example 2
**Input:** `head = [5]`, `left = 1`, `right = 1`
**Output:** `[5]`

## Constraints
- The number of nodes in the list is `n`
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## Hints

> 💡 **Hint 1:** Use a dummy head. Traverse to the node just before position `left` (call it `prev`).

> 💡 **Hint 2:** Reverse the sublist from position `left` to `right` in-place. One approach: repeatedly move the node after `curr` to the front of the reversed section.

> 💡 **Hint 3:** The "insert at front" technique: let `curr` be the start of the reversed section. Repeatedly take `curr.next`, insert it after `prev`, and update pointers.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Dummy head + traverse to predecessor of left. Reverse the sublist using the "insert at front" technique (right - left) times.
