# Next Greater Node In Linked List

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #1019

## Problem Statement

You are given the head of a linked list with `n` nodes. For each node in the list, find the value of the next node that has a strictly larger value. Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `i`th node (1-indexed). If the `i`th node does not have a next greater node, set `answer[i] = 0`.

## Examples

### Example 1
**Input:** `head = [2,1,5]`
**Output:** `[5,5,0]`

### Example 2
**Input:** `head = [2,7,4,3,5]`
**Output:** `[7,0,5,5,0]`

## Constraints
- The number of nodes in the list is `n`
- `1 <= n <= 10^4`
- `1 <= Node.val <= 10^9`

## Hints

> 💡 **Hint 1:** Convert the linked list to an array first. Then apply the standard "next greater element" monotonic stack algorithm.

> 💡 **Hint 2:** Use a monotonic decreasing stack of indices. When you find a greater element, resolve all smaller elements in the stack.

> 💡 **Hint 3:** Initialize the answer array with zeros. Only update when a greater element is found.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Convert list to array, then apply monotonic decreasing stack to find next greater element for each position.
