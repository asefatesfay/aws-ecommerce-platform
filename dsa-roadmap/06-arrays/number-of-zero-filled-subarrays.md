# Number of Zero-Filled Subarrays

**Difficulty:** Medium
**Pattern:** Array / Counting
**LeetCode:** #2348

## Problem Statement

Given an integer array `nums`, return the number of subarrays filled with `0`. A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1
**Input:** `nums = [1, 3, 0, 0, 2, 0, 0, 4]`
**Output:** `6`
**Explanation:** There are 4 zero-filled subarrays of length 1: [0],[0],[0],[0]. Two of length 2: [0,0],[0,0]. Total = 6.

### Example 2
**Input:** `nums = [0, 0, 0, 2, 0, 0]`
**Output:** `9`
**Explanation:** [0],[0],[0],[0,0],[0,0],[0,0,0],[0],[0],[0,0] — 9 subarrays.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Focus on runs of consecutive zeros. Each run of zeros contributes multiple subarrays.

> 💡 **Hint 2:** For a run of k consecutive zeros, how many zero-filled subarrays does it contain? Think about subarrays of length 1, 2, ..., k.

> 💡 **Hint 3:** A run of k zeros contains k*(k+1)/2 zero-filled subarrays. Equivalently, as you extend a run, each new zero adds (current run length) new subarrays. Sum these contributions across all runs.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Check every subarray, count those filled with zeros.

```python
def zero_filled_subarray_brute(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            for j in range(i, n):
                if nums[j] == 0:
                    count += 1
                else:
                    break
    return count
```

---

## Approach 2: Run-Length Counting — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

For a run of k consecutive zeros, it contributes `k*(k+1)/2` subarrays. Equivalently, each new zero in a run adds exactly `run_length` new subarrays (all subarrays ending at the current position).

### Why Each New Zero Adds `run_length` Subarrays

```
Run of zeros at positions [i, i+1, i+2]:
  After position i:   1 new subarray  → [i]
  After position i+1: 2 new subarrays → [i+1], [i,i+1]
  After position i+2: 3 new subarrays → [i+2], [i+1,i+2], [i,i+1,i+2]

Each new zero creates exactly `run_length` new subarrays ending at it.
Total = 1+2+3 = 6 = 3*(3+1)/2 ✓
```

### Visual Trace

```
nums = [1, 3, 0, 0, 2, 0, 0, 4]

x=1: run=0
x=3: run=0
x=0: run=1, total+=1=1
x=0: run=2, total+=2=3
x=2: run=0
x=0: run=1, total+=1=4
x=0: run=2, total+=2=6
x=4: run=0

Answer: 6 ✓
```

```python
def zero_filled_subarray(nums: list[int]) -> int:
    run = 0
    total = 0
    for x in nums:
        if x == 0:
            run += 1
            total += run
        else:
            run = 0
    return total
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Check all subarrays |
| Run-length counting | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Counting subarrays by run-length contribution
- Applying k*(k+1)/2 logic without explicit segmentation pass
- Common pattern for streak-based combinatorial counting

