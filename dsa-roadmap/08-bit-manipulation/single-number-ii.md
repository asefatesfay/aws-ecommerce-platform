# Single Number II

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**LeetCode:** #137

## Problem Statement

Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with linear runtime complexity and use only constant extra space.

## Examples

### Example 1
**Input:** `nums = [2, 2, 3, 2]`
**Output:** `3`

### Example 2
**Input:** `nums = [0, 1, 0, 1, 0, 1, 99]`
**Output:** `99`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Every element appears exactly three times except for one element which appears exactly once

## Hints

> 💡 **Hint 1:** XOR won't work here since it cancels pairs, not triples. Think bit by bit: for each bit position, count how many numbers have that bit set.

> 💡 **Hint 2:** If a bit appears in a multiple of 3 numbers, it belongs to the "triple" elements. If the count is not divisible by 3, that bit belongs to the single element.

> 💡 **Hint 3:** For each of the 32 bit positions, sum the bits across all numbers and take modulo 3. The result gives the corresponding bit of the single number.

## Approach

**Time Complexity:** O(32n) = O(n)
**Space Complexity:** O(1)

For each bit position (0 to 31), count how many numbers have that bit set. If count % 3 != 0, that bit is set in the single number. Reconstruct the answer from these bits.

## Python Implementation

```python
def single_number(nums):
	result = 0

	for bit in range(32):
		bit_sum = 0
		for x in nums:
			bit_sum += (x >> bit) & 1

		if bit_sum % 3:
			result |= 1 << bit

	if result >= 1 << 31:
		result -= 1 << 32

	return result
```

## Typical Interview Use Cases

- When duplicates appear three times instead of two
- Bit-count modulo reasoning for frequency filtering
- Handling signed integers carefully in Python and other languages

