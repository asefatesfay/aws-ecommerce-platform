# Missing Number

**Difficulty:** Easy
**Pattern:** Bit Manipulation / Math
**LeetCode:** #268

## Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Examples

### Example 1
**Input:** `nums = [3, 0, 1]`
**Output:** `2`
**Explanation:** n = 3, range is [0,3]. 2 is missing.

### Example 2
**Input:** `nums = [0, 1]`
**Output:** `2`
**Explanation:** n = 2, range is [0,2]. 2 is missing.

### Example 3
**Input:** `nums = [9,6,4,2,3,5,7,0,1]`
**Output:** `8`

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All numbers in `nums` are unique

## Hints

> 💡 **Hint 1:** The sum of [0, n] is n*(n+1)/2. The missing number is that expected sum minus the actual sum of the array.

> 💡 **Hint 2:** Alternatively, use XOR: XOR all indices 0..n with all elements. Pairs cancel, leaving the missing number.

> 💡 **Hint 3:** Both approaches are O(n) time and O(1) space. The math approach is simpler; the XOR approach avoids potential overflow with very large n.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Math approach: expected sum = n*(n+1)/2, actual sum = sum of array. Missing number = expected - actual. XOR approach: XOR all indices 0..n with all array values; everything cancels except the missing number.

## Python Implementation

```python
def missing_number(nums):
	result = len(nums)
	for i, x in enumerate(nums):
		result ^= i ^ x
	return result
```

## Typical Interview Use Cases

- Recovering one missing value from 0..n under O(1) extra space
- Comparing arithmetic-sum and XOR cancellation approaches
- Common example of using indices as part of the bitwise invariant

