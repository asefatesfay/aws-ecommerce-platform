# Find Duplicate Subtrees

**Difficulty:** Medium
**Pattern:** DFS / Tree Serialization / Hash Map
**LeetCode:** #652

## Problem Statement

Given the root of a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them. Two trees are duplicate if they have the same structure with the same node values.

## Examples

### Example 1
**Input:** `root = [1,2,3,4,null,2,4,null,null,4]`
**Output:** `[[2,4],[4]]`
**Explanation:** The subtree rooted at the second 2 (with child 4) duplicates the first. The leaf 4 appears three times.

### Example 2
**Input:** `root = [2,1,1]`
**Output:** `[[1]]`

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`
- `-200 <= Node.val <= 200`

## Hints

> 💡 **Hint 1:** Serialize each subtree to a unique string. Two subtrees are duplicates if and only if their serializations are equal.

> 💡 **Hint 2:** Do a postorder DFS. At each node, build the serialization as `"left_serial,right_serial,node.val"`. Store each serialization in a hashmap with its count.

> 💡 **Hint 3:** When a serialization's count reaches exactly 2, add the current node to the result (count == 2 ensures you add it only once, not for every additional duplicate).

## Approach

**Time Complexity:** O(n^2) due to string operations (O(n) with hashing optimization)
**Space Complexity:** O(n^2) for storing all serializations

Postorder DFS building subtree serializations. Use a hashmap to count occurrences of each serialization. Add a node to results when its serialization count reaches 2.
