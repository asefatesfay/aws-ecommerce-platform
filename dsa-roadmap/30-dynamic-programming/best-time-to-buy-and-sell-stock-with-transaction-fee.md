# Best Time to Buy and Sell Stock with Transaction Fee

**Difficulty:** Medium
**Pattern:** State Machine DP
**LeetCode:** #714

## Problem Statement
You are given an array `prices` where `prices[i]` is the stock price on day `i`, and an integer `fee`.

You may buy and sell as many times as you want, but you must sell before buying again. Each transaction pays the fee once.

Return the maximum profit.

## Examples

### Example 1
**Input:** `prices = [1,3,2,8,4,9]`, `fee = 2`
**Output:** `8`

### Example 2
**Input:** `prices = [1,3,7,5,10,3]`, `fee = 3`
**Output:** `6`

## Constraints
- `1 <= prices.length <= 5 * 10^4`
- `1 <= prices[i] < 5 * 10^4`
- `0 <= fee < 5 * 10^4`

## DP Breakdown
Two states per day:
- `hold`: max profit while holding one stock
- `cash`: max profit while holding no stock

Transitions for price `p`:
- `newHold = max(hold, cash - p)`
- `newCash = max(cash, hold + p - fee)`

## Hints
- Transaction fee is paid when selling.
- Keep previous day states before updating.
- This is a compact state machine DP.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Scan prices once while updating `hold` and `cash`.