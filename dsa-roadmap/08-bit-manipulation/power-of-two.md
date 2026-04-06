# Power of Two

**Difficulty:** Easy
**Pattern:** Bit Manipulation / Math
**LeetCode:** #231

## Problem Statement

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`. An integer `n` is a power of two if there exists an integer `x` such that `n == 2^x`.

## Examples

### Example 1
**Input:** `n = 1`
**Output:** `true`
**Explanation:** 2^0 = 1.

### Example 2
**Input:** `n = 16`
**Output:** `true`
**Explanation:** 2^4 = 16.

### Example 3
**Input:** `n = 3`
**Output:** `false`

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** A power of two is always positive and has exactly one bit set in its binary representation.

> 💡 **Hint 2:** If n is a power of two, then `n & (n-1)` equals 0. Why? Because n has exactly one set bit, and n-1 has all lower bits set and that bit cleared.

> 💡 **Hint 3:** Check `n > 0 and (n & (n-1)) == 0`.

## Approach

**Time Complexity:** O(1)
**Space Complexity:** O(1)

Check that n is positive and `n & (n-1) == 0`. Powers of two have exactly one set bit; subtracting 1 flips all lower bits, so AND gives 0.
