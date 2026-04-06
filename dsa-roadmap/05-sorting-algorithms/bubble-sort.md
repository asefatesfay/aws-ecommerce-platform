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

### Visual Example

```
Input: [5, 2, 8, 1, 9]

Pass 1 (Find max: 9):
  [5, 2, 8, 1, 9]  → compare 5,2 → swap
  [2, 5, 8, 1, 9]  → compare 5,8 → no swap
  [2, 5, 8, 1, 9]  → compare 8,1 → swap
  [2, 5, 1, 8, 9]  → compare 8,9 → no swap
  [2, 5, 1, 8, 9]  ← 9 in place ✓

Pass 2 (Find 2nd max: 8):
  [2, 5, 1, 8, 9]  → compare 2,5 → no swap
  [2, 5, 1, 8, 9]  → compare 5,1 → swap
  [2, 1, 5, 8, 9]  → compare 5,8 → no swap
  [2, 1, 5, 8, 9]  ← 8 in place ✓

Pass 3 (Find 3rd max: 5):
  [2, 1, 5, 8, 9]  → compare 2,1 → swap
  [1, 2, 5, 8, 9]  → compare 2,5 → no swap
  [1, 2, 5, 8, 9]  ← 5 in place ✓

Pass 4 (Find 4th: 2):
  [1, 2, 5, 8, 9]  → compare 1,2 → no swap
  [1, 2, 5, 8, 9]  ✓ Sorted!
```

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

# Example
result = bubble_sort([5, 2, 8, 1, 9])
# Output: [1, 2, 5, 8, 9]
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
