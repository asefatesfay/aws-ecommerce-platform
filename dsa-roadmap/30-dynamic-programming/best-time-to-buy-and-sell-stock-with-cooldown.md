# Best Time to Buy and Sell Stock with Cooldown

**Difficulty:** Medium
**Pattern:** State Machine DP
**LeetCode:** #309

## Problem Statement
Given stock prices, find the maximum profit. You may complete as many transactions as you like, but after selling you must wait one day (cooldown) before buying again.

## Examples

### Example 1
**Input:** `prices = [1,2,3,0,2]`
**Output:** `3`
**Explanation:** buy(1) → sell(2) → cooldown → buy(0) → sell(2) = 3

### Example 2
**Input:** `prices = [1]`
**Output:** `0`

## Constraints
- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Hints

> 💡 **Hint 1:** Model with 3 states: `held` (holding stock), `sold` (just sold, in cooldown), `rest` (not holding, not in cooldown).

> 💡 **Hint 2:** Transitions: `held = max(held, rest - price)`, `sold = held + price`, `rest = max(rest, sold)`.

> 💡 **Hint 3:** Initialize: `held = -prices[0]`, `sold = 0`, `rest = 0`. Answer is `max(sold, rest)`.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

State machine with 3 states. At each price, update all three states simultaneously using previous values.
