# Spiral Matrix

**Difficulty:** Medium
**Pattern:** Simulation / Layer Peeling
**LeetCode:** #54
**Asked by:** Microsoft, Google, Adobe

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order (clockwise from the top-left).

## Examples

### Example 1
**Input:**
```
matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
```
**Output:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

```
→ → →
      ↓
← ← ↓
↑   ↓
↑ ← ←
```

### Example 2
**Input:**
```
matrix = [[1,  2,  3,  4],
           [5,  6,  7,  8],
           [9, 10, 11, 12]]
```
**Output:** `[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]`

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Hints

> 💡 **Hint 1:** Think of the matrix as concentric layers. Process the outermost layer first (top row → right col → bottom row → left col), then shrink the boundaries and repeat.

> 💡 **Hint 2:** Maintain four boundaries: `top`, `bottom`, `left`, `right`. After traversing each side, shrink the corresponding boundary inward.

> 💡 **Hint 3:** Be careful about single-row or single-column cases — after traversing the top row, check if `top <= bottom` before traversing the bottom row.

## Approach 1: Brute Force

**Time Complexity:** O(m × n × max(m,n))
**Space Complexity:** O(m × n)

Simulate the spiral by tracking direction and visited cells.

```python
def spiral_order_brute(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    result = []
    # directions: right, down, left, up
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0

    for _ in range(m * n):
        result.append(matrix[r][c])
        visited[r][c] = True
        nr, nc = r + dr[di], c + dc[di]
        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
            r, c = nr, nc
        else:
            di = (di + 1) % 4  # turn
            r, c = r + dr[di], c + dc[di]
    return result
```

**Downside:** Uses O(m×n) extra space for the visited array.

---

## Approach 2: Layer Peeling (Boundary Shrinking) — Optimal

**Time Complexity:** O(m × n)
**Space Complexity:** O(1) extra

Maintain four boundaries (`top`, `bottom`, `left`, `right`). Traverse each side, then shrink the boundary inward. No visited array needed.

### Visual Trace

```
matrix = [[1,2,3],[4,5,6],[7,8,9]]
top=0, bottom=2, left=0, right=2

Round 1:
  Top row   (top=0, left→right):   1,2,3  → top=1
  Right col (right=2, top→bottom): 6,9    → right=1
  Bottom row(bottom=2, right→left):8,7    → bottom=1  (check top<=bottom first)
  Left col  (left=0, bottom→top):  4      → left=1    (check left<=right first)

Round 2:
  top=1, bottom=1, left=1, right=1
  Top row: 5 → top=2
  top(2) > bottom(1) → stop

Result: [1,2,3,6,9,8,7,4,5] ✓
```

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):       # → top row
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):        # ↓ right col
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:                          # ← bottom row
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:                          # ↑ left col
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Direction + visited | O(m×n) | O(m×n) | Extra visited array |
| Layer peeling | O(m×n) | O(1) | Optimal — no extra space |

## Follow-up: Spiral Matrix II — #59 (Microsoft/Adobe)

Generate an `n x n` matrix filled with elements 1 to n² in spiral order.

```python
def generate_matrix(n: int) -> list[list[int]]:
    """
    n=3 →
    [[1,2,3],
     [8,9,4],
     [7,6,5]]
    """
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = num; num += 1
        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = num; num += 1
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num; num += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num; num += 1
            left += 1

    return matrix
```

## Follow-up: Rotate Image — #48 (Microsoft/Google/Adobe)

Rotate an n×n matrix 90 degrees clockwise in-place.

```python
def rotate(matrix: list[list[int]]) -> None:
    """
    [[1,2,3],    [[7,4,1],
     [4,5,6],  →  [8,5,2],
     [7,8,9]]      [9,6,3]]
    
    Trick: transpose then reverse each row.
    """
    n = len(matrix)
    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
```

## Typical Interview Use Cases

- Very common at Microsoft/Adobe — tests careful boundary management
- Often asked as "implement without extra space"
- Rotate Image and Spiral Matrix II are common follow-ups in the same session
