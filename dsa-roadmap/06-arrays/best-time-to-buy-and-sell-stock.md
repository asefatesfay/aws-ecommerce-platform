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

## 🔴 Approach 1: Brute Force (Nested Loop)

**Mental Model:** Try every possible buy-sell pair and pick the best.

For each day `i` (buy day), check all future days `j > i` (sell day) and compute profit. Track the maximum.

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

### Why the Brute Force Works

```python
def max_profit_brute(prices):
    """
    Try every possible buy-sell pair.
    Time: O(n²) — two nested loops over the array
    """
    max_profit = 0
    
    # Day i: buy on this day
    for i in range(len(prices)):
        # Day j: sell on a future day (j > i)
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit
```

### Tracing Brute Force: `[7, 1, 5, 3, 6, 4]`

```
i=0 (buy at 7):
  j=1: profit = 1 - 7 = -6  ✗
  j=2: profit = 5 - 7 = -2  ✗
  j=3: profit = 3 - 7 = -4  ✗
  j=4: profit = 6 - 7 = -1  ✗
  j=5: profit = 4 - 7 = -3  ✗

i=1 (buy at 1):
  j=2: profit = 5 - 1 = 4   ← best so far
  j=3: profit = 3 - 1 = 2
  j=4: profit = 6 - 1 = 5   ← NEW BEST!
  j=5: profit = 4 - 1 = 3

i=2 (buy at 5):
  j=3: profit = 3 - 5 = -2  ✗
  j=4: profit = 6 - 5 = 1
  j=5: profit = 4 - 5 = -1  ✗

i=3 (buy at 3):
  j=4: profit = 6 - 3 = 3
  j=5: profit = 4 - 3 = 1

i=4 (buy at 6):
  j=5: profit = 4 - 6 = -2  ✗

Maximum profit: 5 ✓
```

**Problem with brute force:** We visit the same comparisons repeatedly. For large arrays (10⁵ elements), 10¹⁰ operations is too slow.

---

## 🟢 Approach 2: Optimal (Single Pass with Min Tracking)

**Mental Model:** As you scan left to right, remember the lowest price you've seen. At each price, the best profit is `current_price - lowest_price_so_far`.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### Why the Optimal Approach Works

The key insight: **For any sell day, the best buy day is the minimum price before it.** So we don't need nested loops.

```python
def max_profit(prices):
    """
    Track the minimum price seen so far.
    At each price, compute profit = current_price - min_price_so_far.
    Time: O(n) — single pass
    """
    min_price = float("inf")
    best_profit = 0

    for price in prices:
        # If we sell today, what's the best profit?
        profit_if_sell_today = price - min_price
        best_profit = max(best_profit, profit_if_sell_today)
        
        # Update the lowest price seen so far
        min_price = min(min_price, price)

    return best_profit
```

### Tracing Optimal: `[7, 1, 5, 3, 6, 4]`

```
Initial: min_price = ∞, best_profit = 0

Day 0 (price=7):
  profit_if_sell = 7 - ∞ = -∞ (invalid)
  best_profit = max(0, -∞) = 0
  min_price = min(∞, 7) = 7

Day 1 (price=1):
  profit_if_sell = 1 - 7 = -6
  best_profit = max(0, -6) = 0
  min_price = min(7, 1) = 1    ← NEW MINIMUM!

Day 2 (price=5):
  profit_if_sell = 5 - 1 = 4
  best_profit = max(0, 4) = 4   ← PROFIT FOUND!
  min_price = min(1, 5) = 1

Day 3 (price=3):
  profit_if_sell = 3 - 1 = 2
  best_profit = max(4, 2) = 4
  min_price = min(1, 3) = 1

Day 4 (price=6):
  profit_if_sell = 6 - 1 = 5
  best_profit = max(4, 5) = 5   ← NEW BEST!
  min_price = min(1, 6) = 1

Day 5 (price=4):
  profit_if_sell = 4 - 1 = 3
  best_profit = max(5, 3) = 5
  min_price = min(1, 4) = 1

Result: 5 ✓
```

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force | Optimal |
|--------|-----------|---------|
| **Time Complexity** | O(n²) | O(n) |
| **Space Complexity** | O(1) | O(1) |
| **For n=100** | ~10,000 ops | ~100 ops |
| **For n=10⁵** | ~10¹⁰ ops (**too slow**) | ~10⁵ ops ✓ |
| **Key Insight** | Try all pairs | Carry forward the minimum |
| **Interview Viability** | Acceptable for small n, teaches pattern | **Preferred solution** |

**Why optimal wins:** The brute force looks backward at all previous prices for every current price. The optimal approach realizes this is wasteful — just keep the **minimum so far** as a variable. No wasted work.

---

## Python Implementation

```python
def max_profit(prices):
    min_price = float("inf")
    best = 0

    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)

    return best
```

## Typical Interview Use Cases

- Single transaction optimization with one-pass tracking
- Prefix minimum + current value difference pattern
- Common baseline before multi-transaction stock variants

