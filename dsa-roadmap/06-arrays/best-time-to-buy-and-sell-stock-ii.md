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

## Approach 1: Brute Force (DP)

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

For each day, try all possible previous buy days and track the best multi-transaction profit.

```python
def max_profit_brute(prices: list[int]) -> int:
    n = len(prices)
    # dp[i] = max profit using prices[0..i]
    dp = [0] * n
    for i in range(1, n):
        dp[i] = dp[i - 1]  # don't sell today
        for j in range(i):
            if prices[i] > prices[j]:
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j])
    return dp[-1]
```

**Why it's slow:** O(n²) — reconsiders all previous buy days for each sell day.

---

## Approach 2: Greedy (Capture Every Upswing) — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Key insight: any multi-day gain can be decomposed into consecutive single-day gains. Capture every positive consecutive difference.

### Why This Works

```
prices = [1, 5, 3, 6]

Optimal trades: buy at 1, sell at 5 (profit=4), buy at 3, sell at 6 (profit=3). Total=7.

Greedy consecutive differences:
  5-1=4, 3-5=-2 (skip), 6-3=3
  Sum of positives = 4+3 = 7 ✓

This works because: profit(buy@1, sell@6) = (5-1) + (3-5) + (6-3)
Any multi-day gain = sum of all daily gains in that period.
Skipping negative days is equivalent to selling and rebuying.
```

### Visual Trace

```
prices = [7, 1, 5, 3, 6, 4]

i=1: 1-7=-6 → skip
i=2: 5-1=4  → profit += 4 = 4
i=3: 3-5=-2 → skip
i=4: 6-3=3  → profit += 3 = 7
i=5: 4-6=-2 → skip

Answer: 7 ✓
```

```python
def max_profit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| DP | O(n²) | O(n) | Reconsiders all buy days |
| Greedy | O(n) | O(1) | Optimal — capture all upswings |

## Typical Interview Use Cases

- Unlimited transactions greedy pattern
- Demonstrating decomposition of uphill segments into local gains
- Transition point into DP-based stock variants (cooldown/fee/k-transactions)

