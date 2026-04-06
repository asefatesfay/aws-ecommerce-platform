# Kadane's Algorithm

Kadane's Algorithm finds the maximum sum subarray in O(n) time. It's a classic dynamic programming technique where the key insight is: the maximum subarray ending at position i is either the element itself, or the element plus the maximum subarray ending at i-1.

## Core Algorithm

```
max_ending_here = nums[0]
max_so_far = nums[0]

for i in range(1, n):
    max_ending_here = max(nums[i], max_ending_here + nums[i])
    max_so_far = max(max_so_far, max_ending_here)

return max_so_far
```

## Key Insight

At each position, you decide: start a new subarray here, or extend the previous one. If the previous subarray sum is negative, it's better to start fresh.

## Variants

- **Maximum subarray sum:** Classic Kadane's
- **Maximum product subarray:** Track both max and min (negative × negative = positive)
- **Circular array:** Max of (standard Kadane's) and (total sum - minimum subarray sum)
- **With one deletion:** DP with states for "no deletion used" and "deletion used"

## When to Recognize Kadane's

- "Maximum/minimum sum subarray"
- "Maximum product subarray"
- "Best time to buy/sell" (single transaction)
- Any problem asking for optimal contiguous subarray

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Maximum Subarray](./maximum-subarray.md) | Medium |
| [Best Sightseeing Pair](./best-sightseeing-pair.md) | Medium |
| [Maximum Sum Circular Subarray](./maximum-sum-circular-subarray.md) | Medium |
| [Maximum Product Subarray](./maximum-product-subarray.md) | Medium |
| [Longest Turbulent Subarray](./longest-turbulent-subarray.md) | Medium |
| [Maximum Subarray Sum with One Deletion](./maximum-subarray-sum-with-one-deletion.md) | Medium |
| [Maximum Absolute Sum of Any Subarray](./maximum-absolute-sum-of-any-subarray.md) | Medium |
