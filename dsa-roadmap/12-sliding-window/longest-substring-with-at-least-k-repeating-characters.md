# Longest Substring with At Least K Repeating Characters

**Difficulty:** Medium
**Pattern:** Divide and Conquer / Sliding Window
**LeetCode:** #395

## Problem Statement

Given a string `s` and an integer `k`, return the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k`.

## Examples

### Example 1
**Input:** `s = "aaabb"`, `k = 3`
**Output:** `3`
**Explanation:** "aaa" — all characters appear ≥ 3 times.

### Example 2
**Input:** `s = "ababbc"`, `k = 2`
**Output:** `5`
**Explanation:** "ababb" — 'a' appears 2 times, 'b' appears 3 times.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of only lowercase English letters
- `1 <= k <= 10^5`

## Hints

> 💡 **Hint 1:** Characters that appear fewer than k times in the full string cannot be part of any valid substring. They act as "dividers".

> 💡 **Hint 2:** Divide and conquer: find any character with frequency < k. Split the string at all occurrences of that character. Recursively solve each part.

> 💡 **Hint 3:** Alternatively, use a sliding window with a fixed number of unique characters (iterate over 1 to 26 unique characters). For each target unique count, find the longest window with exactly that many unique characters where all have frequency ≥ k.

## Approach

**Time Complexity:** O(n log n) divide and conquer, O(26n) = O(n) sliding window
**Space Complexity:** O(n) recursion stack, O(1) sliding window

Divide and conquer: split at characters with frequency < k, recurse on each part. Or sliding window: for each possible number of unique characters (1..26), find the longest valid window.
