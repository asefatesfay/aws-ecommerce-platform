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

### Visual Example: Prefix × Suffix

```
Input: [1, 2, 3, 4]

Pass 1: Fill output with LEFT products (prefix)
  out[0] = 1 (nothing to left)
  out[1] = 1 (1*1)
  out[2] = 1*2 = 2
  out[3] = 1*2*3 = 6
  After Pass 1: [1, 1, 2, 6]

Pass 2: Multiply by RIGHT products (suffix), right to left
  i=3: suffix=1, out[3] *= 1 = 6, suffix *= 4 = 4
       out[3] = 6 (left=1*2*3, right=1) ✓
       
  i=2: suffix=4, out[2] *= 4 = 8, suffix *= 3 = 12
       out[2] = 8 (left=1*2, right=4) ✓
       
  i=1: suffix=12, out[1] *= 12 = 12, suffix *= 2 = 24
       out[1] = 12 (left=1, right=3*4) ✓
       
  i=0: suffix=24, out[0] *= 24 = 24, suffix *= 1 = 24
       out[0] = 24 (left=1, right=2*3*4) ✓

Final output: [24, 12, 8, 6] ✓
```

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

