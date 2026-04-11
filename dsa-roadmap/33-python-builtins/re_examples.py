"""
re — Regular expressions for pattern matching, searching, and text manipulation.

Covered here:
  Compilation flags  — re.IGNORECASE, MULTILINE, DOTALL, VERBOSE, ASCII
  Search functions   — match, search, fullmatch, findall, finditer
  Substitution       — sub, subn
  Splitting          — split
  Groups             — capturing groups, named groups, non-capturing groups
  Lookahead/behind   — positive/negative lookahead and lookbehind
  Compiled patterns  — re.compile for reuse
  Common patterns    — email, URL, phone, IP address, date, identifier
  String extraction  — pulling structured fields from unstructured text
"""

import re


# ---------------------------------------------------------------------------
# 1. match vs search vs fullmatch
# ---------------------------------------------------------------------------

def demo_match_search_fullmatch():
    print("=" * 60)
    print("match vs search vs fullmatch")
    print("=" * 60)

    text = "Error 404: Page not found at /products"

    # match — must match at the BEGINNING of the string
    m = re.match(r"Error", text)
    print(f"match('Error'):     {'found' if m else 'NO match'}")   # found

    m = re.match(r"404", text)
    print(f"match('404'):       {'found' if m else 'NO match'}")   # NO match (not at start)

    # search — finds the FIRST match anywhere in the string
    m = re.search(r"404", text)
    print(f"search('404'):      {m.group() if m else 'NO match'}")  # 404

    m = re.search(r"\d+", text)
    print(f"search(digits):     {m.group() if m else 'NO match'}")  # 404

    # fullmatch — the ENTIRE string must match
    m = re.fullmatch(r"\d{3}-\d{4}", "555-1234")
    print(f"\nfullmatch phone:    {'valid' if m else 'invalid'}")    # valid

    m = re.fullmatch(r"\d{3}-\d{4}", "555-12345")
    print(f"fullmatch (extra digit): {'valid' if m else 'invalid'}") # invalid

    print()


# ---------------------------------------------------------------------------
# 2. findall and finditer
# ---------------------------------------------------------------------------

def demo_findall_finditer():
    print("=" * 60)
    print("findall and finditer")
    print("=" * 60)

    log = """
    2024-01-15 08:32:11 INFO  User alice logged in from 192.168.1.10
    2024-01-15 08:33:05 ERROR DB connection failed  (attempt 1 of 3)
    2024-01-15 08:33:47 WARN  Memory at 87%
    2024-01-15 08:34:21 INFO  User bob logged in from 10.0.0.45
    2024-01-15 08:35:00 ERROR Timeout after 30s
    """

    # findall — returns a list of strings (or tuples if groups)
    timestamps = re.findall(r"\d{2}:\d{2}:\d{2}", log)
    print("Timestamps:", timestamps)
    # ['08:32:11', '08:33:05', '08:33:47', '08:34:21', '08:35:00']

    error_lines = re.findall(r"ERROR.*", log)
    print("\nError lines:")
    for line in error_lines:
        print(" ", line.strip())

    ip_addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", log)
    print("\nIP addresses found:", ip_addresses)
    # ['192.168.1.10', '10.0.0.45']

    # finditer — returns an iterator of match objects (use for position info)
    print("\nAll numbers and their positions:")
    for m in re.finditer(r"\d+", log):
        print(f"  '{m.group():>4}'  span={m.span()}")

    print()


# ---------------------------------------------------------------------------
# 3. Capturing groups
# ---------------------------------------------------------------------------

def demo_groups():
    print("=" * 60)
    print("Groups: capturing, named, non-capturing")
    print("=" * 60)

    # Positional groups — numbered from left to right
    log_line = "2024-01-15 08:32:11 INFO  User alice logged in"
    pattern  = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+)"

    m = re.match(pattern, log_line)
    if m:
        print("Full match:", m.group(0))
        print("Date:      ", m.group(1))   # 2024-01-15
        print("Time:      ", m.group(2))   # 08:32:11
        print("Level:     ", m.group(3))   # INFO
        print("All groups:", m.groups())

    # Named groups — (?P<name>pattern)
    named_pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+)"
    m = re.match(named_pattern, log_line)
    if m:
        print("\nNamed groups:")
        print("  date  =", m.group("date"))
        print("  time  =", m.group("time"))
        print("  level =", m.group("level"))
        print("  dict  =", m.groupdict())

    # Non-capturing group — (?:pattern) — group without saving
    text = "cat concatenate scatter"
    cats = re.findall(r"(?:cat)(\w*)", text)
    print("\nWords containing 'cat' (suffix only):", cats)
    # ['', 'concatenate', 'ter']  — only the suffix is captured

    # findall with multiple groups returns list of tuples
    csv_line = "Alice,30,Engineer,London"
    fields = re.findall(r"([^,]+)", csv_line)
    print("\nCSV fields:", fields)

    print()


# ---------------------------------------------------------------------------
# 4. Named groups in multi-record extraction
# ---------------------------------------------------------------------------

def demo_structured_extraction():
    print("=" * 60)
    print("Structured extraction with named groups")
    print("=" * 60)

    access_log = """
    GET /api/users/42     200  0.045s  alice
    POST /api/orders      201  0.312s  bob
    GET /api/products/1   404  0.012s  carol
    DELETE /api/users/7   403  0.018s  alice
    GET /api/orders/99    200  0.089s  dave
    """

    pattern = re.compile(
        r"(?P<method>GET|POST|PUT|DELETE|PATCH)\s+"
        r"(?P<path>/\S+)\s+"
        r"(?P<status>\d{3})\s+"
        r"(?P<duration>\d+\.\d+)s\s+"
        r"(?P<user>\w+)"
    )

    records = []
    for m in pattern.finditer(access_log):
        records.append(m.groupdict())

    print("Parsed access log:")
    for r in records:
        print(f"  {r['method']:6} {r['path']:20} {r['status']}  {r['duration']}s  ({r['user']})")

    # Analytics using the extracted data
    errors = [r for r in records if r["status"].startswith("4")]
    print(f"\n4xx errors: {len(errors)}")
    for e in errors:
        print(f"  {e['user']:6} -> {e['method']} {e['path']} {e['status']}")

    slow = [r for r in records if float(r["duration"]) > 0.1]
    print(f"\nSlow requests (>100ms): {[r['path'] for r in slow]}")

    print()


# ---------------------------------------------------------------------------
# 5. sub and subn — find and replace
# ---------------------------------------------------------------------------

def demo_sub():
    print("=" * 60)
    print("sub and subn — substitution")
    print("=" * 60)

    # Basic replacement
    text = "Hello World, hello Python, HELLO everyone"
    result = re.sub(r"hello", "Hi", text, flags=re.IGNORECASE)
    print("sub (case-insensitive):", result)
    # Hi World, Hi Python, Hi everyone

    # subn also returns the count of substitutions
    result, count = re.subn(r"\b\d+\b", "###", "Call 555-1234 or 800-5678 ref #42")
    print(f"subn — replaced {count} numbers: {result}")
    # Call ###-### or ###-### ref #42

    # Back-references — \1, \2 etc. reference captured groups in the replacement
    # Swap first and last name
    names = "Smith, John\nDoe, Jane\nJohnson, Bob"
    swapped = re.sub(r"(\w+), (\w+)", r"\2 \1", names)
    print("\nSwapped names (Last, First -> First Last):")
    print(swapped)
    # John Smith
    # Jane Doe
    # Bob Johnson

    # Replacement with a function
    def mask_phone(m: re.Match) -> str:
        """Mask all but last 4 digits."""
        digits = re.sub(r"\D", "", m.group())
        return "***-***-" + digits[-4:]

    phone_text = "Contact us at 555-867-5309 or (800) 555-0199"
    masked = re.sub(r"\(?\d{3}\)?[\s\-]\d{3}[\s\-]\d{4}", mask_phone, phone_text)
    print("\nMasked phones:", masked)

    # Redact PII — email addresses
    content = "Email alice@example.com or bob.smith@company.org for support"
    redacted = re.sub(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", "[EMAIL REDACTED]", content)
    print("Redacted:", redacted)

    print()


# ---------------------------------------------------------------------------
# 6. split — divide a string by a pattern
# ---------------------------------------------------------------------------

def demo_split():
    print("=" * 60)
    print("re.split — split by pattern")
    print("=" * 60)

    # Split on multiple delimiters (comma, semicolon, or whitespace runs)
    data = "Alice, Bob; Carol  Dave,Eve"
    parts = re.split(r"[,;\s]+", data)
    print("Split by [,;\\s]+:", parts)
    # ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

    # Split and keep delimiters (by wrapping in a group)
    sentence = "first,second;third  fourth"
    tokens = re.split(r"([,;\s]+)", sentence)
    print("Split (keep delimiters):", tokens)

    # Parse a CSV-like line  (handles quoted fields is limited — use csv module for real CSV)
    line = "2024-01-15|New York|John Smith|$1,200.00"
    fields = re.split(r"\|", line)
    print("\nPipe-delimited:", fields)

    # Split camelCase into words
    camel = "getUserProfileByIdAndEmail"
    words = re.sub(r"([A-Z])", r" \1", camel).strip().split()
    print(f"\nCamelCase split: {words}")
    # ['get', 'User', 'Profile', 'By', 'Id', 'And', 'Email']

    print()


# ---------------------------------------------------------------------------
# 7. Lookahead and lookbehind
# ---------------------------------------------------------------------------

def demo_lookaround():
    print("=" * 60)
    print("Lookahead and lookbehind assertions")
    print("=" * 60)

    # Positive lookahead (?=...)  — match X followed by Y (Y not consumed)
    text = "100px 200em 50% 300rem 42"
    only_px = re.findall(r"\d+(?=px)", text)
    print("Numbers before 'px':", only_px)   # ['100']

    only_units = re.findall(r"\d+(?=px|em|rem|%)", text)
    print("Numbers with units:", only_units)  # ['100', '200', '50', '300']

    # Negative lookahead (?!...)  — match X NOT followed by Y
    plain_numbers = re.findall(r"\d+(?!px|em|rem|%|\d)", text)
    print("Plain numbers (no unit):", plain_numbers)   # ['42']

    # Positive lookbehind (?<=...)  — match Y preceded by X (X not consumed)
    prices = "Price: $50.00, Discount: $10.50, Tax: $3.75"
    values = re.findall(r"(?<=\$)\d+\.\d+", prices)
    print("\nPrices after '$':", values)   # ['50.00', '10.50', '3.75']

    # Negative lookbehind (?<!...)
    text2 = "node_id vs node id2 vs node123"
    # Find 'node' not followed by underscore or digit
    matches = re.findall(r"node(?!_)(?!\d)", text2)
    print("'node' without _/digit suffix:", len(matches), "matches")

    # Password validation with lookaheads
    def validate_password(pw: str) -> list:
        errors = []
        if not re.search(r"(?=.*[A-Z])", pw):
            errors.append("needs uppercase")
        if not re.search(r"(?=.*[a-z])", pw):
            errors.append("needs lowercase")
        if not re.search(r"(?=.*\d)", pw):
            errors.append("needs digit")
        if not re.search(r"(?=.*[!@#$%^&*])", pw):
            errors.append("needs special char")
        if len(pw) < 8:
            errors.append("too short")
        return errors or ["valid"]

    for pw in ["abc", "Password1", "P@ssw0rd!", "weakPassw0rd"]:
        print(f"  {pw!r:20} -> {validate_password(pw)}")

    print()


# ---------------------------------------------------------------------------
# 8. Compiled patterns and flags
# ---------------------------------------------------------------------------

def demo_compile_and_flags():
    print("=" * 60)
    print("Compiled patterns and flags")
    print("=" * 60)

    # re.compile — compile once, use many times (faster in loops)
    email_re = re.compile(
        r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}",
        flags=re.IGNORECASE
    )

    texts = [
        "Contact: alice@Example.COM",
        "No email here",
        "Support: help@COMPANY.org and billing@company.org",
    ]
    for text in texts:
        emails = email_re.findall(text)
        print(f"  {text!r:45} -> {emails}")

    # MULTILINE — ^ and $ match start/end of each LINE (not just the whole string)
    data = "first line\nsecond line\nthird line"
    # Without MULTILINE, ^ only matches start of entire string
    print("\nWith MULTILINE:")
    for m in re.finditer(r"^\w+", data, flags=re.MULTILINE):
        print(f"  First word of line: {m.group()!r}")

    # DOTALL — . also matches newline
    html = "<div>\n  <p>Hello</p>\n</div>"
    m = re.search(r"<div>(.+)</div>", html, flags=re.DOTALL)
    if m:
        print(f"\nDOTALL captured:\n{m.group(1)}")

    # VERBOSE — add whitespace and comments for readability
    date_re = re.compile(r"""
        (?P<year>  \d{4})   # four-digit year
        [-/]                # separator (dash or slash)
        (?P<month> \d{1,2}) # one or two digit month
        [-/]                # separator
        (?P<day>   \d{1,2}) # one or two digit day
    """, re.VERBOSE)

    for date_str in ["2024-01-15", "2024/3/5", "2024-12-31"]:
        m = date_re.match(date_str)
        if m:
            print(f"\n{date_str} -> year={m.group('year')}, "
                  f"month={m.group('month'):0>2}, day={m.group('day'):0>2}")

    print()


# ---------------------------------------------------------------------------
# 9. Common real-world patterns
# ---------------------------------------------------------------------------

def demo_common_patterns():
    print("=" * 60)
    print("Common real-world patterns")
    print("=" * 60)

    PATTERNS = {
        "email":      re.compile(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}"),
        "url":        re.compile(r"https?://[\w\-._~:/?#\[\]@!$&'()*+,;=%]+"),
        "phone_us":   re.compile(r"\(?\d{3}\)?[\s.\-]\d{3}[\s.\-]\d{4}"),
        "ipv4":       re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
        "hex_color":  re.compile(r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"),
        "iso_date":   re.compile(r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])"),
        "slug":       re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$"),
        "semver":     re.compile(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?"),
        "jwt":        re.compile(r"eyJ[A-Za-z0-9\-_]+\.eyJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_.+/]*"),
        "credit_card":re.compile(r"\b(?:\d[ \-]?){13,16}\b"),
    }

    test_inputs = {
        "email":       "Send to alice@example.com and bob+test@co.uk",
        "url":         "Visit https://docs.python.org/3/library/re.html for more",
        "phone_us":    "Call (555) 867-5309 or 800.555.0199",
        "ipv4":        "Server at 192.168.1.1 and gateway 10.0.0.1",
        "hex_color":   "Colors: #fff #1a2b3c #ABC #FFD700",
        "iso_date":    "Events on 2024-01-15 and 2024-12-31",
        "slug":        "my-awesome-blog-post",
        "semver":      "Requires version 3.11.0 or 3.12.1-beta",
    }

    for name, text in test_inputs.items():
        pattern = PATTERNS[name]
        found = pattern.findall(text)
        is_match = bool(pattern.fullmatch(text)) if name == "slug" else None
        suffix = f" -> fullmatch={is_match}" if is_match is not None else ""
        print(f"  {name:12} found={found}{suffix}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_match_search_fullmatch()
    demo_findall_finditer()
    demo_groups()
    demo_structured_extraction()
    demo_sub()
    demo_split()
    demo_lookaround()
    demo_compile_and_flags()
    demo_common_patterns()
