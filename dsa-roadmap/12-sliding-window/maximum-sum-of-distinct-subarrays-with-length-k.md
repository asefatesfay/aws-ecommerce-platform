# Maximum Sum of Distinct Subarrays With Length K

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed) + Hash Set
**LeetCode:** #2461

## Problem Statement

You are given an integer array `nums` and an integer `k`. Find the maximum subarray sum of all the subarrays of `nums` that meet the following conditions:
- The length of the subarray is `k`.
- All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return `0`.

## Examples

### Example 1
**Input:** `nums = [1, 5, 4, 2, 9, 9, 9]`, `k = 3`
**Output:** `15`
**Explanation:** Subarrays of length 3 with distinct elements: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15. Max is 15.

### Example 2
**Input:** `nums = [4, 4, 4]`, `k = 3`
**Output:** `0`
**Explanation:** No subarray of length 3 has all distinct elements.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Use a fixed window of size k. Track the current sum and a frequency map (or set) to check for duplicates.

> 💡 **Hint 2:** When sliding the window, add the new element to the frequency map and sum. Remove the outgoing element from the map and sum.

> 💡 **Hint 3:** A window is valid (all distinct) when the frequency map has exactly k entries (or equivalently, no entry has count > 1). Update the maximum sum only for valid windows.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Fixed window with a HashMap tracking element frequencies. Track the number of distinct elements. Update max sum only when the window has k distinct elements.
