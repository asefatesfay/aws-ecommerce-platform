# Sum of Subarray Ranges

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #2104

## Problem Statement

You are given an integer array `nums`. The range of a subarray of `nums` is the difference between the largest and smallest element in the subarray. Return the sum of all subarray ranges of `nums`.

## Examples

### Example 1
**Input:** `nums = [1,2,3]`
**Output:** `4`
**Explanation:** Ranges: [1]=0, [2]=0, [3]=0, [1,2]=1, [2,3]=1, [1,2,3]=2. Sum=4.

### Example 2
**Input:** `nums = [1,3,3]`
**Output:** `4`

### Example 3
**Input:** `nums = [4,-2,-3,4,1]`
**Output:** `59`

## Constraints
- `1 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Sum of ranges = Sum of subarray maximums - Sum of subarray minimums.

> 💡 **Hint 2:** Use the same monotonic stack technique from "Sum of Subarray Minimums" to compute both sums separately.

> 💡 **Hint 3:** For maximums, use a monotonic decreasing stack. For minimums, use a monotonic increasing stack. Subtract.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Compute sum of subarray maximums and sum of subarray minimums separately using monotonic stacks. Return their difference.
