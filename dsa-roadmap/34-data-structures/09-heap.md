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

---

### 1. Kth Largest Element in an Array — #215 (Medium)

**Problem**: Given an integer array and integer k, return the kth largest element (not the kth distinct element).

```
Input:  nums=[3,2,1,5,6,4], k=2
Output: 5

Input:  nums=[3,2,3,1,2,4,5,5,6], k=4
Output: 4
```

**Hints**:
1. Min-heap of size k: push each element, pop when size > k
2. After processing all elements, `heap[0]` is the kth largest
3. Alternative: QuickSelect for O(N) average time

---

### 2. Top K Frequent Elements — #347 (Medium)

**Problem**: Given an integer array and integer k, return the k most frequent elements in any order.

```
Input:  nums=[1,1,1,2,2,3], k=2
Output: [1,2]

Input:  nums=[1], k=1
Output: [1]
```

**Hints**:
1. Count frequencies with a hash map
2. Use a min-heap of size k storing `(freq, num)`; pop when size > k
3. Alternative: bucket sort — bucket[freq] = list of nums with that frequency; scan from high to low

---

### 3. K Closest Points to Origin — #973 (Medium)

**Problem**: Given an array of points on a 2D plane, return the k closest points to the origin (0,0). Distance = Euclidean distance (no need to take square root).

```
Input:  points=[[1,3],[-2,2]], k=1
Output: [[-2,2]]
Explanation: dist(1,3)=√10, dist(-2,2)=√8. Closest is [-2,2].

Input:  points=[[3,3],[5,-1],[-2,4]], k=2
Output: [[3,3],[-2,4]]
```

**Hints**:
1. Max-heap of size k storing `(-dist, point)` (negate for max-heap behavior)
2. Pop when size > k; remaining k elements are the closest
3. Or use `heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)`

---

### 4. Find Median from Data Stream — #295 (Hard)

**Problem**: Design a data structure that supports `addNum(num)` and `findMedian()`. The median is the middle value of a sorted list (or average of two middle values for even length).

```
Input:
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],            [1],     [2],     [],          [3],     []]

Output: [null, null, null, 1.5, null, 2.0]

Trace:
addNum(1) → [1], median = 1.0
addNum(2) → [1,2], median = (1+2)/2 = 1.5
addNum(3) → [1,2,3], median = 2.0
```

**Hints**:
1. Two heaps: `lo` = max-heap (lower half), `hi` = min-heap (upper half)
2. Always keep `len(lo) == len(hi)` or `len(lo) == len(hi) + 1`
3. `findMedian`: if sizes equal, return `(-lo[0] + hi[0]) / 2`; else return `-lo[0]`
4. On `addNum`: push to `lo`, then balance by moving top of `lo` to `hi` if needed

---

### 5. Merge k Sorted Lists — #23 (Hard)

**Problem**: Given an array of k linked lists, each sorted in ascending order, merge all into one sorted linked list.

```
Input:  [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input:  []
Output: []

Input:  [[]]
Output: []
```

**Hints**:
1. Use a min-heap of `(value, list_index, node)` — one entry per list
2. Pop the minimum, add to result, push the next node from that list
3. Total time: O(N log k) where N = total nodes, k = number of lists

---

### 6. Task Scheduler — #621 (Medium)

**Problem**: Given a list of tasks (letters) and a cooldown n, find the minimum number of intervals needed to execute all tasks. Same task must be separated by at least n intervals.

```
Input:  tasks=["A","A","A","B","B","B"], n=2
Output: 8
Schedule: A → B → idle → A → B → idle → A → B

Input:  tasks=["A","A","A","B","B","B"], n=0
Output: 6  (no cooldown needed)

Input:  tasks=["A","A","A","A","A","A","B","C","D","E","F","G"], n=2
Output: 16
```

**Hints**:
1. Always execute the most frequent remaining task first (greedy)
2. Use a max-heap of `(-count, task)`
3. In each round of n+1 slots, pop up to n+1 tasks from the heap, execute them, re-add with decremented count
4. Formula shortcut: `max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq_tasks)`
