# Binary Tree Inorder Traversal

**Difficulty:** Easy
**Pattern:** DFS / Tree Traversal
**LeetCode:** #94

## Problem Statement

Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder visits: Left → Root → Right.

## Examples

### Example 1
**Input:** `root = [1,null,2,3]`
**Output:** `[1,3,2]`
**Explanation:** Go left (null), visit 1, go right to 2, go left to 3, visit 3, visit 2.

### Example 2
**Input:** `root = []`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** Recursive solution: recurse left, append root.val, recurse right. This is the simplest approach and directly mirrors the definition.

> 💡 **Hint 2:** Iterative solution: use a stack. Push nodes as you go left. When you can't go further left, pop a node, record its value, then move to its right child.

> 💡 **Hint 3:** The iterative pattern: `while node or stack: while node: stack.append(node); node = node.left; node = stack.pop(); result.append(node.val); node = node.right`. This simulates the call stack explicitly.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack or explicit stack

Recursive: left → root → right. Iterative: push all left nodes onto a stack, pop and record, then move right.
