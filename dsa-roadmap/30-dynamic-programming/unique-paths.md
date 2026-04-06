# Unique Paths

**Difficulty:** Medium
**Pattern:** 2D Grid DP
**LeetCode:** #62

## Problem Statement
A robot is located at the top-left corner of an `m x n` grid. It can only move either down or right at any point in time.

Return the number of possible unique paths to reach the bottom-right corner.

## Examples

### Example 1
**Input:** `m = 3, n = 7`
**Output:** `28`

### Example 2
**Input:** `m = 3, n = 2`
**Output:** `3`

## Constraints
- `1 <= m, n <= 100`

## DP Breakdown
- **State:** `dp[r][c]` = number of paths to cell `(r, c)`
- **Transition:** `dp[r][c] = dp[r - 1][c] + dp[r][c - 1]`
- **Base cases:** first row and first column are all `1`

## Hints
- To enter a cell, you must come from top or left.
- Initialize border cells first.
- Space can be optimized to 1D array.

## Approach
**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

Use 1D DP where `dp[c]` represents current row's number of paths to column `c`.