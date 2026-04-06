# Palindrome Partitioning

**Difficulty:** Medium
**Pattern:** Backtracking + DP
**LeetCode:** #131

## Problem Statement

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

## Examples

### Example 1
**Input:** `s = "aab"`
**Output:** `[["a","a","b"],["aa","b"]]`

### Example 2
**Input:** `s = "a"`
**Output:** `[["a"]]`

## Constraints
- `1 <= s.length <= 16`
- `s` consists of only lowercase English letters

## Hints

> 💡 **Hint 1:** Backtracking: at each position, try all substrings starting here. If the substring is a palindrome, add it to the current partition and recurse.

> 💡 **Hint 2:** When you reach the end of the string, add the current partition to results.

> 💡 **Hint 3:** Precompute a 2D boolean table `is_palindrome[i][j]` to check palindromes in O(1) during backtracking.

## Approach

**Time Complexity:** O(n × 2^n)
**Space Complexity:** O(n²) for palindrome table

Backtracking with palindrome precomputation. Try all prefixes at each position; recurse on the suffix when the prefix is a palindrome.
