# Merge Two Sorted Lists (Recursive)

**Difficulty:** Easy
**Pattern:** Recursion
**LeetCode:** #21

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

*(This problem also appears in Section 15 — Linked List. Here we focus on the recursive solution.)*

## Examples

### Example 1
**Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`
**Output:** `[1,1,2,3,4,4]`

### Example 2
**Input:** `list1 = []`, `list2 = [0]`
**Output:** `[0]`

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Think recursively: the merged list is the smaller head node, followed by the merge of the remaining lists.

> 💡 **Hint 2:** Base cases: if either list is null, return the other list.

> 💡 **Hint 3:** If list1.val ≤ list2.val: list1.next = merge(list1.next, list2), return list1. Otherwise: list2.next = merge(list1, list2.next), return list2.

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(m + n) recursive call stack

Recursive merge: compare heads, attach the smaller one, recurse on the rest.
