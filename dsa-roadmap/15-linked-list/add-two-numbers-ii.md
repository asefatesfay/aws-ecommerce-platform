# Add Two Numbers II

**Difficulty:** Medium
**Pattern:** Linked List / Stack
**LeetCode:** #445

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not have leading zeros, except the number 0 itself.

## Examples

### Example 1
**Input:** `l1 = [7,2,4,3]`, `l2 = [5,6,4]`
**Output:** `[7,8,0,7]`
**Explanation:** 7243 + 564 = 7807.

### Example 2
**Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
**Output:** `[8,0,7]`

## Constraints
- The number of nodes in each list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros

## Hints

> 💡 **Hint 1:** Unlike "Add Two Numbers I", digits are in forward order. You need to add from the least significant digit.

> 💡 **Hint 2:** Use two stacks to reverse the order. Push all digits of each list onto stacks. Pop and add with carry.

> 💡 **Hint 3:** Build the result list by prepending nodes (insert at head) since you're computing from least significant to most significant.

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(m + n) for stacks

Push both lists onto stacks. Pop and add with carry, prepending result nodes. Handle remaining carry.
