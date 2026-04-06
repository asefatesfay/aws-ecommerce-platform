# Number of Good Ways to Split a String

**Difficulty:** Medium
**Pattern:** Hash Map / Prefix/Suffix Counting
**LeetCode:** #1525

## Problem Statement

You are given a string `s`. A split is called good if you can split `s` into two non-empty strings `sleft` and `sright` where their concatenation is equal to `s` (i.e., `sleft + sright = s`) and the number of distinct characters in `sleft` and `sright` are the same. Return the number of good splits you can make in `s`.

## Examples

### Example 1
**Input:** `s = "aacaba"`
**Output:** `2`
**Explanation:** Splits: "a|acaba" (1 vs 4 distinct), "aa|caba" (1 vs 4), "aac|aba" (2 vs 3), "aaca|ba" (2 vs 2) ✓, "aacab|a" (3 vs 1). Two good splits.

### Example 2
**Input:** `s = "abcd"`
**Output:** `1`
**Explanation:** "ab|cd" — 2 distinct each. Only one good split.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters

## Hints

> 💡 **Hint 1:** For each split position, you need the count of distinct characters in the left and right parts. Precompute these efficiently.

> 💡 **Hint 2:** Build a prefix array: `left[i]` = number of distinct characters in s[0..i]. Build a suffix array: `right[i]` = number of distinct characters in s[i..n-1].

> 💡 **Hint 3:** For each split position i (1 to n-1), check if `left[i-1] == right[i]`. Count the matches.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Precompute prefix distinct counts (left to right) and suffix distinct counts (right to left) using frequency maps. Count positions where prefix and suffix distinct counts are equal.
