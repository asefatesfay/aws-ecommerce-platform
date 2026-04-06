# Reverse Linked List

**Difficulty:** Easy
**Pattern:** Linked List / Iterative or Recursive
**LeetCode:** #206

## Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5]`
**Output:** `[5,4,3,2,1]`

### Example 2
**Input:** `head = [1,2]`
**Output:** `[2,1]`

### Example 3
**Input:** `head = []`
**Output:** `[]`

## Constraints
- The number of nodes in the list is in the range `[0, 5000]`
- `-5000 <= Node.val <= 5000`

## Hints

> 💡 **Hint 1:** Iterative approach: maintain three pointers — `prev` (initially null), `curr` (initially head), and `next`. At each step, reverse the current node's pointer.

> 💡 **Hint 2:** At each step: save `next = curr.next`, set `curr.next = prev`, advance `prev = curr`, advance `curr = next`. Repeat until curr is null.

> 💡 **Hint 3:** Recursive approach: reverse the rest of the list, then make the next node point back to the current node and set current node's next to null.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) iterative, O(n) recursive (call stack)

Iterative: three-pointer reversal. Recursive: reverse the tail, then fix the head's pointer.
