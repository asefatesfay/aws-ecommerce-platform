# Prefix Sum

The prefix sum technique precomputes cumulative sums so that any range sum query can be answered in O(1). It's a simple but powerful preprocessing step.

## Core Idea

Given array `arr`, build `prefix[i] = arr[0] + arr[1] + ... + arr[i]`.

Then: `sum(arr[l..r]) = prefix[r] - prefix[l-1]`

This turns O(n) range sum queries into O(1) after O(n) preprocessing.

## Variants

### 1D Prefix Sum
Standard: `prefix[i] = prefix[i-1] + arr[i]`

### 2D Prefix Sum
`prefix[i][j]` = sum of all elements in the rectangle from (0,0) to (i,j).
Query: `sum(r1,c1,r2,c2) = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]`

### Prefix Sum + HashMap
For "subarray sum equals k": use a HashMap to store prefix sums seen so far. For each prefix sum `p`, check if `p - k` exists in the map.

## When to Recognize Prefix Sum

- "Sum of subarray" or "range sum query"
- "Number of subarrays with sum equal to k"
- "Subarray sum divisible by k" (use modulo)
- "Contiguous array with equal 0s and 1s" (convert 0→-1, find subarray sum = 0)

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Range Sum Query - Immutable](./range-sum-query-immutable.md) | Easy |
| [Running Sum of 1d Array](./running-sum-of-1d-array.md) | Easy |
| [Find Pivot Index](./find-pivot-index.md) | Easy |
| [Maximum Population Year](./maximum-population-year.md) | Easy |
| [Subarray Sum Equals K](./subarray-sum-equals-k.md) | Medium |
| [Subarray Sums Divisible by K](./subarray-sums-divisible-by-k.md) | Medium |
| [Continuous Subarray Sum](./continuous-subarray-sum.md) | Medium |
| [Contiguous Array](./contiguous-array.md) | Medium |
| [Range Addition](./range-addition.md) | Medium |
| [Range Sum Query 2D - Immutable](./range-sum-query-2d-immutable.md) | Medium |
| [Increment Submatrices by One](./increment-submatrices-by-one.md) | Medium |
| [Matrix Block Sum](./matrix-block-sum.md) | Medium |
