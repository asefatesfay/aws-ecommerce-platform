# Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Pattern:** Stack
**LeetCode:** #150

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation. Evaluate the expression. Return an integer that represents the value of the expression. Note that: valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division between two integers always truncates toward zero. There will not be any division by zero. The answer and all intermediate calculations can be represented in a 32-bit integer.

## Examples

### Example 1
**Input:** `tokens = ["2","1","+","3","*"]`
**Output:** `9`
**Explanation:** ((2 + 1) * 3) = 9.

### Example 2
**Input:** `tokens = ["4","13","5","/","+"]`
**Output:** `6`
**Explanation:** (4 + (13 / 5)) = 6.

## Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator or an integer in the range `[-200, 200]`

## Hints

> 💡 **Hint 1:** Use a stack. Push numbers onto the stack.

> 💡 **Hint 2:** When you see an operator, pop two numbers from the stack, apply the operator, and push the result.

> 💡 **Hint 3:** The final answer is the single remaining element on the stack. Note: for non-commutative operations (-, /), the order matters — the second popped is the left operand.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack-based evaluation: push numbers, pop two and apply operator on operator tokens. Result is the last stack element.
