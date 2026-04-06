# Convert Sorted List to Binary Search Tree

**Difficulty:** Medium
**Pattern:** Divide and Conquer / Fast-Slow Pointers
**LeetCode:** #109

## Problem Statement

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Examples

### Example 1
**Input:** `head = [-10,-3,0,5,9]`
**Output:** `[0,-3,9,-10,null,5]`
**Explanation:** One possible answer is [0,-3,9,-10,null,5], which represents the height-balanced BST.

### Example 2
**Input:** `head = []`
**Output:** `[]`

## Constraints
- The number of nodes in `head` is in the range `[0, 2 * 10^4]`
- `-10^5 <= Node.val <= 10^5`

## Hints

> 💡 **Hint 1:** The middle element of the sorted list becomes the root (ensures height balance). Left half becomes the left subtree, right half becomes the right subtree.

> 💡 **Hint 2:** Find the middle using fast/slow pointers. Split the list at the middle. Recursively build left and right subtrees.

> 💡 **Hint 3:** To split: find the node before the middle (slow's predecessor), set its next to null. The right half starts at slow.next.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(log n) recursion depth

Divide and conquer: find middle with fast/slow, split list, recursively build subtrees.
