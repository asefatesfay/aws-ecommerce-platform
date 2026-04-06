# Longest Repeating Character Replacement

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #424

## Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

### Example 1
**Input:** `s = "ABAB"`, `k = 2`
**Output:** `4`
**Explanation:** Replace both 'A's with 'B's or vice versa.

### Example 2
**Input:** `s = "AABABBA"`, `k = 1`
**Output:** `4`
**Explanation:** Replace the 'B' at index 4 to get "AABAAAA" — wait, "AABA" → replace 'B' → "AAAA", length 4.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters
- `0 <= k <= s.length`

## Hints

> 💡 **Hint 1:** A window is valid if `window_size - max_frequency_in_window <= k`. The characters that aren't the most frequent need to be replaced.

> 💡 **Hint 2:** Use a sliding window. Track the frequency of each character in the window and the maximum frequency. Expand right; when the window becomes invalid, shrink left.

> 💡 **Hint 3:** Key insight: you don't need to update `max_freq` when shrinking — if it decreases, the window size also decreases, so it can't be a new maximum. Only update `max_freq` when expanding.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (26 uppercase letters)

Variable window. Track character frequencies and max frequency. Window is valid when `size - max_freq <= k`. Shrink when invalid, track maximum valid window size.
