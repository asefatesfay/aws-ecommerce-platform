# Flatten a Multilevel Doubly Linked List

**Difficulty:** Medium
**Pattern:** Linked List / DFS
**LeetCode:** #430

## Problem Statement

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure. Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let `curr` be a node with a child list. The nodes in the child list should appear after `curr` and before `curr`'s next node in the flattened list.

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`
**Output:** `[1,2,3,7,8,11,12,9,10,4,5,6]`

## Constraints
- The number of nodes in the list is in the range `[0, 1000]`
- `1 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** When you encounter a node with a child, you need to insert the child list between the current node and its next.

> 💡 **Hint 2:** For each node with a child: find the tail of the child list, connect current node to child list head, connect child list tail to current node's original next, clear the child pointer.

> 💡 **Hint 3:** Use a stack or recursion to handle nested children. Or iteratively process: when you see a child, insert it inline and continue.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(depth) for recursion/stack

Iterative: when a node has a child, find the child list's tail, splice it in between current and next, clear child pointer, continue.
