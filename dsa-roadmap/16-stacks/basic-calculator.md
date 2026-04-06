# Basic Calculator

**Difficulty:** Medium
**Pattern:** Stack / Expression Evaluation
**LeetCode:** #224

## Problem Statement

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation. Note: you are not allowed to use any built-in function which evaluates strings as mathematical expressions. The expression contains only `+`, `-`, `(`, `)`, non-negative integers, and spaces.

## Examples

### Example 1
**Input:** `s = "1 + 1"`
**Output:** `2`

### Example 2
**Input:** `s = " 2-1 + 2 "`
**Output:** `3`

### Example 3
**Input:** `s = "(1+(4+5+2)-3)+(6+8)"`
**Output:** `23`

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`
- `s` represents a valid expression
- `'+'` is not used as a unary operation
- `'-'` could be used as a unary operation (e.g., `"-1"` and `"-(2 + 3)"` are valid)
- There will be no two consecutive operators in the input
- Every number and running calculation will fit in a signed 32-bit integer

## Hints

> 💡 **Hint 1:** Use a stack to handle parentheses. When you see `(`, push the current result and sign onto the stack.

> 💡 **Hint 2:** When you see `)`, pop the sign and previous result from the stack and combine with the current result.

> 💡 **Hint 3:** Track the current number being built and the current sign (+1 or -1). Apply the sign when you encounter an operator or closing parenthesis.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack stores (result, sign) pairs for each open parenthesis. Process digit by digit, applying signs and handling parentheses by saving/restoring state.
