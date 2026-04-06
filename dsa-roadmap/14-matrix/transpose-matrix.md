# Transpose Matrix

**Difficulty:** Easy
**Pattern:** Matrix Manipulation
**LeetCode:** #867

## Problem Statement

Given a 2D integer array `matrix`, return the transpose of `matrix`. The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

## Examples

### Example 1
**Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[[1,4,7],[2,5,8],[3,6,9]]`

### Example 2
**Input:** `matrix = [[1,2,3],[4,5,6]]`
**Output:** `[[1,4],[2,5],[3,6]]`

## Constraints
- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `-10^9 <= matrix[i][j] <= 10^9`

## Hints

> 💡 **Hint 1:** The transpose swaps rows and columns: `result[j][i] = matrix[i][j]`.

> 💡 **Hint 2:** The result has dimensions n × m (swapped from m × n). Create a new matrix of the right size.

> 💡 **Hint 3:** For square matrices, you can transpose in-place by swapping `matrix[i][j]` with `matrix[j][i]` for all i < j.

## Approach

**Time Complexity:** O(m × n)
**Space Complexity:** O(m × n) for the output (O(1) extra for square in-place)

Create result[n][m] and set `result[j][i] = matrix[i][j]` for all valid i, j.
