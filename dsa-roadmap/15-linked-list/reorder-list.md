# Reorder List

**Difficulty:** Medium
**Pattern:** Linked List / Fast-Slow + Reversal + Merge
**LeetCode:** #143

## Problem Statement

You are given the head of a singly linked-list: `L0 → L1 → … → Ln-1 → Ln`. Reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`. You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Examples

### Example 1
**Input:** `head = [1,2,3,4]`
**Output:** `[1,4,2,3]`

### Example 2
**Input:** `head = [1,2,3,4,5]`
**Output:** `[1,5,2,4,3]`

## Constraints
- The number of nodes in the list is in the range `[1, 5 * 10^4]`
- `1 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** This problem combines three techniques: find the middle, reverse the second half, merge the two halves.

> 💡 **Hint 2:** Step 1: Find the middle using fast/slow pointers. Step 2: Reverse the second half. Step 3: Merge the first half and reversed second half alternately.

> 💡 **Hint 3:** For the merge step, alternate between taking from the first half and the reversed second half.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Three steps: find middle (fast/slow), reverse second half, merge two halves alternately.
