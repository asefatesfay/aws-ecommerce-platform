# Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium
**Pattern:** Stack
**LeetCode:** #1249

## Problem Statement

Given a string `s` of `'('`, `')'` and lowercase English characters, remove the minimum number of parentheses (in any positions) so that the resulting parentheses string is valid and return any valid string. A parentheses string is valid if and only if: it is the empty string, contains only lowercase characters, or can be written as `AB` (A concatenated with B), where A and B are valid strings, or can be written as `(A)`, where A is a valid string.

## Examples

### Example 1
**Input:** `s = "lee(t(c)o)de)"`
**Output:** `"lee(t(c)o)de"`

### Example 2
**Input:** `s = "a)b(c)d"`
**Output:** `"ab(c)d"`

### Example 3
**Input:** `s = "))(("`
**Output:** `""`

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either a lowercase letter, `'('`, or `')'`

## Hints

> 💡 **Hint 1:** Use a stack to track indices of unmatched `(`. When you see `)`, if the stack is non-empty, pop (matched pair). If empty, mark this `)` for removal.

> 💡 **Hint 2:** After processing, any indices remaining in the stack are unmatched `(` — mark them for removal too.

> 💡 **Hint 3:** Build the result by including all characters not marked for removal.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack of unmatched `(` indices. Mark unmatched `)` immediately. After scan, mark remaining stack indices. Build result excluding marked indices.
