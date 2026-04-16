# Maximum Subarray

**Difficulty:** Medium
**Pattern:** Kadane's Algorithm / Dynamic Programming
**LeetCode:** #53
**Asked by:** Microsoft, Google, Adobe, Amazon

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum and return its sum. A subarray is a contiguous part of an array.

## Examples

### Example 1
**Input:** `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Output:** `6`
**Explanation:** The subarray `[4, -1, 2, 1]` has the largest sum = 6.

### Example 2
**Input:** `nums = [1]`
**Output:** `1`

### Example 3
**Input:** `nums = [5, 4, -1, 7, 8]`
**Output:** `23`
**Explanation:** The entire array `[5, 4, -1, 7, 8]` has sum 23.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** At each position, you have two choices: extend the current subarray or start a new one from here. When should you start fresh?

> 💡 **Hint 2:** Start a new subarray when the current running sum becomes negative — a negative prefix only hurts any future subarray.

> 💡 **Hint 3:** `current = max(nums[i], current + nums[i])`. Track the global maximum across all positions.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Try every possible subarray, track the maximum sum.

```python
def max_subarray_brute(nums: list[int]) -> int:
    best = float('-inf')
    n = len(nums)
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += nums[j]
            best = max(best, current)
    return best
```

**Why it's slow:** O(n²) — for n=100,000 this is 10 billion operations.

---

## Approach 2: Divide and Conquer (O(n log n))

Split array in half, recursively find max subarray in left half, right half, and crossing the midpoint.

```python
def max_subarray_dc(nums: list[int]) -> int:
    def helper(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_max = helper(left, mid)
        right_max = helper(mid + 1, right)
        # Find max crossing subarray
        cross_left = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += nums[i]
            cross_left = max(cross_left, total)
        cross_right = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += nums[i]
            cross_right = max(cross_right, total)
        return max(left_max, right_max, cross_left + cross_right)
    return helper(0, len(nums) - 1)
```

---

## Approach 3: Kadane's Algorithm — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

At each position, decide: extend the current subarray or start fresh. Start fresh when the running sum goes negative (a negative prefix only hurts).

### Visual Trace

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=0: num=-2, current=max(-2, 0+-2)=-2, best=-2
i=1: num=1,  current=max(1, -2+1)=1,   best=1
i=2: num=-3, current=max(-3, 1-3)=-2,  best=1
i=3: num=4,  current=max(4, -2+4)=4,   best=4
i=4: num=-1, current=max(-1, 4-1)=3,   best=4
i=5: num=2,  current=max(2, 3+2)=5,    best=5
i=6: num=1,  current=max(1, 5+1)=6,    best=6  ← answer
i=7: num=-5, current=max(-5, 6-5)=1,   best=6
i=8: num=4,  current=max(4, 1+4)=5,    best=6
```

```python
def max_subarray(nums: list[int]) -> int:
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Try all subarrays |
| Divide & conquer | O(n log n) | O(log n) | Elegant but not optimal |
| Kadane's | O(n) | O(1) | Best — industry standard |

## Follow-up: Return the Actual Subarray

```python
def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """Returns (max_sum, start_index, end_index)"""
    best_sum = current = nums[0]
    best_start = best_end = 0
    start = 0

    for i in range(1, len(nums)):
        if current + nums[i] < nums[i]:
            current = nums[i]
            start = i          # start fresh here
        else:
            current += nums[i]

        if current > best_sum:
            best_sum = current
            best_start = start
            best_end = i

    return best_sum, best_start, best_end

# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Returns: (6, 3, 6)  → subarray nums[3:7] = [4,-1,2,1]
```

## Follow-up: Maximum Product Subarray — #152 (Microsoft favorite)

```python
def max_product(nums: list[int]) -> int:
    """
    Track both max and min at each position (negatives can flip sign).
    
    nums = [2, 3, -2, 4] → 6 (subarray [2,3])
    nums = [-2, 0, -1]   → 0
    """
    max_prod = min_prod = best = nums[0]
    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        best = max(best, max_prod)
    return best
```

## Typical Interview Use Cases

- Classic Microsoft/Google phone screen question
- Tests understanding of DP vs greedy thinking
- Follow-ups: return indices, handle circular array, maximum product variant
