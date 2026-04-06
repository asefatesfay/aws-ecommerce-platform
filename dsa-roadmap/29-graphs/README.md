# 29. Graphs

## Overview
Graphs consist of nodes (vertices) and edges. They can be directed/undirected, weighted/unweighted, cyclic/acyclic.

## Key Algorithms
- **DFS**: explore as deep as possible before backtracking. Use for connected components, cycle detection, topological sort.
- **BFS**: explore level by level. Use for shortest path in unweighted graphs, multi-source problems.
- **Topological Sort**: linear ordering of vertices in a DAG. Use Kahn's algorithm (BFS) or DFS.
- **Union-Find**: efficiently track connected components. Use for Kruskal's MST, cycle detection.
- **Dijkstra**: shortest path in weighted graphs with non-negative weights.

## When to Use
- "Number of connected components" → DFS/BFS or Union-Find
- "Shortest path (unweighted)" → BFS
- "Shortest path (weighted)" → Dijkstra
- "Course prerequisites / dependency order" → Topological Sort
- "Detect cycle" → DFS with visited states or Union-Find

## Problems
| Problem | Difficulty |
|---------|-----------|
| Number of Islands | Medium |
| Clone Graph | Medium |
| Course Schedule II | Medium |
| Word Ladder | Hard |
| Number of Provinces | Medium |
| Redundant Connection | Medium |
| Network Delay Time | Medium |
| Alien Dictionary | Hard |
