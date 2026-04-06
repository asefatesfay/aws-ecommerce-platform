# Selection Sort

**Type:** Comparison-based, in-place
**Stable:** No (standard implementation)

## Concept

Divide the array into a sorted portion (left) and unsorted portion (right). On each pass, find the minimum element in the unsorted portion and swap it into the next position of the sorted portion.

## How It Works

- Pass 1: find minimum in entire array, swap with index 0
- Pass 2: find minimum in indices 1..n-1, swap with index 1
- Pass k: find minimum in indices k..n-1, swap with index k
- After n-1 passes, array is sorted

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n²) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

Note: Unlike Bubble Sort, there's no early-exit optimization — it always does O(n²) comparisons.

## Python Implementation

```python
def selection_sort(nums):
	arr = nums[:]
	n = len(arr)

	for i in range(n - 1):
		min_idx = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		if min_idx != i:
			arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr
```

## When to Use

- When the cost of swapping is high (e.g., large objects) — Selection Sort does at most n-1 swaps, the minimum possible for a comparison sort
- Small arrays
- Memory-constrained environments (O(1) space)

## Key Property: Minimum Swaps

Selection Sort performs at most n-1 swaps. This makes it useful when write operations are expensive (e.g., writing to flash memory).

## Why It's Not Stable

When swapping the minimum element into position, it may jump over equal elements, breaking their relative order. A stable variant exists but requires shifting instead of swapping, which increases write operations.

## Comparison with Bubble Sort

Both are O(n²), but Selection Sort does far fewer swaps (O(n) vs O(n²)). However, Bubble Sort can exit early on sorted input; Selection Sort cannot.

## Typical Interview Use Cases

- Explain trade-off between comparisons and writes
- Situations where minimizing swaps is important
- Mostly conceptual; usually replaced by better O(n log n) solutions
