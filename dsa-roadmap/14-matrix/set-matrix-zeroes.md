# Set Matrix Zeroes

**Difficulty:** Medium
**Pattern:** Matrix / In-Place Marking
**LeetCode:** #73

## Problem Statement

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`s. You must do it in place.

## Examples

### Example 1
**Input:** `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
**Output:** `[[1,0,1],[0,0,0],[1,0,1]]`

### Example 2
**Input:** `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`
**Output:** `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`

## Constraints
- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** The naive approach: scan for zeros, then zero out rows and columns. But you need to be careful not to zero out cells that weren't originally zero.

> 💡 **Hint 2:** Use the first row and first column as markers. If matrix[i][j] == 0, mark matrix[i][0] = 0 and matrix[0][j] = 0. Then use these markers to zero out rows and columns.

> 💡 **Hint 3:** Handle the first row and first column separately (use two boolean flags to track if they originally contained zeros). Process the rest of the matrix using the markers.

## Approach

**Time Complexity:** O(m × n)
**Space Complexity:** O(1)

Use the first row and column as markers. Two passes: first to mark, second to zero out. Handle the first row/column separately with boolean flags.
