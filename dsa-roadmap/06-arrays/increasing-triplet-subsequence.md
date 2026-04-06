# Increasing Triplet Subsequence

**Difficulty:** Medium
**Pattern:** Greedy / Tracking Minimums
**LeetCode:** #334

## Problem Statement

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

Follow-up: Can you implement a solution that runs in O(n) time and O(1) space?

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4, 5]`
**Output:** `true`
**Explanation:** Any triplet like (0,1,2) works.

### Example 2
**Input:** `nums = [5, 4, 3, 2, 1]`
**Output:** `false`
**Explanation:** No increasing triplet exists.

### Example 3
**Input:** `nums = [2, 1, 5, 0, 4, 6]`
**Output:** `true`
**Explanation:** (1, 4, 5) → values (1, 4, 6).

## Constraints
- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** You need to find three numbers in increasing order. Think about maintaining the smallest and second-smallest values seen so far.

> 💡 **Hint 2:** Keep two variables: `first` (smallest value seen) and `second` (smallest value seen that is greater than some previous `first`). If you find a number greater than `second`, you've found your triplet.

> 💡 **Hint 3:** Update greedily: if current ≤ first, update first. Else if current ≤ second, update second. Else return true. The key insight: even if `first` gets updated after `second` was set, `second` still "remembers" that a valid smaller value existed before it.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Maintain two variables representing the smallest and second-smallest values in a potential increasing triplet. Greedily update them as you scan; if any element exceeds both, an increasing triplet exists.

## Python Implementation

```python
def increasing_triplet(nums):
	first = float("inf")
	second = float("inf")

	for x in nums:
		if x <= first:
			first = x
		elif x <= second:
			second = x
		else:
			return True

	return False
```

## Typical Interview Use Cases

- Existence checks for increasing subsequences of fixed length
- Greedy state compression from O(n^2) DP intuition to O(1)
- Precursor to LIS reasoning and patience sorting discussions

