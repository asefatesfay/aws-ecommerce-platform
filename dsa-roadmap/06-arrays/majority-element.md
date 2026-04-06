# Majority Element

**Difficulty:** Easy
**Pattern:** Boyer-Moore Voting / Hash Map
**LeetCode:** #169

## Problem Statement

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Examples

### Example 1
**Input:** `nums = [3, 2, 3]`
**Output:** `3`

### Example 2
**Input:** `nums = [2, 2, 1, 1, 1, 2, 2]`
**Output:** `2`

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element always exists

## Hints

> 💡 **Hint 1:** The brute force is O(n²). A HashMap counting frequencies gives O(n) time and O(n) space. Can you do O(1) space?

> 💡 **Hint 2:** Think about the Boyer-Moore Voting Algorithm. The majority element appears more than n/2 times, so it "outvotes" all other elements combined.

> 💡 **Hint 3:** Maintain a candidate and a count. When count is 0, set the current element as the new candidate. If the current element matches the candidate, increment count; otherwise decrement. The final candidate is the majority element.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Boyer-Moore Voting: maintain a candidate and a vote count. The majority element's votes can never be fully cancelled out by minority elements, so the final candidate is always the majority element.
