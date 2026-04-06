# Binary Search

Binary search finds a target in a sorted array in O(log n) by repeatedly halving the search space. The key is correctly defining the invariant and handling boundaries.

## Core Template

```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2  # avoid overflow
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

## Binary Search on Answer

Many problems ask for the minimum/maximum value satisfying a condition. If the condition is monotonic (once true, always true), binary search on the answer space.

Pattern: "Find the minimum X such that condition(X) is true"
```python
left, right = min_possible, max_possible
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left
```

## Common Pitfalls

- Off-by-one errors in boundary conditions
- Infinite loops when mid doesn't change (use `left = mid + 1` or `right = mid - 1`)
- Integer overflow: use `left + (right - left) // 2`

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Binary Search](./binary-search.md) | Easy |
| [First Bad Version](./first-bad-version.md) | Easy |
| [Valid Perfect Square](./valid-perfect-square.md) | Easy |
| [Search Insert Position](./search-insert-position.md) | Easy |
| [Guess Number Higher or Lower](./guess-number-higher-or-lower.md) | Easy |
| [Find Smallest Letter Greater Than Target](./find-smallest-letter-greater-than-target.md) | Easy |
| [Find First and Last Position of Element in Sorted Array](./find-first-and-last-position-of-element-in-sorted-array.md) | Medium |
| [Search in Rotated Sorted Array](./search-in-rotated-sorted-array.md) | Medium |
| [Search in Rotated Sorted Array II](./search-in-rotated-sorted-array-ii.md) | Medium |
| [Find Minimum in Rotated Sorted Array](./find-minimum-in-rotated-sorted-array.md) | Medium |
| [Find Peak Element](./find-peak-element.md) | Medium |
| [Find in Mountain Array](./find-in-mountain-array.md) | Hard |
| [Koko Eating Bananas](./koko-eating-bananas.md) | Medium |
| [Capacity To Ship Packages Within D Days](./capacity-to-ship-packages-within-d-days.md) | Medium |
| [Minimum Number of Days to Make m Bouquets](./minimum-number-of-days-to-make-m-bouquets.md) | Medium |
| [Magnetic Force Between Two Balls](./magnetic-force-between-two-balls.md) | Medium |
| [Split Array Largest Sum](./split-array-largest-sum.md) | Hard |
| [Search a 2D Matrix](./search-a-2d-matrix.md) | Medium |
| [Search a 2D Matrix II](./search-a-2d-matrix-ii.md) | Medium |
| [Random Pick with Weight](./random-pick-with-weight.md) | Medium |
| [Find K Closest Elements](./find-k-closest-elements.md) | Medium |
| [Heaters](./heaters.md) | Medium |
| [Median of Two Sorted Arrays](./median-of-two-sorted-arrays.md) | Hard |
| [Find K-th Smallest Pair Distance](./find-k-th-smallest-pair-distance.md) | Hard |
