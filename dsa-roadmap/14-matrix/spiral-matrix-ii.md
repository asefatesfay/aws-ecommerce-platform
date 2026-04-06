# Spiral Matrix II

**Difficulty:** Medium
**Pattern:** Matrix Traversal / Boundary Simulation
**LeetCode:** #59

## Problem Statement

Given a positive integer `n`, generate an `n x n` matrix filled with elements from `1` to `n²` in spiral order.

## Examples

### Example 1
**Input:** `n = 3`
**Output:** `[[1,2,3],[8,9,4],[7,6,5]]`

### Example 2
**Input:** `n = 1`
**Output:** `[[1]]`

## Constraints
- `1 <= n <= 20`

## Hints

> 💡 **Hint 1:** This is the inverse of Spiral Matrix I — instead of reading in spiral order, you're writing in spiral order.

> 💡 **Hint 2:** Use the same boundary simulation approach. Maintain top/bottom/left/right boundaries. Fill numbers 1 to n² in spiral order.

> 💡 **Hint 3:** Use a counter starting at 1. Fill each boundary traversal with consecutive numbers, shrinking boundaries after each side.

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(n²) for the output matrix

Same boundary simulation as Spiral Matrix I, but writing values 1..n² instead of reading them.
