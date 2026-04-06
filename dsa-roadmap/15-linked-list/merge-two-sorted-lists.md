# Merge Two Sorted Lists

**Difficulty:** Easy
**Pattern:** Linked List / Two Pointers
**LeetCode:** #21

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## Examples

### Example 1
**Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`
**Output:** `[1,1,2,3,4,4]`

### Example 2
**Input:** `list1 = []`, `list2 = []`
**Output:** `[]`

### Example 3
**Input:** `list1 = []`, `list2 = [0]`
**Output:** `[0]`

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Use a dummy head to simplify the merge. Maintain a current pointer for the result list.

> 💡 **Hint 2:** Compare the heads of both lists. Append the smaller one to the result and advance that list's pointer.

> 💡 **Hint 3:** When one list is exhausted, append the remainder of the other list directly (no need to iterate — just point to it).

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

Dummy head + two-pointer merge. Compare heads, append smaller, advance. Attach remaining list at the end.
