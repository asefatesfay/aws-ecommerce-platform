# Shell Sort

**Type:** Comparison-based, in-place
**Stable:** No

## Concept

Shell Sort is a generalization of Insertion Sort. Instead of comparing adjacent elements, it compares elements that are far apart (separated by a "gap"), then progressively reduces the gap until it reaches 1 (at which point it's a standard Insertion Sort on a nearly-sorted array).

The key insight: moving elements large distances in early passes makes the final Insertion Sort pass very fast.

## How It Works

1. Choose a gap sequence (e.g., n/2, n/4, ..., 1)
2. For each gap size, perform a gapped Insertion Sort
3. Elements gap positions apart are compared and swapped if out of order
4. Reduce the gap and repeat
5. Final pass with gap=1 is a standard Insertion Sort on a nearly-sorted array

## Gap Sequences

The choice of gap sequence significantly affects performance:

| Sequence | Worst Case |
|----------|-----------|
| Shell's original (n/2, n/4, ..., 1) | O(n²) |
| Hibbard (1, 3, 7, 15, ..., 2^k-1) | O(n^1.5) |
| Sedgewick | O(n^4/3) |
| Ciura (1,4,10,23,57,132,301,701) | Best known empirically |

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(1) |
| Average | Depends on gap sequence | O(1) |
| Worst | O(n²) to O(n^1.5) | O(1) |

## When to Use

- When you need better than O(n²) but can't use O(n) extra space
- Embedded systems where memory is extremely limited
- Moderate-sized arrays where Merge Sort's O(n) space is a concern
- Rarely used in modern software — mostly of historical/academic interest

## Key Insight

Shell Sort's efficiency comes from the fact that Insertion Sort is fast on nearly-sorted data. By pre-sorting with large gaps, each subsequent pass has fewer inversions to fix.
