# Increment Submatrices by One

**Difficulty:** Medium
**Pattern:** 2D Difference Array
**LeetCode:** #2536

## Problem Statement

You are given a positive integer `n`, indicating that we initially have an `n x n` 0-indexed integer matrix `mat` filled with zeroes. You are also given a 2D integer array `query`. For each `query[i] = [row1i, col1i, row2i, col2i]`, you should increment all the elements in the submatrix from `(row1i, col1i)` to `(row2i, col2i)` by 1. Return `mat` after performing all the queries.

## Examples

### Example 1
**Input:** `n = 3`, `queries = [[1,1,2,2],[0,0,1,1]]`
**Output:** `[[1,1,0],[1,2,1],[0,1,1]]`

### Example 2
**Input:** `n = 2`, `queries = [[0,0,1,1]]`
**Output:** `[[1,1],[1,1]]`

## Constraints
- `1 <= n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1i <= row2i < n`
- `0 <= col1i <= col2i < n`

## Hints

> 💡 **Hint 1:** Applying each query naively is O(n²) per query. Use a 2D difference array for O(1) updates.

> 💡 **Hint 2:** For a 2D difference array, to increment rectangle (r1,c1) to (r2,c2): add 1 at (r1,c1), subtract 1 at (r1,c2+1), subtract 1 at (r2+1,c1), add 1 at (r2+1,c2+1).

> 💡 **Hint 3:** After all queries, compute the 2D prefix sum of the difference array to get the final matrix.

## Approach

**Time Complexity:** O(q + n²) where q = number of queries
**Space Complexity:** O(n²)

2D difference array for O(1) range updates, then 2D prefix sum to reconstruct the final matrix.
