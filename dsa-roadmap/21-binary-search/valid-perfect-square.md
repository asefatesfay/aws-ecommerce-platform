# Valid Perfect Square

**Difficulty:** Easy
**Pattern:** Binary Search / Math
**LeetCode:** #367

## Problem Statement

Given a positive integer `num`, return `true` if `num` is a perfect square or `false` otherwise. A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself. You must not use any built-in library function, such as `sqrt`.

## Examples

### Example 1
**Input:** `num = 16`
**Output:** `true`
**Explanation:** 4 * 4 = 16.

### Example 2
**Input:** `num = 14`
**Output:** `false`

## Constraints
- `1 <= num <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Binary search for an integer x such that x*x == num.

> 💡 **Hint 2:** Search space: [1, num]. If mid*mid == num, return true. If mid*mid < num, search right. If mid*mid > num, search left.

> 💡 **Hint 3:** Use long to avoid overflow when computing mid*mid.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search for the square root. Return true if found exactly.
