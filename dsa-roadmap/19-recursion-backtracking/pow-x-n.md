# Pow(x, n)

**Difficulty:** Medium
**Pattern:** Recursion / Fast Exponentiation
**LeetCode:** #50

## Problem Statement

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

## Examples

### Example 1
**Input:** `x = 2.00000`, `n = 10`
**Output:** `1024.00000`

### Example 2
**Input:** `x = 2.10000`, `n = 3`
**Output:** `9.26100`

### Example 3
**Input:** `x = 2.00000`, `n = -2`
**Output:** `0.25000`
**Explanation:** 2^(-2) = 1/4 = 0.25.

## Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31-1`
- `n` is an integer
- Either `x` is not zero or `n > 0`
- `-10^4 <= x^n <= 10^4`

## Hints

> 💡 **Hint 1:** Naive multiplication is O(n). Use fast exponentiation (exponentiation by squaring) for O(log n).

> 💡 **Hint 2:** If n is even: `x^n = (x^(n/2))^2`. If n is odd: `x^n = x * x^(n-1)`. Handle negative n by computing `1 / pow(x, -n)`.

> 💡 **Hint 3:** Be careful with n = INT_MIN (overflow when negating). Use long for n.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(log n) recursive, O(1) iterative

Fast exponentiation: halve the exponent at each step. Square the base for even exponents, multiply by base for odd.
