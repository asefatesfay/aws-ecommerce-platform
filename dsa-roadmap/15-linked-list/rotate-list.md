# Rotate List

**Difficulty:** Medium
**Pattern:** Linked List Manipulation
**LeetCode:** #61

## Problem Statement

Given the head of a linked list, rotate the list to the right by `k` places.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`, `k = 2`
**Output:** `[4,5,1,2,3]`

### Example 2
**Input:** `head = [0,1,2]`, `k = 4`
**Output:** `[2,0,1]`

## Constraints
- The number of nodes in the list is in the range `[0, 500]`
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Hints

> 💡 **Hint 1:** First find the length of the list. Then k = k % length (rotating by length is a no-op).

> 💡 **Hint 2:** The new tail is at position (length - k - 1) from the head. The new head is the node after the new tail.

> 💡 **Hint 3:** Make the list circular (connect tail to head), then find the new tail and break the circle there.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Find length, compute effective rotation (k % n), make circular, find new tail at position n-k-1, break the circle.
