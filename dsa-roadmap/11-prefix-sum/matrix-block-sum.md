# Matrix Block Sum

**Difficulty:** Medium
**Pattern:** 2D Prefix Sum
**LeetCode:** #1314

## Problem Statement

Given a `m x n` matrix `mat` and an integer `k`, return a matrix `answer` where each `answer[i][j]` is the sum of all elements `mat[r][c]` for `i - k <= r <= i + k` and `j - k <= c <= j + k`.

## Examples

### Example 1
**Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
**Output:** `[[12,21,16],[27,45,33],[24,39,28]]`

### Example 2
**Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 2`
**Output:** `[[45,45,45],[45,45,45],[45,45,45]]`

## Constraints
- `m == mat.length`, `n == mat[i].length`
- `1 <= m, n, k <= 100`
- `1 <= mat[i][j] <= 100`

## Hints

> 💡 **Hint 1:** For each cell (i,j), you need the sum of a rectangular block. This is a 2D range sum query.

> 💡 **Hint 2:** Build a 2D prefix sum of `mat`. Then for each (i,j), compute the block sum using the prefix sum formula with clamped boundaries.

> 💡 **Hint 3:** The block for (i,j) spans rows [max(0,i-k), min(m-1,i+k)] and columns [max(0,j-k), min(n-1,j+k)]. Use the 2D prefix sum query formula on these clamped bounds.

## Approach

**Time Complexity:** O(mn)
**Space Complexity:** O(mn)

Build 2D prefix sum, then for each cell compute the block sum using the prefix sum formula with boundary clamping.
