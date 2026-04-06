# Search in a Binary Search Tree

**Difficulty:** Easy
**Pattern:** BST Search
**LeetCode:** #700

## Problem Statement

You are given the root of a binary search tree (BST) and an integer `val`. Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

## Examples

### Example 1
**Input:** `root = [4,2,7,1,3]`, `val = 2`
**Output:** `[2,1,3]`
**Explanation:** The node with value 2 is found; return the subtree rooted at it.

### Example 2
**Input:** `root = [4,2,7,1,3]`, `val = 5`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree
- `1 <= val <= 10^7`

## Hints

> 💡 **Hint 1:** Use the BST property: if `val < node.val`, the target must be in the left subtree. If `val > node.val`, it's in the right subtree. If equal, you found it.

> 💡 **Hint 2:** This is a simple recursive or iterative search. Iterative is preferred to avoid stack overhead: `while node: if val == node.val: return node; elif val < node.val: node = node.left; else: node = node.right`.

> 💡 **Hint 3:** Return null if you reach a null node without finding the value.

## Approach

**Time Complexity:** O(h) where h is the height (O(log n) balanced, O(n) worst case)
**Space Complexity:** O(1) iterative, O(h) recursive

Iterative BST search: compare val with current node, go left if smaller, right if larger, return node if equal.
