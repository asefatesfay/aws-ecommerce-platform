# Insertion Sort

**Type:** Comparison-based, in-place
**Stable:** Yes

## Concept

Build the sorted array one element at a time. For each new element, find its correct position in the already-sorted left portion by shifting larger elements right, then insert it.

Think of sorting a hand of playing cards: you pick up one card at a time and insert it into the right position among the cards you're already holding.

## How It Works

- Start with index 1 (index 0 is trivially sorted)
- For each element at index i, store it as `key`
- Shift all elements in the sorted portion that are greater than `key` one position to the right
- Insert `key` into the gap

### Visual Example

```
Input: [5, 2, 8, 1, 9]

Pass 1: key=2 (at index 1)
  Sorted: [5], Insert 2
  [5, 2, 8, 1, 9]  → Shift 5 right
  [_, 5, 8, 1, 9]  → Insert 2 at 0
  [2, 5, 8, 1, 9]  ✓

Pass 2: key=8 (at index 2)
  Sorted: [2, 5], Insert 8
  [2, 5, 8, 1, 9]  → 8 > 5, no shift needed
  [2, 5, 8, 1, 9]  ✓

Pass 3: key=1 (at index 3)
  Sorted: [2, 5, 8], Insert 1
  [2, 5, 8, 1, 9]  → Shift 8 right
  [2, 5, _, 8, 9]  → Shift 5 right
  [2, _, 5, 8, 9]  → Shift 2 right
  [_, 2, 5, 8, 9]  → Insert 1 at 0
  [1, 2, 5, 8, 9]  ✓

Pass 4: key=9 (at index 4)
  Sorted: [1, 2, 5, 8], Insert 9
  [1, 2, 5, 8, 9]  → 9 > 8, no shift needed
  [1, 2, 5, 8, 9]  ✓
```

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best (sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

## Python Implementation

```python
def insertion_sort(nums):
	arr = nums[:]

	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key

	return arr

# Example
result = insertion_sort([5, 2, 8, 1, 9])
# Output: [1, 2, 5, 8, 9]
```

## When to Use

- Small arrays (n < 20) — very low constant factor, cache-friendly
- Nearly sorted data — approaches O(n) performance
- Online sorting — can sort a stream of data as it arrives
- As the base case in hybrid sorts (Timsort uses Insertion Sort for small runs)

## Key Insight

The number of operations is proportional to the number of inversions in the array. An inversion is a pair (i, j) where i < j but arr[i] > arr[j]. A sorted array has 0 inversions; a reverse-sorted array has n(n-1)/2 inversions.

## Why It's Preferred Over Bubble/Selection for Small n

- Fewer comparisons on average than Bubble Sort
- Fewer writes than Bubble Sort
- Adaptive: naturally fast on nearly-sorted input
- Used internally by Python's Timsort and Java's Arrays.sort for small subarrays

## Typical Interview Use Cases

- Nearly sorted arrays where O(n) best case is valuable
- Small partitions inside hybrid algorithms
- Online insertion into a sorted list (conceptual usage)
