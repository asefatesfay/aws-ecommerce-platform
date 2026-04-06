# Spiral Matrix

**Difficulty:** Medium
**Pattern:** Matrix Traversal / Boundary Simulation
**LeetCode:** #54

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order.

## Examples

### Example 1
**Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[1,2,3,6,9,8,7,4,5]`

### Example 2
**Input:** `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
**Output:** `[1,2,3,4,8,12,11,10,9,5,6,7]`

## Constraints
- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Hints

> 💡 **Hint 1:** Maintain four boundaries: top, bottom, left, right. Traverse the outermost layer, then shrink the boundaries inward.

> 💡 **Hint 2:** Four traversals per layer: left→right along top row, top→bottom along right column, right→left along bottom row, bottom→top along left column. After each traversal, shrink the corresponding boundary.

> 💡 **Hint 3:** Check that the boundary is still valid before each traversal (e.g., top ≤ bottom before traversing bottom row left-to-right).

## Approach

**Time Complexity:** O(m × n)
**Space Complexity:** O(1) extra (output not counted)

Boundary simulation: maintain top/bottom/left/right pointers. Traverse each side and shrink boundaries until all elements are visited.
