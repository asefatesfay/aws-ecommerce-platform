# Word Pattern

**Difficulty:** Easy
**Pattern:** Hash Map / Bijection
**LeetCode:** #290

## Problem Statement

Given a `pattern` and a string `s`, find if `s` follows the same pattern. Here "follow" means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

## Examples

### Example 1
**Input:** `pattern = "abba"`, `s = "dog cat cat dog"`
**Output:** `true`

### Example 2
**Input:** `pattern = "abba"`, `s = "dog cat cat fish"`
**Output:** `false`

### Example 3
**Input:** `pattern = "aaaa"`, `s = "dog cat cat dog"`
**Output:** `false`

## Constraints
- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces
- `s` does not contain any leading or trailing spaces
- All the words in `s` are separated by a single space

## Hints

> 💡 **Hint 1:** Split `s` into words. Check that the number of words equals the length of `pattern`.

> 💡 **Hint 2:** This is the same bijection problem as Isomorphic Strings, but between pattern characters and words instead of characters.

> 💡 **Hint 3:** Use two maps: char→word and word→char. For each (pattern[i], word[i]) pair, verify both mappings are consistent.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Split s into words, verify equal length with pattern, then check bijection using two HashMaps (char→word and word→char).
