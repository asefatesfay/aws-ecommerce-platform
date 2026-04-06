# Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium
**Pattern:** Divide and Conquer / Tree Construction
**LeetCode:** #105

## Problem Statement

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Examples

### Example 1
**Input:** `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`
**Output:** `[3,9,20,null,null,15,7]`
**Explanation:** Root is 3 (first in preorder). In inorder, 3 is at index 1, so left subtree has 1 node [9] and right has 2 nodes [15,7].

### Example 2
**Input:** `preorder = [-1]`, `inorder = [-1]`
**Output:** `[-1]`

## Constraints
- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- All values are unique

## Hints

> 💡 **Hint 1:** The first element of `preorder` is always the root. Find that value in `inorder` — everything to its left is the left subtree, everything to its right is the right subtree.

> 💡 **Hint 2:** If the root is at index `k` in `inorder`, the left subtree has `k` nodes. So the left subtree's preorder is `preorder[1:k+1]` and its inorder is `inorder[:k]`. Recurse on both halves.

> 💡 **Hint 3:** Build a hashmap from value → inorder index upfront. This makes the "find root in inorder" step O(1) instead of O(n), bringing total time from O(n^2) to O(n).

## Approach

**Time Complexity:** O(n) with hashmap
**Space Complexity:** O(n) for the hashmap and recursion stack

Preorder's first element is the root. Use a hashmap to find its inorder index in O(1). Split both arrays at that index and recurse to build left and right subtrees.
