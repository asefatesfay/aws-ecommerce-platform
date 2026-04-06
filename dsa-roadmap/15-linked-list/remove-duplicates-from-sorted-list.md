# Remove Duplicates from Sorted List

**Difficulty:** Easy
**Pattern:** Linked List Traversal
**LeetCode:** #83

## Problem Statement

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Examples

### Example 1
**Input:** `head = [1,1,2]`
**Output:** `[1,2]`

### Example 2
**Input:** `head = [1,1,2,3,3]`
**Output:** `[1,2,3]`

## Constraints
- The number of nodes in the list is in the range `[0, 300]`
- `-100 <= Node.val <= 100`
- The list is guaranteed to be sorted in ascending order

## Hints

> 💡 **Hint 1:** Since the list is sorted, duplicates are adjacent. Scan through and skip nodes with the same value as the current node.

> 💡 **Hint 2:** For each node, advance `curr.next` past all nodes with the same value as `curr`.

> 💡 **Hint 3:** Set `curr.next` to the first node with a different value, then advance `curr`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass: for each node, skip all subsequent nodes with the same value by advancing the next pointer.
