# Node Navigation Intuition

Files in this folder build mental models for navigating pointer-based data structures.

| File | What it covers |
|------|---------------|
| [node-navigation.md](./node-navigation.md) | Core mental model — sticky note analogy, pointer patterns, universal checklist |
| [linked-list-problems.md](./linked-list-problems.md) | 10 problems easy→hard with step-by-step pointer traces |
| [tree-problems.md](./tree-problems.md) | 10 problems easy→hard, bottom-up vs top-down recursion |
| [graph-problems.md](./graph-problems.md) | 8 problems easy→hard, DFS vs BFS with mermaid diagrams |

## Reading Order

1. Start with `node-navigation.md` — builds the core mental model
2. `linked-list-problems.md` — master pointer manipulation
3. `tree-problems.md` — master recursion patterns
4. `graph-problems.md` — master traversal + visited set patterns

## Quick Pattern Reference

```
LINKED LIST          TREE                    GRAPH
─────────────────────────────────────────────────────
Reversal             Bottom-up DFS           DFS + visited set
  prev/curr/nxt        return values up        cycle detection

Slow/fast ptrs       Top-down DFS            BFS + visited set
  cycle, middle        pass state down         shortest path

Dummy head           Global variable         Multi-source BFS
  simplify edge        cross-subtree           spread from all
  cases                problems               sources at once
```
