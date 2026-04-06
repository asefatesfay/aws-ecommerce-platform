# Isomorphic Strings

**Difficulty:** Easy
**Pattern:** Hash Map / Bijection
**LeetCode:** #205

## Problem Statement

Given two strings `s` and `t`, determine if they are isomorphic. Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Examples

### Example 1
**Input:** `s = "egg"`, `t = "add"`
**Output:** `true`
**Explanation:** 'e' → 'a', 'g' → 'd'.

### Example 2
**Input:** `s = "foo"`, `t = "bar"`
**Output:** `false`
**Explanation:** 'o' would need to map to both 'a' and 'r'.

### Example 3
**Input:** `s = "paper"`, `t = "title"`
**Output:** `true`

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII character

## Hints

> 💡 **Hint 1:** You need a bijection (one-to-one mapping) between characters of s and t. Two conditions: each s-char maps to exactly one t-char, and each t-char is mapped to by exactly one s-char.

> 💡 **Hint 2:** Use two HashMaps: one for s→t mapping and one for t→s mapping. For each position, check consistency in both directions.

> 💡 **Hint 3:** If s[i] is already mapped to something other than t[i], or t[i] is already mapped from something other than s[i], return false.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (bounded by character set size)

Maintain two maps (s→t and t→s). For each character pair, verify both mappings are consistent. Return false on any inconsistency.
