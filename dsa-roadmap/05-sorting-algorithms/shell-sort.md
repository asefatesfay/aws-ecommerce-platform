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

### Visual Example (input: [5, 2, 8, 1, 9])

```
n=5, initial gap = 5 // 2 = 2

Gap=2 (compare indices i and i-2):
  [5, 2, 8, 1, 9]  → compare 5,8 (no swap)
  [5, 2, 8, 1, 9]  → compare 2,1 (swap)
  [5, 1, 8, 2, 9]  ← After gap=2

Gap=1 (standard Insertion Sort on nearly-sorted array):
  [5, 1, 8, 2, 9]  → Shifts with gap=1
  → ... → [1, 2, 5, 8, 9] ✓
```

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

## Python Implementation

```python
def shell_sort(nums):
	arr = nums[:]
	n = len(arr)
	gap = n // 2

	while gap > 0:
		for i in range(gap, n):
			temp = arr[i]
			j = i
			while j >= gap and arr[j - gap] > temp:
				arr[j] = arr[j - gap]
				j -= gap
			arr[j] = temp
		gap //= 2

	return arr

# Example
result = shell_sort([5, 2, 8, 1, 9])
# Output: [1, 2, 5, 8, 9]
```

## When to Use

- When you need better than O(n²) but can't use O(n) extra space
- Embedded systems where memory is extremely limited
- Moderate-sized arrays where Merge Sort's O(n) space is a concern
- Rarely used in modern software — mostly of historical/academic interest

## Key Insight

Shell Sort's efficiency comes from the fact that Insertion Sort is fast on nearly-sorted data. By pre-sorting with large gaps, each subsequent pass has fewer inversions to fix.

## Typical Interview Use Cases

- Rare in mainstream interviews, but useful for discussing gap-based optimization
- Demonstrating how algorithm performance can depend on tuning parameters
- Good contrast against Insertion Sort and O(n log n) algorithms
