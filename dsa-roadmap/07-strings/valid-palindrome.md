# Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #125

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1
**Input:** `s = "A man, a plan, a canal: Panama"`
**Output:** `true`
**Explanation:** After cleaning: "amanaplanacanalpanama" — a palindrome.

### Example 2
**Input:** `s = "race a car"`
**Output:** `false`
**Explanation:** After cleaning: "raceacar" — not a palindrome.

### Example 3
**Input:** `s = " "`
**Output:** `true`
**Explanation:** After cleaning: "" — an empty string is a palindrome.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## Hints

> 💡 **Hint 1:** Use two pointers starting at both ends. Skip non-alphanumeric characters as you move inward.

> 💡 **Hint 2:** At each step, compare the characters at the two pointers (case-insensitive). If they don't match, return false.

> 💡 **Hint 3:** Continue until the pointers meet. If all comparisons passed, return true. No need to build a cleaned string.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers from both ends, skipping non-alphanumeric characters and comparing case-insensitively. Return false on any mismatch, true if pointers cross.
