"""
string  — String constants, Template, Formatter.
textwrap — Wrap, indent, dedent, and shorten text.
pprint   — Pretty-print nested data structures.

string covered:
  Constants   — ascii_letters, ascii_lowercase, ascii_uppercase,
                digits, hexdigits, octdigits, punctuation, whitespace, printable
  Template    — $variable substitution with safe_substitute
  Formatter   — custom format string handling (advanced)
  capwords    — capitalise words (like title() but handles consecutive whitespace)

textwrap covered:
  wrap()      — wrap text into lines of a given width (returns list)
  fill()      — wrap + join (returns string)
  shorten()   — truncate to a width, adding placeholder
  dedent()    — remove common leading whitespace
  indent()    — add prefix to every line (or selective lines)
  TextWrapper — reusable object with custom settings

pprint covered:
  pprint()    — pretty-print with indentation
  pformat()   — return as string (don't print)
  PrettyPrinter — reusable with custom indent/width/depth
  pp()        — compact shorthand (Python 3.8+)
"""

import string
import textwrap
from pprint import pprint, pformat, PrettyPrinter


# ---------------------------------------------------------------------------
# 1. string constants — character sets used in DSA and data validation
# ---------------------------------------------------------------------------

def demo_string_constants():
    print("=" * 60)
    print("string constants")
    print("=" * 60)

    print("ascii_lowercase: ", string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
    print("ascii_uppercase: ", string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print("ascii_letters:   ", string.ascii_letters[:20], "...")
    print("digits:          ", string.digits)            # 0123456789
    print("hexdigits:       ", string.hexdigits)         # 0123456789abcdefABCDEF
    print("octdigits:       ", string.octdigits)         # 01234567
    print("punctuation:     ", string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    print("whitespace repr: ", repr(string.whitespace))  # ' \t\n\r\x0b\x0c'

    # DSA use-case: valid identifier characters
    IDENT_CHARS = string.ascii_letters + string.digits + "_"
    def is_valid_identifier(s: str) -> bool:
        return bool(s) and s[0].isalpha() and all(c in IDENT_CHARS for c in s)

    for test in ["my_var", "_ok", "2bad", "has space", "valid123"]:
        print(f"  {test!r:12} valid identifier: {is_valid_identifier(test)}")

    # Count vowels / consonants using set membership
    vowels = set("aeiouAEIOU")
    text   = "Hello World from Python"
    v_count = sum(1 for c in text if c in vowels)
    c_count = sum(1 for c in text if c.isalpha() and c not in vowels)
    print(f"\n'{text}'  vowels={v_count}  consonants={c_count}")

    # Build alphabet frequency map
    sample = "the quick brown fox jumps over the lazy dog"
    freq = {letter: sample.count(letter) for letter in string.ascii_lowercase}
    top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Top 5 letters in pangram:", top5)

    print()


# ---------------------------------------------------------------------------
# 2. string.Template — safe variable substitution
# ---------------------------------------------------------------------------

def demo_template():
    print("=" * 60)
    print("string.Template")
    print("=" * 60)

    # --- 2a: basic substitution ---
    tmpl = string.Template("Hello, $name! You have $count new messages.")
    result = tmpl.substitute(name="Alice", count=5)
    print(result)

    # substitute() raises KeyError if a variable is missing
    try:
        tmpl.substitute(name="Bob")   # missing 'count'
    except KeyError as e:
        print(f"Missing key: {e}")

    # safe_substitute() leaves missing placeholders intact
    partial = tmpl.safe_substitute(name="Bob")
    print(f"safe_substitute with missing 'count': {partial!r}")

    # --- 2b: HTML email template ---
    email_tmpl = string.Template("""
Subject: Order Confirmation #$order_id
Dear $customer_name,

Your order for $item_count item(s) totalling $$$total has been confirmed.
Expected delivery: $delivery_date

Thank you for shopping with us!
""".strip())

    email = email_tmpl.substitute(
        order_id="ORD-2024-001",
        customer_name="Alice Johnson",
        item_count=3,
        total="149.99",
        delivery_date="March 20, 2024",
    )
    print("\nEmail:")
    print(email)

    # --- 2c: SQL template (use parameterised queries for real SQL!) ---
    # Template is safe for non-SQL uses like generating config files, reports
    cfg_tmpl = string.Template("""
[database]
host     = $host
port     = $port
name     = $db_name

[cache]
ttl      = $cache_ttl
max_size = $max_size
""".strip())

    cfg = cfg_tmpl.substitute(
        host="db.prod.example.com", port=5432, db_name="ecommerce",
        cache_ttl=300, max_size=1000
    )
    print("\nGenerated config:")
    print(cfg)

    print()


# ---------------------------------------------------------------------------
# 3. string.capwords and Formatter
# ---------------------------------------------------------------------------

def demo_capwords_formatter():
    print("=" * 60)
    print("string.capwords and Formatter")
    print("=" * 60)

    # capwords is like title() but handles multiple spaces correctly
    s1 = "hello world  from   python"
    print(f"title():    {s1.title()!r}")       # double spaces preserved with extra caps
    print(f"capwords(): {string.capwords(s1)!r}")  # collapses whitespace first

    # With a custom separator
    s2 = "hello-world-from-python"
    print(f"capwords('-'): {string.capwords(s2, '-')!r}")  # Hello-World-From-Python

    # Custom Formatter subclass
    class ThousandsFormatter(string.Formatter):
        """Format numbers with thousands separators."""

        def format_field(self, value, format_spec):
            if isinstance(value, (int, float)) and not format_spec:
                return f"{value:,}"
            return super().format_field(value, format_spec)

    fmt = ThousandsFormatter()
    print("\nCustom Formatter:")
    print(fmt.format("Revenue: {revenue}  Users: {users}",
                     revenue=1_234_567.89, users=98_765))

    print()


# ---------------------------------------------------------------------------
# 4. textwrap — wrap, fill, shorten, dedent, indent
# ---------------------------------------------------------------------------

def demo_textwrap():
    print("=" * 60)
    print("textwrap")
    print("=" * 60)

    long_text = (
        "Python is a high-level, general-purpose programming language. "
        "Its design philosophy emphasises code readability with the use of "
        "significant indentation. Python is dynamically typed and garbage-collected. "
        "It supports multiple programming paradigms, including structured, "
        "object-oriented, and functional programming."
    )

    # wrap — returns a list of lines at most `width` characters wide
    lines = textwrap.wrap(long_text, width=60)
    print("textwrap.wrap(width=60):")
    for line in lines:
        print(f"  |{line}|")

    # fill — wrap + join into a single string
    filled = textwrap.fill(long_text, width=60)
    print(f"\ntextwrap.fill(width=60):\n{filled}")

    # shorten — truncate with a placeholder
    short = textwrap.shorten(long_text, width=80, placeholder=" [...]")
    print(f"\ntextwrap.shorten(80): {short!r}")

    # fill with initial_indent and subsequent_indent
    indented = textwrap.fill(
        long_text, width=70,
        initial_indent="   > ",       # first line
        subsequent_indent="     ",    # rest
    )
    print(f"\nWith indents:\n{indented}")

    print()


# ---------------------------------------------------------------------------
# 5. dedent and indent
# ---------------------------------------------------------------------------

def demo_dedent_indent():
    print("=" * 60)
    print("dedent and indent")
    print("=" * 60)

    # dedent — remove common leading whitespace (essential for docstrings)
    raw_code = """
        def greet(name):
            print(f"Hello, {name}!")
            return True
    """
    clean = textwrap.dedent(raw_code).strip()
    print("After dedent:")
    print(clean)

    # indent — add prefix to lines
    code_block = "value = 42\nprint(value)\nreturn value"
    indented = textwrap.indent(code_block, "    ")   # 4 spaces
    print(f"\nAfter indent(4 spaces):\n{indented}")

    # indent with a predicate — only indent non-empty lines
    mixed = "line 1\n\nline 2\n   \nline 3"
    selective = textwrap.indent(mixed, ">>> ", predicate=lambda l: l.strip())
    print(f"\nSelective indent (non-empty only):\n{selective}")

    # Practical: generate Python code as a string
    def generate_class(name: str, fields: list[tuple[str, str]]) -> str:
        lines = [f"class {name}:"]
        init_args = ", ".join(f"{f}: {t}" for f, t in fields)
        lines.append(f"    def __init__(self, {init_args}):")
        for f, _ in fields:
            lines.append(f"        self.{f} = {f}")
        return "\n".join(lines)

    code = generate_class("Point", [("x", "float"), ("y", "float"), ("z", "float")])
    print(f"\nGenerated class:\n{code}")

    print()


# ---------------------------------------------------------------------------
# 6. pprint — pretty-print nested structures
# ---------------------------------------------------------------------------

def demo_pprint():
    print("=" * 60)
    print("pprint — pretty-print nested structures")
    print("=" * 60)

    nested_data = {
        "users": [
            {"id": 1, "name": "Alice", "roles": ["admin", "editor"],
             "address": {"city": "New York", "zip": "10001", "country": "US"}},
            {"id": 2, "name": "Bob", "roles": ["viewer"],
             "address": {"city": "Los Angeles", "zip": "90001", "country": "US"}},
        ],
        "config": {
            "max_connections": 100,
            "timeout": 30,
            "features": {"dark_mode": True, "beta": False, "v2_api": True},
        },
        "stats": {"total_users": 2, "active": 2, "inactive": 0},
    }

    print("Default pprint (width=80):")
    pprint(nested_data)

    # pformat — get the pretty string without printing
    pretty_str = pformat(nested_data, indent=2, width=60)
    print(f"\npformat (width=60):\n{pretty_str}")

    # depth — only show top N levels
    print("\nDepth=1 (top-level keys only):")
    pprint(nested_data, depth=1)

    print("\nDepth=2:")
    pprint(nested_data, depth=2)

    # PrettyPrinter — reusable with custom settings
    pp = PrettyPrinter(indent=4, width=60, sort_dicts=False)
    print("\nCustom PrettyPrinter (indent=4, no sort):")
    pp.pprint({"z": 1, "a": 2, "m": 3})  # keys in insertion order

    # Practical: log a complex API response
    api_response = {
        "status": 200,
        "data": {
            "products": [
                {"sku": "PROD-001", "name": "Laptop Pro 15", "price": 1299.99,
                 "inventory": {"warehouse_a": 50, "warehouse_b": 30},
                 "tags": ["electronics", "computers", "featured"]},
                {"sku": "PROD-002", "name": "Wireless Mouse", "price": 29.99,
                 "inventory": {"warehouse_a": 200, "warehouse_b": 150},
                 "tags": ["accessories", "bestseller"]},
            ],
            "pagination": {"page": 1, "per_page": 20, "total": 2, "pages": 1},
        },
        "timestamp": "2024-01-15T08:32:11Z",
    }

    print("\nAPI Response (pretty-printed):")
    pprint(api_response, indent=2)

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_string_constants()
    demo_template()
    demo_capwords_formatter()
    demo_textwrap()
    demo_dedent_indent()
    demo_pprint()
