# Minimum Window Substring

**Difficulty:** Hard
**Pattern:** Sliding Window (Variable)
**LeetCode:** #76

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Examples

### Example 1
**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`
**Output:** `"BANC"`
**Explanation:** "BANC" is the minimum window containing A, B, C.

### Example 2
**Input:** `s = "a"`, `t = "a"`
**Output:** `"a"`

### Example 3
**Input:** `s = "a"`, `t = "aa"`
**Output:** `""`

## Constraints
- `m == s.length`, `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters

## Hints

> 💡 **Hint 1:** Use a variable sliding window. Track how many characters of t are "satisfied" (present in sufficient quantity) in the current window.

> 💡 **Hint 2:** Expand right until all characters of t are covered (window is valid). Then shrink from the left as much as possible while keeping the window valid. Record the minimum valid window.

> 💡 **Hint 3:** Use two frequency maps: one for t's requirements, one for the current window. Track a `formed` counter (how many distinct characters meet their required frequency). When `formed == len(required)`, the window is valid.

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(m + n)

Variable window with two frequency maps and a `formed` counter. Expand to satisfy all requirements, then shrink to minimize. Track the minimum valid window.
