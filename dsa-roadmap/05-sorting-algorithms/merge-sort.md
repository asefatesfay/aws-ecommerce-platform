# Merge Sort

**Type:** Comparison-based, divide and conquer
**Stable:** Yes

## Concept

Recursively split the array in half until you have subarrays of size 1 (trivially sorted), then merge pairs of sorted subarrays back together. The merge step is the key: combining two sorted arrays into one sorted array takes O(n) time.

## How It Works

1. **Divide:** Split array into two halves at the midpoint
2. **Conquer:** Recursively sort each half
3. **Merge:** Combine the two sorted halves using a two-pointer merge

The merge step: maintain two pointers, one for each half. Always pick the smaller of the two current elements and advance that pointer.

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

The recursion tree has log n levels, and each level does O(n) work total → O(n log n) guaranteed.

## When to Use

- When stability is required (preserving relative order of equal elements)
- When guaranteed O(n log n) is needed (Quick Sort has O(n²) worst case)
- Sorting linked lists — Merge Sort is optimal for linked lists (no random access needed)
- External sorting (data too large for memory) — merge sorted chunks from disk

## Key Insight

Merge Sort is the go-to for linked list sorting because it doesn't require random access. For arrays, Quick Sort is often faster in practice due to better cache behavior, but Merge Sort's stability and guaranteed complexity make it preferable in many contexts.

## Variants

- **Bottom-up Merge Sort:** Iterative version — merge pairs of size 1, then size 2, then size 4, etc. Avoids recursion overhead.
- **Timsort:** Python's built-in sort — hybrid of Merge Sort and Insertion Sort. Detects natural runs and merges them efficiently.

## Interview Relevance

Merge Sort appears directly in problems like "Sort List" (LeetCode 148) and "Count of Inversions". The merge step pattern also appears in "Merge k Sorted Lists".
