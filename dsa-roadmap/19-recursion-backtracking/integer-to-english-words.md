# Integer to English Words

**Difficulty:** Hard
**Pattern:** Recursion / String Building
**LeetCode:** #273

## Problem Statement

Convert a non-negative integer `num` to its English words representation.

## Examples

### Example 1
**Input:** `num = 123`
**Output:** `"One Hundred Twenty Three"`

### Example 2
**Input:** `num = 12345`
**Output:** `"Twelve Thousand Three Hundred Forty Five"`

### Example 3
**Input:** `num = 1000010`
**Output:** `"One Million Ten"`

## Constraints
- `0 <= num <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Break the number into groups of three digits (ones, thousands, millions, billions). Process each group separately.

> 💡 **Hint 2:** For each group of three digits, handle hundreds, tens, and ones. Use lookup arrays for ones (1-19) and tens (20, 30, ..., 90).

> 💡 **Hint 3:** Recursively convert each three-digit group, then append the appropriate scale word (Thousand, Million, Billion). Handle edge cases: 0, numbers ending in 0s.

## Approach

**Time Complexity:** O(1) — bounded by 32-bit integer
**Space Complexity:** O(1)

Process in groups of 1000. For each group, convert three digits to words using lookup tables. Append scale words.
