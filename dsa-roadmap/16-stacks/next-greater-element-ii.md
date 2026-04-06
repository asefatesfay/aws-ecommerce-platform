# Next Greater Element II

**Difficulty:** Medium
**Pattern:** Monotonic Stack (Circular)
**LeetCode:** #503

## Problem Statement

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return the next greater number for every element in `nums`. The next greater number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

## Examples

### Example 1
**Input:** `nums = [1,2,1]`
**Output:** `[2,-1,2]`
**Explanation:** For 1 at index 0: next greater is 2. For 2: no greater exists. For 1 at index 2: next greater is 2 (wrapping around).

### Example 2
**Input:** `nums = [1,2,3,4,3]`
**Output:** `[2,3,4,-1,4]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** For a circular array, simulate two passes by iterating indices 0 to 2n-1 (using modulo).

> 💡 **Hint 2:** Use a monotonic decreasing stack of indices. On the second pass, don't push new indices — only resolve existing ones.

> 💡 **Hint 3:** When the current element is greater than the stack top's element, pop and record the answer. Continue until the stack is empty or the top is greater.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic stack with two-pass simulation (indices 0 to 2n-1 mod n). Resolve elements on the second pass without pushing new ones.
