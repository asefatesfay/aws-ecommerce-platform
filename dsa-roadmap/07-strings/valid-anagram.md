# Valid Anagram

**Difficulty:** Easy
**Pattern:** Hash Map / Character Frequency
**LeetCode:** #242

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Examples

### Example 1
**Input:** `s = "anagram"`, `t = "nagaram"`
**Output:** `true`

### Example 2
**Input:** `s = "rat"`, `t = "car"`
**Output:** `false`

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** Two strings are anagrams if and only if they have the same character frequencies.

> 💡 **Hint 2:** Count the frequency of each character in both strings and compare. A 26-element array works since only lowercase letters are used.

> 💡 **Hint 3:** Alternatively, increment counts for characters in `s` and decrement for characters in `t`. If all counts are 0 at the end, they're anagrams. Also check that lengths are equal first.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (fixed 26-character alphabet)

Count character frequencies in both strings using a 26-element array (or HashMap for Unicode follow-up). Compare the two frequency arrays for equality.
