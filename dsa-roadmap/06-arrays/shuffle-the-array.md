# Shuffle the Array

**Difficulty:** Easy
**Pattern:** Array Manipulation
**LeetCode:** #1470

## Problem Statement

Given an array `nums` consisting of `2n` elements in the form `[x1, x2, ..., xn, y1, y2, ..., yn]`, return the array in the form `[x1, y1, x2, y2, ..., xn, yn]`.

## Examples

### Example 1
**Input:** `nums = [2, 5, 1, 3, 4, 7]`, `n = 3`
**Output:** `[2, 3, 5, 4, 1, 7]`
**Explanation:** x1=2, x2=5, x3=1 and y1=3, y2=4, y3=7. Interleaved: [2,3,5,4,1,7].

### Example 2
**Input:** `nums = [1, 2, 3, 4, 4, 3, 2, 1]`, `n = 4`
**Output:** `[1, 4, 2, 3, 3, 2, 4, 1]`

## Constraints
- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`

## Hints

> 💡 **Hint 1:** The first half of the array contains the x values (indices 0 to n-1) and the second half contains the y values (indices n to 2n-1).

> 💡 **Hint 2:** For position i in the result, you need x[i] = nums[i] and y[i] = nums[n+i]. Build the result by alternating between these two sources.

> 💡 **Hint 3:** Iterate i from 0 to n-1 and for each i, append nums[i] then nums[n+i] to the result array.

## Approach 1: Brute Force (Naive Interleave)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Collect x values and y values separately, then interleave.

```python
def shuffle_brute(nums: list[int], n: int) -> list[int]:
    xs = nums[:n]
    ys = nums[n:]
    result = []
    for x, y in zip(xs, ys):
        result.append(x)
        result.append(y)
    return result
```

This is already O(n) — the "brute force" here is just using extra lists.

---

## Approach 2: Direct Index Mapping — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Map directly from source indices to destination indices without intermediate lists.

### Visual Trace

```
nums = [2, 5, 1, 3, 4, 7], n=3
x values: nums[0..2] = [2, 5, 1]
y values: nums[3..5] = [3, 4, 7]

i=0: out[0]=nums[0]=2, out[1]=nums[3]=3
i=1: out[2]=nums[1]=5, out[3]=nums[4]=4
i=2: out[4]=nums[2]=1, out[5]=nums[5]=7

Result: [2, 3, 5, 4, 1, 7] ✓
```

```python
def shuffle(nums: list[int], n: int) -> list[int]:
    out = [0] * (2 * n)
    for i in range(n):
        out[2 * i] = nums[i]       # x_i at even positions
        out[2 * i + 1] = nums[n + i]  # y_i at odd positions
    return out
```

### One-liner (Pythonic)

```python
def shuffle_pythonic(nums: list[int], n: int) -> list[int]:
    return [val for pair in zip(nums[:n], nums[n:]) for val in pair]
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Separate lists + zip | O(n) | O(n) | Clear but 3 extra arrays |
| Direct index mapping | O(n) | O(n) | Optimal — single output array |

## Typical Interview Use Cases

- Straightforward index-mapping transformation
- Warm-up for interleaving and zipper-merge style tasks
- Testing off-by-one correctness in derived index formulas

