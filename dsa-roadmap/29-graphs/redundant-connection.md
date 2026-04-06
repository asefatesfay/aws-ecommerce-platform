# Redundant Connection

**Difficulty:** Medium
**Pattern:** Union-Find
**LeetCode:** #684

## Problem Statement
Given a graph that started as a tree with n nodes and one extra edge added, find and return that extra edge. If multiple answers exist, return the last one in the input.

## Examples

### Example 1
**Input:** `edges = [[1,2],[1,3],[2,3]]`
**Output:** `[2,3]`

### Example 2
**Input:** `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`
**Output:** `[1,4]`

## Constraints
- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`

## Hints

> 💡 **Hint 1:** Process edges one by one. Use Union-Find to track connected components.

> 💡 **Hint 2:** For each edge `[u, v]`, if `find(u) == find(v)`, they're already connected — this edge creates a cycle and is the answer.

> 💡 **Hint 3:** Otherwise, union them and continue.

## Approach
**Time Complexity:** O(N × α(N)) ≈ O(N)
**Space Complexity:** O(N)

Union-Find: process edges in order. The first edge where both endpoints are already in the same component is the redundant edge.
