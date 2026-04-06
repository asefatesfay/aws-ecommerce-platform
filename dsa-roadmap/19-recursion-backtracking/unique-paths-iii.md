# Unique Paths III

**Difficulty:** Hard
**Pattern:** Backtracking / DFS
**LeetCode:** #980

## Problem Statement

You are given an `m x n` integer array `grid` where `grid[i][j]` could be: `1` representing the starting square (exactly one), `2` representing the ending square (exactly one), `0` representing empty squares we can walk over, `-1` representing obstacles that we cannot walk over. Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

## Examples

### Example 1
**Input:** `grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]`
**Output:** `2`

### Example 2
**Input:** `grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]`
**Output:** `4`

## Constraints
- `m == grid.length`, `n == grid[i].length`
- `1 <= m, n <= 20`
- `1 <= m * n <= 20`
- `-1 <= grid[i][j] <= 2`
- There is exactly one starting cell and one ending cell

## Hints

> 💡 **Hint 1:** Count the total non-obstacle cells (including start and end). A valid path must visit all of them.

> 💡 **Hint 2:** DFS/backtracking from the start. Mark cells as visited. When you reach the end, check if all non-obstacle cells were visited.

> 💡 **Hint 3:** Unmark cells when backtracking. Count valid complete paths.

## Approach

**Time Complexity:** O(4^(m×n))
**Space Complexity:** O(m×n)

DFS with backtracking. Count non-obstacle cells. A path is valid when it reaches the end having visited all non-obstacle cells.
