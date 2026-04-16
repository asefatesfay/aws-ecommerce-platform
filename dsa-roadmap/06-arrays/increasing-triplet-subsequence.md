# Increasing Triplet Subsequence

**Difficulty:** Medium
**Pattern:** Greedy / Tracking Minimums
**LeetCode:** #334

## Problem Statement

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

Follow-up: Can you implement a solution that runs in O(n) time and O(1) space?

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4, 5]`
**Output:** `true`
**Explanation:** Any triplet like (0,1,2) works.

### Example 2
**Input:** `nums = [5, 4, 3, 2, 1]`
**Output:** `false`
**Explanation:** No increasing triplet exists.

### Example 3
**Input:** `nums = [2, 1, 5, 0, 4, 6]`
**Output:** `true`
**Explanation:** (1, 4, 5) → values (1, 4, 6).

## Constraints
- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** You need to find three numbers in increasing order. Think about maintaining the smallest and second-smallest values seen so far.

> 💡 **Hint 2:** Keep two variables: `first` (smallest value seen) and `second` (smallest value seen that is greater than some previous `first`). If you find a number greater than `second`, you've found your triplet.

> 💡 **Hint 3:** Update greedily: if current ≤ first, update first. Else if current ≤ second, update second. Else return true. The key insight: even if `first` gets updated after `second` was set, `second` still "remembers" that a valid smaller value existed before it.

## Approach 1: Brute Force (O(n³))

**Time Complexity:** O(n³)
**Space Complexity:** O(1)

Check every triple of indices.

```python
def increasing_triplet_brute(nums: list[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False
```

---

## Approach 2: DP / Patience Sort (O(n²))

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

For each element, find the longest increasing subsequence ending there. Return True if any length ≥ 3.

```python
def increasing_triplet_dp(nums: list[int]) -> bool:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] >= 3:
            return True
    return False
```

---

## Approach 3: Greedy (Two Minimums) — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track `first` (smallest seen) and `second` (smallest value that has a smaller value before it). If any element exceeds both, a triplet exists.

### The Tricky Part

```
nums = [5, 1, 4, 0, 6]

first=5, second=∞
x=1: 1<5 → first=1
x=4: 4>first=1, 4<second=∞ → second=4
x=0: 0<first=1 → first=0  ← first updated AFTER second was set!
x=6: 6>second=4 → True ✓

Even though first=0 now comes AFTER second=4 in the array,
second=4 still "remembers" that a value < 4 existed before it (the old first=1).
The invariant holds: there exists some index before second's index where value < second.
```

### Visual Trace

```
nums = [2, 1, 5, 0, 4, 6]

first=∞, second=∞
x=2: 2<∞ → first=2
x=1: 1<2 → first=1
x=5: 5>first=1, 5>second=∞? No, 5<∞ → second=5
x=0: 0<first=1 → first=0
x=4: 4>first=0, 4<second=5 → second=4
x=6: 6>second=4 → True ✓  (triplet: 1 < 4 < 6)
```

```python
def increasing_triplet(nums: list[int]) -> bool:
    first = second = float('inf')
    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            return True
    return False
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n³) | O(1) | Try all triples |
| DP | O(n²) | O(n) | LIS-based |
| Greedy (two mins) | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Existence checks for increasing subsequences of fixed length
- Greedy state compression from O(n^2) DP intuition to O(1)
- Precursor to LIS reasoning and patience sorting discussions

