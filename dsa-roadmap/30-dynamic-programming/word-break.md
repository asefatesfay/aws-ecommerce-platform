# Word Break

**Difficulty:** Medium
**Pattern:** 1D DP / BFS
**LeetCode:** #139

## Problem Statement
Given string `s` and dictionary `wordDict`, return `true` if `s` can be segmented into valid dictionary words.
Words may be reused.

## Input/Output Examples
1. Input: `s = "leetcode", wordDict = ["leet","code"]` -> Output: `true`
2. Input: `s = "applepenapple", wordDict = ["apple","pen"]` -> Output: `true`
3. Input: `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]` -> Output: `false`

## Why This Is DP (overlapping + optimal substructure)
- Overlapping: suffix starting at index `i` is tested repeatedly.
- Optimal substructure: `dp[i]` is true if any split `j` has `dp[j]` true and `s[j:i]` in dictionary.

## Mermaid Visual
```mermaid
flowchart LR
    A[index i] --> B[index j]
    B --> C[s[j:i] in dict]
    C --> D[dp[i] = true]
```

## Brute Force (Python)
```python
def word_break_bruteforce(s, word_dict):
    words = set(word_dict)
    def dfs(i):
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in words and dfs(j):
                return True
        return False

    return dfs(0)
```

## Optimal DP (Python)
```python
def word_break_dp(s, word_dict):
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]
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
- Brute force recursion: `O(2^n)` split exploration in the worst case, `O(n)` stack.
- Optimal DP: `O(n^2)` time, `O(n)` space.
