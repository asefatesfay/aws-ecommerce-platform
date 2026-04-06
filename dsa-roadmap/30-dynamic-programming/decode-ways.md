# Decode Ways

**Difficulty:** Medium
**Pattern:** String DP / 1D DP
**LeetCode:** #91

## Problem Statement
A message containing letters `A-Z` is encoded as:
- `'A' -> "1"`, `'B' -> "2"`, ..., `'Z' -> "26"`

Given a string `s` containing only digits, return the number of ways to decode it.

## Examples

### Example 1
**Input:** `s = "12"`
**Output:** `2`
**Explanation:** `"AB"` (`1 2`) or `"L"` (`12`)

### Example 2
**Input:** `s = "226"`
**Output:** `3`

### Example 3
**Input:** `s = "06"`
**Output:** `0`

## Constraints
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeroes

## DP Breakdown
- **State:** `dp[i]` = number of ways to decode prefix of length `i`
- **Base cases:** `dp[0] = 1`, `dp[1] = 1` if first char is not `'0'`, else `0`
- Add `dp[i-1]` if one-digit code is valid
- Add `dp[i-2]` if two-digit code is in `[10, 26]`

## Hints
- `'0'` cannot stand alone.
- Valid two-digit window is `10` to `26`.
- Iterate left to right with two previous states.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Track previous two DP values while validating one-digit and two-digit decodings.