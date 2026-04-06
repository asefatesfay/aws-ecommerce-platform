# Best Time to Buy and Sell Stock II

**Difficulty:** Medium
**Pattern:** Greedy
**LeetCode:** #122

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

## Examples

### Example 1
**Input:** `prices = [7, 1, 5, 3, 6, 4]`
**Output:** `7`
**Explanation:** Buy day 2 (price=1), sell day 3 (price=5), profit=4. Buy day 4 (price=3), sell day 5 (price=6), profit=3. Total = 7.

### Example 2
**Input:** `prices = [1, 2, 3, 4, 5]`
**Output:** `4`
**Explanation:** Buy day 1, sell day 5. Or equivalently, capture every upward step.

### Example 3
**Input:** `prices = [7, 6, 4, 3, 1]`
**Output:** `0`

## Constraints
- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Hints

> 💡 **Hint 1:** Unlike Stock I, you can make multiple transactions. Think about what the maximum possible profit looks like.

> 💡 **Hint 2:** The maximum profit equals the sum of all positive price differences between consecutive days. If prices[i+1] > prices[i], you'd want to capture that gain.

> 💡 **Hint 3:** Greedily add every positive consecutive difference: `profit += max(0, prices[i+1] - prices[i])` for all i. This is equivalent to buying at every local minimum and selling at every local maximum.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Sum up all positive consecutive differences. This greedy approach works because any multi-day gain can be decomposed into a sum of single-day gains, and we capture all of them.
