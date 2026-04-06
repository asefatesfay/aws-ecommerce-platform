# Delete Node in a Linked List

**Difficulty:** Medium
**Pattern:** Linked List Trick
**LeetCode:** #237

## Problem Statement

There is a singly-linked list and you are given access to a node to be deleted. You will not be given access to the first node of the list. Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before the given node should be in the same order.
- All the values after the given node should be in the same order.

## Examples

### Example 1
**Input:** `head = [4,5,1,9]`, `node = 5`
**Output:** `[4,1,9]`

### Example 2
**Input:** `head = [4,5,1,9]`, `node = 1`
**Output:** `[4,5,9]`

## Constraints
- The number of nodes in the given list is in the range `[2, 1000]`
- `-1000 <= Node.val <= 1000`
- The value of each node in the list is unique
- The node to be deleted is in the list and is not a tail node

## Hints

> 💡 **Hint 1:** You can't delete the node directly (no access to previous node). But you can make it "disappear" by overwriting it.

> 💡 **Hint 2:** Copy the value of the next node into the current node, then delete the next node.

> 💡 **Hint 3:** `node.val = node.next.val; node.next = node.next.next`. This effectively removes the current node's value from the list.

## Approach

**Time Complexity:** O(1)
**Space Complexity:** O(1)

Copy next node's value into current node, then skip the next node. The current node effectively "becomes" the next node.
