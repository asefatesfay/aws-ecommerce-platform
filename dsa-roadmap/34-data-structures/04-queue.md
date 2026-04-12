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

---

### 1. Implement Queue using Stacks — #232 (Easy)

**Problem**: Implement a FIFO queue using only two stacks. Support `push`, `pop`, `peek`, `empty`.

```
Input:
["MyQueue","push","push","peek","pop","empty"]
[[],       [1],   [2],   [],    [],   []]

Output: [null, null, null, 1, 1, false]

Trace:
push(1) → inbox: [1]
push(2) → inbox: [1, 2]
peek()  → transfer inbox to outbox: outbox=[2,1], return 1
pop()   → return 1 from outbox, outbox=[2]
empty() → false
```

**Hints**:
1. Use two stacks: `inbox` and `outbox`
2. `push` always goes to inbox
3. `pop`/`peek`: if outbox is empty, pour all of inbox into outbox (reverses order)

---

### 2. Binary Tree Level Order Traversal — #102 (Medium)

**Problem**: Given the root of a binary tree, return the level-order traversal of its nodes' values (i.e., from left to right, level by level).

```
Input:
    3
   / \
  9  20
     / \
    15   7

Output: [[3], [9, 20], [15, 7]]

Input: [1]
Output: [[1]]

Input: []
Output: []
```

**Hints**:
1. Use a queue; start with the root
2. Each iteration, process all nodes currently in the queue (one full level)
3. For each node, add its children to the queue for the next level

---

### 3. Rotting Oranges — #994 (Medium)

**Problem**: A grid contains `0` (empty), `1` (fresh orange), `2` (rotten orange). Every minute, fresh oranges adjacent (4-directionally) to rotten ones become rotten. Return the minimum minutes until no fresh orange remains, or `-1` if impossible.

```
Input:
[[2,1,1],
 [1,1,0],
 [0,1,1]]
Output: 4

Input:
[[2,1,1],
 [0,1,1],
 [1,0,1]]
Output: -1  (bottom-left orange is isolated)

Input:
[[0,2]]
Output: 0  (no fresh oranges)
```

**Hints**:
1. Multi-source BFS: start with all rotten oranges in the queue simultaneously
2. Each BFS level = 1 minute; spread rot to all 4 neighbors
3. After BFS, if any fresh orange remains, return -1

---

### 4. Word Ladder — #127 (Hard)

**Problem**: Given `beginWord`, `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, where each step changes exactly one letter and each intermediate word must be in `wordList`. Return 0 if no path exists.

```
Input:  beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"]
Output: 5
Path:   hit → hot → dot → dog → cog  (5 words = 4 transformations)

Input:  beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log"]
Output: 0  ("cog" not in wordList)
```

**Hints**:
1. BFS from `beginWord`; each level = one transformation
2. For each word, try changing each character to a-z and check if it's in the word set
3. Remove words from the set as you visit them to avoid revisiting

---

### 5. Open the Lock — #752 (Medium)

**Problem**: A lock has 4 circular wheels (0-9). Start at "0000". Given a list of `deadends` (forbidden states) and a `target`, find the minimum number of turns to reach the target. Each turn rotates one wheel by 1 (wrapping 0↔9).

```
Input:  deadends=["0201","0101","0102","1212","2002"], target="0202"
Output: 6
Path:   0000 → 1000 → 1100 → 1200 → 1201 → 1202 → 0202

Input:  deadends=["8888"], target="0009"
Output: 1
Path:   0000 → 0009

Input:  deadends=["8887","8889","8878","8898","8788","8988","7888","9888"], target="8888"
Output: -1  (target is surrounded by deadends)
```

**Hints**:
1. BFS on the state space — each state is a 4-digit string
2. From each state, generate 8 neighbors (each wheel ±1)
3. Skip deadends and already-visited states

---

### 6. Sliding Window Maximum — #239 (Hard)

**Problem**: Given an array and window size k, return the maximum value in each sliding window of size k.

```
Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]

Explanation:
Window [1,3,-1]  → max 3
Window [3,-1,-3] → max 3
Window [-1,-3,5] → max 5
Window [-3,5,3]  → max 5
Window [5,3,6]   → max 6
Window [3,6,7]   → max 7
```

**Hints**:
1. Use a monotonic decreasing deque of indices
2. Remove indices from the front when they fall outside the window
3. Remove indices from the back when their value ≤ current value
4. Front of deque is always the index of the current window's maximum
