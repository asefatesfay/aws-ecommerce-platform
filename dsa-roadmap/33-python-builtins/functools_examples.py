"""
functools — Higher-order functions and tools for callables.

Covered here:
  lru_cache / cache  — memoize expensive repeated calls
  reduce             — fold a sequence into a single value
  partial            — freeze some arguments of a function
  wraps              — preserve metadata when writing decorators
  total_ordering     — define < or == once, get all comparisons for free
"""

import time
from functools import lru_cache, cache, reduce, partial, wraps, total_ordering


# ---------------------------------------------------------------------------
# 1. lru_cache — memoize recursive or repeated expensive calls
# ---------------------------------------------------------------------------

def demo_lru_cache():
    print("=" * 60)
    print("lru_cache")
    print("=" * 60)

    # --- 1a: classic Fibonacci ---
    # Without cache: O(2^n) calls.  With cache: O(n) calls.
    @lru_cache(maxsize=None)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    print("fib(10):", fib(10))   # 55
    print("fib(40):", fib(40))   # 102334155  (instant with cache)
    print("Cache info:", fib.cache_info())
    # CacheInfo(hits=38, misses=41, maxsize=None, currsize=41)

    # --- 1b: simulate an expensive DB lookup ---
    call_count = {"n": 0}

    @lru_cache(maxsize=128)
    def get_user_from_db(user_id: int) -> dict:
        call_count["n"] += 1
        # pretend this is a slow network call
        return {"id": user_id, "name": f"User_{user_id}", "active": True}

    # First calls hit the "database"
    get_user_from_db(1)
    get_user_from_db(2)
    get_user_from_db(1)   # cache hit — db NOT called again
    get_user_from_db(3)

    print("DB calls made (should be 3, not 4):", call_count["n"])   # 3

    # --- 1c: lru_cache with maxsize eviction ---
    @lru_cache(maxsize=2)
    def expensive(n):
        return n * n

    expensive(1)
    expensive(2)
    expensive(3)   # evicts 1 (LRU)
    expensive(1)   # miss: 1 was evicted
    print("Cache info (maxsize=2):", expensive.cache_info())
    # hits=0, misses=4 — because 1 was evicted before re-access

    print()


# ---------------------------------------------------------------------------
# 2. cache — simpler memoize (Python 3.9+), equivalent to lru_cache(maxsize=None)
# ---------------------------------------------------------------------------

def demo_cache():
    print("=" * 60)
    print("cache  (Python 3.9+)")
    print("=" * 60)

    @cache
    def count_paths(m: int, n: int) -> int:
        """Number of paths in an m x n grid moving only right or down."""
        if m == 1 or n == 1:
            return 1
        return count_paths(m - 1, n) + count_paths(m, n - 1)

    print("Paths in 3x3 grid:", count_paths(3, 3))   # 6
    print("Paths in 5x5 grid:", count_paths(5, 5))   # 70
    print("Paths in 10x10 grid:", count_paths(10, 10))   # 48620
    print("Cache info:", count_paths.cache_info())

    print()


# ---------------------------------------------------------------------------
# 3. reduce — fold a sequence into one value
# ---------------------------------------------------------------------------

def demo_reduce():
    print("=" * 60)
    print("reduce")
    print("=" * 60)

    # --- 3a: product of a list ---
    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda acc, x: acc * x, nums)
    print("Product of", nums, "=", product)   # 120

    # --- 3b: find max without max() ---
    values = [3, 1, 4, 1, 5, 9, 2, 6]
    maximum = reduce(lambda a, b: a if a > b else b, values)
    print("Max of", values, "=", maximum)   # 9

    # --- 3c: flatten a list of lists ---
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = reduce(lambda acc, lst: acc + lst, nested, [])
    print("Flattened:", flat)   # [1, 2, 3, 4, 5, 6]

    # --- 3d: build a dict from a list of (key, value) pairs ---
    pairs = [("name", "Alice"), ("role", "engineer"), ("level", "senior")]
    result_dict = reduce(lambda d, kv: {**d, kv[0]: kv[1]}, pairs, {})
    print("Dict from pairs:", result_dict)
    # {'name': 'Alice', 'role': 'engineer', 'level': 'senior'}

    # --- 3e: compose functions (pipeline of transformations) ---
    pipeline = [
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 3,
    ]
    value = reduce(lambda v, fn: fn(v), pipeline, 10)
    print("Pipeline result (start=10):", value)   # ((10+1)*2)-3 = 19

    print()


# ---------------------------------------------------------------------------
# 4. partial — freeze arguments to create specialised functions
# ---------------------------------------------------------------------------

def demo_partial():
    print("=" * 60)
    print("partial")
    print("=" * 60)

    # --- 4a: create a base-2 and base-16 converter ---
    def convert(number: int, base: int) -> str:
        digits = []
        while number:
            digits.append("0123456789ABCDEF"[number % base])
            number //= base
        return "".join(reversed(digits)) or "0"

    to_binary = partial(convert, base=2)
    to_hex    = partial(convert, base=16)

    print("255 in binary:", to_binary(255))    # 11111111
    print("255 in hex:   ", to_hex(255))       # FF
    print("10 in binary: ", to_binary(10))     # 1010

    # --- 4b: pre-configure an API call ---
    def make_request(endpoint: str, method: str = "GET",
                     timeout: int = 30, verify_ssl: bool = True) -> str:
        return f"{method} {endpoint} (timeout={timeout}, ssl={verify_ssl})"

    # Internal admin client always uses POST and skips SSL in dev
    admin_post = partial(make_request, method="POST", verify_ssl=False)
    print(admin_post("/api/admin/reset", timeout=5))
    # POST /api/admin/reset (timeout=5, ssl=False)

    # Read-only client always uses GET with a 10s timeout
    quick_get = partial(make_request, method="GET", timeout=10)
    print(quick_get("/api/products"))
    # GET /api/products (timeout=10, ssl=True)

    # --- 4c: use partial with map ---
    def multiply(x, factor):
        return x * factor

    double = partial(multiply, factor=2)
    triple = partial(multiply, factor=3)

    nums = [1, 2, 3, 4, 5]
    print("Doubled:", list(map(double, nums)))   # [2, 4, 6, 8, 10]
    print("Tripled:", list(map(triple, nums)))   # [3, 6, 9, 12, 15]

    print()


# ---------------------------------------------------------------------------
# 5. wraps — write decorators without losing the original function's metadata
# ---------------------------------------------------------------------------

def demo_wraps():
    print("=" * 60)
    print("wraps  (preserving function metadata inside decorators)")
    print("=" * 60)

    # ------- WITHOUT wraps (broken metadata) -------
    def timer_bad(fn):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"  [{fn.__name__}] took {elapsed:.6f}s")
            return result
        return wrapper

    @timer_bad
    def add(a, b):
        """Add two numbers."""
        return a + b

    print("Bad decorator: function name is", add.__name__)   # 'wrapper'  ← broken
    print("Bad decorator: docstring  is  ", add.__doc__)     # None       ← lost

    # ------- WITH wraps (correct metadata) -------
    def timer_good(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"  [{fn.__name__}] took {elapsed:.6f}s")
            return result
        return wrapper

    @timer_good
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    print("Good decorator: function name is", multiply.__name__)   # 'multiply' ✓
    print("Good decorator: docstring  is  ", multiply.__doc__)     # 'Multiply...' ✓

    result = multiply(6, 7)
    print("multiply(6, 7) =", result)   # 42

    # --- Real use-case: retry decorator ---
    def retry(max_attempts: int = 3):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        return fn(*args, **kwargs)
                    except Exception as exc:
                        print(f"  Attempt {attempt} failed: {exc}")
                        if attempt == max_attempts:
                            raise
            return wrapper
        return decorator

    call_count = {"n": 0}

    @retry(max_attempts=3)
    def unstable_api_call():
        """Simulates a flaky network call."""
        call_count["n"] += 1
        if call_count["n"] < 3:
            raise ConnectionError("timeout")
        return "success"

    print("Calling unstable API...")
    print("Result:", unstable_api_call())   # succeeds on 3rd attempt
    print("Function name preserved:", unstable_api_call.__name__)
    # 'unstable_api_call'  (not 'wrapper')

    print()


# ---------------------------------------------------------------------------
# 6. total_ordering — define one comparison, get them all
# ---------------------------------------------------------------------------

def demo_total_ordering():
    print("=" * 60)
    print("total_ordering")
    print("=" * 60)

    @total_ordering
    class Card:
        """Playing card.  Only __eq__ and __lt__ are defined manually."""
        RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

        def __init__(self, rank: str, suit: str):
            self.rank = rank
            self.suit = suit
            self._value = self.RANKS.index(rank)

        def __eq__(self, other):
            return self._value == other._value

        def __lt__(self, other):
            return self._value < other._value

        def __repr__(self):
            return f"{self.rank}{self.suit}"

    hand = [Card("K", "♠"), Card("A", "♥"), Card("3", "♦"), Card("10", "♣"), Card("J", "♣")]
    print("Original hand:", hand)

    hand.sort()
    print("Sorted hand:  ", hand)   # [3♦, 10♣, J♣, K♠, A♥]

    c1 = Card("K", "♠")
    c2 = Card("A", "♥")

    # total_ordering auto-generates >, >=, <=  from __eq__ and __lt__
    print(f"{c1} > {c2}:  ", c1 > c2)    # False
    print(f"{c1} >= {c2}: ", c1 >= c2)   # False
    print(f"{c1} <= {c2}: ", c1 <= c2)   # True
    print(f"{c2} > {c1}:  ", c2 > c1)    # True
    print("Max card:", max(hand))        # A♥

    # --- Product comparison by price ---
    @total_ordering
    class Product:
        def __init__(self, name: str, price: float):
            self.name  = name
            self.price = price

        def __eq__(self, other):
            return self.price == other.price

        def __lt__(self, other):
            return self.price < other.price

        def __repr__(self):
            return f"{self.name}(${self.price})"

    products = [
        Product("Laptop", 999.99),
        Product("Phone",  499.49),
        Product("Tablet", 649.00),
    ]
    print("Cheapest:", min(products))    # Phone($499.49)
    print("Priciest:", max(products))    # Laptop($999.99)
    print("Sorted:  ", sorted(products))

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_lru_cache()
    demo_cache()
    demo_reduce()
    demo_partial()
    demo_wraps()
    demo_total_ordering()
