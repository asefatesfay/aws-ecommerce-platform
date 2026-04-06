# Intersection of Two Linked Lists

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #160

## Problem Statement

Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`. The linked lists must retain their original structure after the function returns.

## Examples

### Example 1
**Input:** `intersectVal = 8`, `listA = [4,1,8,4,5]`, `listB = [5,6,1,8,4,5]`, `skipA = 2`, `skipB = 3`
**Output:** Node with value 8
**Explanation:** Both lists share the tail starting at node with value 8.

### Example 2
**Input:** `intersectVal = 0`, `listA = [2,6,4]`, `listB = [1,5]`
**Output:** null

## Constraints
- The number of nodes of `listA` is `m`
- The number of nodes of `listB` is `n`
- `1 <= m, n <= 3 * 10^4`
- `1 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** If you traverse both lists and switch to the other list when you reach the end, both pointers will have traveled the same total distance when they meet.

> 💡 **Hint 2:** Pointer A traverses listA then listB. Pointer B traverses listB then listA. They meet at the intersection (or both reach null if no intersection).

> 💡 **Hint 3:** This works because both pointers travel a + b + c total steps (where a, b are the non-shared lengths and c is the shared length).

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

Two pointers that switch lists when they reach the end. They meet at the intersection after traveling equal total distances.
