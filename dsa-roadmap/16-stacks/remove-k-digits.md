# Remove K Digits

**Difficulty:** Medium
**Pattern:** Monotonic Stack / Greedy
**LeetCode:** #402

## Problem Statement

Given string `num` representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

## Examples

### Example 1
**Input:** `num = "1432219"`, `k = 3`
**Output:** `"1219"`
**Explanation:** Remove 4, 3, 2 to get "1219".

### Example 2
**Input:** `num = "10200"`, `k = 1`
**Output:** `"200"` → actually `"200"` but leading zeros removed → `"200"`

### Example 3
**Input:** `num = "10"`, `k = 2`
**Output:** `"0"`

## Constraints
- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits
- `num` does not have any leading zeros except for the zero itself

## Hints

> 💡 **Hint 1:** Greedy: to minimize the number, remove digits that are larger than the digit following them (from left to right).

> 💡 **Hint 2:** Use a monotonic increasing stack. For each digit, pop digits from the stack that are larger than the current digit (while k > 0). Push the current digit.

> 💡 **Hint 3:** If k > 0 after processing all digits, remove from the end (the stack is increasing, so the largest are at the end). Remove leading zeros from the result.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic increasing stack. Pop larger digits greedily. Handle remaining k by truncating the end. Strip leading zeros.
