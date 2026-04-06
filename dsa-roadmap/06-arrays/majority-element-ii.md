# Majority Element II

**Difficulty:** Medium
**Pattern:** Boyer-Moore Voting (Extended)
**LeetCode:** #229

## Problem Statement

Given an integer array of size `n`, find all elements that appear more than `⌊n / 3⌋` times. Return all such elements in any order.

## Examples

### Example 1
**Input:** `nums = [3, 2, 3]`
**Output:** `[3]`

### Example 2
**Input:** `nums = [1, 2]`
**Output:** `[1, 2]`

### Example 3
**Input:** `nums = [1, 1, 1, 3, 3, 2, 2, 2]`
**Output:** `[1, 2]`

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** How many elements can appear more than n/3 times? At most 2 (since 3 × (n/3 + 1) > n). So you're looking for at most 2 candidates.

> 💡 **Hint 2:** Extend Boyer-Moore Voting to track 2 candidates and 2 counts. When both counts are 0, assign the current element to an empty candidate slot. If it matches a candidate, increment that count; otherwise decrement both counts.

> 💡 **Hint 3:** After the first pass, you have at most 2 candidates. Do a second pass to verify each candidate actually appears more than n/3 times (the voting algorithm finds candidates, not guarantees).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two-pass Boyer-Moore with two candidates: first pass finds up to 2 candidates using the voting logic, second pass counts actual occurrences to confirm which candidates truly exceed n/3.

## Python Implementation

```python
def majority_element(nums):
	cand1 = cand2 = None
	cnt1 = cnt2 = 0

	for x in nums:
		if x == cand1:
			cnt1 += 1
		elif x == cand2:
			cnt2 += 1
		elif cnt1 == 0:
			cand1, cnt1 = x, 1
		elif cnt2 == 0:
			cand2, cnt2 = x, 1
		else:
			cnt1 -= 1
			cnt2 -= 1

	out = []
	for c in (cand1, cand2):
		if c is not None and nums.count(c) > len(nums) // 3:
			out.append(c)
	return out
```

## Typical Interview Use Cases

- Frequency threshold problems with strict O(1) extra space
- Understanding why at most 2 candidates can exceed n/3
- Follow-up to classic Boyer-Moore majority element

