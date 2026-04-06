# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #3

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

### Example 1
**Input:** `s = "abcabcbb"`
**Output:** `3`
**Explanation:** "abc" is the longest substring without repeating characters.

### Example 2
**Input:** `s = "bbbbb"`
**Output:** `1`

### Example 3
**Input:** `s = "pwwkew"`
**Output:** `3`
**Explanation:** "wke" is the answer.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces

## Hints

> 💡 **Hint 1:** Use a sliding window. Expand the right pointer. When a duplicate is found, shrink from the left.

> 💡 **Hint 2:** Use a HashSet to track characters in the current window. When s[right] is already in the set, remove s[left] from the set and advance left.

> 💡 **Hint 3:** Alternatively, use a HashMap storing the last seen index of each character. When a duplicate is found, jump left directly to max(left, last_seen[char] + 1).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, alphabet_size))

Variable window with a HashSet or HashMap. Expand right; when a duplicate is encountered, shrink left until the duplicate is removed. Track maximum window size.
