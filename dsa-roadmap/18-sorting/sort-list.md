# Sort List

**Difficulty:** Medium
**Pattern:** Merge Sort on Linked List
**LeetCode:** #148

## Problem Statement

Given the head of a linked list, return the list after sorting it in ascending order.

## Examples

### Example 1
**Input:** `head = [4,2,1,3]`
**Output:** `[1,2,3,4]`

### Example 2
**Input:** `head = [-1,5,3,4,0]`
**Output:** `[-1,0,3,4,5]`

## Constraints
- The number of nodes in the list is in the range `[0, 5 * 10^4]`
- `-10^5 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** Merge sort is ideal for linked lists — it doesn't require random access and has O(n log n) guaranteed.

> 💡 **Hint 2:** Find the middle using fast/slow pointers. Split the list. Recursively sort each half. Merge the two sorted halves.

> 💡 **Hint 3:** For O(1) space, use bottom-up merge sort: start with sublists of size 1, merge pairs, then size 2, merge pairs, etc.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(log n) recursive, O(1) bottom-up

Top-down: find middle, split, sort halves, merge. Bottom-up: iteratively merge sublists of increasing sizes.
