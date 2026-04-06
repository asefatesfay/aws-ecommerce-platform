# Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Pattern:** Array / Greedy / Tracking Minimum
**LeetCode:** #121

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve. If no profit is possible, return `0`.

## Examples

### Example 1
**Input:** `prices = [7, 1, 5, 3, 6, 4]`
**Output:** `5`
**Explanation:** Buy on day 2 (price=1), sell on day 5 (price=6). Profit = 6 - 1 = 5.

### Example 2
**Input:** `prices = [7, 6, 4, 3, 1]`
**Output:** `0`
**Explanation:** Prices only decrease, so no transaction is profitable.

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Hints

> 💡 **Hint 1:** You must buy before you sell. So for each day you consider selling, the best buy day is the minimum price seen so far.

> 💡 **Hint 2:** Track the minimum price seen so far as you scan left to right. At each day, the potential profit is `current_price - min_price_so_far`.

> 💡 **Hint 3:** Update the global maximum profit at each step. Update the minimum price whenever you see a lower price. One pass is sufficient.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass: track the minimum price seen so far and the maximum profit. At each price, compute the profit if selling today (current price minus minimum so far), update the maximum profit, then update the minimum price.
