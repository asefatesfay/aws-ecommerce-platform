# Arrays

Arrays are the most fundamental data structure. Most DSA problems involve arrays in some form. Mastering array manipulation patterns is the foundation for everything else.

## Key Concepts

- **In-place modification:** Modify the array without extra space. Common tricks: two-pointer (read/write pointers), swapping, overwriting.
- **Index as identity:** The index itself carries information (e.g., mark visited elements by negating, use index to count occurrences).
- **Sorted array properties:** Duplicates are adjacent, binary search is possible, two pointers work from both ends.
- **Prefix/suffix:** Precompute running values to answer range queries in O(1).

## When to Recognize Array Patterns

- "In-place" → two-pointer or index tricks
- "Sorted array" → binary search or two pointers
- "Subarray" → sliding window or prefix sum
- "Missing/duplicate" → index-as-identity or XOR
- "Majority element" → Boyer-Moore voting

## Common Techniques

### Two-Pointer (Read/Write)
Use a slow pointer (write position) and fast pointer (read position). Write pointer only advances when a valid element is found.

### Cyclic Sort
For arrays containing values 1..n, each value belongs at index value-1. Swap elements to their correct positions in O(n).

### Boyer-Moore Voting
Find majority element in O(n) time, O(1) space. Maintain a candidate and count; increment on match, decrement on mismatch; reset when count hits 0.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Move Zeroes](./move-zeroes.md) | Easy |
| [Remove Element](./remove-element.md) | Easy |
| [Shuffle the Array](./shuffle-the-array.md) | Easy |
| [Remove Duplicates from Sorted Array](./remove-duplicates-from-sorted-array.md) | Easy |
| [Remove Duplicates from Sorted Array II](./remove-duplicates-from-sorted-array-ii.md) | Medium |
| [Rotate Array](./rotate-array.md) | Medium |
| [Max Consecutive Ones](./max-consecutive-ones.md) | Easy |
| [Third Maximum Number](./third-maximum-number.md) | Easy |
| [Missing Ranges](./missing-ranges.md) | Easy |
| [Majority Element](./majority-element.md) | Easy |
| [Majority Element II](./majority-element-ii.md) | Medium |
| [Best Time to Buy and Sell Stock](./best-time-to-buy-and-sell-stock.md) | Easy |
| [Best Time to Buy and Sell Stock II](./best-time-to-buy-and-sell-stock-ii.md) | Medium |
| [Number of Zero-Filled Subarrays](./number-of-zero-filled-subarrays.md) | Medium |
| [Increasing Triplet Subsequence](./increasing-triplet-subsequence.md) | Medium |
| [Product of Array Except Self](./product-of-array-except-self.md) | Medium |
| [Next Permutation](./next-permutation.md) | Medium |
| [First Missing Positive](./first-missing-positive.md) | Hard |
