# Heap Sort

**Type:** Comparison-based, in-place
**Stable:** No

## Concept

Use a max-heap data structure to sort in-place. First, build a max-heap from the array. Then repeatedly extract the maximum (root) and place it at the end of the array, reducing the heap size by 1 each time.

## How It Works

**Phase 1 — Build Max-Heap:**
- Start from the last non-leaf node (index n/2 - 1) and heapify downward
- After this phase, arr[0] is the maximum element

**Phase 2 — Extract and Sort:**
- Swap arr[0] (max) with arr[n-1] (last element)
- Reduce heap size by 1
- Heapify down from root to restore heap property
- Repeat until heap size is 1

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(1) |
| Average | O(n log n) | O(1) |
| Worst | O(n log n) | O(1) |

Building the heap is O(n) (not O(n log n) — this is a non-obvious result). Each of the n extractions takes O(log n) → total O(n log n).

## Python Implementation

```python
def heap_sort(nums):
	arr = nums[:]

	def sift_down(i, heap_size):
		while True:
			largest = i
			left = 2 * i + 1
			right = 2 * i + 2

			if left < heap_size and arr[left] > arr[largest]:
				largest = left
			if right < heap_size and arr[right] > arr[largest]:
				largest = right

			if largest == i:
				break

			arr[i], arr[largest] = arr[largest], arr[i]
			i = largest

	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		sift_down(i, n)

	for end in range(n - 1, 0, -1):
		arr[0], arr[end] = arr[end], arr[0]
		sift_down(0, end)

	return arr
```

## When to Use

- When O(1) extra space is required AND O(n log n) worst-case is required
- Heap Sort is the only comparison sort that achieves both simultaneously
- In practice, Quick Sort and Merge Sort are preferred due to better cache behavior
- The heap data structure itself is more commonly used for priority queues

## Key Insight

Heap Sort's weakness is poor cache performance — heap operations jump around memory non-sequentially, causing many cache misses. This is why it's slower in practice than Quick Sort despite the same asymptotic complexity.

## Heapify Operation

The core operation: given a node whose children are valid heaps, restore the heap property by swapping the node with its largest child and recursing. This is O(log n).

## Interview Relevance

Understanding heaps is critical for priority queue problems (Section 25). Heap Sort itself rarely appears directly in interviews, but the heap data structure is everywhere.

## Typical Interview Use Cases

- Need O(n log n) worst-case with O(1) extra space
- Bridge topic into heap/priority-queue problems
- Useful for discussing trade-offs vs Quick Sort and Merge Sort
