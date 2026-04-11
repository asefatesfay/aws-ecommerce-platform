"""
copy — Shallow and deep copying of Python objects.

Why this matters in DSA:
  - In graph/tree problems, accidentally sharing mutable nodes introduces hard-to-find bugs.
  - DP with memoised state grids or backtracking solution paths need independent copies.
  - "=" never copies — it only creates a new reference to the same object.

Covered here:
  Assignment vs copy       — showing the difference concretely
  copy.copy()              — shallow copy (new container, same element references)
  copy.deepcopy()          — fully independent recursive copy
  copy.copy on custom objs — __copy__ dunder
  copy.deepcopy custom     — __deepcopy__ dunder
  copy.deepcopy with memo  — avoid infinite loops in cyclic structures
  DSA gotchas              — 2D grids, adjacency lists, backtracking paths
"""

import copy
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# 1. Assignment vs shallow copy vs deep copy — the core difference
# ---------------------------------------------------------------------------

def demo_assignment_vs_copy():
    print("=" * 60)
    print("Assignment  vs  copy  vs  deepcopy")
    print("=" * 60)

    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Assignment — alias, NOT a copy
    alias    = original
    shallow  = copy.copy(original)
    deep     = copy.deepcopy(original)

    # Mutate a nested element
    original[0][0] = 99

    print("After original[0][0] = 99:")
    print("  original:", original)
    print("  alias:   ", alias)     # SAME reference — also changed
    print("  shallow: ", shallow)   # inner list is shared — also changed!
    print("  deep:    ", deep)      # fully independent — unchanged

    # Mutate the outer list (add row)
    original.append([10, 11, 12])
    print("\nAfter original.append([10,11,12]):")
    print("  original:", original)
    print("  alias:   ", alias)     # changed (same object)
    print("  shallow: ", shallow)   # NOT changed (new outer list)
    print("  deep:    ", deep)      # NOT changed

    print()


# ---------------------------------------------------------------------------
# 2. Shallow copy details — what IS and ISN'T shared
# ---------------------------------------------------------------------------

def demo_shallow_copy():
    print("=" * 60)
    print("Shallow copy — what is shared")
    print("=" * 60)

    # Lists
    original_list = [[1, 2], [3, 4]]
    shallow_list  = copy.copy(original_list)

    print("id(original_list):", id(original_list))
    print("id(shallow_list): ", id(shallow_list))   # different container
    print("id(original_list[0]):", id(original_list[0]))
    print("id(shallow_list[0]): ", id(shallow_list[0]))  # SAME inner list

    # Dicts
    original_dict = {"a": [1, 2, 3], "b": {"nested": True}}
    shallow_dict  = copy.copy(original_dict)

    shallow_dict["a"].append(99)   # mutates shared list
    print("\nAfter shallow_dict['a'].append(99):")
    print("  original_dict['a']:", original_dict["a"])  # [1, 2, 3, 99] — affected!
    print("  shallow_dict['a']: ", shallow_dict["a"])

    shallow_dict["c"] = "new key"
    print("\nAfter adding 'c' to shallow_dict:")
    print("  'c' in original_dict:", "c" in original_dict)  # False — outer is separate
    print("  'c' in shallow_dict: ", "c" in shallow_dict)   # True

    # Sets, frozensets, tuples — copy returns the same object (immutable anyway)
    s = frozenset([1, 2, 3])
    s2 = copy.copy(s)
    print("\nfrozenset copy is same object:", s is s2)  # True (immutable, no point copying)

    print()


# ---------------------------------------------------------------------------
# 3. Deep copy details
# ---------------------------------------------------------------------------

def demo_deep_copy():
    print("=" * 60)
    print("deepcopy — fully independent")
    print("=" * 60)

    original = {
        "name": "Alice",
        "scores": [95, 87, 92],
        "address": {"city": "NYC", "zip": "10001"},
        "friends": [{"name": "Bob"}, {"name": "Carol"}],
    }

    deep = copy.deepcopy(original)

    # Mutate deeply nested data
    deep["scores"].append(100)
    deep["address"]["city"] = "LA"
    deep["friends"][0]["name"] = "Dave"

    print("After modifying deep copy:")
    print("  original scores:     ", original["scores"])   # [95, 87, 92] — untouched
    print("  deep scores:         ", deep["scores"])        # [95, 87, 92, 100]
    print("  original city:       ", original["address"]["city"])  # NYC
    print("  deep city:           ", deep["address"]["city"])       # LA
    print("  original friend 0:   ", original["friends"][0]["name"])  # Bob
    print("  deep friend 0:       ", deep["friends"][0]["name"])       # Dave

    print()


# ---------------------------------------------------------------------------
# 4. __copy__ and __deepcopy__ on custom objects
# ---------------------------------------------------------------------------

def demo_custom_copy():
    print("=" * 60)
    print("Custom __copy__ and __deepcopy__")
    print("=" * 60)

    class Config:
        """A config object. Shallow copy shares defaults; deep copy is independent."""
        _defaults = {"timeout": 30, "retries": 3}   # class-level attribute

        def __init__(self, host: str, port: int):
            self.host     = host
            self.port     = port
            self.overrides: dict = {}

        def __copy__(self):
            """Shallow copy: new object, shared _defaults."""
            new = Config.__new__(Config)
            new.__dict__.update(self.__dict__)
            # overrides is still shared!
            return new

        def __deepcopy__(self, memo: dict):
            """Deep copy: completely independent."""
            new = Config.__new__(Config)
            memo[id(self)] = new
            for k, v in self.__dict__.items():
                setattr(new, k, copy.deepcopy(v, memo))
            return new

        def __repr__(self):
            return f"Config({self.host}:{self.port}, overrides={self.overrides})"

    original = Config("prod.server.com", 443)
    original.overrides["debug"] = False

    shallow = copy.copy(original)
    deep    = copy.deepcopy(original)

    shallow.overrides["debug"] = True   # modifies shared dict

    print("Original:", original)   # debug=True (affected by shallow mutation)
    print("Shallow: ", shallow)    # debug=True
    print("Deep:    ", deep)       # debug=False (independent)

    deep.host = "dev.server.com"
    print("\nAfter deep.host='dev.server.com':")
    print("  original.host:", original.host)   # prod.server.com
    print("  deep.host:    ", deep.host)       # dev.server.com

    print()


# ---------------------------------------------------------------------------
# 5. Cyclic structures — deepcopy handles them with memo
# ---------------------------------------------------------------------------

def demo_cyclic_deepcopy():
    print("=" * 60)
    print("deepcopy handles cyclic structures (via memo)")
    print("=" * 60)

    # Linked list with back-reference
    class Node:
        def __init__(self, val: int):
            self.val  = val
            self.next = None

        def __repr__(self):
            return f"Node({self.val})"

    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    c.next = a   # cycle: a -> b -> c -> a

    # deepcopy uses a memo dict to detect already-copied objects,
    # so it won't loop infinitely
    copied_a = copy.deepcopy(a)
    print("Original a:", a)
    print("Copied   a:", copied_a)
    print("Are they different objects?", a is not copied_a)  # True
    print("a.next is b:", a.next is b)              # True
    print("copied_a.next is b:", copied_a.next is b)  # False (own copy)
    # The cycle is preserved in the copy:
    print("Cycle preserved:", copied_a.next.next.next is copied_a)  # True

    print()


# ---------------------------------------------------------------------------
# 6. DSA gotchas — 2D grid, backtracking path, adjacency list
# ---------------------------------------------------------------------------

def demo_dsa_gotchas():
    print("=" * 60)
    print("DSA gotchas — 2D grid, backtracking, adjacency list")
    print("=" * 60)

    # --- 6a: 2D grid initialisation BUG ---
    print("2D grid bug (wrong way):")
    # WRONG: all rows point to the same list!
    wrong_grid = [[0] * 3] * 3
    wrong_grid[0][0] = 9
    print("  wrong_grid:", wrong_grid)
    # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  — ALL rows changed!

    print("2D grid (correct):")
    # RIGHT: list comprehension creates independent inner lists
    correct_grid = [[0] * 3 for _ in range(3)]
    correct_grid[0][0] = 9
    print("  correct_grid:", correct_grid)
    # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]

    # --- 6b: backtracking — append to path then restore ---
    def find_paths(graph: dict, start: int, end: int) -> list[list[int]]:
        """Find all simple paths from start to end."""
        results = []
        path    = [start]
        visited = {start}

        def dfs(node: int) -> None:
            if node == end:
                results.append(path[:])   # MUST copy! list[:] is a shallow copy of ints
                return
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    path.append(neighbour)
                    dfs(neighbour)
                    path.pop()             # restore — backtrack
                    visited.discard(neighbour)

        dfs(start)
        return results

    graph = {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}
    paths = find_paths(graph, 1, 5)
    print("\nAll paths from 1 to 5:", paths)
    # [[1, 2, 4, 5], [1, 3, 4, 5]]

    # --- 6c: deep copy a graph adjacency list before mutation ---
    adj = {0: [1, 2], 1: [2], 2: []}
    adj_copy = copy.deepcopy(adj)
    adj_copy[0].append(3)
    adj_copy[3] = []

    print("\nOriginal graph:", adj)     # unchanged
    print("Modified copy: ", adj_copy)

    # --- 6d: DP state copy — grid representing DP table ---
    def knapsack_trace(weights, values, capacity):
        """0/1 knapsack with path recovery — needs to preserve state at each step."""
        n = len(weights)
        # dp[i][w] = max value using items 0..i-1 with capacity w
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                dp[i][w] = dp[i - 1][w]
                if weights[i - 1] <= w:
                    dp[i][w] = max(dp[i][w],
                                   dp[i - 1][w - weights[i - 1]] + values[i - 1])

        # Trace back which items were selected
        selected = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected.append(i - 1)
                w -= weights[i - 1]

        return dp[n][capacity], list(reversed(selected))

    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    capacity = 8
    max_val, items = knapsack_trace(weights, values, capacity)
    print(f"\nKnapsack (cap={capacity}): max value = {max_val}, items taken = {items}")
    # max value = 10, items = [1, 3] (0-indexed)

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_assignment_vs_copy()
    demo_shallow_copy()
    demo_deep_copy()
    demo_custom_copy()
    demo_cyclic_deepcopy()
    demo_dsa_gotchas()
