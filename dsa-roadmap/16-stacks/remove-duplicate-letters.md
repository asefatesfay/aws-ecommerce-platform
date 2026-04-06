# Remove Duplicate Letters

**Difficulty:** Medium
**Pattern:** Monotonic Stack / Greedy
**LeetCode:** #316

## Problem Statement

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

## Examples

### Example 1
**Input:** `s = "bcabc"`
**Output:** `"abc"`

### Example 2
**Input:** `s = "cbacdcbc"`
**Output:** `"acdb"`

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** Use a greedy approach with a monotonic stack. You want the lexicographically smallest result.

> 💡 **Hint 2:** For each character, if it's already in the stack (result), skip it. Otherwise, pop characters from the stack that are greater than the current character AND will appear again later in the string.

> 💡 **Hint 3:** Track: (1) a `seen` set of characters in the stack, (2) a `last_occurrence` map for each character. Pop from stack when `stack.top > current` AND `last_occurrence[stack.top] > current_index`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (26 characters)

Greedy monotonic stack: maintain the lexicographically smallest sequence by popping larger characters that will appear again later.
