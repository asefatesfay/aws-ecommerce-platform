# Graph

## What is it?
A collection of **nodes (vertices)** connected by **edges**. Graphs can be directed/undirected, weighted/unweighted, cyclic/acyclic.

## Visual Example
```
Undirected graph:          Directed graph (DAG):
    0 --- 1                    0 → 1
    |   / |                    ↓   ↓
    |  /  |                    2 → 3
    | /   |
    2 --- 3

Adjacency list:
0: [1, 2]
1: [0, 2, 3]
2: [0, 1, 3]
3: [1, 2]

BFS from 0: 0, 1, 2, 3
DFS from 0: 0, 1, 2, 3 (or 0, 2, 1, 3 depending on order)
```

## Implementation

```python
from collections import defaultdict, deque
import heapq

class Graph:
    """Directed/undirected weighted graph using adjacency list."""
    def __init__(self, directed=False):
        self._adj = defaultdict(list)  # node → [(neighbor, weight)]
        self._directed = directed
        self._nodes = set()

    def add_edge(self, u, v, weight=1):
        """Add edge u→v (and v→u if undirected) — O(1)"""
        self._adj[u].append((v, weight))
        self._nodes.update([u, v])
        if not self._directed:
            self._adj[v].append((u, weight))

    def neighbors(self, node):
        return self._adj[node]

    # ── Traversals ──────────────────────────────────────────────────────────

    def dfs(self, start):
        """Depth-first search — O(V + E)"""
        visited, result = set(), []
        def _dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor, _ in self._adj[node]:
                if neighbor not in visited:
                    _dfs(neighbor)
        _dfs(start)
        return result

    def bfs(self, start):
        """Breadth-first search — O(V + E)"""
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor, _ in self._adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def bfs_shortest_path(self, start, end):
        """Shortest path in unweighted graph — O(V + E)"""
        if start == end:
            return [start]
        visited = {start}
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            for neighbor, _ in self._adj[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []  # no path

    # ── Cycle Detection ─────────────────────────────────────────────────────

    def has_cycle_undirected(self):
        """Detect cycle in undirected graph — O(V + E)"""
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbor, _ in self._adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True  # back edge = cycle
            return False
        for node in self._nodes:
            if node not in visited:
                if dfs(node, -1):
                    return True
        return False

    def has_cycle_directed(self):
        """Detect cycle in directed graph using DFS colors — O(V + E)"""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {node: WHITE for node in self._nodes}
        def dfs(node):
            color[node] = GRAY
            for neighbor, _ in self._adj[node]:
                if color[neighbor] == GRAY:
                    return True  # back edge
                if color[neighbor] == WHITE and dfs(neighbor):
                    return True
            color[node] = BLACK
            return False
        return any(dfs(n) for n in self._nodes if color[n] == WHITE)

    # ── Topological Sort ────────────────────────────────────────────────────

    def topological_sort(self):
        """Kahn's algorithm (BFS) — O(V + E). Returns [] if cycle."""
        in_degree = defaultdict(int)
        for node in self._nodes:
            for neighbor, _ in self._adj[node]:
                in_degree[neighbor] += 1
        queue = deque([n for n in self._nodes if in_degree[n] == 0])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor, _ in self._adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == len(self._nodes) else []

    # ── Shortest Path ───────────────────────────────────────────────────────

    def dijkstra(self, start):
        """Shortest paths from start (non-negative weights) — O((V+E) log V)"""
        dist = {node: float('inf') for node in self._nodes}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for neighbor, weight in self._adj[node]:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        return dist

    def count_components(self):
        """Count connected components — O(V + E)"""
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for neighbor, _ in self._adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for node in self._nodes:
            if node not in visited:
                dfs(node)
                count += 1
        return count
```

## Example Usage
```python
g = Graph(directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

print(g.bfs(0))                    # [0, 1, 2, 3]
print(g.dfs(0))                    # [0, 1, 3, 2]
print(g.bfs_shortest_path(0, 3))   # [0, 1, 3]
print(g.has_cycle_undirected())    # True (0-1-3-2-0)
print(g.count_components())        # 1

# Weighted graph + Dijkstra
wg = Graph(directed=True)
wg.add_edge(0, 1, 4)
wg.add_edge(0, 2, 1)
wg.add_edge(2, 1, 2)
wg.add_edge(1, 3, 1)
print(wg.dijkstra(0))  # {0:0, 1:3, 2:1, 3:4}
```

## When to Use
- Network connectivity problems
- Shortest path problems
- Dependency resolution (topological sort)
- Social network analysis
- Map/routing problems

## LeetCode Problems

---

### 1. Number of Islands — #200 (Medium)

**Problem**: Given a 2D grid of `'1'` (land) and `'0'` (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

```
Input:
[["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]
Output: 1

Input:
[["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]]
Output: 3
```

**Hints**:
1. DFS or BFS from each unvisited `'1'`
2. Mark visited cells as `'0'` (or use a visited set) to avoid revisiting
3. Each DFS/BFS call from a new `'1'` = one island

---

### 2. Course Schedule — #207 (Medium)

**Problem**: There are `numCourses` courses (0 to numCourses-1). Given a list of `prerequisites` where `[a, b]` means you must take course b before a, determine if it's possible to finish all courses.

```
Input:  numCourses=2, prerequisites=[[1,0]]
Output: true  (take 0 then 1)

Input:  numCourses=2, prerequisites=[[1,0],[0,1]]
Output: false  (cycle: 0 requires 1, 1 requires 0)

Input:  numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]
Output: true
```

**Hints**:
1. Build a directed graph; the problem reduces to cycle detection
2. DFS with 3 states: unvisited (0), in-progress (1), done (2)
3. If you reach an in-progress node, there's a cycle → return false

---

### 3. Course Schedule II — #210 (Medium)

**Problem**: Same as Course Schedule, but return the order in which courses should be taken. If impossible (cycle), return an empty array.

```
Input:  numCourses=2, prerequisites=[[1,0]]
Output: [0,1]

Input:  numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]  (or [0,1,2,3])

Input:  numCourses=1, prerequisites=[]
Output: [0]
```

**Hints**:
1. Topological sort (Kahn's algorithm): start with nodes that have in-degree 0
2. Process each node, reduce in-degree of its neighbors; add neighbors with in-degree 0 to queue
3. If the result contains all nodes, return it; otherwise a cycle exists

---

### 4. Network Delay Time — #743 (Medium)

**Problem**: There are `n` nodes and `times[i] = [u, v, w]` means a signal travels from node u to v in w time. A signal is sent from node `k`. Return the time for all nodes to receive the signal, or -1 if impossible.

```
Input:  times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
Output: 2
Explanation: Signal from 2 reaches 1 in 1, 3 in 1, 4 in 2. Max = 2.

Input:  times=[[1,2,1]], n=2, k=1
Output: 1

Input:  times=[[1,2,1]], n=2, k=2
Output: -1  (node 1 never receives signal)
```

**Hints**:
1. Dijkstra's algorithm from node k
2. Use a min-heap: `(distance, node)`
3. Answer = max distance among all nodes; if any node is unreachable (dist=inf), return -1

---

### 5. Pacific Atlantic Water Flow — #417 (Medium)

**Problem**: An `m x n` island has rain water that flows to adjacent cells with equal or lower height. Water can flow to the Pacific (top/left edges) or Atlantic (bottom/right edges). Return all cells from which water can flow to both oceans.

```
Input:
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Hints**:
1. Reverse the flow: BFS/DFS from ocean edges inward (water flows uphill in reverse)
2. Find all cells reachable from Pacific edges; find all cells reachable from Atlantic edges
3. Return the intersection

---

### 6. Word Ladder — #127 (Hard)

**Problem**: Transform `beginWord` to `endWord` one letter at a time, where each intermediate word must be in `wordList`. Return the length of the shortest transformation sequence, or 0 if none exists.

```
Input:  beginWord="hit", endWord="cog"
        wordList=["hot","dot","dog","lot","log","cog"]
Output: 5
Path:   hit → hot → dot → dog → cog

Input:  beginWord="hit", endWord="cog"
        wordList=["hot","dot","dog","lot","log"]
Output: 0  ("cog" not in wordList)
```

**Hints**:
1. BFS from `beginWord`; each level = one transformation
2. For each word, try replacing each character with a-z; if the result is in the word set, add to queue
3. Remove words from the set as visited to avoid cycles
