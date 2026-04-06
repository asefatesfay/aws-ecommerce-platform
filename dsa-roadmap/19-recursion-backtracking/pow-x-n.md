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

## Python Implementation

```python
def my_pow(x, n):
	def fast_pow(base, exponent):
		if exponent == 0:
			return 1.0

		half = fast_pow(base, exponent // 2)
		if exponent % 2 == 0:
			return half * half
		return half * half * base

	if n < 0:
		x = 1 / x
		n = -n

	return fast_pow(x, n)
```

## Step-by-Step Example

**Input:** `x = 2`, `n = 10`

1. `10` is even, so compute `pow(2, 5)` once and square it.
2. `5` is odd, so compute `pow(2, 2)` once, square it, then multiply by `2`.
3. `2` is even, so compute `pow(2, 1)` once and square it.
4. `1` is odd, so compute `pow(2, 0) = 1`, then return `1 * 1 * 2 = 2`.
5. Unwind: `pow(2, 2) = 2 * 2 = 4`.
6. Unwind: `pow(2, 5) = 4 * 4 * 2 = 32`.
7. Unwind: `pow(2, 10) = 32 * 32 = 1024`.

**Output:** `1024`

## Flow Diagram

```mermaid
flowchart TD
	A[my_pow x n] --> B{n < 0?}
	B -- Yes --> C[invert x and negate n]
	B -- No --> D[call fast_pow]
	C --> D
	D --> E{exponent == 0?}
	E -- Yes --> F[return 1]
	E -- No --> G[compute half = fast_pow(base, exponent // 2)]
	G --> H{exponent even?}
	H -- Yes --> I[return half * half]
	H -- No --> J[return half * half * base]
```

## Edge Cases

- Negative exponent: convert to reciprocal first.
- `n = 0` should always return `1`.
- Very large `|n|` is still safe because recursion depth is only `O(log n)`.
