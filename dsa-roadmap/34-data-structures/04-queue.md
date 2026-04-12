# Queue

## What is it?
A **First-In, First-Out (FIFO)** data structure. Think of a line at a coffee shop — first person in line gets served first.

## Visual Example
```
enqueue(1) → enqueue(2) → enqueue(3) → dequeue() → peek()

Front → [1][2][3] ← Back

dequeue() removes from front → returns 1
Front → [2][3] ← Back

peek() returns 2 (front, without removing)
```

## Key Operations
| Operation | Time | Description |
|-----------|------|-------------|
| enqueue(val) | O(1) | Add to back |
| dequeue() | O(1) | Remove from front |
| peek() | O(1) | View front without removing |
| is_empty() | O(1) | Check if empty |

## Implementation

```python
from collections import deque

class Queue:
    """FIFO queue backed by collections.deque"""
    def __init__(self):
        self._data = deque()

    def enqueue(self, val):
        self._data.append(val)      # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self._data.popleft() # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class QueueUsingTwoStacks:
    """
    Queue implemented with two stacks.
    Amortized O(1) dequeue — LeetCode #232
    
    Intuition: inbox receives new items; outbox serves items.
    When outbox is empty, flip inbox into outbox (reverses order).
    """
    def __init__(self):
        self._inbox = []
        self._outbox = []

    def push(self, val):
        self._inbox.append(val)

    def pop(self):
        self._refill()
        return self._outbox.pop()

    def peek(self):
        self._refill()
        return self._outbox[-1]

    def empty(self):
        return not self._inbox and not self._outbox

    def _refill(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
```

## Example Usage
```python
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")
print(q.dequeue())  # Alice (first in, first out)
print(q.peek())     # Bob
print(len(q))       # 2

# BFS example using queue
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

## When to Use
- BFS (shortest path in unweighted graphs)
- Level-order tree traversal
- Task scheduling / job queues
- Sliding window problems (with deque)
- Multi-source BFS (rotting oranges, walls and gates)

## LeetCode Problems

| Problem | Difficulty | How Queue Helps |
|---------|-----------|-----------------|
| Implement Queue using Stacks (#232) | Easy | Two-stack queue |
| Number of Recent Calls (#933) | Easy | Sliding window with deque |
| Moving Average from Data Stream (#346) | Easy | Fixed-size window |
| Binary Tree Level Order Traversal (#102) | Medium | BFS with queue |
| Rotting Oranges (#994) | Medium | Multi-source BFS |
| Walls and Gates (#286) | Medium | Multi-source BFS |
| Word Ladder (#127) | Hard | BFS shortest path |
| Sliding Window Maximum (#239) | Hard | Monotonic deque |
| Open the Lock (#752) | Medium | BFS state space |
| Snakes and Ladders (#909) | Medium | BFS on board |
