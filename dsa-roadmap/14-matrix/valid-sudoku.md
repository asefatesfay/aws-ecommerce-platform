# Valid Sudoku

**Difficulty:** Medium
**Pattern:** Hash Set / Matrix Validation
**LeetCode:** #36

## Problem Statement

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

Note: A Sudoku board could be valid but not necessarily solvable.

## Examples

### Example 1
**Input:** A partially filled 9×9 board
**Output:** `true` (if no rule is violated)

### Example 2
**Input:** A board with a repeated digit in a row
**Output:** `false`

## Constraints
- `board.length == 9`, `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`

## Hints

> 💡 **Hint 1:** Use three sets of HashSets: one for rows, one for columns, one for 3×3 boxes. For each cell, check if the digit already exists in the corresponding row, column, and box.

> 💡 **Hint 2:** The box index for cell (r, c) is `(r // 3) * 3 + (c // 3)`.

> 💡 **Hint 3:** Single pass through all 81 cells. For each non-empty cell, check all three sets and add to them. Return false on any duplicate.

## Approach

**Time Complexity:** O(1) — fixed 9×9 board
**Space Complexity:** O(1) — fixed size sets

Single pass with three arrays of HashSets (9 rows, 9 columns, 9 boxes). Check and record each digit.
