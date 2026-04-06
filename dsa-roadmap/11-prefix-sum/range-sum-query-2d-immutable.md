# Range Sum Query 2D - Immutable

**Difficulty:** Medium
**Pattern:** 2D Prefix Sum
**LeetCode:** #304

## Problem Statement

Given a 2D matrix `matrix`, handle multiple queries of the following type: calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

Implement the `NumMatrix` class with `sumRegion(row1, col1, row2, col2)` that returns the sum of elements in the rectangle.

## Examples

### Example 1
**Input:** Matrix is `[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]`
`sumRegion(2,1,4,3)` → `8`, `sumRegion(1,1,2,2)` → `11`, `sumRegion(1,2,2,4)` → `12`

## Constraints
- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^4 <= matrix[i][j] <= 10^4`
- At most `10^4` calls to `sumRegion`

## Hints

> 💡 **Hint 1:** Extend the 1D prefix sum to 2D. `prefix[i][j]` = sum of all elements in the rectangle from (0,0) to (i-1,j-1).

> 💡 **Hint 2:** Build: `prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]` (inclusion-exclusion).

> 💡 **Hint 3:** Query: `sumRegion(r1,c1,r2,c2) = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`.

## Approach

**Time Complexity:** O(mn) preprocessing, O(1) per query
**Space Complexity:** O(mn)

2D prefix sum with inclusion-exclusion formula for both building and querying.
