# Bubble Sort

**Type:** Comparison-based, in-place
**Stable:** Yes

## Concept

Repeatedly step through the list, compare adjacent elements, and swap them if they're in the wrong order. After each full pass, the largest unsorted element "bubbles up" to its correct position at the end.

## How It Works

- Pass 1: compare index 0&1, 1&2, 2&3, ... — largest element reaches the end
- Pass 2: same, but stop one earlier — second largest is now in place
- Repeat n-1 times total

**Optimization:** If no swaps occur during a pass, the array is already sorted — exit early. This gives O(n) best case on already-sorted input.

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best (sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

## Python Implementation

```python
def bubble_sort(nums):
	arr = nums[:]  # keep input unchanged
	n = len(arr)

	for i in range(n - 1):
		swapped = False
		for j in range(0, n - 1 - i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break

	return arr
```

## When to Use

- Teaching/learning purposes
- Very small arrays (n < 10)
- Nearly sorted data with the early-exit optimization
- Never in production for large datasets

## Key Insight

After k passes, the last k elements are guaranteed to be in their final sorted positions. You can reduce the inner loop bound by k each pass.

## Comparison with Insertion Sort

Both are O(n²) average, but Insertion Sort is generally faster in practice because it does fewer comparisons and writes. Bubble Sort's main advantage is its simplicity and the easy early-exit optimization.

## Typical Interview Use Cases

- Rarely used as the final optimal solution
- Useful as a warm-up to explain stability and in-place sorting
- Occasionally accepted for very small input constraints
