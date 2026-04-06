# Partition List

**Difficulty:** Medium
**Pattern:** Linked List / Two Lists
**LeetCode:** #86

## Problem Statement

Given the head of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`. You should preserve the original relative order of the nodes in each of the two partitions.

## Examples

### Example 1
**Input:** `head = [1,4,3,2,5,2]`, `x = 3`
**Output:** `[1,2,2,4,3,5]`

### Example 2
**Input:** `head = [2,1]`, `x = 2`
**Output:** `[1,2]`

## Constraints
- The number of nodes in the list is in the range `[0, 200]`
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Hints

> 💡 **Hint 1:** Create two separate lists: one for nodes < x and one for nodes >= x.

> 💡 **Hint 2:** Scan through the original list. Append each node to the appropriate list based on its value.

> 💡 **Hint 3:** Connect the tail of the "less" list to the head of the "greater-or-equal" list. Set the tail of the second list to null.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two dummy heads for two sublists. Scan and partition. Connect the two lists at the end.
