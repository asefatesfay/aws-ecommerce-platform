# Delete Nodes and Return Forest

**Difficulty:** Medium
**Pattern:** DFS / Tree Modification
**LeetCode:** #1110

## Problem Statement

Given the root of a binary tree, each node in the tree has a distinct value. After deleting all nodes with values in `to_delete`, we are left with a forest (a disjoint union of trees). Return the roots of the trees in the remaining forest. You may return the result in any order.

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5,6,7]`, `to_delete = [3,5]`
**Output:** `[[1,2,null,4],[6],[7]]`
**Explanation:** Deleting 3 and 5 splits the tree into three separate trees.

### Example 2
**Input:** `root = [1,2,4,null,3]`, `to_delete = [3]`
**Output:** `[[1,2,4]]`

## Constraints
- The number of nodes in the tree is at most `1000`
- Each node has a distinct value between `1` and `1000`
- `to_delete.length <= 1000`

## Hints

> 💡 **Hint 1:** Convert `to_delete` to a set for O(1) lookup. Do a postorder DFS — process children before the parent so you can correctly handle disconnected subtrees.

> 💡 **Hint 2:** Pass an `is_root` flag down. A node is a root of a new tree if its parent was deleted (or it's the original root and not deleted). When a node is a root and not deleted, add it to the result.

> 💡 **Hint 3:** When you delete a node, its children become roots of new trees (if they exist). Return null from the DFS when a node is deleted, so the parent's pointer gets set to null automatically.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) for the delete set and result list

Postorder DFS with an `is_root` flag. When a node is deleted, add its non-null children to the result as new roots. Return null for deleted nodes so parent pointers are cleaned up.
