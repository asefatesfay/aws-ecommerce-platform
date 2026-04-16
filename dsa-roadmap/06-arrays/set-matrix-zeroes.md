# Set Matrix Zeroes

**Difficulty:** Medium
**Pattern:** In-Place Marking
**LeetCode:** #73
**Asked by:** Microsoft, Adobe, Google

## Problem Statement

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`. Do it in-place.

## Examples

### Example 1
**Input:**
```
[[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]
```
**Output:**
```
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
```

### Example 2
**Input:**
```
[[0, 1, 2, 0],
 [3, 4, 5, 2],
 [1, 3, 1, 5]]
```
**Output:**
```
[[0, 0, 0, 0],
 [0, 4, 5, 0],
 [0, 3, 1, 0]]
```

## Constraints
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Naive approach: collect all (row, col) positions of zeros, then zero out those rows and columns. This uses O(m+n) space.

> 💡 **Hint 2:** O(1) space trick: use the first row and first column as markers. If `matrix[i][j] == 0`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`.

> 💡 **Hint 3:** Handle the first row and first column separately with boolean flags, since they're used as markers and might get zeroed out themselves.

## Approach 1: Brute Force

**Time Complexity:** O(m² × n²)
**Space Complexity:** O(m × n)

For each zero found, scan its entire row and column to zero them out. Problem: zeroing a row/column might introduce new zeros that get processed again.

```python
def set_zeroes_brute(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    # First collect all zero positions
    zeros = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
    # Then zero out rows and columns
    for r, c in zeros:
        for j in range(n):
            matrix[r][j] = 0
        for i in range(m):
            matrix[i][c] = 0
```

---

## Approach 2: Extra Sets (O(m+n) Space)

**Time Complexity:** O(m × n)
**Space Complexity:** O(m + n)

Collect zero rows and columns in sets, then zero them out in a second pass.

```python
def set_zeroes_sets(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
```

---

## Approach 3: First Row/Col as Markers — Optimal

**Time Complexity:** O(m × n)
**Space Complexity:** O(1)

Use the first row and first column as marker arrays. Handle them separately with boolean flags since they're used as markers and might get zeroed themselves.

### Visual Trace

```
Input:
[[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]

Step 1: Check if first row/col have zeros.
  first_row_has_zero = False
  first_col_has_zero = False

Step 2: Scan rest of matrix (rows 1+, cols 1+).
  (1,1)=0 → mark matrix[1][0]=0, matrix[0][1]=0

After marking:
[[1, 0, 1],   ← col 1 marked
 [0, 0, 1],   ← row 1 marked
 [1, 1, 1]]

Step 3: Zero out cells based on markers (rows 1+, cols 1+).
  (1,1): row1 marked → 0. (1,2): row1 marked → 0.
  (2,1): col1 marked → 0.

Step 4: Handle first row/col (using saved flags).
  first_row_has_zero=False → skip.
  first_col_has_zero=False → skip.

Result:
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]] ✓
```

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    # Save whether first row/col originally had zeros
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row/col as markers for the rest
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out based on markers (skip first row/col)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle first row and col using saved flags
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(m²×n²) | O(m×n) | Re-processes zeros |
| Extra sets | O(m×n) | O(m+n) | Clean but uses extra space |
| First row/col markers | O(m×n) | O(1) | Optimal — in-place |

## Typical Interview Use Cases

- Very common at Microsoft/Adobe — tests in-place matrix manipulation
- The O(1) space solution is the expected answer in senior interviews
- Tests careful handling of edge cases (first row/col as markers)
