# Edit Distance

**Difficulty:** Medium
**Pattern:** 2D String DP
**LeetCode:** #72

## Problem Statement
Given two strings `word1` and `word2`, return the minimum number of operations (insert, delete, replace) to convert `word1` to `word2`.

## Examples

### Example 1
**Input:** `word1 = "horse"`, `word2 = "ros"`
**Output:** `3`
**Explanation:** horse → rorse (replace h→r) → rose (delete r) → ros (delete e)

### Example 2
**Input:** `word1 = "intention"`, `word2 = "execution"`
**Output:** `5`

## Constraints
- `0 <= word1.length, word2.length <= 500`
- Only lowercase English letters

## Hints

> 💡 **Hint 1:** `dp[i][j]` = min operations to convert `word1[:i]` to `word2[:j]`.

> 💡 **Hint 2:** If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]` (no operation needed). Otherwise: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` (delete, insert, replace).

> 💡 **Hint 3:** Base cases: `dp[i][0] = i` (delete all), `dp[0][j] = j` (insert all).

## Approach
**Time Complexity:** O(M × N)
**Space Complexity:** O(M × N)

Classic 2D DP. Three choices at each mismatch: insert, delete, or replace — take the minimum.
