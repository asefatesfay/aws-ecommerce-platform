# Capacity To Ship Packages Within D Days

**Difficulty:** Medium
**Pattern:** Binary Search on Answer
**LeetCode:** #1011

## Problem Statement

A conveyor belt has packages that must be shipped from one port to another within `days` days. The `i`th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

## Examples

### Example 1
**Input:** `weights = [1,2,3,4,5,6,7,8,9,10]`, `days = 5`
**Output:** `15`

### Example 2
**Input:** `weights = [3,2,2,4,1,4]`, `days = 3`
**Output:** `6`

## Constraints
- `1 <= days <= weights.length <= 5 * 10^4`
- `1 <= weights[i] <= 500`

## Hints

> 💡 **Hint 1:** Binary search on the capacity. The minimum possible capacity is max(weights) (must fit the heaviest package). The maximum is sum(weights) (ship everything in one day).

> 💡 **Hint 2:** For a given capacity, simulate loading: greedily fill each day until adding the next package would exceed capacity. Count days needed.

> 💡 **Hint 3:** If days needed ≤ target days, capacity is feasible (try smaller). Otherwise, try larger.

## Approach

**Time Complexity:** O(n log(sum))
**Space Complexity:** O(1)

Binary search on capacity [max(weights), sum(weights)]. Check feasibility by simulating greedy loading.
