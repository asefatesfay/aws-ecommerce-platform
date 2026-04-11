"""
heapq — Min-heap operations on a plain Python list.

Key insight: Python's heapq gives you a min-heap.
To simulate a max-heap, negate values when pushing and negate again when popping.

Covered here:
  heappush / heappop          — push/pop maintaining heap invariant
  heapify                     — turn any list into a heap in-place O(n)
  nlargest / nsmallest        — top-K without full sort O(n log k)
  heapreplace / heappushpop   — efficient combined push+pop variants
  min-heap priority queue     — task scheduling by priority
  max-heap via negation       — sliding window maximum, top bids
  merge sorted streams        — merge k sorted iterables efficiently
  Dijkstra shortest path      — classic graph algorithm using a heap
"""

import heapq
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# 1. Basic heappush / heappop / heapify
# ---------------------------------------------------------------------------

def demo_basics():
    print("=" * 60)
    print("heappush / heappop / heapify")
    print("=" * 60)

    # --- 1a: build a heap one item at a time ---
    min_heap = []
    for price in [42, 17, 88, 5, 31]:
        heapq.heappush(min_heap, price)

    print("Internal heap list:", min_heap)
    # [5, 17, 88, 42, 31]  — heap-ordered, NOT sorted

    print("Popping in ascending order:")
    while min_heap:
        print(" ", heapq.heappop(min_heap), end="")
    print()   # 5 17 31 42 88

    # --- 1b: heapify — convert an existing list in O(n) ---
    scores = [64, 21, 99, 33, 78, 45]
    heapq.heapify(scores)
    print("heapify result:", scores)   # heap-ordered, lowest at index 0
    print("Min score:", scores[0])    # 21 (peek without popping)

    # --- 1c: heapreplace — pop smallest and push new item atomically ---
    top3_heap = [10, 20, 30]   # already a valid min-heap
    heapq.heapify(top3_heap)

    incoming = [5, 15, 25, 35]
    for val in incoming:
        if val > top3_heap[0]:         # only add if larger than current min
            heapq.heapreplace(top3_heap, val)

    print("Top 3 largest from stream:", sorted(top3_heap))   # [25, 30, 35]

    print()


# ---------------------------------------------------------------------------
# 2. nlargest / nsmallest — top-K selection
# ---------------------------------------------------------------------------

def demo_top_k():
    print("=" * 60)
    print("nlargest / nsmallest  (top-K without full sort)")
    print("=" * 60)

    # --- 2a: find the 3 highest-rated products ---
    products = [
        {"name": "Laptop Pro",    "rating": 4.8, "reviews": 1200},
        {"name": "Wireless Mouse","rating": 4.5, "reviews": 800},
        {"name": "USB-C Hub",     "rating": 4.9, "reviews": 340},
        {"name": "Keyboard",      "rating": 4.3, "reviews": 2100},
        {"name": "Monitor 4K",    "rating": 4.7, "reviews": 560},
        {"name": "Webcam HD",     "rating": 4.6, "reviews": 920},
    ]

    top3_rated = heapq.nlargest(3, products, key=lambda p: p["rating"])
    print("Top 3 highest-rated products:")
    for p in top3_rated:
        print(f"  {p['name']:20s}  rating={p['rating']}")
    # USB-C Hub (4.9), Laptop Pro (4.8), Monitor 4K (4.7)

    # --- 2b: find 2 cheapest flights ---
    flights = [
        ("NYC", "LAX", 289),
        ("NYC", "ORD", 175),
        ("NYC", "MIA", 210),
        ("NYC", "SEA", 335),
        ("NYC", "DEN", 198),
    ]

    cheapest_2 = heapq.nsmallest(2, flights, key=lambda f: f[2])
    print("\nCheapest 2 flights from NYC:")
    for origin, dest, price in cheapest_2:
        print(f"  {origin} -> {dest}: ${price}")
    # NYC -> ORD: $175,  NYC -> DEN: $198

    # --- 2c: when to use nlargest/nsmallest vs sorted ---
    # Rule of thumb:
    #   k << n  -> heapq.nlargest/nsmallest is faster O(n log k)
    #   k ~ n   -> sorted + slice is simpler O(n log n)
    import random
    data = random.sample(range(1_000_000), 100_000)

    top10 = heapq.nlargest(10, data)    # efficient for large n, small k
    print("\nTop 10 values (heapq):", top10)

    print()


# ---------------------------------------------------------------------------
# 3. Priority queue for task scheduling
# ---------------------------------------------------------------------------

def demo_priority_queue():
    print("=" * 60)
    print("Priority queue  (task scheduler)")
    print("=" * 60)

    # Each entry: (priority, tie-breaker, task_name)
    # Lower priority number = higher urgency (min-heap pops smallest first)
    task_queue = []
    counter = 0   # tie-breaker to avoid comparing task names

    def add_task(priority: int, task_name: str):
        nonlocal counter
        heapq.heappush(task_queue, (priority, counter, task_name))
        counter += 1

    add_task(3, "send weekly report")
    add_task(1, "fix production outage")    # highest urgency
    add_task(2, "review pull requests")
    add_task(1, "respond to incident PagerDuty")  # same priority as outage
    add_task(4, "update documentation")

    print("Processing tasks by priority:")
    while task_queue:
        priority, _, task = heapq.heappop(task_queue)
        print(f"  [{priority}] {task}")
    # [1] fix production outage
    # [1] respond to incident PagerDuty
    # [2] review pull requests
    # [3] send weekly report
    # [4] update documentation

    print()


# ---------------------------------------------------------------------------
# 4. Max-heap via negation
# ---------------------------------------------------------------------------

def demo_max_heap():
    print("=" * 60)
    print("Max-heap via negation")
    print("=" * 60)

    # --- 4a: keep track of the K highest bids ---
    max_heap = []
    bids = [500, 750, 620, 810, 590, 700, 880, 720]

    for bid in bids:
        heapq.heappush(max_heap, -bid)   # negate to simulate max-heap

    print("Bids in order (highest first):")
    while max_heap:
        print(" ", -heapq.heappop(max_heap), end="")
    print()   # 880 810 750 720 700 620 590 500

    # --- 4b: sliding window maximum (brute-force with max-heap) ---
    prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    k = 3    # window size

    # (value, index) pairs; we check index to know if element is still in window
    heap = []   # max-heap (negate values)
    result = []

    for i, price in enumerate(prices):
        heapq.heappush(heap, (-price, i))

        # remove stale elements outside the window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        if i >= k - 1:
            result.append(-heap[0][0])

    print("Prices:          ", prices)
    print("Sliding max (k=3):", result)
    # [4, 4, 5, 9, 9, 9, 6, 6]

    print()


# ---------------------------------------------------------------------------
# 5. merge — merge k sorted iterables without loading all into memory
# ---------------------------------------------------------------------------

def demo_merge():
    print("=" * 60)
    print("heapq.merge  (k sorted streams)")
    print("=" * 60)

    # --- 5a: merge sorted log files by timestamp ---
    log_file_1 = [(1000, "server-A", "started"),
                  (1005, "server-A", "request received"),
                  (1020, "server-A", "request processed")]

    log_file_2 = [(1002, "server-B", "started"),
                  (1008, "server-B", "request received"),
                  (1015, "server-B", "error: timeout")]

    log_file_3 = [(1001, "server-C", "started"),
                  (1012, "server-C", "request received")]

    merged = heapq.merge(log_file_1, log_file_2, log_file_3)

    print("Merged chronological log:")
    for ts, server, event in merged:
        print(f"  t={ts:4d}  {server:8}  {event}")
    # Sorted by timestamp across all three files

    # --- 5b: merge pre-sorted chunks from disk ---
    chunk_a = [2, 5, 8, 11]
    chunk_b = [1, 4, 7, 10, 13]
    chunk_c = [3, 6, 9, 12]

    all_sorted = list(heapq.merge(chunk_a, chunk_b, chunk_c))
    print("\nMerged sorted chunks:", all_sorted)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print()


# ---------------------------------------------------------------------------
# 6. Dijkstra's shortest path using heapq
# ---------------------------------------------------------------------------

def demo_dijkstra():
    print("=" * 60)
    print("Dijkstra shortest path")
    print("=" * 60)

    # Graph: {node: [(neighbour, weight), ...]}
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [("E", 3)],
        "E": [],
    }
    # Shortest paths from A:
    # A->C->B->D->E = 1+2+1+3 = 7

    def dijkstra(graph: dict, start: str) -> dict:
        dist = {node: float("inf") for node in graph}
        dist[start] = 0
        heap = [(0, start)]   # (distance, node)

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue   # stale entry
            for neighbour, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(heap, (new_dist, neighbour))

        return dist

    distances = dijkstra(graph, "A")
    print("Shortest distances from A:")
    for node, d in sorted(distances.items()):
        print(f"  A -> {node}: {d}")
    # A->A: 0, A->B: 3, A->C: 1, A->D: 4, A->E: 7

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_basics()
    demo_top_k()
    demo_priority_queue()
    demo_max_heap()
    demo_merge()
    demo_dijkstra()
