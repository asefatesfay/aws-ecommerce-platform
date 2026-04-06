# Determine if Two Strings Are Close

**Difficulty:** Medium
**Pattern:** Hash Map / Frequency Analysis
**LeetCode:** #1657

## Problem Statement

Two strings are considered close if you can attain one from the other using the following operations:
- **Operation 1:** Swap any two existing characters (e.g., "abcde" → "aecdb")
- **Operation 2:** Transform every occurrence of one existing character into another existing character, and do the same with the other character (e.g., "aacabb" → "bbcbaa")

You can use the operations on either string as many times as necessary. Given two strings `word1` and `word2`, return `true` if `word1` and `word2` are close, and `false` otherwise.

## Examples

### Example 1
**Input:** `word1 = "abc"`, `word2 = "bca"`
**Output:** `true`
**Explanation:** Operation 1: swap any characters to rearrange.

### Example 2
**Input:** `word1 = "a"`, `word2 = "aa"`
**Output:** `false`

### Example 3
**Input:** `word1 = "cabbba"`, `word2 = "abbccc"`
**Output:** `true`
**Explanation:** Both have the same set of characters {a,b,c} and the same multiset of frequencies {1,2,3}.

## Constraints
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** Operation 1 lets you rearrange characters freely. Operation 2 lets you swap the roles of two characters. Think about what invariants are preserved.

> 💡 **Hint 2:** Two conditions must hold: (1) both strings must use the same set of distinct characters, and (2) the multiset of character frequencies must be the same.

> 💡 **Hint 3:** Check that `set(word1) == set(word2)` and that `sorted(Counter(word1).values()) == sorted(Counter(word2).values())`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 26 distinct characters)

Count character frequencies for both strings. Verify two conditions: same set of characters used, and same sorted list of frequency values.
