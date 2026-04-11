"""
contextlib — Utilities for working with context managers (with statements).
io         — Core tools for stream I/O (StringIO, BytesIO).

contextlib covered:
  @contextmanager         — build a context manager from a generator
  asynccontextmanager     — async equivalent
  contextmanager error handling — try/finally in the generator
  suppress()              — silence specific exceptions
  closing()               — wrap objects that have .close() but not __exit__
  ExitStack               — dynamically combine multiple context managers
  nullcontext()           — no-op context manager (Python 3.7+)
  redirect_stdout/stderr  — capture or redirect output
  AbstractContextManager  — base class for custom context managers
  chdir()                 — temporarily change the working directory (3.11+)

io covered:
  StringIO    — in-memory text stream (file-like object for strings)
  BytesIO     — in-memory binary stream
  TextIOWrapper — wrap a binary stream as text
  Common use cases: capture print() output, build strings via write(),
                    create fake files for testing, parse CSV from a string
"""

import io
import sys
import time
import tempfile
import os
from contextlib import (
    contextmanager, suppress, closing, ExitStack,
    nullcontext, redirect_stdout, redirect_stderr,
    AbstractContextManager,
)


# ---------------------------------------------------------------------------
# 1. @contextmanager — simplest way to write a context manager
# ---------------------------------------------------------------------------

def demo_contextmanager():
    print("=" * 60)
    print("@contextmanager")
    print("=" * 60)

    # --- 1a: timer context manager ---
    @contextmanager
    def timer(label: str = ""):
        start = time.perf_counter()
        try:
            yield          # <-- code inside 'with' runs here
        finally:
            elapsed = time.perf_counter() - start
            tag = f"[{label}] " if label else ""
            print(f"  {tag}elapsed: {elapsed*1000:.2f}ms")

    with timer("list comprehension"):
        nums = [x**2 for x in range(10_000)]

    with timer("generator"):
        nums = sum(x**2 for x in range(10_000))

    # --- 1b: temporary in-memory patch ---
    @contextmanager
    def patch_env(key: str, value: str):
        """Temporarily set an environment variable."""
        original = os.environ.get(key)
        os.environ[key] = value
        try:
            yield
        finally:
            if original is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = original

    with patch_env("DEBUG", "true"):
        print(f"  Inside: DEBUG = {os.environ.get('DEBUG')}")
    print(f"  Outside: DEBUG = {os.environ.get('DEBUG')}")  # restored

    # --- 1c: managed DB connection simulation ---
    class FakeDB:
        def __init__(self, name):
            self.name    = name
            self.connected = False

        def connect(self):
            self.connected = True
            return self

        def execute(self, sql):
            return f"[{self.name}] result of: {sql}"

        def close(self):
            self.connected = False

    @contextmanager
    def db_connection(name: str):
        db = FakeDB(name)
        db.connect()
        print(f"  DB connected: {db.name}")
        try:
            yield db
        except Exception as e:
            print(f"  DB error: {e}")
            raise
        finally:
            db.close()
            print(f"  DB closed: {db.name}")

    with db_connection("mydb") as db:
        result = db.execute("SELECT * FROM users")
        print(" ", result)

    print()


# ---------------------------------------------------------------------------
# 2. contextmanager with error handling
# ---------------------------------------------------------------------------

def demo_contextmanager_errors():
    print("=" * 60)
    print("@contextmanager — error handling")
    print("=" * 60)

    @contextmanager
    def transaction(name: str):
        """Simulate a database transaction."""
        print(f"  BEGIN {name}")
        try:
            yield name
            print(f"  COMMIT {name}")
        except Exception as e:
            print(f"  ROLLBACK {name} due to: {e}")
            # Re-raise so the caller knows about the error
            raise

    # Successful transaction
    try:
        with transaction("order_insert"):
            print("  Inserting order...")
            print("  Updating inventory...")
    except Exception:
        pass

    print()

    # Failed transaction
    try:
        with transaction("payment_process"):
            print("  Charging card...")
            raise ValueError("Card declined")
            print("  This never runs")
    except ValueError:
        print("  Caught error outside the context manager")

    print()


# ---------------------------------------------------------------------------
# 3. suppress — silently ignore specified exceptions
# ---------------------------------------------------------------------------

def demo_suppress():
    print("=" * 60)
    print("suppress — silence specific exceptions")
    print("=" * 60)

    # Without suppress:
    # try:
    #     os.remove("nonexistent.txt")
    # except FileNotFoundError:
    #     pass

    # With suppress:
    with suppress(FileNotFoundError):
        os.remove("/tmp/nonexistent_file_abc.txt")
    print("Completed (FileNotFoundError silenced)")

    # Suppress multiple exception types
    data = {"a": 1, "b": 2}
    with suppress(KeyError, TypeError):
        val = data["missing_key"]
        print("This won't run")
    print("KeyError silenced")

    # Practical: safe integer conversion
    def safe_int(value: str) -> int | None:
        with suppress(ValueError, TypeError):
            return int(value)
        return None

    test_inputs = ["42", "3.14", "abc", None, "0"]
    for inp in test_inputs:
        print(f"  safe_int({inp!r:8}) = {safe_int(inp)}")

    print()


# ---------------------------------------------------------------------------
# 4. closing — safely close objects without __exit__
# ---------------------------------------------------------------------------

def demo_closing():
    print("=" * 60)
    print("closing — wrap closeable objects")
    print("=" * 60)

    # Some objects have .close() but no __enter__/__exit__
    class ResourcePool:
        def __init__(self, name: str, size: int):
            self.name = name
            self.size = size
            self.open = True
            print(f"  Pool '{name}' opened (size={size})")

        def acquire(self):
            return f"connection from {self.name}"

        def close(self):
            self.open = False
            print(f"  Pool '{self.name}' closed")

    pool = ResourcePool("db_pool", 10)
    with closing(pool):
        conn = pool.acquire()
        print(f"  Using: {conn}")
    # close() is called even if an exception occurs

    print(f"  Pool still open: {pool.open}")   # False

    # Also works with io objects explicitly if needed
    sio = io.StringIO("some data")
    with closing(sio):
        content = sio.read()
        print(f"\n  Read from StringIO: '{content}'")
    # sio is now closed

    print()


# ---------------------------------------------------------------------------
# 5. ExitStack — dynamically manage multiple context managers
# ---------------------------------------------------------------------------

def demo_exit_stack():
    print("=" * 60)
    print("ExitStack — combine context managers dynamically")
    print("=" * 60)

    # --- 5a: open N files at once safely ---
    @contextmanager
    def fake_file(name: str):
        print(f"  Opening {name}")
        try:
            yield io.StringIO(f"content of {name}")
        finally:
            print(f"  Closing {name}")

    filenames = ["config.yaml", "data.json", "schema.sql"]
    with ExitStack() as stack:
        files = [stack.enter_context(fake_file(fn)) for fn in filenames]
        for fn, f in zip(filenames, files):
            print(f"  Read {fn}: '{f.read()}'")
    # All 3 files closed even if one raises

    print()

    # --- 5b: conditionally activate a context manager ---
    def process(debug: bool = False):
        capture = io.StringIO()
        with ExitStack() as stack:
            if debug:
                stack.enter_context(redirect_stdout(capture))
            print("Processing data...")    # only captured in debug mode
            print("Done.")

        if debug:
            output = capture.getvalue()
            print(f"  Captured output: {output!r}")

    process(debug=False)
    process(debug=True)

    # --- 5c: defer cleanup callbacks ---
    resources = []
    with ExitStack() as stack:
        stack.callback(lambda: print("  Callback 1: cleanup A"))
        stack.callback(lambda: print("  Callback 2: cleanup B"))
        resources.append("database")
        resources.append("cache")
        print("  Working with:", resources)
    # Callbacks run in reverse LIFO order when the block exits

    print()


# ---------------------------------------------------------------------------
# 6. redirect_stdout / redirect_stderr
# ---------------------------------------------------------------------------

def demo_redirect():
    print("=" * 60)
    print("redirect_stdout / redirect_stderr")
    print("=" * 60)

    # --- 6a: capture print() output as a string ---
    def noisy_function():
        print("Step 1: loading data")
        print("Step 2: processing")
        print("Step 3: writing results")
        return 42

    capture_buffer = io.StringIO()
    with redirect_stdout(capture_buffer):
        result = noisy_function()

    captured_text = capture_buffer.getvalue()
    print(f"Function returned: {result}")
    print(f"Captured {len(captured_text.splitlines())} lines:")
    for line in captured_text.splitlines():
        print(f"  | {line}")

    # --- 6b: redirect stderr to suppress warnings ---
    import warnings
    err_buffer = io.StringIO()
    with redirect_stderr(err_buffer):
        warnings.warn("This warning is suppressed from console", stacklevel=2)

    print(f"\nSuppressed stderr ({len(err_buffer.getvalue())} bytes)")

    # --- 6c: capture print() for testing ---
    def format_report(items: list[dict]) -> str:
        buf = io.StringIO()
        with redirect_stdout(buf):
            for item in items:
                print(f"{item['name']:20} ${item['price']:.2f}")
        return buf.getvalue()

    products = [
        {"name": "Laptop",  "price": 999.99},
        {"name": "Keyboard","price":  79.99},
    ]
    report = format_report(products)
    print("Report:\n" + report)

    print()


# ---------------------------------------------------------------------------
# 7. io.StringIO — in-memory text streams
# ---------------------------------------------------------------------------

def demo_stringio():
    print("=" * 60)
    print("io.StringIO — in-memory text buffer")
    print("=" * 60)

    # --- 7a: build a large string efficiently with write() ---
    buf = io.StringIO()
    headers = ["id", "name", "score"]
    rows    = [(1, "Alice", 95), (2, "Bob", 87), (3, "Carol", 92)]

    buf.write(",".join(headers) + "\n")
    for row in rows:
        buf.write(",".join(str(v) for v in row) + "\n")

    csv_text = buf.getvalue()
    print("CSV output:")
    print(csv_text)

    # --- 7b: read from a StringIO as if it were a file ---
    source = io.StringIO("line 1\nline 2\nline 3\n")
    for line in source:
        print(f"  read: {line.rstrip()!r}")

    # --- 7c: seek and tell ---
    stream = io.StringIO("Hello, World!")
    pos_start = stream.tell()
    content   = stream.read(5)
    pos_after = stream.tell()
    print(f"\nRead 5 chars: {content!r}  (pos {pos_start} -> {pos_after})")
    stream.seek(0)
    print("After seek(0):", stream.read())

    # --- 7d: parse CSV from a string (no temp file needed) ---
    import csv
    raw_csv = "name,age,city\nAlice,30,NYC\nBob,25,LA\nCarol,35,Chicago"
    reader  = csv.DictReader(io.StringIO(raw_csv))
    print("\nParsed CSV:")
    for row in reader:
        print(f"  {row}")

    print()


# ---------------------------------------------------------------------------
# 8. io.BytesIO — in-memory binary streams
# ---------------------------------------------------------------------------

def demo_bytesio():
    print("=" * 60)
    print("io.BytesIO — in-memory binary buffer")
    print("=" * 60)

    # --- 8a: build binary data in memory before writing to disk ---
    buf = io.BytesIO()
    buf.write(b"PNG\x89\x50\x4e\x47")   # fake PNG header
    buf.write(b"\x00" * 100)             # placeholder data

    size = buf.tell()
    print(f"Built {size} bytes in memory")
    buf.seek(0)
    header = buf.read(8)
    print(f"Header: {header!r}")

    # --- 8b: decode bytes as text using TextIOWrapper ---
    raw_bytes = b"name,age\nAlice,30\nBob,25\n"
    byte_stream = io.BytesIO(raw_bytes)
    text_stream = io.TextIOWrapper(byte_stream, encoding="utf-8")

    print("\nDecoded as text:")
    for line in text_stream:
        print(f"  {line.rstrip()!r}")

    # --- 8c: common pattern: download bytes, process without disk ---
    def process_image_bytes(image_data: bytes) -> dict:
        """Simulate processing without writing to disk."""
        buf = io.BytesIO(image_data)
        buf.seek(0)
        size = len(buf.read())
        return {"size_bytes": size, "is_empty": size == 0}

    fake_image = b"\xff\xd8\xff" + b"\x00" * 997  # fake JPEG header + data
    result = process_image_bytes(fake_image)
    print(f"\nImage processing result: {result}")

    print()


# ---------------------------------------------------------------------------
# 9. Custom context manager class (AbstractContextManager)
# ---------------------------------------------------------------------------

def demo_custom_cm_class():
    print("=" * 60)
    print("Custom context manager class")
    print("=" * 60)

    class RateLimit(AbstractContextManager):
        """Allow at most `limit` calls per `window_secs` seconds (leaky bucket)."""

        def __init__(self, limit: int, window_secs: float = 1.0, name: str = ""):
            self.limit       = limit
            self.window_secs = window_secs
            self.name        = name or "rate_limiter"
            self.call_times: list[float] = []

        def __enter__(self) -> RateLimit:
            now = time.monotonic()
            # Remove expired entries
            self.call_times = [t for t in self.call_times if now - t < self.window_secs]
            if len(self.call_times) >= self.limit:
                wait = self.window_secs - (now - self.call_times[0])
                print(f"  [{self.name}] Rate limit hit — sleeping {wait:.2f}s")
                time.sleep(wait)
            self.call_times.append(time.monotonic())
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return False   # don't suppress exceptions

    limiter = RateLimit(limit=3, window_secs=0.5, name="api")
    for i in range(5):
        with limiter:
            print(f"  Call {i + 1}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("CONTEXTLIB")
    print("=" * 60)
    demo_contextmanager()
    demo_contextmanager_errors()
    demo_suppress()
    demo_closing()
    demo_exit_stack()
    demo_redirect()

    print("=" * 60)
    print("IO")
    print("=" * 60)
    demo_stringio()
    demo_bytesio()
    demo_custom_cm_class()
