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

| Problem | Difficulty | Algorithm |
|---------|-----------|-----------|
| Number of Islands (#200) | Medium | DFS/BFS on grid |
| Clone Graph (#133) | Medium | DFS + hash map |
| Course Schedule (#207) | Medium | Cycle detection (directed) |
| Course Schedule II (#210) | Medium | Topological sort |
| Pacific Atlantic Water Flow (#417) | Medium | Multi-source BFS |
| Number of Provinces (#547) | Medium | DFS components |
| Word Ladder (#127) | Hard | BFS shortest path |
| Network Delay Time (#743) | Medium | Dijkstra |
| Cheapest Flights Within K Stops (#787) | Medium | Bellman-Ford / Dijkstra |
| Alien Dictionary (#269) | Hard | Topological sort |
| Critical Connections (#1192) | Hard | Tarjan's bridges |
| Swim in Rising Water (#778) | Hard | Dijkstra / Binary search |
| Reconstruct Itinerary (#332) | Hard | Eulerian path (DFS) |
