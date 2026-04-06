# Valid Parenthesis String

**Difficulty:** Medium
**Pattern:** Stack / Greedy
**LeetCode:** #678

## Problem Statement

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid. The following rules define a valid string:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

## Examples

### Example 1
**Input:** `s = "()"`
**Output:** `true`

### Example 2
**Input:** `s = "(*)"`
**Output:** `true`

### Example 3
**Input:** `s = "(*))"`
**Output:** `true`

## Constraints
- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`

## Hints

> 💡 **Hint 1:** Track a range of possible open parenthesis counts. `*` can be `(`, `)`, or empty, so it changes the range.

> 💡 **Hint 2:** Maintain `lo` (minimum possible open count) and `hi` (maximum possible open count). For `(`: lo++, hi++. For `)`: lo--, hi--. For `*`: lo--, hi++.

> 💡 **Hint 3:** If `hi < 0` at any point, return false (too many closing brackets). Clamp `lo` to 0 (can't have negative open count). At the end, return `lo == 0`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track range [lo, hi] of possible open parenthesis counts. Return false if hi < 0; clamp lo to 0. Valid if lo == 0 at end.
