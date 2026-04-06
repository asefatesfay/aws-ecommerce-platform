# Middle of the Linked List

**Difficulty:** Easy
**Pattern:** Fast/Slow Pointers
**LeetCode:** #876

## Problem Statement

Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`
**Output:** `[3,4,5]` (node with value 3)

### Example 2
**Input:** `head = [1,2,3,4,5,6]`
**Output:** `[4,5,6]` (node with value 4 — second middle)

## Constraints
- The number of nodes in the list is in the range `[1, 100]`
- `1 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Use fast and slow pointers. Slow moves one step at a time, fast moves two steps.

> 💡 **Hint 2:** When fast reaches the end (null or last node), slow is at the middle.

> 💡 **Hint 3:** For even-length lists, this naturally returns the second middle node (since fast stops at null, not the last node).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Fast/slow pointers: slow advances 1 step, fast advances 2 steps. When fast is null or fast.next is null, slow is at the middle.
