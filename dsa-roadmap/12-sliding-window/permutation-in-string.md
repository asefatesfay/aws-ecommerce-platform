# Permutation in String

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed) + Frequency Map
**LeetCode:** #567

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

## Examples

### Example 1
**Input:** `s1 = "ab"`, `s2 = "eidbaooo"`
**Output:** `true`
**Explanation:** "ba" is a permutation of "ab" and is a substring of "eidbaooo".

### Example 2
**Input:** `s1 = "ab"`, `s2 = "eidboaoo"`
**Output:** `false`

## Constraints
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** A permutation of s1 is any string with the same character frequencies as s1. You need to find a window of size len(s1) in s2 with matching frequencies.

> 💡 **Hint 2:** This is essentially the same as "Find All Anagrams" — just return true as soon as you find one match instead of collecting all indices.

> 💡 **Hint 3:** Use a fixed window of size len(s1) with a match counter. Return true when all 26 character counts match.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Fixed window of size len(s1). Maintain frequency difference between s1 and the current window. Return true when all differences are zero.
