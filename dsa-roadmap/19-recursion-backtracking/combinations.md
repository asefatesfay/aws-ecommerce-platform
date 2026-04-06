# Combinations

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #77

## Problem Statement

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`. You may return the answer in any order.

## Examples

### Example 1
**Input:** `n = 4`, `k = 2`
**Output:** `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`

### Example 2
**Input:** `n = 1`, `k = 1`
**Output:** `[[1]]`

## Constraints
- `1 <= n <= 20`
- `1 <= k <= n`

## Hints

> 💡 **Hint 1:** Backtracking with a start number. At each step, choose a number from start to n.

> 💡 **Hint 2:** When the combination has k numbers, add to results.

> 💡 **Hint 3:** Pruning: if the remaining numbers available (n - start + 1) are fewer than the remaining slots needed (k - current_size), stop early.

## Approach

**Time Complexity:** O(C(n,k) × k)
**Space Complexity:** O(k)

Backtracking with start index and pruning when not enough numbers remain.
