# Coin Change II

**Difficulty:** Medium
**Pattern:** Unbounded Knapsack DP
**LeetCode:** #518

## Problem Statement
Given `amount` and `coins`, return the number of combinations to make up `amount`.
Each coin can be used unlimited times. Order does not matter.

## Input/Output Examples
1. Input: `amount = 5, coins = [1,2,5]` -> Output: `4`
2. Input: `amount = 3, coins = [2]` -> Output: `0`
3. Input: `amount = 10, coins = [10]` -> Output: `1`

## Why This Is DP (overlapping + optimal substructure)
- Overlapping: same remaining amount after choosing some prefix of coins appears repeatedly.
- Optimal substructure: combinations for amount `a` include combinations for `a - coin`.

## Mermaid Visual
```mermaid
flowchart LR
    A[dp[a]] --> B[dp[a-coin1]]
    A --> C[dp[a-coin2]]
```

## Brute Force (Python)
```python
def change_bruteforce(amount, coins):
    n = len(coins)
    def dfs(i, rem):
        if rem == 0:
            return 1
        if i == n or rem < 0:
            return 0
        use = dfs(i, rem - coins[i])
        skip = dfs(i + 1, rem)
        return use + skip

    return dfs(0, amount)
```

## Optimal DP (Python)
```python
def change_dp(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]
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
- Brute force recursion: exponential in amount and branching choices.
- Optimal DP: `O(len(coins) * amount)` time, `O(amount)` space.
