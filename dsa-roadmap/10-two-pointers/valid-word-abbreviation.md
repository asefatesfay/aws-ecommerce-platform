# Valid Word Abbreviation

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #408

## Problem Statement

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros. Given a string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

## Examples

### Example 1
**Input:** `word = "internationalization"`, `abbr = "i12iz4n"`
**Output:** `true`
**Explanation:** i + 12 chars + iz + 4 chars + n matches "internationalization".

### Example 2
**Input:** `word = "apple"`, `abbr = "a2e"`
**Output:** `false`

### Example 3
**Input:** `word = "hi"`, `abbr = "2"`
**Output:** `true`

## Constraints
- `1 <= word.length <= 20`
- `word` consists of only lowercase English letters
- `1 <= abbr.length <= 10`
- `abbr` consists of lowercase English letters and digits
- There are no leading zeros in any number in `abbr`

## Hints

> 💡 **Hint 1:** Use two pointers: one for `word` and one for `abbr`. Advance them in sync.

> 💡 **Hint 2:** When the abbr pointer points to a digit, parse the full number (may be multi-digit). Advance the word pointer by that many positions.

> 💡 **Hint 3:** When the abbr pointer points to a letter, it must match the current word character. If it doesn't, return false. Check for leading zeros: if the digit is '0', return false immediately.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers: when abbr has a digit, parse the number and skip that many characters in word. When abbr has a letter, match it directly with word. Return true if both pointers reach their ends simultaneously.
