# Interleaving String

**Difficulty:** Medium
**Pattern:** String DP / 2D DP
**LeetCode:** #97

## Problem Statement
Given strings `s1`, `s2`, and `s3`, return `true` if `s3` is formed by an interleaving of `s1` and `s2`.

Interleaving keeps the relative order of characters from each string.

## Examples

### Example 1
**Input:** `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
**Output:** `true`

### Example 2
**Input:** `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
**Output:** `false`

## Constraints
- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`

## DP Breakdown
- If `len(s1) + len(s2) != len(s3)`, return `false`.
- **State:** `dp[i][j]` = whether `s3[0..i+j-1]` can be formed by `s1[0..i-1]` and `s2[0..j-1]`
- **Transition:**
  - from top if `dp[i-1][j]` and `s1[i-1] == s3[i+j-1]`
  - from left if `dp[i][j-1]` and `s2[j-1] == s3[i+j-1]`
- **Base case:** `dp[0][0] = true`

## Hints
- Think in prefixes, not suffixes.
- At each point, next char in `s3` must come from `s1` or `s2`.
- 1D compression is possible but 2D is clearer first.

## Approach
**Time Complexity:** O(len(s1) * len(s2))
**Space Complexity:** O(len(s1) * len(s2))

Fill a 2D boolean table by matching prefix transitions.