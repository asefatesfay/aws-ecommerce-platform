# Unique Paths II

**Difficulty:** Medium
**Pattern:** 2D Grid DP
**LeetCode:** #63

## Problem Statement
A robot moves on an `m x n` grid from top-left to bottom-right, moving only down or right.

Some cells are obstacles (`1`) that cannot be visited. Return the number of unique paths.

## Examples

### Example 1
**Input:** `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]`
**Output:** `2`

### Example 2
**Input:** `obstacleGrid = [[0,1],[0,0]]`
**Output:** `1`

## Constraints
- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`

## DP Breakdown
- **State:** `dp[r][c]` = number of ways to reach `(r, c)`
- If cell is obstacle, `dp[r][c] = 0`
- Else, `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`
- **Base case:** `dp[0][0] = 1` only if start is not blocked

## Hints
- Handle blocked start or blocked destination early.
- First row/column require careful obstacle propagation.
- 1D rolling DP works well here.

## Approach
**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

Traverse row by row and set `dp[c] = 0` when obstacle is found.