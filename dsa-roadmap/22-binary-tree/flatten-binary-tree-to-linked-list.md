# Flatten Binary Tree to Linked List

**Difficulty:** Medium
**Pattern:** DFS / Tree Modification
**LeetCode:** #114

## Problem Statement

Given the root of a binary tree, flatten the tree into a "linked list" in-place. The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`. The linked list should be in the same order as a preorder traversal of the binary tree.

## Examples

### Example 1
**Input:** `root = [1,2,5,3,4,null,6]`
**Output:** `[1,null,2,null,3,null,4,null,5,null,6]`
**Explanation:** Preorder: 1,2,3,4,5,6. Each node's right points to the next, left is null.

### Example 2
**Input:** `root = []`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`
- `-100 <= Node.val <= 100`

## Hints

> 💡 **Hint 1:** The flattened order is preorder (root, left, right). After flattening, the right pointer of each node points to the next preorder node.

> 💡 **Hint 2:** Key insight: for any node, the tail of the flattened left subtree should connect to the head of the right subtree. Flatten left, flatten right, then wire: `node.right = flattened_left`, `tail_of_left.right = original_right`.

> 💡 **Hint 3:** Morris traversal approach (O(1) space): for each node with a left child, find the rightmost node of the left subtree. Connect it to the right child. Move the left subtree to the right. Set left to null. Repeat.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for recursion, O(1) for Morris traversal

Recursive: flatten left and right subtrees, then rewire so the flattened left subtree comes before the flattened right subtree. Or use Morris traversal for O(1) space.
