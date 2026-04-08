# Fibonacci Number

**Difficulty:** Easy
**Pattern:** 1D DP / Fibonacci
**LeetCode:** #509

## Problem Statement
Fibonacci is defined by:
- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n-1) + F(n-2)` for `n > 1`
Return `F(n)`.

## Input/Output Examples
1. Input: `n = 2` -> Output: `1`
2. Input: `n = 3` -> Output: `2`
3. Input: `n = 4` -> Output: `3`

## Why This Is DP (overlapping + optimal substructure)
- Overlapping: recursive calls compute `F(k)` many times.
- Optimal substructure: `F(n)` is composed directly from `F(n-1)` and `F(n-2)`.

## Mermaid Visual
```mermaid
flowchart TD
    Fn[F(n)] --> Fn1[F(n-1)]
    Fn --> Fn2[F(n-2)]
```

## Brute Force (Python)
```python
def fib_bruteforce(n):
    if n < 2:
        return n
    return fib_bruteforce(n - 1) + fib_bruteforce(n - 2)
```

## Optimal DP (Python)
```python
def fib_dp(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
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

## Common Pitfalls
- Incorrect base handling for `n = 0` and `n = 1`.
- Off-by-one loop range when filling states.
- Accidentally swapping update order for rolling variables.

## Complexity (brute force + optimal)
- Brute force recursion: `O(2^n)` time, `O(n)` stack.
- Optimal DP: `O(n)` time, `O(1)` space.
