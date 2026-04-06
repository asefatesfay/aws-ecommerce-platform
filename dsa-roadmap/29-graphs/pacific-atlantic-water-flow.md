# Pacific Atlantic Water Flow

**Difficulty:** Medium
**Pattern:** Multi-Source BFS/DFS
**LeetCode:** #417

## Problem Statement
Given an `m × n` matrix of heights, water can flow to adjacent cells with equal or lower height. The Pacific ocean touches the top/left edges, Atlantic touches bottom/right. Return all cells from which water can flow to both oceans.

## Examples

### Example 1
**Input:** `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
**Output:** `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

## Constraints
- `m, n` in range `[1, 200]`
- `0 <= heights[i][j] <= 10⁵`

## Hints

> 💡 **Hint 1:** Instead of flowing water downhill from each cell, reverse the problem: flow water uphill from each ocean.

> 💡 **Hint 2:** BFS/DFS from all Pacific border cells (top row + left column) — mark cells reachable going uphill. Do the same from Atlantic border cells.

> 💡 **Hint 3:** Cells in both reachable sets are the answer.

## Approach
**Time Complexity:** O(M × N)
**Space Complexity:** O(M × N)

Two multi-source BFS/DFS — one from Pacific borders, one from Atlantic borders. Intersection of reachable cells is the answer.
