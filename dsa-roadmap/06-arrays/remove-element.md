# Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #27

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. The order of the remaining elements may be changed. Return the number of elements in `nums` that are not equal to `val`.

The judge will check the first `k` elements of `nums` (where `k` is your return value) to verify correctness. Elements beyond index `k` don't matter.

## Examples

### Example 1
**Input:** `nums = [3, 2, 2, 3]`, `val = 3`
**Output:** `2`, `nums = [2, 2, _, _]`
**Explanation:** The first 2 elements are `[2, 2]`. The underscores represent values that don't matter.

### Example 2
**Input:** `nums = [0, 1, 2, 2, 3, 0, 4, 2]`, `val = 2`
**Output:** `5`, `nums = [0, 1, 4, 0, 3, _, _, _]`
**Explanation:** 5 elements are not equal to 2. Order among them doesn't matter.

## Constraints
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Hints

> 💡 **Hint 1:** You need to keep all elements that are NOT equal to `val`. Think about a write pointer that only advances when you write a valid element.

> 💡 **Hint 2:** Use a single pointer `k` starting at 0. Iterate through the array; whenever `nums[i] != val`, copy `nums[i]` to `nums[k]` and increment `k`.

> 💡 **Hint 3:** The return value is `k` — the count of elements not equal to `val`. The first `k` positions of `nums` will hold those elements.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Maintain a write pointer `k`. Scan through the array; whenever the current element is not equal to `val`, write it to position `k` and increment `k`. Return `k` as the new length.

## Python Implementation

```python
def remove_element(nums, val):
	k = 0
	for x in nums:
		if x != val:
			nums[k] = x
			k += 1
	return k
```

## Typical Interview Use Cases

- In-place removal with returned logical length
- Follow-up on unstable output ordering constraints
- Foundation for deduplication and stream-compaction patterns

