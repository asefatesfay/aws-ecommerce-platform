# Merge Strings Alternately

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #1768

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

## Examples

### Example 1
**Input:** `word1 = "abc"`, `word2 = "pqr"`
**Output:** `"apbqcr"`

### Example 2
**Input:** `word1 = "ab"`, `word2 = "pqrs"`
**Output:** `"apbqrs"`
**Explanation:** word2 is longer, so "rs" is appended at the end.

### Example 3
**Input:** `word1 = "abcd"`, `word2 = "pq"`
**Output:** `"apbqcd"`

## Constraints
- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** Use two pointers, one for each string. Alternate between them, appending one character at a time.

> 💡 **Hint 2:** Continue while both pointers are valid. After one string is exhausted, append the remainder of the other.

> 💡 **Hint 3:** A single loop with `i < max(len1, len2)` works cleanly — just check bounds before accessing each string.

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(m + n)

Single loop up to max length, alternately appending characters from each string (with bounds checking). Append remaining characters of the longer string.
