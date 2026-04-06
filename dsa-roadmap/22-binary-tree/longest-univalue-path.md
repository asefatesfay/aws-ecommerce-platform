# Longest Univalue Path

**Difficulty:** Medium
**Pattern:** DFS / Tree DP
**LeetCode:** #687

## Problem Statement

Given the root of a binary tree, return the length of the longest path where each node in the path has the same value. This path may or may not pass through the root. The length of the path between two nodes is represented by the number of edges between them.

## Examples

### Example 1
**Input:** `root = [5,4,5,1,1,null,5]`
**Output:** `2`
**Explanation:** The path 5→5→5 has length 2 (two edges).

### Example 2
**Input:** `root = [1,4,5,4,4,null,5]`
**Output:** `2`
**Explanation:** The path 4→4→4 has length 2.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`
- `-1000 <= Node.val <= 1000`
- The depth of the tree will not exceed `1000`

## Hints

> 💡 **Hint 1:** For each node, compute the longest univalue path going through it. This path can extend into the left subtree, the right subtree, or both (making a "V" shape through the node).

> 💡 **Hint 2:** The DFS function returns the longest univalue path that can be extended upward (i.e., a single arm, not a V). At each node, check if the left/right child has the same value — if so, extend the arm by 1.

> 💡 **Hint 3:** Use a global variable to track the maximum path seen so far. At each node, the candidate answer is `left_arm + right_arm` (the V-shape). The return value is `max(left_arm, right_arm)` (the single arm that can extend upward).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS returning the longest single-direction univalue arm. At each node, update a global max with `left_arm + right_arm`. Arms only extend when child values match the current node's value.
