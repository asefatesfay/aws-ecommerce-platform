# Add Two Numbers

**Difficulty:** Medium
**Pattern:** Linked List / Math Simulation
**LeetCode:** #2

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not have leading zeros, except the number 0 itself.

## Examples

### Example 1
**Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
**Output:** `[7,0,8]`
**Explanation:** 342 + 465 = 807.

### Example 2
**Input:** `l1 = [0]`, `l2 = [0]`
**Output:** `[0]`

### Example 3
**Input:** `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
**Output:** `[8,9,9,9,0,0,0,1]`

## Constraints
- The number of nodes in each list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros

## Hints

> 💡 **Hint 1:** Simulate grade-school addition digit by digit. Maintain a carry.

> 💡 **Hint 2:** At each step, sum the current digits from both lists (use 0 if a list is exhausted) plus the carry. The new digit is `sum % 10`, the new carry is `sum // 10`.

> 💡 **Hint 3:** Continue until both lists are exhausted AND carry is 0. Use a dummy head to simplify result list construction.

## Approach

**Time Complexity:** O(max(m, n))
**Space Complexity:** O(max(m, n)) for the result

Simulate addition with carry. Dummy head for result. Continue while either list has nodes or carry is non-zero.
