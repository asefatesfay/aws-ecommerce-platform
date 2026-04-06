# Sorting

This section covers problems where sorting is the key insight, or where understanding sorting algorithms (like quickselect) is essential.

## Key Techniques

- **Quickselect:** Find the kth largest/smallest in O(n) average time using the partition step from quicksort.
- **Custom comparator:** Sort by a derived key (e.g., sort by frequency, sort by string length).
- **Counting sort / Radix sort:** For integer keys in a bounded range.
- **Sort + scan:** Many problems become trivial after sorting.

## When Sorting Helps

- "Top K" problems → sort or use a heap
- "Kth largest/smallest" → quickselect or heap
- "Group by frequency" → sort by frequency
- "Maximum gap" → sort then scan adjacent pairs

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Sort Characters By Frequency](./sort-characters-by-frequency.md) | Medium |
| [Top K Frequent Words](./top-k-frequent-words.md) | Medium |
| [Maximum Gap](./maximum-gap.md) | Medium |
| [Contains Duplicate III](./contains-duplicate-iii.md) | Hard |
| [Sort an Array](./sort-an-array.md) | Medium |
| [Sort List](./sort-list.md) | Medium |
| [Reverse Pairs](./reverse-pairs.md) | Hard |
| [Count of Range Sum](./count-of-range-sum.md) | Hard |
| [Sort Colors](./sort-colors.md) | Medium |
| [Kth Largest Element in an Array](./kth-largest-element-in-an-array.md) | Medium |
| [Find the Kth Largest Integer in the Array](./find-the-kth-largest-integer-in-the-array.md) | Medium |
