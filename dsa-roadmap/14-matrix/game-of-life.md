# Game of Life

**Difficulty:** Medium
**Pattern:** Matrix Simulation / In-Place
**LeetCode:** #289

## Problem Statement

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970." The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (1) or dead (0). Each cell interacts with its eight neighbors. Apply the following rules simultaneously to every cell:
1. Live cell with < 2 live neighbors → dies (underpopulation)
2. Live cell with 2 or 3 live neighbors → lives
3. Live cell with > 3 live neighbors → dies (overpopulation)
4. Dead cell with exactly 3 live neighbors → becomes alive (reproduction)

Return the next state of the board.

## Examples

### Example 1
**Input:** `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`
**Output:** `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

## Constraints
- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j]` is `0` or `1`

## Hints

> 💡 **Hint 1:** The naive approach uses a copy of the board. For in-place, you need to encode both old and new states in the same cell.

> 💡 **Hint 2:** Use extra bits: encode "was alive, now dead" as 2, "was dead, now alive" as 3 (or use negative values). Count neighbors using the original state (check if abs(cell) == 1 or cell & 1 == 1).

> 💡 **Hint 3:** After updating all cells with encoded states, do a second pass to decode: 2 → 0, 3 → 1, others stay.

## Approach

**Time Complexity:** O(m × n)
**Space Complexity:** O(1) with in-place encoding

Two-pass in-place: first pass encodes transitions using extra state values, second pass decodes to final 0/1 values.
