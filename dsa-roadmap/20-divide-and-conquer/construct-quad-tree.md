# Construct Quad Tree

**Difficulty:** Medium
**Pattern:** Divide and Conquer
**LeetCode:** #427

## Problem Statement

Given a `n * n` matrix `grid` of `0`'s and `1`'s only, we want to represent the `grid` with a Quad-Tree. Return the root of the Quad-Tree representing the `grid`. A Quad-Tree is a tree data structure in which each internal node has exactly four children. Each node has two attributes: `val` (True if the node represents a grid of all 1's or if it is a leaf node, False otherwise) and `isLeaf` (True if the node is a leaf node, False otherwise). We can construct a Quad-Tree from a two-dimensional area using the following steps: If the current grid has the same value (all 1's or all 0's), set `isLeaf` True and set `val` to the value of the grid and set the four children to Null. If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids.

## Examples

### Example 1
**Input:** `grid = [[0,1],[1,0]]`
**Output:** `[[0,1],[1,0],[1,1],[1,1],[1,0]]`

## Constraints
- `n == grid.length == grid[i].length`
- `n == 2^x` where `0 <= x <= 6`

## Hints

> 💡 **Hint 1:** Recursively process each quadrant. Base case: 1×1 grid is always a leaf.

> 💡 **Hint 2:** For a region, check if all values are the same. If yes, create a leaf node. If no, divide into four quadrants and recurse.

> 💡 **Hint 3:** Use a 2D prefix sum to efficiently check if a region is uniform (all same value) in O(1).

## Approach

**Time Complexity:** O(n² log n) with prefix sum, O(n² log² n) without
**Space Complexity:** O(log n) recursion depth

Divide and conquer: check uniformity, create leaf or split into four quadrants and recurse.
