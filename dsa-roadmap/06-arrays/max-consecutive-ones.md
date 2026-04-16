# Max Consecutive Ones

**Difficulty:** Easy
**Pattern:** Array / Counting
**LeetCode:** #485

## Problem Statement

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

## Examples

### Example 1
**Input:** `nums = [1, 1, 0, 1, 1, 1]`
**Output:** `3`
**Explanation:** The last three elements are all 1s, giving a run of 3.

### Example 2
**Input:** `nums = [1, 0, 1, 1, 0, 1]`
**Output:** `2`

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

## Hints

> 💡 **Hint 1:** Scan through the array, keeping a running count of the current streak of 1s.

> 💡 **Hint 2:** When you see a 1, increment the current count. When you see a 0, reset the current count to 0.

> 💡 **Hint 3:** At each step, update a global maximum with the current count. Return the maximum at the end.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

For each position, scan forward to count the current run.

```python
def find_max_consecutive_ones_brute(nums: list[int]) -> int:
    best = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            count = 0
            for j in range(i, n):
                if nums[j] == 1:
                    count += 1
                else:
                    break
            best = max(best, count)
    return best
```

---

## Approach 2: Single Pass — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track the current run length. Reset to 0 on a 0, update the global max at each step.

### Visual Trace

```
nums = [1, 1, 0, 1, 1, 1]

x=1: cur=1, best=1
x=1: cur=2, best=2
x=0: cur=0
x=1: cur=1, best=2
x=1: cur=2, best=2
x=1: cur=3, best=3

Answer: 3 ✓
```

```python
def find_max_consecutive_ones(nums: list[int]) -> int:
    best = cur = 0
    for x in nums:
        if x == 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best
```

### Follow-up: Max Consecutive Ones III — #1004 (Google)

Allow flipping at most k zeros. Find the longest subarray of 1s.

```python
def longest_ones(nums: list[int], k: int) -> int:
    """
    Sliding window: expand right, shrink left when zeros > k.
    nums=[1,1,1,0,0,0,1,1,1,1,0], k=2 → 6
    """
    left = zeros = best = 0
    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Restart from each 1 |
| Single pass | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Run-length counting on binary arrays
- Base form of sliding-window style streak tracking
- Extends naturally to "max consecutive ones with at most k flips"

