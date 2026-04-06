# Subarray Sum Equals K

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map
**LeetCode:** #560

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

## Examples

### Example 1
**Input:** `nums = [1, 1, 1]`, `k = 2`
**Output:** `2`
**Explanation:** [1,1] at indices (0,1) and (1,2).

### Example 2
**Input:** `nums = [1, 2, 3]`, `k = 3`
**Output:** `2`
**Explanation:** [3] and [1,2].

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Hints

> 💡 **Hint 1:** A subarray sum from index l to r equals `prefix[r] - prefix[l-1]`. You want this to equal k, so you need `prefix[r] - k` to have appeared as a prefix sum before.

> 💡 **Hint 2:** Use a HashMap to count how many times each prefix sum has been seen. Initialize with `{0: 1}` (empty prefix sum of 0 appears once).

> 💡 **Hint 3:** For each index, compute the running prefix sum. Add `map[prefix_sum - k]` to the count (number of valid left endpoints). Then increment `map[prefix_sum]`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Running prefix sum with a HashMap counting occurrences. For each prefix sum p, add the count of (p - k) from the map to the answer, then record p in the map.
