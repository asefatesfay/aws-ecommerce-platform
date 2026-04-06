# Jump Game II

**Difficulty:** Medium
**Pattern:** Greedy — BFS-like
**LeetCode:** #45

## Problem Statement
Given `nums` where `nums[i]` is the max jump from index `i`, return the minimum number of jumps to reach the last index. You can always reach the last index.

## Examples

### Example 1
**Input:** `nums = [2,3,1,1,4]`
**Output:** `2`
**Explanation:** Jump from index 0 to 1 (jump 1), then to last index (jump 2).

### Example 2
**Input:** `nums = [2,3,0,1,4]`
**Output:** `2`

## Constraints
- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 1000`

## Hints

> 💡 **Hint 1:** Think of it like BFS levels. Each "level" is the range of indices reachable with the current number of jumps.

> 💡 **Hint 2:** Track `current_end` (end of current jump level) and `farthest` (farthest reachable from current level). When you reach `current_end`, increment jumps and set `current_end = farthest`.

> 💡 **Hint 3:** Stop as soon as `current_end >= last index`.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Greedy BFS: track the farthest reachable index within the current jump. When the current jump's range is exhausted, take another jump.
