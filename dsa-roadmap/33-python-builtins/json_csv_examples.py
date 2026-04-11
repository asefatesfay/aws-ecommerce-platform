"""
json — Encode Python objects to JSON strings and decode JSON back to Python.
csv  — Read and write comma-separated values files/streams.

json covered:
  json.dumps()     — Python object -> JSON string
  json.loads()     — JSON string -> Python object
  json.dump()      — write JSON to a file
  json.load()      — read JSON from a file
  indent / sort_keys / separators — formatting options
  ensure_ascii     — handle non-ASCII characters
  default=         — handle un-serialisable types (datetime, Enum, dataclass, etc.)
  object_hook=     — customise decoding (JSON -> custom objects)
  JSONEncoder subclass — fully customise encoding
  JSONDecoder subclass — fully customise decoding

csv covered:
  csv.reader       — iterate rows as lists
  csv.writer       — write rows from lists
  csv.DictReader   — iterate rows as OrderedDict / dict (header row as keys)
  csv.DictWriter   — write rows from dicts
  Quoting modes    — QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE
  Custom dialect   — define delimiter, quotechar, lineterminator
  StringIO + csv   — parse CSV from a string (no file needed)
"""

import csv
import io
import json
import os
import tempfile
from datetime import datetime, date
from decimal import Decimal
from enum import Enum


# ===========================================================================
# JSON
# ===========================================================================

# ---------------------------------------------------------------------------
# 1. json.dumps and json.loads — basic encode/decode
# ---------------------------------------------------------------------------

def demo_json_basics():
    print("=" * 60)
    print("json.dumps  and  json.loads")
    print("=" * 60)

    # Python -> JSON
    product = {
        "id":       42,
        "name":     "Laptop Pro",
        "price":    999.99,
        "in_stock": True,
        "tags":     ["electronics", "computers"],
        "specs":    {"ram": "16GB", "storage": "512GB"},
        "rating":   None,   # None becomes JSON null
    }

    json_str = json.dumps(product)
    print("Compact JSON:")
    print(json_str)

    # Pretty-print with indent
    pretty = json.dumps(product, indent=2)
    print("\nFormatted JSON:")
    print(pretty)

    # Sort keys for deterministic output (useful in tests/diffs)
    stable = json.dumps(product, sort_keys=True, indent=2)
    print("\nSorted keys:")
    print(stable[:120], "...")

    # JSON -> Python
    recovered = json.loads(json_str)
    print("\nDecoded Python type:", type(recovered))
    print("Name:", recovered["name"])
    print("Tags:", recovered["tags"])
    print("Rating is None:", recovered["rating"] is None)

    # Type mapping
    print("\nJSON <-> Python type mapping:")
    samples = [
        ("JSON object",  '{"a": 1}',      dict),
        ("JSON array",   '[1, 2, 3]',      list),
        ("JSON string",  '"hello"',        str),
        ("JSON int",     '42',             int),
        ("JSON float",   '3.14',           float),
        ("JSON true",    'true',           bool),
        ("JSON null",    'null',           type(None)),
    ]
    for label, raw, expected_type in samples:
        val = json.loads(raw)
        print(f"  {label:15} -> {type(val).__name__:6} == {expected_type.__name__}: "
              f"{isinstance(val, expected_type)}")

    print()


# ---------------------------------------------------------------------------
# 2. json.dump / json.load — file I/O
# ---------------------------------------------------------------------------

def demo_json_file():
    print("=" * 60)
    print("json.dump  and  json.load  (file I/O)")
    print("=" * 60)

    data = {
        "version": "2.1.0",
        "users":   [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
        "config":  {"debug": False, "timeout": 30},
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                     delete=False, encoding="utf-8") as f:
        path = f.name
        json.dump(data, f, indent=2)
        print(f"Wrote to {os.path.basename(path)}")

    with open(path, encoding="utf-8") as f:
        loaded = json.load(f)
    os.unlink(path)

    print("Loaded version:", loaded["version"])
    print("First user:", loaded["users"][0])

    # Streaming large JSON line-by-line (JSON Lines / NDJSON)
    records = [
        {"event": "click", "user": "alice", "ts": 1000},
        {"event": "view",  "user": "bob",   "ts": 1001},
        {"event": "buy",   "user": "alice", "ts": 1002},
    ]

    buf = io.StringIO()
    for record in records:
        buf.write(json.dumps(record) + "\n")   # one JSON object per line

    buf.seek(0)
    print("\nJSON Lines parsed:")
    for line in buf:
        obj = json.loads(line)
        print(f"  {obj}")

    print()


# ---------------------------------------------------------------------------
# 3. Custom encoding — datetime, Decimal, Enum, dataclass
# ---------------------------------------------------------------------------

def demo_custom_encoding():
    print("=" * 60)
    print("Custom JSON encoding (default= and JSONEncoder)")
    print("=" * 60)

    class Status(Enum):
        PENDING   = "pending"
        SHIPPED   = "shipped"
        DELIVERED = "delivered"

    order = {
        "id":         12345,
        "created_at": datetime(2024, 3, 15, 9, 30, 0),
        "total":      Decimal("149.99"),
        "status":     Status.SHIPPED,
        "tags":       frozenset(["express", "fragile"]),
    }

    # --- Method 1: default= function for simple cases ---
    def json_default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, (set, frozenset)):
            return sorted(obj)   # convert to sorted list
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON-serialisable")

    encoded = json.dumps(order, default=json_default, indent=2)
    print("Encoded with default=:")
    print(encoded)

    # --- Method 2: JSONEncoder subclass for full control ---
    class AppEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return {"__type__": "datetime", "value": obj.isoformat()}
            if isinstance(obj, Decimal):
                return {"__type__": "Decimal", "value": str(obj)}
            return super().default(obj)

    order2 = {"total": Decimal("299.95"), "ts": datetime(2024, 6, 1, 12, 0)}
    roundtrip_str = json.dumps(order2, cls=AppEncoder, indent=2)
    print("\nEncoded with AppEncoder:")
    print(roundtrip_str)

    print()


# ---------------------------------------------------------------------------
# 4. Custom decoding — object_hook and parse_float
# ---------------------------------------------------------------------------

def demo_custom_decoding():
    print("=" * 60)
    print("Custom JSON decoding (object_hook, parse_float)")
    print("=" * 60)

    # object_hook is called for every JSON object (dict)
    def revive_types(dct: dict):
        """Reconstruct typed objects from the __type__ hint."""
        if "__type__" in dct:
            if dct["__type__"] == "datetime":
                return datetime.fromisoformat(dct["value"])
            if dct["__type__"] == "Decimal":
                return Decimal(dct["value"])
        return dct

    json_str = json.dumps({
        "price": {"__type__": "Decimal", "value": "49.99"},
        "created": {"__type__": "datetime", "value": "2024-03-15T09:30:00"},
        "name": "Widget",
    })

    recovered = json.loads(json_str, object_hook=revive_types)
    print("Recovered types:")
    print(f"  price   : {recovered['price']}  type={type(recovered['price']).__name__}")
    print(f"  created : {recovered['created']}  type={type(recovered['created']).__name__}")

    # parse_float — use Decimal instead of float for prices
    price_json = '{"price": 19.99, "tax": 0.135}'
    precise = json.loads(price_json, parse_float=Decimal)
    print(f"\nWith parse_float=Decimal:")
    print(f"  price: {precise['price']}  type={type(precise['price']).__name__}")

    print()


# ---------------------------------------------------------------------------
# 5. json with non-ASCII and separators
# ---------------------------------------------------------------------------

def demo_json_options():
    print("=" * 60)
    print("JSON options: ensure_ascii, separators")
    print("=" * 60)

    data = {"message": "こんにちは世界", "emoji": "🐍", "name": "café"}

    # ensure_ascii=True (default) — escapes non-ASCII
    ascii_str   = json.dumps(data, ensure_ascii=True)
    unicode_str = json.dumps(data, ensure_ascii=False)
    print("ensure_ascii=True: ", ascii_str)
    print("ensure_ascii=False:", unicode_str)

    # separators — remove whitespace for minimal output (useful in networking)
    compact = json.dumps({"a": 1, "b": 2, "c": [3, 4, 5]}, separators=(",", ":"))
    print("\nCompact separators:", compact)
    # {"a":1,"b":2,"c":[3,4,5]}  vs  {"a": 1, "b": 2, "c": [3, 4, 5]}

    spacious = json.dumps({"a": 1, "b": 2, "c": [3, 4, 5]}, separators=(", ", " = "))
    print("Custom separators: ", spacious)

    print()


# ===========================================================================
# CSV
# ===========================================================================

# ---------------------------------------------------------------------------
# 6. csv.reader and csv.writer
# ---------------------------------------------------------------------------

def demo_csv_reader_writer():
    print("=" * 60)
    print("csv.reader  and  csv.writer")
    print("=" * 60)

    # Write with csv.writer
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["id", "name", "price", "in_stock"])  # header
    writer.writerows([
        [1, "Laptop Pro",    999.99, True],
        [2, "Wireless Mouse", 29.99, True],
        [3, "USB-C Hub",      49.99, False],
    ])
    csv_text = buf.getvalue()
    print("Written CSV:")
    print(csv_text)

    # Read with csv.reader
    print("Read back:")
    reader = csv.reader(io.StringIO(csv_text))
    header = next(reader)
    print("  Header:", header)
    for row in reader:
        print(f"  {row}")

    print()


# ---------------------------------------------------------------------------
# 7. csv.DictReader and csv.DictWriter
# ---------------------------------------------------------------------------

def demo_csv_dict():
    print("=" * 60)
    print("csv.DictReader  and  csv.DictWriter")
    print("=" * 60)

    # DictWriter — write dicts as CSV
    fieldnames = ["name", "department", "salary", "years"]
    employees  = [
        {"name": "Alice",  "department": "Engineering", "salary": 95_000, "years": 8},
        {"name": "Bob",    "department": "Marketing",   "salary": 72_000, "years": 3},
        {"name": "Carol",  "department": "Engineering", "salary": 105_000,"years": 5},
    ]

    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)
    csv_out = buf.getvalue()
    print("DictWriter output:")
    print(csv_out)

    # DictReader — read CSV into dicts
    reader = csv.DictReader(io.StringIO(csv_out))
    print("DictReader rows:")
    for row in reader:
        # Values are always strings — convert as needed
        salary = int(row["salary"])
        years  = int(row["years"])
        bonus  = salary * 0.1 * (years / 5)
        print(f"  {row['name']:6} dept={row['department']:12} "
              f"salary=${salary:,}  bonus=${bonus:,.0f}")

    print()


# ---------------------------------------------------------------------------
# 8. Custom dialect and quoting modes
# ---------------------------------------------------------------------------

def demo_csv_dialect():
    print("=" * 60)
    print("CSV dialects and quoting modes")
    print("=" * 60)

    # Register a custom dialect
    csv.register_dialect(
        "pipe_separated",
        delimiter="|",
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",
    )

    data = [
        ["Alice Johnson", "alice@example.com", 95_000],
        ["Bob O'Reilly",  "bob@example.com",    72_000],  # apostrophe in name
    ]

    buf = io.StringIO()
    writer = csv.writer(buf, dialect="pipe_separated")
    writer.writerow(["name", "email", "salary"])
    writer.writerows(data)
    print("Pipe-delimited CSV:")
    print(buf.getvalue())

    # QUOTE_ALL — quote every field
    buf2 = io.StringIO()
    writer2 = csv.writer(buf2, quoting=csv.QUOTE_ALL)
    writer2.writerow(["a field", 42, True, None])
    print("QUOTE_ALL:", buf2.getvalue())

    # QUOTE_NONNUMERIC — quote strings, leave numbers bare
    buf3 = io.StringIO()
    writer3 = csv.writer(buf3, quoting=csv.QUOTE_NONNUMERIC)
    writer3.writerow(["a field", 42, 3.14])
    print("QUOTE_NONNUMERIC:", buf3.getvalue())

    # Parse tab-separated values (TSV)
    tsv_data = "name\tage\tcity\nAlice\t30\tNYC\nBob\t25\tLA"
    reader = csv.DictReader(io.StringIO(tsv_data), delimiter="\t")
    print("TSV parsed:")
    for row in reader:
        print(f"  {row}")

    print()


# ---------------------------------------------------------------------------
# 9. Practical patterns: data transformation pipeline
# ---------------------------------------------------------------------------

def demo_json_csv_pipeline():
    print("=" * 60)
    print("Practical: JSON API response -> CSV report")
    print("=" * 60)

    # Simulate a JSON API response
    api_json = json.dumps({
        "status": "success",
        "data": {
            "orders": [
                {"id": 101, "customer": "Alice", "items": 3, "total": 149.99, "status": "delivered"},
                {"id": 102, "customer": "Bob",   "items": 1, "total":  29.99, "status": "pending"},
                {"id": 103, "customer": "Carol", "items": 5, "total": 499.95, "status": "shipped"},
                {"id": 104, "customer": "Dave",  "items": 2, "total":  89.98, "status": "delivered"},
            ]
        }
    })

    # Step 1: Parse JSON
    response = json.loads(api_json)
    orders   = response["data"]["orders"]

    # Step 2: Filter and transform
    delivered = [
        {
            "Order ID":   f"ORD-{o['id']}",
            "Customer":   o["customer"],
            "Items":      o["items"],
            "Total ($)":  f"{o['total']:.2f}",
            "Status":     o["status"].title(),
        }
        for o in orders
        if o["status"] == "delivered"
    ]

    # Step 3: Write to CSV
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=delivered[0].keys())
    writer.writeheader()
    writer.writerows(delivered)
    print("CSV Report (delivered orders):")
    print(buf.getvalue())

    # Step 4: Summary as JSON
    summary = {
        "total_orders":     len(orders),
        "delivered_orders": len(delivered),
        "total_revenue":    round(sum(float(d["Total ($)"]) for d in delivered), 2),
        "generated_at":     datetime.now().isoformat(timespec="seconds"),
    }
    print("Summary JSON:")
    print(json.dumps(summary, indent=2))

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("JSON")
    print("=" * 60)
    demo_json_basics()
    demo_json_file()
    demo_custom_encoding()
    demo_custom_decoding()
    demo_json_options()

    print("=" * 60)
    print("CSV")
    print("=" * 60)
    demo_csv_reader_writer()
    demo_csv_dict()
    demo_csv_dialect()
    demo_json_csv_pipeline()
