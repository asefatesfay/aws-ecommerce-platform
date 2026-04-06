# Longest Palindromic Substring

**Difficulty:** Medium
**Pattern:** Expand Around Center / Two Pointers
**LeetCode:** #5

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

### Example 1
**Input:** `s = "babad"`
**Output:** `"bab"` (or `"aba"` — both are valid)

### Example 2
**Input:** `s = "cbbd"`
**Output:** `"bb"`

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters

## Hints

> 💡 **Hint 1:** A palindrome expands symmetrically from its center. For a string of length n, there are 2n-1 possible centers (n single characters + n-1 gaps between characters).

> 💡 **Hint 2:** For each center, expand outward as long as the characters on both sides match. Track the longest palindrome found.

> 💡 **Hint 3:** Handle both odd-length palindromes (center is a single character) and even-length palindromes (center is between two characters) separately, or with a helper function that takes left and right starting positions.

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Expand around each of the 2n-1 centers. For each center, expand while characters match and track the maximum length palindrome found. Return the substring corresponding to the maximum.
