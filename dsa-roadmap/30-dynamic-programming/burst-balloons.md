# Burst Balloons

**Difficulty:** Hard
**Pattern:** Interval DP
**LeetCode:** #312

## Problem Statement
You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon has a number `nums[i]`.

If you burst balloon `i`, you gain `nums[left] * nums[i] * nums[right]` coins, where `left` and `right` are adjacent balloons still not burst. After bursting, `left` and `right` become adjacent.

Return the maximum coins you can collect.

## Examples

### Example 1
**Input:** `nums = [3,1,5,8]`
**Output:** `167`

### Example 2
**Input:** `nums = [1,5]`
**Output:** `10`

## Constraints
- `1 <= nums.length <= 300`
- `0 <= nums[i] <= 100`

## DP Breakdown
Classic interval DP idea: choose the **last** balloon to burst in each interval.

- Add virtual boundaries: `arr = [1] + nums + [1]`
- **State:** `dp[l][r]` = max coins from bursting balloons in open interval `(l, r)`
- **Transition:**
  `dp[l][r] = max(dp[l][k] + arr[l] * arr[k] * arr[r] + dp[k][r])`
  for every `k` in `(l, r)`
- **Base case:** intervals of length `<= 1` have zero coins

## Hints
- Bursting order forward is hard; choosing last burst makes neighbors fixed.
- Compute by increasing interval length.
- Virtual `1`s at both ends simplify edge handling.

## Approach
**Time Complexity:** O(N^3)
**Space Complexity:** O(N^2)

Use interval length expansion and try each split point as the last burst balloon.