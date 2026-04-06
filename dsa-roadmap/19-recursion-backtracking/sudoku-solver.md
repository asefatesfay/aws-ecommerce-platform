# Sudoku Solver

**Difficulty:** Hard
**Pattern:** Backtracking / Constraint Satisfaction
**LeetCode:** #37

## Problem Statement

Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.

The `'.'` character indicates empty cells.

## Examples

### Example 1
**Input:** A partially filled 9×9 board
**Output:** The same board filled with the solution

## Constraints
- `board.length == 9`, `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`
- It is guaranteed that the input board has only one solution

## Hints

> 💡 **Hint 1:** Find the first empty cell. Try placing digits 1-9. Check if the placement is valid (no conflict in row, column, or 3×3 box).

> 💡 **Hint 2:** If valid, place the digit and recurse. If the recursion returns true (solved), propagate true. If false, undo the placement (backtrack) and try the next digit.

> 💡 **Hint 3:** Precompute sets for each row, column, and box to enable O(1) validity checks. The box index for cell (r,c) is `(r//3)*3 + c//3`.

## Approach

**Time Complexity:** O(9^m) where m is the number of empty cells
**Space Complexity:** O(1) extra (modifying in-place)

Backtracking: find empty cell, try digits 1-9 with validity check, recurse, backtrack on failure.
