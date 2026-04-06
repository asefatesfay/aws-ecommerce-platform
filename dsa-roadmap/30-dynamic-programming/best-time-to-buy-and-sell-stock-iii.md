# Best Time to Buy and Sell Stock III

**Difficulty:** Hard
**Pattern:** State Machine DP
**LeetCode:** #123

## Problem Statement
Given an array `prices`, find the maximum profit with at most **two** transactions.

You may not hold multiple stocks at once. You must sell before buying again.

## Examples

### Example 1
**Input:** `prices = [3,3,5,0,0,3,1,4]`
**Output:** `6`

### Example 2
**Input:** `prices = [1,2,3,4,5]`
**Output:** `4`

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^5`

## DP Breakdown
Track four states:
- `buy1`: best after first buy
- `sell1`: best after first sell
- `buy2`: best after second buy
- `sell2`: best after second sell

For each price `p`:
- `buy1 = max(buy1, -p)`
- `sell1 = max(sell1, buy1 + p)`
- `buy2 = max(buy2, sell1 - p)`
- `sell2 = max(sell2, buy2 + p)`

Answer is `sell2`.

## Hints
- Each state depends on previous transaction stage.
- Initialize buys with very negative value.
- This is equivalent to `k=2` transaction DP but optimized.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Maintain the four running DP states in one pass.