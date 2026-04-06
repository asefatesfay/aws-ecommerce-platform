# 27. Data Structure Design

## Overview
Design problems require combining multiple data structures to achieve specific time complexity guarantees. The key is identifying which operations need to be O(1) or O(log N) and choosing structures accordingly.

## Key Concepts
- **Hash Map + Doubly Linked List** → LRU Cache (O(1) get/put)
- **Two Stacks** → Queue (amortized O(1))
- **Hash Map + Heap** → LFU Cache
- **Sorted Set / TreeMap** → range queries with O(log N)
- **Stack with min tracking** → Min Stack

## When to Use
- "Design a data structure that supports X in O(1)" → think hash map
- "Most recently used" → doubly linked list + hash map
- "Least frequently used" → frequency buckets + hash map
- "Random access in O(1)" → array + hash map

## Problems
| Problem | Difficulty |
|---------|-----------|
| Implement Queue using Stacks | Easy |
| Min Stack | Medium |
| LRU Cache | Medium |
| LFU Cache | Hard |
| Design Twitter | Medium |
| Insert Delete GetRandom O(1) | Medium |
| All O`one Data Structure | Hard |
