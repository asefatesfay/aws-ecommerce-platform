# Find Peak Element

**Difficulty:** Medium
**Pattern:** Binary Search
**LeetCode:** #162

## Problem Statement

A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array. You must write an algorithm that runs in O(log n) time.

## Examples

### Example 1
**Input:** `nums = [1,2,3,1]`
**Output:** `2`
**Explanation:** 3 is a peak element.

### Example 2
**Input:** `nums = [1,2,1,3,5,6,4]`
**Output:** `5`
**Explanation:** 6 is a peak element (index 5).

## Constraints
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`

## Hints

> 💡 **Hint 1:** If nums[mid] < nums[mid+1], there must be a peak to the right (the array is going up). Move left = mid + 1.

> 💡 **Hint 2:** If nums[mid] > nums[mid+1], there must be a peak at mid or to the left. Move right = mid.

> 💡 **Hint 3:** When left == right, that's a peak.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search: always move toward the ascending direction. A peak is guaranteed to exist in that direction.
