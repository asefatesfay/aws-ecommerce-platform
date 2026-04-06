# Combination Sum III

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #216

## Problem Statement

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true: Only numbers `1` through `9` are used. Each number is used at most once. Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

## Examples

### Example 1
**Input:** `k = 3`, `n = 7`
**Output:** `[[1,2,4]]`

### Example 2
**Input:** `k = 3`, `n = 9`
**Output:** `[[1,2,6],[1,3,5],[2,3,4]]`

## Constraints
- `2 <= k <= 9`
- `1 <= n <= 60`

## Hints

> 💡 **Hint 1:** Backtracking with a start number (1-9), current combination, and remaining sum.

> 💡 **Hint 2:** When the combination has k numbers and sum equals n, add to results.

> 💡 **Hint 3:** Prune: if remaining < 0 or combination size > k, stop. Start from the previous number + 1 to avoid reuse.

## Approach

**Time Complexity:** O(C(9,k) × k)
**Space Complexity:** O(k)

Backtracking over digits 1-9 with size and sum constraints.
