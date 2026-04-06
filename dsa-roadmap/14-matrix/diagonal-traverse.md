# Diagonal Traverse

**Difficulty:** Medium
**Pattern:** Matrix Traversal / Direction Simulation
**LeetCode:** #498

## Problem Statement

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

## Examples

### Example 1
**Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[1,2,4,7,5,3,6,8,9]`
**Explanation:** Diagonals: [1], [2,4], [3,5,7], [6,8], [9] — alternating up-right and down-left.

### Example 2
**Input:** `mat = [[1,2],[3,4]]`
**Output:** `[1,2,3,4]`

## Constraints
- `m == mat.length`, `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

## Hints

> 💡 **Hint 1:** Diagonals alternate direction: odd diagonals go up-right, even diagonals go down-left (or vice versa depending on indexing).

> 💡 **Hint 2:** Track the current direction. When you hit a boundary, change direction and adjust position. The boundary handling is the tricky part.

> 💡 **Hint 3:** Alternatively, collect all diagonals (elements with the same i+j sum belong to the same diagonal), then reverse alternate diagonals and concatenate.

## Approach

**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n) for output

Simulate the diagonal traversal with direction tracking, or group by diagonal index (i+j) and reverse alternating groups.
