# Two Pointers

The two-pointer technique uses two indices to traverse a data structure, often reducing O(n²) brute force to O(n). It's one of the most versatile patterns in DSA.

## Variants

### Opposite Ends (Converging)
Start one pointer at the left, one at the right. Move them toward each other based on a condition. Used for: sorted array pair sums, palindrome checks, container problems.

### Same Direction (Slow/Fast)
Both pointers start at the left but move at different speeds. Used for: removing duplicates, cycle detection, finding the middle of a list.

### Sliding Window (Fixed Gap)
Two pointers maintain a window of fixed or variable size. Covered in Section 12.

## When to Recognize Two Pointers

- Sorted array + find pair/triplet with target sum
- "In-place" modification of array
- Palindrome or symmetry check
- Merging two sorted arrays/lists
- Removing elements while preserving order

## Key Insight

For sorted arrays, if the sum of two elements is too large, move the right pointer left. If too small, move the left pointer right. This eliminates one element per step → O(n).

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Squares of a Sorted Array](./squares-of-a-sorted-array.md) | Easy |
| [Merge Strings Alternately](./merge-strings-alternately.md) | Easy |
| [Valid Word Abbreviation](./valid-word-abbreviation.md) | Easy |
| [Two Sum II](./two-sum-ii.md) | Medium |
| [Container With Most Water](./container-with-most-water.md) | Medium |
| [3Sum](./3sum.md) | Medium |
| [4Sum](./4sum.md) | Medium |
| [Trapping Rain Water](./trapping-rain-water.md) | Hard |
| [Count Subarrays With Fixed Bounds](./count-subarrays-with-fixed-bounds.md) | Hard |
| [Merge Sorted Array](./merge-sorted-array.md) | Easy |
| [Backspace String Compare](./backspace-string-compare.md) | Easy |
| [Count Binary Substrings](./count-binary-substrings.md) | Easy |
| [String Compression](./string-compression.md) | Medium |
| [Boats to Save People](./boats-to-save-people.md) | Medium |
| [Longest Palindromic Substring](./longest-palindromic-substring.md) | Medium |
