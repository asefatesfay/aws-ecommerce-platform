# Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #340

## Problem Statement

Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

## Examples

### Example 1
**Input:** `s = "eceba"`, `k = 2`
**Output:** `3`
**Explanation:** "ece" has 2 distinct characters.

### Example 2
**Input:** `s = "aa"`, `k = 1`
**Output:** `2`

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `0 <= k <= 50`

## Hints

> 💡 **Hint 1:** This is the generalization of "At Most Two Distinct Characters". Replace 2 with k.

> 💡 **Hint 2:** Variable sliding window with a HashMap tracking character frequencies. Expand right; when distinct characters > k, shrink from the left.

> 💡 **Hint 3:** Remove a character from the map when its count reaches 0. Track maximum window size.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Variable window with a frequency map. Shrink when distinct characters > k. Track maximum valid window size.
