# Delete the Middle Node of a Linked List

**Difficulty:** Medium
**Pattern:** Fast/Slow Pointers
**LeetCode:** #2095

## Problem Statement

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list. The middle node of a linked list of size `n` is the `⌊n / 2⌋`th node from the start using 0-based indexing.

## Examples

### Example 1
**Input:** `head = [1,3,4,7,1,2,6]`
**Output:** `[1,3,4,1,2,6]`
**Explanation:** Middle node (index 3) has value 7. Delete it.

### Example 2
**Input:** `head = [1,2,3,4]`
**Output:** `[1,2,4]`
**Explanation:** Middle node (index 2) has value 3.

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`
- `1 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** Use fast/slow pointers to find the middle, but you need the node before the middle to delete it.

> 💡 **Hint 2:** Use a dummy head. Let slow start at dummy and fast start at head. Advance slow by 1 and fast by 2. When fast reaches the end, slow is at the predecessor of the middle.

> 💡 **Hint 3:** Set `slow.next = slow.next.next` to delete the middle node.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Dummy head + fast/slow pointers where slow starts one step behind. When fast reaches end, slow is at the predecessor of the middle node.
