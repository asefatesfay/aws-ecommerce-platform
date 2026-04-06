# Remove Nth Node From End of List

**Difficulty:** Medium
**Pattern:** Fast/Slow Pointers
**LeetCode:** #19

## Problem Statement

Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`, `n = 2`
**Output:** `[1,2,3,5]`
**Explanation:** Remove the 2nd node from the end (value 4).

### Example 2
**Input:** `head = [1]`, `n = 1`
**Output:** `[]`

### Example 3
**Input:** `head = [1,2]`, `n = 1`
**Output:** `[1]`

## Constraints
- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Hints

> 💡 **Hint 1:** Use a dummy head to handle the edge case of removing the first node. Use two pointers.

> 💡 **Hint 2:** Advance the fast pointer n+1 steps ahead of the slow pointer. Then advance both until fast reaches null.

> 💡 **Hint 3:** When fast is null, slow is at the node just before the one to remove. Set `slow.next = slow.next.next`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Dummy head + two pointers with n+1 gap. When fast reaches null, slow is at the predecessor of the node to remove.
