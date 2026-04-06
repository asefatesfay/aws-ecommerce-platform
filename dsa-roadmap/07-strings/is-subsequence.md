# Is Subsequence

**Difficulty:** Easy
**Pattern:** Two Pointers / Greedy
**LeetCode:** #392

## Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

## Examples

### Example 1
**Input:** `s = "ace"`, `t = "abcde"`
**Output:** `true`
**Explanation:** 'a', 'c', 'e' appear in order in "abcde".

### Example 2
**Input:** `s = "aec"`, `t = "abcde"`
**Output:** `false`
**Explanation:** 'e' comes before 'c' in t, but we need 'c' before 'e'.

## Constraints
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters

## Hints

> 💡 **Hint 1:** Use two pointers: one for `s` and one for `t`. Try to match characters of `s` in order within `t`.

> 💡 **Hint 2:** Advance the `t` pointer always. Advance the `s` pointer only when the current characters match.

> 💡 **Hint 3:** If the `s` pointer reaches the end of `s`, all characters were matched — return true. If the `t` pointer reaches the end first, return false.

## Approach

**Time Complexity:** O(n) where n = len(t)
**Space Complexity:** O(1)

Greedy two-pointer: scan through t, advancing the s pointer whenever there's a match. Return true if s is fully matched.
