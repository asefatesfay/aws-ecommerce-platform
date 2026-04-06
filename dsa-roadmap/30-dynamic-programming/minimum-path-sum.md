# Minimum Path Sum

**Difficulty:** Medium
**Pattern:** 2D Grid DP
**LeetCode:** #64

## Problem Statement
Given an `m x n` grid filled with non-negative numbers, find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.

You can only move right or down.

## Examples

### Example 1
**Input:** `grid = [[1,3,1],[1,5,1],[4,2,1]]`
**Output:** `7`

### Example 2
**Input:** `grid = [[1,2,3],[4,5,6]]`
**Output:** `12`

## Constraints
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 100`

## DP Breakdown
- **State:** `dp[r][c]` = minimum path sum to reach `(r, c)`
- **Transition:** `dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])`
- **Base case:** `dp[0][0] = grid[0][0]`

## Hints
- This is shortest path on DAG-like movement constraints.
- Initialize first row and first column separately.
- Use 1D DP to reduce space.

## Approach
**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

Use rolling row DP where each cell stores current minimum cumulative sum.