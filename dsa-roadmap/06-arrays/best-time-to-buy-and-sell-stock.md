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

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Try every buy-sell pair.

```python
def max_profit_brute(prices: list[int]) -> int:
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best
```

**Why it's slow:** For n=100,000 this is ~5 billion comparisons.

---

## Approach 2: Track Minimum — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

For any sell day, the best buy day is the minimum price before it. Track the running minimum in a single pass.

### Visual Trace

```
prices = [7, 1, 5, 3, 6, 4]

min_price=∞, best=0

price=7: best=max(0, 7-∞)=0,  min_price=7
price=1: best=max(0, 1-7)=0,  min_price=1  ← new min
price=5: best=max(0, 5-1)=4,  min_price=1
price=3: best=max(4, 3-1)=4,  min_price=1
price=6: best=max(4, 6-1)=5,  min_price=1  ← new best
price=4: best=max(5, 4-1)=5,  min_price=1

Answer: 5 ✓
```

```python
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Try all pairs |
| Track minimum | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Single transaction optimization with one-pass tracking
- Prefix minimum + current value difference pattern
- Common baseline before multi-transaction stock variants

