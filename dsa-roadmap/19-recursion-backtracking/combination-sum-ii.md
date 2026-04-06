# Combination Sum II

**Difficulty:** Medium
**Pattern:** Backtracking (with Duplicates)
**LeetCode:** #40

## Problem Statement

Given a collection of candidate numbers `candidates` and a target number `target`, find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution set must not contain duplicate combinations.

## Examples

### Example 1
**Input:** `candidates = [10,1,2,7,6,1,5]`, `target = 8`
**Output:** `[[1,1,6],[1,2,5],[1,7],[2,6]]`

### Example 2
**Input:** `candidates = [2,5,2,1,2]`, `target = 5`
**Output:** `[[1,2,2],[5]]`

## Constraints
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Hints

> 💡 **Hint 1:** Sort the candidates first. This groups duplicates together and enables pruning.

> 💡 **Hint 2:** Use a start index. Each element can only be used once (advance start by 1 after choosing).

> 💡 **Hint 3:** Skip duplicates at the same recursion level: if `i > start` and `candidates[i] == candidates[i-1]`, skip. This prevents duplicate combinations.

## Approach

**Time Complexity:** O(2^n)
**Space Complexity:** O(n) recursion depth

Sort + backtracking. Skip duplicate values at the same level. Each element used at most once.
