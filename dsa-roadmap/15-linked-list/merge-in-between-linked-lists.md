# Merge In Between Linked Lists

**Difficulty:** Medium
**Pattern:** Linked List Manipulation
**LeetCode:** #1669

## Problem Statement

You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively. Remove `list1`'s nodes from the `a`th node to the `b`th node, and put `list2` in their place. Return the head of the resulting linked list.

## Examples

### Example 1
**Input:** `list1 = [0,1,2,3,4,5]`, `a = 3`, `b = 4`, `list2 = [1000000,1000001,1000002]`
**Output:** `[0,1,2,1000000,1000001,1000002,5]`

### Example 2
**Input:** `list1 = [0,1,2,3,4,5,6]`, `a = 2`, `b = 5`, `list2 = [1000000,1000001,1000002,1000003,1000004]`
**Output:** `[0,1,1000000,1000001,1000002,1000003,1000004,6]`

## Constraints
- `3 <= list1.length <= 10^4`
- `1 <= a <= b < list1.length - 1`
- `1 <= list2.length <= 10^4`

## Hints

> 💡 **Hint 1:** Find the node just before position `a` (call it `nodeA`) and the node just after position `b` (call it `nodeB`).

> 💡 **Hint 2:** Find the tail of `list2`.

> 💡 **Hint 3:** Connect: `nodeA.next = list2.head`, `list2.tail.next = nodeB`.

## Approach

**Time Complexity:** O(n + m)
**Space Complexity:** O(1)

Traverse to find the predecessor of position a and the successor of position b. Find list2's tail. Wire up the connections.
