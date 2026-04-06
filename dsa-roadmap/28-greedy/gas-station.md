# Gas Station

**Difficulty:** Medium
**Pattern:** Greedy
**LeetCode:** #134

## Problem Statement
There are `n` gas stations in a circle. `gas[i]` is the gas at station `i`, `cost[i]` is the gas to travel from `i` to `i+1`. Find the starting station index to complete the circuit, or return -1 if impossible.

## Examples

### Example 1
**Input:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`
**Output:** `3`

### Example 2
**Input:** `gas = [2,3,4]`, `cost = [3,4,3]`
**Output:** `-1`

## Constraints
- `n == gas.length == cost.length`
- `1 <= n <= 10⁵`
- `0 <= gas[i], cost[i] <= 10⁴`

## Hints

> 💡 **Hint 1:** If total gas < total cost, it's impossible. Otherwise, a solution always exists.

> 💡 **Hint 2:** Track running tank. If tank goes negative at station `i`, reset the starting point to `i+1` and reset tank to 0.

> 💡 **Hint 3:** The greedy insight: if you can't reach station `i` from any station before it, then none of those stations can be the answer either.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Single pass: if total gas ≥ total cost, a solution exists. Find it by resetting start whenever the running sum goes negative.
