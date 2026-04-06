# 30. Dynamic Programming

## Overview
Dynamic Programming (DP) solves optimization and counting problems by reusing solutions to overlapping subproblems. Most interview DP questions are about defining the right state, writing the transition, and choosing memoization (top-down) or tabulation (bottom-up).

This section is organized by pattern, from foundational 1D recurrences to advanced state-machine and interval/string DP.

## Key Concepts
- **Optimal substructure**: optimal solution built from optimal subproblem solutions
- **Overlapping subproblems**: same subproblems solved multiple times
- **State definition**: what information uniquely identifies a subproblem
- **Transition**: how to compute state from previous states
- **Base cases**: smallest states that must be initialized correctly
- **Iteration order**: sequence that guarantees dependencies are already computed

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

## How to Study This Section
1. For each problem, write the state in one sentence before coding.
2. Derive transition from choices (take/skip, match/mismatch, buy/sell/hold).
3. Identify base cases and validate on tiny inputs.
4. Choose top-down first for clarity; convert to bottom-up for optimization.
5. Revisit space optimization only after correctness is stable.

## When to Use
- "Maximum/minimum" with choices → DP
- "Number of ways" → DP
- "Can we achieve X?" → DP
- Recursive solution with repeated subproblems → memoize it

## Problems
### 1D DP
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Fibonacci Number](./fibonacci-number.md) | Easy | #509 |
| [Climbing Stairs](./climbing-stairs.md) | Easy | #70 |
| [Min Cost Climbing Stairs](./min-cost-climbing-stairs.md) | Easy | #746 |
| [House Robber](./house-robber.md) | Medium | #198 |
| [House Robber II](./house-robber-ii.md) | Medium | #213 |

### 0/1 Knapsack
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Partition Equal Subset Sum](./partition-equal-subset-sum.md) | Medium | #416 |
| [Target Sum](./target-sum.md) | Medium | #494 |

### Unbounded Knapsack
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Coin Change](./coin-change.md) | Medium | #322 |
| [Coin Change II](./coin-change-ii.md) | Medium | #518 |
| [Perfect Squares](./perfect-squares.md) | Medium | #279 |

### LIS Family
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Longest Increasing Subsequence](./longest-increasing-subsequence.md) | Medium | #300 |

### 2D Grid DP
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Unique Paths](./unique-paths.md) | Medium | #62 |
| [Unique Paths II](./unique-paths-ii.md) | Medium | #63 |
| [Minimum Path Sum](./minimum-path-sum.md) | Medium | #64 |
| [Burst Balloons](./burst-balloons.md) | Hard | #312 |

### String DP
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Longest Common Subsequence](./longest-common-subsequence.md) | Medium | #1143 |
| [Edit Distance](./edit-distance.md) | Medium | #72 |
| [Decode Ways](./decode-ways.md) | Medium | #91 |
| [Word Break](./word-break.md) | Medium | #139 |
| [Interleaving String](./interleaving-string.md) | Medium | #97 |

### State Machine DP (Stocks)
| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| [Best Time to Buy and Sell Stock with Cooldown](./best-time-to-buy-and-sell-stock-with-cooldown.md) | Medium | #309 |
| [Best Time to Buy and Sell Stock with Transaction Fee](./best-time-to-buy-and-sell-stock-with-transaction-fee.md) | Medium | #714 |
| [Best Time to Buy and Sell Stock III](./best-time-to-buy-and-sell-stock-iii.md) | Hard | #123 |
| [Best Time to Buy and Sell Stock IV](./best-time-to-buy-and-sell-stock-iv.md) | Hard | #188 |

## Progress
- Implemented in this section: 24 indexed problems (including foundational and advanced starter set)
- Next expansion target: Tree/Graph DP, Bitmask DP, Digit DP, Probability DP coverage
