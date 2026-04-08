# Best Time to Buy and Sell Stock III

**Difficulty:** Hard
**Pattern:** State Machine DP
**LeetCode:** #123

## Problem Statement
Given `prices[i]` as the stock price on day `i`, return the maximum profit with at most two transactions.
You must sell before you buy again.

## Input/Output Examples
1. Input: `prices = [3,3,5,0,0,3,1,4]` -> Output: `6`
2. Input: `prices = [1,2,3,4,5]` -> Output: `4`
3. Input: `prices = [7,6,4,3,1]` -> Output: `0`

## Why This Is DP (overlapping + optimal substructure)
- Overlapping: many paths reach the same day and transaction state (holding or not, trades used).
- Optimal substructure: best profit at day `i` depends only on best states at day `i-1`.

## Mermaid Visual
```mermaid
stateDiagram-v2
    [*] --> Buy1
    Buy1 --> Sell1: sell
    Sell1 --> Buy2: buy
    Buy2 --> Sell2: sell
    Sell2 --> [*]
```

## Brute Force (Python)
```python
def max_profit_bruteforce(prices):
    n = len(prices)
    def dfs(i, holding, used):
        if i == n:
            return 0 if not holding else float("-inf")

        best = dfs(i + 1, holding, used)  # skip

        if holding:
            if used < 2:
                best = max(best, prices[i] + dfs(i + 1, 0, used + 1))
        else:
            best = max(best, -prices[i] + dfs(i + 1, 1, used))

        return best

    return dfs(0, 0, 0)
```

## Optimal DP (Python)
```python
def max_profit_dp(prices):
    buy1 = float("-inf")
    sell1 = 0
    buy2 = float("-inf")
    sell2 = 0

    for p in prices:
        buy1 = max(buy1, -p)
        sell1 = max(sell1, buy1 + p)
        buy2 = max(buy2, sell1 - p)
        sell2 = max(sell2, buy2 + p)

    return sell2
```

## DP Checklist
- Define the DP state clearly before coding.
- Identify base cases that stop recursion/iteration.
- Write recurrence from smaller subproblems.
- Ensure transitions are valid for problem constraints.
- Decide top-down memo vs bottom-up table.
- Check if state compression is possible.
- Verify behavior on empty or minimal inputs.
- Confirm impossible states are handled safely.
- Test with monotonic, random, and duplicate-heavy data.
- Re-check off-by-one around boundaries.

## Minimal Test Harness (Python)
```python
def run_small_cases(cases, solver):
    """Simple harness to quickly smoke-test a DP implementation."""
    results = []
    for args, expected in cases:
        if isinstance(args, tuple):
            got = solver(*args)
        else:
            got = solver(args)
        results.append((got, expected, got == expected))
    return results
```

## Complexity (brute force + optimal)
- Brute force recursion: exponential in days (roughly `O(3^n)`), `O(n)` stack.
- Optimal DP: `O(n)` time, `O(1)` space.
