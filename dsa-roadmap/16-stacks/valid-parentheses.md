# Valid Parentheses

**Difficulty:** Easy
**Pattern:** Stack
**LeetCode:** #20

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1
**Input:** `s = "()"`
**Output:** `true`

### Example 2
**Input:** `s = "()[]{}"`
**Output:** `true`

### Example 3
**Input:** `s = "(]"`
**Output:** `false`

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`

## Hints

> 💡 **Hint 1:** Use a stack. Push open brackets onto the stack.

> 💡 **Hint 2:** When you see a close bracket, check if the top of the stack is the matching open bracket. If yes, pop. If no (or stack is empty), return false.

> 💡 **Hint 3:** At the end, the stack should be empty. If it's not, there are unmatched open brackets.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack-based matching: push open brackets, pop and verify on close brackets. Return true iff stack is empty at the end.
