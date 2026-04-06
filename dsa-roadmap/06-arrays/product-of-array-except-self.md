# Product of Array Except Self

**Difficulty:** Medium
**Pattern:** Prefix/Suffix Products
**LeetCode:** #238

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4]`
**Output:** `[24, 12, 8, 6]`
**Explanation:** answer[0] = 2*3*4=24, answer[1] = 1*3*4=12, answer[2] = 1*2*4=8, answer[3] = 1*2*3=6.

### Example 2
**Input:** `nums = [-1, 1, 0, -3, 3]`
**Output:** `[0, 0, 9, 0, 0]`

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer

## Hints

> 💡 **Hint 1:** For each position i, the answer is (product of all elements to the left of i) × (product of all elements to the right of i).

> 💡 **Hint 2:** Precompute a prefix product array and a suffix product array. Then answer[i] = prefix[i-1] * suffix[i+1].

> 💡 **Hint 3:** To achieve O(1) extra space (excluding output), do two passes over the output array: first fill it with prefix products (left to right), then multiply in suffix products (right to left) using a running variable.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) extra (output array doesn't count)

Two-pass approach: first pass fills the output with prefix products. Second pass multiplies each position by the running suffix product, computed on the fly from right to left.

## Python Implementation

```python
def product_except_self(nums):
	n = len(nums)
	out = [1] * n

	prefix = 1
	for i in range(n):
		out[i] = prefix
		prefix *= nums[i]

	suffix = 1
	for i in range(n - 1, -1, -1):
		out[i] *= suffix
		suffix *= nums[i]

	return out
```

## Typical Interview Use Cases

- Prefix/suffix decomposition without division
- O(1) auxiliary-space follow-up handling
- Core pattern reused in many left-right accumulation problems

