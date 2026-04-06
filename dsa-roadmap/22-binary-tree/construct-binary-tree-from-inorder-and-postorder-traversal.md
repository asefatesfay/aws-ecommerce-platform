# Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium
**Pattern:** Divide and Conquer / Tree Construction
**LeetCode:** #106

## Problem Statement

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

## Examples

### Example 1
**Input:** `inorder = [9,3,15,20,7]`, `postorder = [9,15,7,20,3]`
**Output:** `[3,9,20,null,null,15,7]`
**Explanation:** Root is 3 (last in postorder). In inorder, 3 is at index 1, so left has 1 node [9] and right has 2 nodes [15,7].

### Example 2
**Input:** `inorder = [-1]`, `postorder = [-1]`
**Output:** `[-1]`

## Constraints
- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- All values are unique

## Hints

> 💡 **Hint 1:** The last element of `postorder` is always the root (postorder = Left → Right → Root). Find that value in `inorder` to split left and right subtrees.

> 💡 **Hint 2:** If the root is at index `k` in `inorder`, the left subtree has `k` nodes. The right subtree's postorder is `postorder[k:-1]` and the left's is `postorder[:k]`. Process right subtree first (pop from end of postorder).

> 💡 **Hint 3:** Use a hashmap for O(1) inorder lookups. Process postorder from right to left (root, then right subtree, then left subtree) to avoid slicing arrays.

## Approach

**Time Complexity:** O(n) with hashmap
**Space Complexity:** O(n) for the hashmap and recursion stack

Postorder's last element is the root. Use a hashmap to find its inorder index. Split both arrays and recurse — build right subtree before left (postorder processes right before left when read backwards).
