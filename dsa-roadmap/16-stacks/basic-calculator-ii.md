# Basic Calculator II

**Difficulty:** Medium
**Pattern:** Stack / Expression Evaluation
**LeetCode:** #227

## Problem Statement

Given a string `s` which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero. You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`. Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions.

## Examples

### Example 1
**Input:** `s = "3+2*2"`
**Output:** `7`

### Example 2
**Input:** `s = " 3/2 "`
**Output:** `1`

### Example 3
**Input:** `s = " 3+5 / 2 "`
**Output:** `5`

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators `+`, `-`, `*`, `/` separated by spaces
- `s` represents a valid expression
- All integers in the expression are non-negative and in the range `[0, 2^31 - 1]`

## Hints

> 💡 **Hint 1:** Handle operator precedence: `*` and `/` have higher precedence than `+` and `-`.

> 💡 **Hint 2:** Use a stack. For `+` and `-`, push the number (with sign) onto the stack. For `*` and `/`, pop the top, apply the operation with the current number, and push the result.

> 💡 **Hint 3:** At the end, sum all values in the stack. This handles precedence because `*` and `/` are resolved immediately, while `+` and `-` are deferred.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack-based: resolve `*` and `/` immediately, defer `+` and `-` to the stack. Sum the stack at the end.
