# Single Number III

**Difficulty:** Medium
**Pattern:** Bit Manipulation / XOR
**LeetCode:** #260

## Problem Statement

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order. You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

## Examples

### Example 1
**Input:** `nums = [1, 2, 1, 3, 2, 5]`
**Output:** `[3, 5]`
**Explanation:** 3 and 5 each appear once; 1 and 2 appear twice.

### Example 2
**Input:** `nums = [-1, 0]`
**Output:** `[-1, 0]`

## Constraints
- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each integer in `nums` will appear twice, only two integers will appear once

## Hints

> 💡 **Hint 1:** XOR all elements. The result is `a ^ b` where a and b are the two unique numbers. Since a ≠ b, this XOR is non-zero.

> 💡 **Hint 2:** Find any set bit in `a ^ b` (e.g., the lowest set bit using `x & (-x)`). This bit differs between a and b, so it can be used to partition all numbers into two groups.

> 💡 **Hint 3:** XOR all numbers in each group separately. Each group contains exactly one unique number (plus pairs that cancel), so each group's XOR gives one of the two answers.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

XOR all elements to get `a ^ b`. Use the lowest set bit to split numbers into two groups. XOR each group independently to isolate a and b.

## Python Implementation

```python
def single_number(nums):
	xor_all = 0
	for x in nums:
		xor_all ^= x

	diff_bit = xor_all & -xor_all
	a = b = 0

	for x in nums:
		if x & diff_bit:
			a ^= x
		else:
			b ^= x

	return [a, b]
```

## Typical Interview Use Cases

- Isolating two unique numbers among paired duplicates
- Splitting by the lowest differing bit after aggregate XOR
- Important follow-up to the simpler single-number pattern

