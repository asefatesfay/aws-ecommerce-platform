# Sort Characters By Frequency

**Difficulty:** Medium
**Pattern:** Hash Map + Sorting
**LeetCode:** #451

## Problem Statement

Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.

## Examples

### Example 1
**Input:** `s = "tree"`
**Output:** `"eert"` or `"eetr"`
**Explanation:** 'e' appears twice, 'r' and 't' appear once.

### Example 2
**Input:** `s = "cccaaa"`
**Output:** `"cccaaa"` or `"aaaccc"`

### Example 3
**Input:** `s = "Aabb"`
**Output:** `"bbAa"` or `"bbaA"`

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits

## Hints

> 💡 **Hint 1:** Count character frequencies using a HashMap.

> 💡 **Hint 2:** Sort characters by frequency in descending order.

> 💡 **Hint 3:** Build the result string by repeating each character by its frequency.

## Approach

**Time Complexity:** O(n log n) or O(n) with bucket sort
**Space Complexity:** O(n)

Count frequencies, sort by frequency descending, build result string.
