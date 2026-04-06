# Serialize and Deserialize Binary Tree

**Difficulty:** Hard
**Pattern:** BFS / DFS / Tree Encoding
**LeetCode:** #297

## Problem Statement

Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a data structure into a sequence of bits so that it can be stored or transmitted. Deserialization is the reverse process. There is no restriction on how your serialization/deserialization algorithm should work — just ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

## Examples

### Example 1
**Input:** `root = [1,2,3,null,null,4,5]`
**Output:** `[1,2,3,null,null,4,5]`
**Explanation:** Serialize to a string, then deserialize back to the same tree.

### Example 2
**Input:** `root = []`
**Output:** `[]`

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`
- `-1000 <= Node.val <= 1000`

## Hints

> 💡 **Hint 1:** For serialization, do a preorder DFS. Represent null nodes explicitly (e.g., "N"). Join values with a delimiter like ",". Example: tree [1,2,3] → "1,2,N,N,3,N,N".

> 💡 **Hint 2:** For deserialization, split the string by the delimiter to get a list of tokens. Use a pointer (or convert to a deque and popleft). Recursively build: if current token is "N", return null; otherwise create a node and recurse for left then right.

> 💡 **Hint 3:** BFS serialization also works: encode level by level, including nulls. Deserialization uses a queue of parent nodes — for each parent, the next two tokens are its left and right children.

## Approach

**Time Complexity:** O(n) for both serialize and deserialize
**Space Complexity:** O(n) for the string and recursion stack

Preorder DFS serialization with explicit null markers. Deserialization uses a deque of tokens, consuming one token per recursive call to reconstruct the tree.
