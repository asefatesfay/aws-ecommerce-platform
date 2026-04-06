# 30. Dynamic Programming

## Overview
DP solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation. Two approaches: top-down (memoization) and bottom-up (tabulation).

## Key Concepts
- **Optimal substructure**: optimal solution built from optimal subproblem solutions
- **Overlapping subproblems**: same subproblems solved multiple times
- **State definition**: what information uniquely identifies a subproblem
- **Transition**: how to compute state from previous states

## Common Patterns
| Pattern | Key Idea |
|---------|---------|
| 1D DP | `dp[i]` depends on `dp[i-1]` or `dp[i-k]` |
| 0/1 Knapsack | Include or exclude each item |
| Unbounded Knapsack | Can use each item multiple times |
| LIS | `dp[i]` = longest increasing subsequence ending at i |
| Grid DP | `dp[i][j]` depends on neighbors |
| String DP | `dp[i][j]` for two string prefixes |
| State Machine | States represent phases (buy/sell/cooldown) |

## When to Use
- "Maximum/minimum" with choices → DP
- "Number of ways" → DP
- "Can we achieve X?" → DP
- Recursive solution with repeated subproblems → memoize it

## Problems
| Problem | Difficulty |
|---------|-----------|
| Climbing Stairs | Easy |
| House Robber | Medium |
| Coin Change | Medium |
| Longest Increasing Subsequence | Medium |
| Longest Common Subsequence | Medium |
| Edit Distance | Medium |
| Word Break | Medium |
| Burst Balloons | Hard |
