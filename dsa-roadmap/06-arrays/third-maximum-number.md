# Third Maximum Number

**Difficulty:** Easy
**Pattern:** Array / Tracking Top-K
**LeetCode:** #414

## Problem Statement

Given an integer array `nums`, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

## Examples

### Example 1
**Input:** `nums = [3, 2, 1]`
**Output:** `1`
**Explanation:** The third maximum is 1.

### Example 2
**Input:** `nums = [1, 2]`
**Output:** `2`
**Explanation:** The third maximum does not exist, so return the maximum (2).

### Example 3
**Input:** `nums = [2, 2, 3, 1]`
**Output:** `1`
**Explanation:** The third distinct maximum is 1. Note that 2 appears twice but counts as one distinct value.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** You need to track the top 3 distinct values. Use three variables: first, second, third maximum.

> 💡 **Hint 2:** Initialize all three to negative infinity. For each number, update the three variables carefully — skip duplicates, and cascade updates (if a number beats first, the old first becomes second, old second becomes third).

> 💡 **Hint 3:** Be careful with the initial values — since nums can contain `Integer.MIN_VALUE`, use a sentinel like `None` or a separate boolean to track whether each slot has been filled.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Maintain three variables for the top three distinct maximums. For each element, skip if it equals any of the three. Otherwise, update the three variables in order, cascading values down. If the third maximum was never set, return the first maximum.

## Python Implementation

```python
def third_max(nums):
	first = second = third = None

	for x in nums:
		if x == first or x == second or x == third:
			continue

		if first is None or x > first:
			third = second
			second = first
			first = x
		elif second is None or x > second:
			third = second
			second = x
		elif third is None or x > third:
			third = x

	return third if third is not None else first
```

## Typical Interview Use Cases

- Distinct top-k tracking in one pass
- Sentinel handling and duplicate filtering
- Alternative to sorting when only small-order statistics are needed

