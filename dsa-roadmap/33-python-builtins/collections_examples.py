"""
collections — Python's built-in high-performance container datatypes.

Covered here:
  Counter       — count elements instantly
  defaultdict   — dict that auto-creates missing keys
  deque         — double-ended queue (O(1) append/pop on both ends)
  namedtuple    — lightweight immutable record with named fields
  OrderedDict   — dict that remembers insertion order (and exposes move_to_end)
  ChainMap      — stack multiple dicts into one view
"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap


# ---------------------------------------------------------------------------
# 1. Counter — word frequency, top-N, arithmetic
# ---------------------------------------------------------------------------

def demo_counter():
    print("=" * 60)
    print("Counter")
    print("=" * 60)

    # --- 1a: word frequency in a sentence ---
    sentence = "the cat sat on the mat the cat"
    freq = Counter(sentence.split())
    print("Word counts:", freq)
    # Counter({'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1})

    print("Most common 2:", freq.most_common(2))
    # [('the', 3), ('cat', 2)]

    # --- 1b: character frequency ---
    char_freq = Counter("abracadabra")
    print("Char counts:", char_freq)
    # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

    # --- 1c: e-commerce — count orders per product ---
    orders = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    order_count = Counter(orders)
    print("Orders per product:", order_count)
    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
    print("Apple orders:", order_count["apple"])   # 3
    print("Missing key:", order_count["mango"])    # 0  (no KeyError!)

    # --- 1d: set-style arithmetic ---
    inventory_a = Counter({"apple": 5, "banana": 3})
    inventory_b = Counter({"apple": 2, "cherry": 4})
    print("Combined inventory:", inventory_a + inventory_b)
    # Counter({'apple': 7, 'cherry': 4, 'banana': 3})
    print("Remaining after shipment:", inventory_a - inventory_b)
    # Counter({'banana': 3, 'apple': 3})

    # --- 1e: subtract (useful for ticket/seat reservation) ---
    seats = Counter({"economy": 100, "business": 20, "first": 5})
    booked = Counter({"economy": 40, "business": 5})
    seats.subtract(booked)
    print("Remaining seats:", seats)
    # Counter({'economy': 60, 'business': 15, 'first': 5})

    print()


# ---------------------------------------------------------------------------
# 2. defaultdict — grouping and frequency counting without KeyError
# ---------------------------------------------------------------------------

def demo_defaultdict():
    print("=" * 60)
    print("defaultdict")
    print("=" * 60)

    # --- 2a: group orders by customer ---
    raw_orders = [
        ("alice", "laptop"),
        ("bob",   "phone"),
        ("alice", "mouse"),
        ("carol", "keyboard"),
        ("bob",   "monitor"),
        ("alice", "webcam"),
    ]

    orders_by_customer = defaultdict(list)
    for customer, item in raw_orders:
        orders_by_customer[customer].append(item)

    print("Customer orders:")
    for customer, items in orders_by_customer.items():
        print(f"  {customer}: {items}")
    # alice: ['laptop', 'mouse', 'webcam']
    # bob:   ['phone', 'monitor']
    # carol: ['keyboard']

    # --- 2b: frequency counter from scratch ---
    log_lines = ["ERROR", "INFO", "ERROR", "WARN", "INFO", "ERROR"]
    level_count = defaultdict(int)
    for level in log_lines:
        level_count[level] += 1

    print("Log level counts:", dict(level_count))
    # {'ERROR': 3, 'INFO': 2, 'WARN': 1}

    # --- 2c: adjacency list for a graph ---
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    graph = defaultdict(list)
    for src, dst in edges:
        graph[src].append(dst)

    print("Adjacency list:")
    for node, neighbours in sorted(graph.items()):
        print(f"  {node} -> {neighbours}")
    # 1 -> [2, 3]
    # 2 -> [4]
    # 3 -> [4]
    # 4 -> [5]

    # --- 2d: defaultdict(set) to track unique visitors per page ---
    visits = [
        ("home",    "alice"),
        ("about",   "bob"),
        ("home",    "alice"),   # duplicate — ignored by set
        ("home",    "carol"),
        ("about",   "alice"),
    ]
    unique_visitors = defaultdict(set)
    for page, user in visits:
        unique_visitors[page].add(user)

    print("Unique visitors per page:")
    for page, users in unique_visitors.items():
        print(f"  {page}: {sorted(users)}")
    # about: ['alice', 'bob']
    # home:  ['alice', 'carol']

    print()


# ---------------------------------------------------------------------------
# 3. deque — O(1) append and pop from both ends
# ---------------------------------------------------------------------------

def demo_deque():
    print("=" * 60)
    print("deque")
    print("=" * 60)

    # --- 3a: basic operations ---
    dq = deque([1, 2, 3])
    dq.appendleft(0)        # add to left
    dq.append(4)            # add to right
    print("After appendleft(0) and append(4):", list(dq))  # [0, 1, 2, 3, 4]

    dq.popleft()            # remove from left
    dq.pop()                # remove from right
    print("After popleft() and pop():", list(dq))           # [1, 2, 3]

    # --- 3b: fixed-size sliding window (last 3 prices) ---
    price_stream = [10, 14, 11, 17, 9, 13, 18, 12]
    window = deque(maxlen=3)
    print("Sliding window (size 3):")
    for price in price_stream:
        window.append(price)
        print(f"  added {price} -> window = {list(window)}")
    # When window is full, oldest value is auto-removed

    # --- 3c: BFS level-order traversal (queue behaviour) ---
    # Simple tree as adjacency list
    tree = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
    queue = deque([1])
    bfs_order = []
    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        queue.extend(tree[node])
    print("BFS order:", bfs_order)   # [1, 2, 3, 4, 5, 6]

    # --- 3d: undo history (stack of recent actions) ---
    history = deque(maxlen=5)
    for action in ["type A", "type B", "delete", "type C", "paste", "type D", "type E"]:
        history.append(action)

    print("Last 5 actions (undo history):", list(history))
    # ['type C', 'paste', 'type D', 'type E']  older ones dropped

    # --- 3e: rotate — useful for round-robin scheduling ---
    tasks = deque(["Alice", "Bob", "Carol", "Dave"])
    print("Round-robin for 6 turns:")
    for turn in range(6):
        current = tasks[0]
        print(f"  Turn {turn + 1}: {current}")
        tasks.rotate(-1)   # move front to back

    print()


# ---------------------------------------------------------------------------
# 4. namedtuple — lightweight immutable records
# ---------------------------------------------------------------------------

def demo_namedtuple():
    print("=" * 60)
    print("namedtuple")
    print("=" * 60)

    # --- 4a: 2D point ---
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print("Point:", p)                    # Point(x=3, y=4)
    print("x =", p.x, "  y =", p.y)       # x = 3   y = 4
    distance = (p.x**2 + p.y**2) ** 0.5
    print("Distance from origin:", distance)   # 5.0

    # --- 4b: employee records ---
    Employee = namedtuple("Employee", ["name", "department", "salary"])
    employees = [
        Employee("Alice", "Engineering", 95000),
        Employee("Bob",   "Marketing",   72000),
        Employee("Carol", "Engineering", 105000),
        Employee("Dave",  "Marketing",   68000),
    ]

    print("All employees:")
    for emp in employees:
        print(f"  {emp.name:8} | {emp.department:12} | ${emp.salary:,}")

    # Sort by salary descending
    top_earners = sorted(employees, key=lambda e: e.salary, reverse=True)
    print("Top earner:", top_earners[0].name)   # Carol

    # --- 4c: HTTP response record ---
    Response = namedtuple("Response", ["status_code", "body", "headers"])
    ok       = Response(200, '{"result": "ok"}', {"Content-Type": "application/json"})
    not_found = Response(404, "Not Found",         {})

    print("Status:", ok.status_code)         # 200
    print("Body:",   ok.body)                # {"result": "ok"}
    print("404 body:", not_found.body)       # Not Found

    # _replace creates a modified copy (namedtuples are immutable)
    redirected = ok._replace(status_code=301)
    print("Redirected response:", redirected)
    # Response(status_code=301, body='{"result": "ok"}', headers={...})

    print()


# ---------------------------------------------------------------------------
# 5. OrderedDict — dict with move_to_end (classic LRU cache pattern)
# ---------------------------------------------------------------------------

def demo_ordered_dict():
    print("=" * 60)
    print("OrderedDict  (LRU cache simulation)")
    print("=" * 60)

    class LRUCache:
        """Least-Recently-Used cache backed by OrderedDict."""

        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = OrderedDict()

        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)   # mark as recently used
            return self.cache[key]

        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)   # evict least recently used

        def __repr__(self):
            return f"LRUCache({dict(self.cache)})"

    lru = LRUCache(3)
    lru.put(1, "page_A")
    lru.put(2, "page_B")
    lru.put(3, "page_C")
    print("After 3 inserts:", lru)
    # LRUCache({1: 'page_A', 2: 'page_B', 3: 'page_C'})

    lru.get(1)              # access key 1  -> moves to end (most recent)
    print("After get(1):", lru)
    # LRUCache({2: 'page_B', 3: 'page_C', 1: 'page_A'})

    lru.put(4, "page_D")    # capacity exceeded -> evict key 2 (least recent)
    print("After put(4):", lru)
    # LRUCache({3: 'page_C', 1: 'page_A', 4: 'page_D'})

    print("get(2):", lru.get(2))   # -1 (evicted)
    print("get(3):", lru.get(3))   # page_C

    print()


# ---------------------------------------------------------------------------
# 6. ChainMap — layered config / scoping
# ---------------------------------------------------------------------------

def demo_chain_map():
    print("=" * 60)
    print("ChainMap  (layered configuration)")
    print("=" * 60)

    # --- 6a: environment config override pattern ---
    defaults = {
        "debug":    False,
        "timeout":  30,
        "host":     "prod.example.com",
        "log_level": "WARNING",
    }
    dev_overrides = {
        "debug":    True,
        "host":     "localhost",
        "log_level": "DEBUG",
    }

    # dev_overrides is searched first, then defaults
    config = ChainMap(dev_overrides, defaults)

    print("debug   :", config["debug"])      # True  (from dev_overrides)
    print("timeout :", config["timeout"])    # 30    (from defaults)
    print("host    :", config["host"])       # localhost (from dev_overrides)

    # Writing always goes to the first map
    config["port"] = 8080
    print("Port in dev_overrides:", dev_overrides.get("port"))  # 8080
    print("Port in defaults:     ", defaults.get("port"))       # None

    # --- 6b: function scope simulation (outer -> inner) ---
    global_scope = {"x": 10, "y": 20}
    local_scope  = {"x": 99}   # x is shadowed locally

    scope = ChainMap(local_scope, global_scope)
    print("x (local shadows global):", scope["x"])   # 99
    print("y (only in global):",       scope["y"])   # 20

    # Listing all maps
    print("All maps:", list(scope.maps))

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_counter()
    demo_defaultdict()
    demo_deque()
    demo_namedtuple()
    demo_ordered_dict()
    demo_chain_map()
