# Longest Substring with At Most Two Distinct Characters

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #159

## Problem Statement

Given a string `s`, return the length of the longest substring that contains at most two distinct characters.

## Examples

### Example 1
**Input:** `s = "eceba"`
**Output:** `3`
**Explanation:** "ece" has 2 distinct characters and length 3.

### Example 2
**Input:** `s = "ccaabbb"`
**Output:** `5`
**Explanation:** "aabbb" has 2 distinct characters and length 5.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of English letters

## Hints

> 💡 **Hint 1:** Variable sliding window. Track the frequency of each character in the window using a HashMap.

> 💡 **Hint 2:** Expand right. When the number of distinct characters exceeds 2, shrink from the left until only 2 remain.

> 💡 **Hint 3:** Track the maximum window size seen while the constraint holds.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 3 entries in the map at any time)

Variable window with a frequency map. Shrink when distinct characters > 2. Track maximum valid window size.
