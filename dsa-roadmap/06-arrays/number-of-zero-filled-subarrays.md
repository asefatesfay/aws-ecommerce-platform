# Number of Zero-Filled Subarrays

**Difficulty:** Medium
**Pattern:** Array / Counting
**LeetCode:** #2348

## Problem Statement

Given an integer array `nums`, return the number of subarrays filled with `0`. A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1
**Input:** `nums = [1, 3, 0, 0, 2, 0, 0, 4]`
**Output:** `6`
**Explanation:** There are 4 zero-filled subarrays of length 1: [0],[0],[0],[0]. Two of length 2: [0,0],[0,0]. Total = 6.

### Example 2
**Input:** `nums = [0, 0, 0, 2, 0, 0]`
**Output:** `9`
**Explanation:** [0],[0],[0],[0,0],[0,0],[0,0,0],[0],[0],[0,0] — 9 subarrays.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Focus on runs of consecutive zeros. Each run of zeros contributes multiple subarrays.

> 💡 **Hint 2:** For a run of k consecutive zeros, how many zero-filled subarrays does it contain? Think about subarrays of length 1, 2, ..., k.

> 💡 **Hint 3:** A run of k zeros contains k*(k+1)/2 zero-filled subarrays. Equivalently, as you extend a run, each new zero adds (current run length) new subarrays. Sum these contributions across all runs.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track the current run length of zeros. When you see a zero, increment the run length and add it to the total count (each new zero creates exactly `run_length` new subarrays ending at the current position). Reset the run length to 0 on non-zero elements.
