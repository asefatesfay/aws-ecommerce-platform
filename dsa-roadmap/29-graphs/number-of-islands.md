# Number of Islands

**Difficulty:** Medium
**Pattern:** DFS / BFS on Grid
**LeetCode:** #200

## Problem Statement
Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

## Examples

### Example 1
**Input:**
```
11110
11010
11000
00000
```
**Output:** `1`

### Example 2
**Input:**
```
11000
11000
00100
00011
```
**Output:** `3`

## Constraints
- `m, n` in range `[1, 300]`
- `grid[i][j]` is '0' or '1'

## Hints

> 💡 **Hint 1:** Iterate through every cell. When you find a '1', increment the island count and use DFS/BFS to mark all connected '1's as visited.

> 💡 **Hint 2:** Mark visited cells by changing '1' to '0' (or use a visited set) to avoid counting the same island twice.

> 💡 **Hint 3:** DFS explores all 4 directions (up, down, left, right) recursively. BFS uses a queue.

## Approach
**Time Complexity:** O(M × N)
**Space Complexity:** O(M × N) for recursion stack

For each unvisited '1', run DFS/BFS to sink the entire island (mark as '0'). Count how many times you start a new DFS/BFS.
