# Longest Common Subsequence

**Difficulty:** Medium
**Pattern:** 2D String DP
**LeetCode:** #1143

## Problem Statement
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence derived by deleting some characters without changing the order.

## Examples

### Example 1
**Input:** `text1 = "abcde"`, `text2 = "ace"`
**Output:** `3`
**Explanation:** "ace" is the LCS.

### Example 2
**Input:** `text1 = "abc"`, `text2 = "abc"`
**Output:** `3`

### Example 3
**Input:** `text1 = "abc"`, `text2 = "def"`
**Output:** `0`

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- Only lowercase English letters

## Hints

> 💡 **Hint 1:** `dp[i][j]` = LCS of `text1[:i]` and `text2[:j]`.

> 💡 **Hint 2:** If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

> 💡 **Hint 3:** Base case: `dp[0][j] = dp[i][0] = 0` (empty string has LCS 0 with anything).

## Approach
**Time Complexity:** O(M × N)
**Space Complexity:** O(M × N), optimizable to O(min(M,N))

2D DP table. Match characters or take the best of skipping one character from either string.
