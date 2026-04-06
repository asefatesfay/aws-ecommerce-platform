# Kth Smallest Element in a BST

**Difficulty:** Medium
**Pattern:** BST Inorder Traversal
**LeetCode:** #230

## Problem Statement

Given the root of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

## Examples

### Example 1
**Input:** `root = [3,1,4,null,2]`, `k = 1`
**Output:** `1`
**Explanation:** Inorder: [1,2,3,4]. The 1st smallest is 1.

### Example 2
**Input:** `root = [5,3,6,2,4,null,null,1]`, `k = 3`
**Output:** `3`
**Explanation:** Inorder: [1,2,3,4,5,6]. The 3rd smallest is 3.

## Constraints
- The number of nodes in the tree is `n`
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Hints

> 💡 **Hint 1:** BST inorder traversal produces values in ascending sorted order. The kth smallest is simply the kth value in the inorder traversal.

> 💡 **Hint 2:** Use an iterative inorder traversal with a counter. Decrement k each time you visit a node. When k reaches 0, you've found the answer — return immediately without traversing the rest.

> 💡 **Hint 3:** For the follow-up (frequent insertions/deletions + frequent kth queries), augment each node with the size of its subtree. Then you can find the kth smallest in O(log n) by comparing k with the left subtree size.

## Approach

**Time Complexity:** O(h + k) where h is the height
**Space Complexity:** O(h) for the stack

Iterative inorder traversal: push left nodes onto a stack, pop and decrement k, move right. Return the node's value when k reaches 0.
