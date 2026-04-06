# Insert into a Sorted Circular Linked List

**Difficulty:** Medium
**Pattern:** Linked List / Circular
**LeetCode:** #708

## Problem Statement

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value `insertVal` into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list. If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted. If the list is empty (i.e., the given node is `null`), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

## Examples

### Example 1
**Input:** `head = [3,4,1]`, `insertVal = 2`
**Output:** `[3,4,1,2]`

### Example 2
**Input:** `head = []`, `insertVal = 1`
**Output:** `[1]`

## Constraints
- `0 <= Number of Nodes <= 5 * 10^3`
- `-10^6 <= Node.val, insertVal <= 10^6`

## Hints

> 💡 **Hint 1:** Traverse the circular list looking for the right insertion point. There are three cases.

> 💡 **Hint 2:** Case 1: `curr.val <= insertVal <= curr.next.val` — insert between curr and curr.next (normal case). Case 2: `curr.val > curr.next.val` (at the "seam" of the circle) — insert if insertVal >= curr.val OR insertVal <= curr.next.val. Case 3: traversed the whole list without finding a spot — insert anywhere (all values are equal).

> 💡 **Hint 3:** Handle the empty list case separately. Use a do-while loop to traverse the circular list.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Traverse the circular list checking three insertion cases. Handle empty list and all-equal-values edge cases.
