# Find All Anagrams in a String

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed) + Frequency Map
**LeetCode:** #438

## Problem Statement

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order. An anagram is a rearrangement of all characters of a word.

## Examples

### Example 1
**Input:** `s = "cbaebabacd"`, `p = "abc"`
**Output:** `[0, 6]`
**Explanation:** "cba" at index 0 and "bac" at index 6 are anagrams of "abc".

### Example 2
**Input:** `s = "abab"`, `p = "ab"`
**Output:** `[0, 1, 2]`

## Constraints
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** An anagram has the same character frequencies. Use a fixed window of size len(p) and compare frequency maps.

> 💡 **Hint 2:** Maintain a frequency map of the current window. Slide the window: add the new character, remove the outgoing character.

> 💡 **Hint 3:** Instead of comparing full maps each step, maintain a `matches` counter tracking how many characters have matching frequencies. Update it when adding/removing characters.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (26 characters)

Fixed window of size len(p). Maintain frequency maps for p and the current window. Track a match counter to avoid full map comparison at each step.
