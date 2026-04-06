# Maximum Average Subarray I

**Difficulty:** Easy
**Pattern:** Sliding Window (Fixed)
**LeetCode:** #643

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.

## Examples

### Example 1
**Input:** `nums = [1, 12, -5, -6, 50, 3]`, `k = 4`
**Output:** `12.75`
**Explanation:** Maximum average is (12-5-6+50)/4 = 51/4 = 12.75.

### Example 2
**Input:** `nums = [5]`, `k = 1`
**Output:** `5.0`

## Constraints
- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** Compute the sum of the first k elements. This is your initial window.

> 💡 **Hint 2:** Slide the window: add the next element and remove the leftmost element. Update the running sum.

> 💡 **Hint 3:** Track the maximum sum seen. Divide by k at the end to get the maximum average.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Fixed sliding window of size k. Maintain a running sum, updating by adding the new element and subtracting the element leaving the window. Track the maximum sum.
