# Linked List Cycle II

**Difficulty:** Medium
**Pattern:** Fast/Slow Pointers (Floyd's Algorithm)
**LeetCode:** #142

## Problem Statement

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `null`. Do not modify the linked list.

## Examples

### Example 1
**Input:** `head = [3,2,0,-4]`, `pos = 1` (tail connects to node at index 1)
**Output:** Node with value 2
**Explanation:** The cycle begins at node index 1.

### Example 2
**Input:** `head = [1,2]`, `pos = 0`
**Output:** Node with value 1

### Example 3
**Input:** `head = [1]`, `pos = -1`
**Output:** null

## Constraints
- The number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list

## Hints

> 💡 **Hint 1:** First detect if there's a cycle using fast/slow pointers. If they meet, there's a cycle.

> 💡 **Hint 2:** When fast and slow meet inside the cycle, reset one pointer to the head. Then advance both one step at a time.

> 💡 **Hint 3:** The point where they meet again is the cycle entry. This works due to a mathematical property of Floyd's algorithm: the distance from head to cycle entry equals the distance from the meeting point to cycle entry.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Floyd's cycle detection: detect meeting point, then reset one pointer to head and advance both at speed 1 until they meet — that's the cycle entry.
