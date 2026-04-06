# Quick Sort

**Type:** Comparison-based, divide and conquer, in-place
**Stable:** No (standard implementation)

## Concept

Choose a pivot element, partition the array so all elements less than the pivot are on its left and all greater are on its right, then recursively sort each side. The pivot ends up in its final sorted position after partitioning.

## How It Works

1. **Choose pivot:** Common strategies: last element, first element, random, median-of-three
2. **Partition:** Rearrange so elements < pivot are left, elements > pivot are right, pivot is in final position
3. **Recurse:** Sort left subarray and right subarray independently

**Lomuto partition scheme:** Use a pointer `i` for the boundary of elements ≤ pivot. Scan with pointer `j`; when arr[j] ≤ pivot, swap arr[i+1] and arr[j], advance i.

**Hoare partition scheme:** Two pointers from both ends moving toward each other. Slightly more efficient but trickier to implement.

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst (sorted input, bad pivot) | O(n²) | O(n) |

## Python Implementation

```python
def quick_sort(nums):
	arr = nums[:]

	def partition(lo, hi):
		pivot = arr[hi]
		i = lo
		for j in range(lo, hi):
			if arr[j] <= pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[hi] = arr[hi], arr[i]
		return i

	def sort(lo, hi):
		if lo >= hi:
			return
		p = partition(lo, hi)
		sort(lo, p - 1)
		sort(p + 1, hi)

	sort(0, len(arr) - 1)
	return arr
```

## Avoiding Worst Case

- **Random pivot:** Shuffle input or pick random pivot → O(n log n) expected with high probability
- **Median-of-three:** Pick median of first, middle, last elements as pivot
- **3-way partition (Dutch National Flag):** Handle duplicates efficiently — partition into < pivot, = pivot, > pivot

## When to Use

- General-purpose sorting when average performance matters more than worst-case guarantee
- In-place sorting with O(log n) stack space
- When cache performance matters (better locality than Merge Sort)
- Not suitable when stability is required

## Key Insight

Quick Sort's average performance is excellent because the partition step is cache-friendly and the constant factors are small. In practice, it often outperforms Merge Sort on arrays despite the same asymptotic complexity.

## Interview Relevance

The partition logic appears in "Kth Largest Element in an Array" (QuickSelect — same idea, only recurse into one side). Understanding Quick Sort deeply helps with many selection problems.

## Typical Interview Use Cases

- In-place average-case fast sorting
- Partition-based problems (QuickSelect, Dutch National Flag variants)
- Comparing expected vs worst-case behavior and pivot strategy choices
