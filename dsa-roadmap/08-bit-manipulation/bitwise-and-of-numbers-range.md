# Bitwise AND of Numbers Range

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**LeetCode:** #201

## Problem Statement

Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

## Examples

### Example 1
**Input:** `left = 5`, `right = 7`
**Output:** `4`
**Explanation:** 5 & 6 & 7 = 101 & 110 & 111 = 100 = 4.

### Example 2
**Input:** `left = 0`, `right = 0`
**Output:** `0`

### Example 3
**Input:** `left = 1`, `right = 2147483647`
**Output:** `0`

## Constraints
- `0 <= left <= right <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** If any bit position has both a 0 and a 1 somewhere in the range [left, right], that bit will be 0 in the AND result. Think about which bits are guaranteed to be the same across all numbers in the range.

> 💡 **Hint 2:** The AND of a range is the common prefix of left and right in binary. Any bit that differs between left and right (and all numbers in between) will be 0.

> 💡 **Hint 3:** Shift both left and right right until they're equal, counting the shifts. The result is the common prefix shifted back left by the shift count.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Right-shift both numbers until they're equal (counting shifts). The equal value is the common binary prefix. Left-shift it back by the shift count to get the answer.
