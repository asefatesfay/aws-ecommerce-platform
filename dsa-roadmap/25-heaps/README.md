# 25. Heaps (Priority Queues)

## Overview
A heap is a complete binary tree satisfying the heap property. A min-heap always has the smallest element at the root; a max-heap has the largest. Python's `heapq` is a min-heap by default (negate values for max-heap).

## Key Concepts
- `heappush` / `heappop` — O(log N)
- `heapify` — O(N) to build from a list
- **Two Heaps**: maintain a max-heap for the lower half and min-heap for the upper half (median finding)
- **K-Way Merge**: merge K sorted lists using a min-heap of size K
- **Top K**: use a min-heap of size K to track the K largest elements

## When to Use
- "Find the K largest/smallest" → heap of size K
- "Median of a stream" → two heaps
- "Merge K sorted lists" → K-way merge with heap
- "Next task by priority" → priority queue
- Dijkstra's shortest path

## Problems
| Problem | Difficulty |
|---------|-----------|
| Last Stone Weight | Easy |
| Kth Largest Element in a Stream | Easy |
| K Closest Points to Origin | Medium |
| Top K Frequent Elements | Medium |
| Find K Pairs with Smallest Sums | Medium |
| Kth Smallest in Sorted Matrix | Medium |
| Find Median from Data Stream | Hard |
| Merge k Sorted Lists | Hard |
| Sliding Window Median | Hard |
