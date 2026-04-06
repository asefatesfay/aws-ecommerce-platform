# Path Sum III

**Difficulty:** Medium
**Pattern:** DFS / Prefix Sum
**LeetCode:** #437

## Problem Statement

Given the root of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`. The path does not need to start or end at the root or a leaf, but it must go downward (traveling only from parent nodes to child nodes).

## Examples

### Example 1
**Input:** `root = [10,5,-3,3,2,null,11,3,-2,null,1]`, `targetSum = 8`
**Output:** `3`
**Explanation:** Paths summing to 8: 5→3, 5→2→1, -3→11.

### Example 2
**Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]`, `targetSum = 22`
**Output:** `3`

## Constraints
- The number of nodes in the tree is in the range `[0, 1000]`
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`

## Hints

> 💡 **Hint 1:** Think of prefix sums on a path from root to current node. If `prefix_sum[j] - prefix_sum[i] == targetSum`, then the subpath from node i+1 to node j sums to targetSum.

> 💡 **Hint 2:** Use a hashmap to store the count of each prefix sum seen on the current root-to-node path. At each node, check if `current_prefix_sum - targetSum` exists in the map — each occurrence is a valid path ending here.

> 💡 **Hint 3:** After recursing into children, remove the current node's prefix sum from the map (decrement count). This is the backtracking step — the prefix sum is only valid for paths going through the current node.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack and prefix sum map

DFS with a prefix sum hashmap. At each node, count how many previous prefix sums equal `current_sum - targetSum`. Add current sum to map, recurse, then remove it (backtrack).
