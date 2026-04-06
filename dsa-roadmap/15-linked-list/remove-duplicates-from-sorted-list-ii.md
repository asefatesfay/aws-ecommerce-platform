# Remove Duplicates from Sorted List II

**Difficulty:** Medium
**Pattern:** Linked List / Dummy Head
**LeetCode:** #82

## Problem Statement

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

## Examples

### Example 1
**Input:** `head = [1,2,3,3,4,4,5]`
**Output:** `[1,2,5]`

### Example 2
**Input:** `head = [1,1,1,2,3]`
**Output:** `[2,3]`

## Constraints
- The number of nodes in the list is in the range `[0, 300]`
- `-100 <= Node.val <= 100`
- The list is guaranteed to be sorted in ascending order

## Hints

> 💡 **Hint 1:** Use a dummy head. Maintain a `prev` pointer to the last confirmed unique node.

> 💡 **Hint 2:** For each group of nodes with the same value, check if the group has more than one node. If yes, skip the entire group by setting `prev.next` to the node after the group.

> 💡 **Hint 3:** If the group has only one node, it's unique — advance `prev` to it. Continue until the end.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Dummy head + prev pointer. For each value, scan ahead to find the end of the group. Skip the group if it has duplicates; advance prev if it's unique.
