# Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Top K / Heap / Bucket Sort
**LeetCode:** #347

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Examples

### Example 1
**Input:** `nums = [1,1,1,2,2,3]`, `k = 2`
**Output:** `[1,2]`

### Example 2
**Input:** `nums = [1]`, `k = 1`
**Output:** `[1]`

## Constraints
- `1 <= nums.length <= 10⁵`
- `k` is in range `[1, number of unique elements]`
- Answer is guaranteed to be unique

## Hints

> 💡 **Hint 1:** First count frequencies using a hash map.

> 💡 **Hint 2:** Heap approach: maintain a min-heap of size k. Push `(freq, num)` pairs. When heap exceeds k, pop the minimum frequency element.

> 💡 **Hint 3:** Bucket sort approach (O(N)): create buckets where index = frequency. Fill buckets, then read from highest frequency down until you have k elements.

## Approach
**Time Complexity:** O(N log k) with heap, O(N) with bucket sort
**Space Complexity:** O(N)

Count frequencies, then use a min-heap of size k to keep the k most frequent, or use bucket sort for linear time.
