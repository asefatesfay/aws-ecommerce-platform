# Rotate Image

**Difficulty:** Medium
**Pattern:** Matrix Manipulation / In-Place
**LeetCode:** #48

## Problem Statement

You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix and do the rotation.

## Examples

### Example 1
**Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[[7,4,1],[8,5,2],[9,6,3]]`

### Example 2
**Input:** `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]`
**Output:** `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]`

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

> 💡 **Hint 1:** A 90° clockwise rotation can be decomposed into two simpler operations.

> 💡 **Hint 2:** First transpose the matrix (swap matrix[i][j] with matrix[j][i] for i < j). Then reverse each row.

> 💡 **Hint 3:** Alternatively, reverse the entire matrix (flip upside down), then transpose. Both achieve 90° clockwise rotation.

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Transpose in-place (swap across main diagonal), then reverse each row. Two O(n²) passes, no extra space.
