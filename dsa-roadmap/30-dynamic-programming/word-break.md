# Word Break

**Difficulty:** Medium
**Pattern:** 1D DP / BFS
**LeetCode:** #139

## Problem Statement
Given a string `s` and a dictionary `wordDict`, return true if `s` can be segmented into a space-separated sequence of dictionary words.

## Examples

### Example 1
**Input:** `s = "leetcode"`, `wordDict = ["leet","code"]`
**Output:** `true`

### Example 2
**Input:** `s = "applepenapple"`, `wordDict = ["apple","pen"]`
**Output:** `true`

### Example 3
**Input:** `s = "catsandog"`, `wordDict = ["cats","dog","sand","and","cat"]`
**Output:** `false`

## Constraints
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`

## Hints

> 💡 **Hint 1:** `dp[i]` = true if `s[:i]` can be segmented. `dp[0] = true` (empty string).

> 💡 **Hint 2:** For each position `i`, check all `j < i`: if `dp[j]` is true and `s[j:i]` is in the dictionary, set `dp[i] = true`.

> 💡 **Hint 3:** Convert `wordDict` to a set for O(1) lookup. Only check substrings up to the max word length.

## Approach
**Time Complexity:** O(N² × M) where M = avg word length
**Space Complexity:** O(N)

DP where `dp[i]` means the first i characters can be segmented. Check all valid splits.
