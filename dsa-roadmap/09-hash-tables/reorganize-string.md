# Reorganize String

**Difficulty:** Medium
**Pattern:** Hash Map / Greedy / Heap
**LeetCode:** #767

## Problem Statement

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or return `""` if not possible.

## Examples

### Example 1
**Input:** `s = "aab"`
**Output:** `"aba"`

### Example 2
**Input:** `s = "aaab"`
**Output:** `""`
**Explanation:** Impossible — 'a' appears 3 times in a 4-character string.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** When is it impossible? If any character appears more than `(n+1)/2` times, it's impossible to avoid adjacent duplicates.

> 💡 **Hint 2:** Greedy approach: always place the most frequent remaining character that isn't the same as the last placed character. A max-heap helps efficiently get the most frequent character.

> 💡 **Hint 3:** Use a max-heap of (count, char). At each step, pop the most frequent character. If it's the same as the last placed, pop the second most frequent, place it, and push the first back. Continue until the heap is empty or you're stuck.

## Approach

**Time Complexity:** O(n log k) where k is the number of distinct characters
**Space Complexity:** O(k)

Max-heap greedy: always pick the most frequent character that differs from the last placed. If impossible (most frequent equals last and no alternative), return "".
