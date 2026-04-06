# Maximum Gap

**Difficulty:** Medium
**Pattern:** Radix Sort / Bucket Sort
**LeetCode:** #164

## Problem Statement

Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return `0`. You must write an algorithm that runs in linear time and uses linear extra space.

## Examples

### Example 1
**Input:** `nums = [3,6,1]`
**Output:** `3`
**Explanation:** Sorted: [1,3,6]. Max gap = 6-3 = 3.

### Example 2
**Input:** `nums = [10]`
**Output:** `0`

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** The requirement for O(n) time means you can't use comparison sort. Use Radix Sort or the Bucket Sort approach.

> 💡 **Hint 2:** Bucket approach: by the pigeonhole principle, if n numbers span range [min, max], the maximum gap is at least (max-min)/(n-1). Create n-1 buckets of this size.

> 💡 **Hint 3:** Each bucket stores only the min and max of its elements. The maximum gap must occur between buckets (not within), so scan adjacent bucket pairs for the maximum gap.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Bucket sort: create n-1 buckets, place each number in its bucket, then find the maximum gap between consecutive non-empty buckets.
