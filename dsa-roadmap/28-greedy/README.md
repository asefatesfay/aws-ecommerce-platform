# 28. Greedy Algorithms

## Overview
Greedy algorithms make the locally optimal choice at each step, hoping to find a global optimum. They work when the problem has the **greedy choice property** and **optimal substructure**.

## Key Concepts
- **Greedy choice property**: a locally optimal choice leads to a globally optimal solution
- **Optimal substructure**: optimal solution contains optimal solutions to subproblems
- Always ask: "Does making the greedy choice now ever hurt us later?"

## When to Use
- Interval scheduling (sort by end time, pick earliest-ending)
- Jump games (track maximum reachable index)
- Task scheduling (sort by deadline or profit)
- Coin change with standard denominations

## Common Patterns
- Sort by end time → interval greedy
- Sort by ratio → fractional knapsack
- Always pick the minimum/maximum available → heap + greedy
- Two-pass (left-to-right then right-to-left) → candy problem

## Problems
| Problem | Difficulty |
|---------|-----------|
| Assign Cookies | Easy |
| Jump Game | Medium |
| Jump Game II | Medium |
| Gas Station | Medium |
| Task Scheduler | Medium |
| Candy | Hard |
| Minimum Number of Refueling Stops | Hard |
