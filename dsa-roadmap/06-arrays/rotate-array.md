# Rotate Array

**Difficulty:** Medium
**Pattern:** Array Manipulation / Reversal
**LeetCode:** #189

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. Do it in-place with O(1) extra space.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`
**Output:** `[5, 6, 7, 1, 2, 3, 4]`
**Explanation:** Rotate right by 1: [7,1,2,3,4,5,6]. By 2: [6,7,1,2,3,4,5]. By 3: [5,6,7,1,2,3,4].

### Example 2
**Input:** `nums = [-1, -100, 3, 99]`, `k = 2`
**Output:** `[3, 99, -1, -100]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Hints

> 💡 **Hint 1:** First, handle the case where k ≥ n by taking k = k % n. Rotating by n is the same as not rotating.

> 💡 **Hint 2:** There's an elegant O(1) space solution using three reversals. Think about what happens when you reverse the entire array, then reverse parts of it.

> 💡 **Hint 3:** Reverse the entire array, then reverse the first k elements, then reverse the remaining n-k elements. This achieves the rotation in three O(n) passes with O(1) space.

## Approach 1: Brute Force (Extra Array)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Copy the last k elements to the front using a new array.

```python
def rotate_brute(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    rotated = nums[-k:] + nums[:-k]
    for i in range(n):
        nums[i] = rotated[i]
```

**Downside:** O(n) extra space. The problem requires O(1).

---

## Approach 2: Rotate One Step at a Time

**Time Complexity:** O(n × k)
**Space Complexity:** O(1)

Rotate by 1 step, k times.

```python
def rotate_one_by_one(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    for _ in range(k):
        last = nums[-1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last
```

**Downside:** O(n×k) — for k=n/2 this is O(n²).

---

## Approach 3: Three Reversals — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Reverse the whole array, then reverse the first k elements, then reverse the rest.

### Why It Works

```
Original:  [1, 2, 3, 4, 5, 6, 7], k=3
Expected:  [5, 6, 7, 1, 2, 3, 4]

Step 1 — Reverse all:    [7, 6, 5, 4, 3, 2, 1]
Step 2 — Reverse [0,k):  [5, 6, 7, 4, 3, 2, 1]
Step 3 — Reverse [k,n):  [5, 6, 7, 1, 2, 3, 4] ✓

Intuition: reversing the whole array puts the last k elements at the front
(but reversed). Reversing each half fixes the order within each part.
```

### Visual Trace

```
nums = [1,2,3,4,5,6,7], k=3, n=7

k = 3 % 7 = 3

reverse(0, 6): [7,6,5,4,3,2,1]
reverse(0, 2): [5,6,7,4,3,2,1]
reverse(3, 6): [5,6,7,1,2,3,4] ✓
```

```python
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Extra array | O(n) | O(n) | Simple but not in-place |
| One step at a time | O(n×k) | O(1) | Too slow for large k |
| Three reversals | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- In-place array transformation with O(1) extra space
- Comparing cyclic replacement vs reversal approaches
- Common follow-up after string/array reversal practice

