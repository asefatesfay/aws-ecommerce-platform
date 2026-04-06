# Candy Crush

**Difficulty:** Medium
**Pattern:** Matrix Simulation
**LeetCode:** #723

## Problem Statement

This question is about implementing a basic elimination algorithm for Candy Crush. Given a 2D integer array `board` representing the grid of candy, you need to do the following steps repeatedly until the board becomes stable:
1. Mark all cells that have 3 or more identical candies in a row (horizontally or vertically) for crushing.
2. Crush all marked cells simultaneously (set to 0).
3. Drop the remaining candies downward (gravity).

Return the final stable board.

## Examples

### Example 1
**Input:** `board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]`
**Output:** `[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]`

## Constraints
- `m == board.length`, `n == board[i].length`
- `3 <= m, n <= 50`
- `1 <= board[i][j] <= 2000`

## Hints

> 💡 **Hint 1:** Simulate the process in a loop. Each iteration: mark cells to crush, crush them, apply gravity. Repeat until no cells are marked.

> 💡 **Hint 2:** For marking: scan horizontally and vertically for runs of 3+ identical non-zero values. Mark them (e.g., negate the value).

> 💡 **Hint 3:** For gravity: for each column, collect non-zero values from bottom to top, then fill the column from bottom with those values and zeros above.

## Approach

**Time Complexity:** O((m × n)²) in the worst case
**Space Complexity:** O(1) extra

Simulate: mark (scan for runs of 3+), crush (set marked to 0), drop (gravity per column). Repeat until stable.
