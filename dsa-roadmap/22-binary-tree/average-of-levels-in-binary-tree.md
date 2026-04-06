# Average of Levels in Binary Tree

**Difficulty:** Easy
**Pattern:** BFS / Level Order Traversal
**LeetCode:** #637

## Problem Statement

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10^-5` of the actual answer will be accepted.

## Examples

### Example 1
**Input:** `root = [3,9,20,15,7]`
**Output:** `[3.00000, 14.50000, 11.00000]`
**Explanation:** Level 0: avg(3) = 3. Level 1: avg(9, 20) = 14.5. Level 2: avg(15, 7) = 11.

### Example 2
**Input:** `root = [3,9,20,15,7,null,null]`
**Output:** `[3.00000, 14.50000, 11.00000]`

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** This is a classic BFS level-order traversal. Use a queue and process nodes level by level.

> 💡 **Hint 2:** At the start of each level, record the queue size — that tells you exactly how many nodes belong to this level. Sum their values, then divide by the count.

> 💡 **Hint 3:** Watch out for integer overflow when summing values. Node values can be up to 2^31 - 1, and a level can have many nodes, so use a 64-bit integer or float for the running sum.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(w) where w is the maximum width of the tree

BFS with level snapshots: at each level, record queue size, sum all node values in that level, divide by count, and append to result.
