# Min Heap / Max Heap

## What is it?
A **complete binary tree** where every parent is smaller than its children (min-heap) or larger (max-heap). The root always holds the minimum (or maximum) element, giving O(1) access to the extreme value.

## Visual Example
```
Min-Heap for [3, 1, 6, 5, 2, 4]:

        1          ← root (minimum)
       / \
      2   4
     / \ /
    5  3 6

Array representation: [1, 2, 4, 5, 3, 6]
Parent of i: (i-1)//2
Left child: 2i+1
Right child: 2i+2

After push(0):
        0          ← new minimum bubbles up
       / \
      2   1
     / \ / \
    5  3 6  4
```

## Key Operations
| Operation | Time | Description |
|-----------|------|-------------|
| push(val) | O(log N) | Add element, sift up |
| pop() | O(log N) | Remove root, sift down |
| peek() | O(1) | View min/max |
| heapify(arr) | O(N) | Build from array |

## Implementation

```python
import heapq

# Python's heapq is a MIN-heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print(heapq.heappop(heap))  # 1 (minimum)
print(heap[0])               # 3 (peek at minimum)

# MAX-heap: negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))  # 5 (maximum)

# Heap with tuples (priority, value)
task_queue = []
heapq.heappush(task_queue, (3, "low priority task"))
heapq.heappush(task_queue, (1, "urgent task"))
heapq.heappush(task_queue, (2, "medium task"))
priority, task = heapq.heappop(task_queue)
print(task)  # "urgent task"

# Build heap from list in O(N)
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)
print(nums[0])  # 1 (minimum)


class MinHeap:
    """Min-heap from scratch for interview understanding."""
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if not self._data:
            raise IndexError("Heap is empty")
        self._swap(0, len(self._data) - 1)
        val = self._data.pop()
        if self._data:
            self._sift_down(0)
        return val

    def peek(self):
        return self._data[0]

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] < self._data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            smallest = i
            for child in [2*i+1, 2*i+2]:
                if child < n and self._data[child] < self._data[smallest]:
                    smallest = child
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __len__(self):
        return len(self._data)
```

## Common Patterns

### Top K Elements
```python
def top_k_largest(nums, k):
    """O(N log K) — maintain min-heap of size K"""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest
    return sorted(heap, reverse=True)

# Example: top 3 of [3,1,4,1,5,9,2,6]
print(top_k_largest([3,1,4,1,5,9,2,6], 3))  # [9, 6, 5]
```

### K-Way Merge
```python
def merge_k_sorted_lists(lists):
    """Merge K sorted arrays using min-heap — O(N log K)"""
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result
```

### Two Heaps (Median)
```python
class MedianFinder:
    """Find median from data stream — LeetCode #295"""
    def __init__(self):
        self.lo = []  # max-heap (lower half), negate for max
        self.hi = []  # min-heap (upper half)

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## When to Use
- "Find K largest/smallest" → min-heap of size K
- "Always need the minimum/maximum" → heap
- "Merge K sorted sequences" → K-way merge
- "Median of a stream" → two heaps
- Dijkstra's algorithm, Prim's MST

## LeetCode Problems

| Problem | Difficulty | Pattern |
|---------|-----------|---------|
| Kth Largest Element in Array (#215) | Medium | Min-heap size K |
| Top K Frequent Elements (#347) | Medium | Min-heap size K |
| K Closest Points to Origin (#973) | Medium | Min-heap size K |
| Find Median from Data Stream (#295) | Hard | Two heaps |
| Merge k Sorted Lists (#23) | Hard | K-way merge |
| Task Scheduler (#621) | Medium | Max-heap + greedy |
| Last Stone Weight (#1046) | Easy | Max-heap simulation |
| Kth Smallest in Sorted Matrix (#378) | Medium | Min-heap |
| Sliding Window Median (#480) | Hard | Two heaps |
| IPO (#502) | Hard | Two heaps |
| Furthest Building You Can Reach (#1642) | Medium | Min-heap |
| Find K Pairs with Smallest Sums (#373) | Medium | Min-heap |
