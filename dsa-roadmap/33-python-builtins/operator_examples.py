"""
operator — Standard operators as callable functions.

Python's operator module exposes every built-in operator as a first-class
callable.  This matters because:
  - It is faster than an equivalent lambda at runtime (implemented in C).
  - It is more readable in functional pipelines.
  - It is picklable (lambdas are not).

Covered here:
  Arithmetic operators   — add, sub, mul, truediv, floordiv, mod, pow, neg, abs, pos
  Comparison operators   — eq, ne, lt, le, gt, ge
  Logical / bitwise      — and_, or_, xor, not_, truth, inv, lshift, rshift
  Sequence operators     — getitem, setitem, delitem, contains, indexOf, countOf
  In-place operators     — iadd, imul, isub, ...
  Access helpers         — attrgetter, itemgetter, methodcaller (advanced usage)
  Practical pipelines    — map/filter with operators, compose with reduce
"""

import operator
from functools import reduce


# ---------------------------------------------------------------------------
# 1. Arithmetic operators
# ---------------------------------------------------------------------------

def demo_arithmetic():
    print("=" * 60)
    print("Arithmetic operators")
    print("=" * 60)

    a, b = 17, 5

    print(f"add({a}, {b})       =", operator.add(a, b))        # 22
    print(f"sub({a}, {b})       =", operator.sub(a, b))        # 12
    print(f"mul({a}, {b})       =", operator.mul(a, b))        # 85
    print(f"truediv({a}, {b})   =", operator.truediv(a, b))    # 3.4
    print(f"floordiv({a}, {b})  =", operator.floordiv(a, b))   # 3
    print(f"mod({a}, {b})       =", operator.mod(a, b))        # 2
    print(f"pow({a}, {b})       =", operator.pow(a, b))        # 1419857
    print(f"neg({a})            =", operator.neg(a))           # -17
    print(f"abs(-{a})           =", operator.abs(-a))          # 17
    print(f"pos(-{a})           =", operator.pos(-a))          # -17 (identity)

    # operator + reduce — more legible than nested lambdas
    nums = [2, 3, 4, 5]
    product  = reduce(operator.mul, nums, 1)
    total    = reduce(operator.add, nums, 0)
    print(f"\nreduce(mul, {nums}) = {product}")        # 120
    print(f"reduce(add, {nums}) = {total}")           # 14

    # operator + map — sum of squares
    squares_sum = sum(map(operator.mul, nums, nums))   # element-wise multiply
    print(f"sum of squares {nums}: {squares_sum}")    # 4+9+16+25 = 54

    print()


# ---------------------------------------------------------------------------
# 2. Comparison operators
# ---------------------------------------------------------------------------

def demo_comparison():
    print("=" * 60)
    print("Comparison operators")
    print("=" * 60)

    pairs = [(1, 2), (5, 5), (9, 3)]
    ops = [
        ("eq", operator.eq),
        ("ne", operator.ne),
        ("lt", operator.lt),
        ("le", operator.le),
        ("gt", operator.gt),
        ("ge", operator.ge),
    ]

    print(f"{'Pair':>10}  {'eq':>5} {'ne':>5} {'lt':>5} {'le':>5} {'gt':>5} {'ge':>5}")
    for a, b in pairs:
        results = [str(fn(a, b)) for _, fn in ops]
        print(f"({a}, {b}){' ':>5}  {'  '.join(f'{r:>5}' for r in results)}")

    # Real use case: filter items using an operator function
    threshold = 300
    prices = [150, 499, 299, 700, 280, 350]
    above = list(filter(lambda p: operator.gt(p, threshold), prices))
    below = list(filter(lambda p: operator.le(p, threshold), prices))
    print(f"\nPrices above ${threshold}: {above}")
    print(f"Prices at or below ${threshold}: {below}")

    # Sort stability check: use operator.eq to find duplicates
    items = [4, 2, 7, 2, 9, 4, 4]
    duplicates = [x for i, x in enumerate(items)
                  if any(operator.eq(x, items[j]) for j in range(i))]
    print("Duplicates:", sorted(set(duplicates)))   # [2, 4]

    print()


# ---------------------------------------------------------------------------
# 3. Logical and bitwise operators
# ---------------------------------------------------------------------------

def demo_logical_bitwise():
    print("=" * 60)
    print("Logical and bitwise operators")
    print("=" * 60)

    # Logical (work on truthy/falsy values)
    print("not_(True) =", operator.not_(True))    # False
    print("not_(0)    =", operator.not_(0))        # True
    print("truth([])  =", operator.truth([]))      # False
    print("truth([1]) =", operator.truth([1]))     # True

    # and_ / or_ short-circuit like Python's and / or
    print("and_(1, 2) =", operator.and_(1, 2))    # 0  (bitwise AND)
    print("or_(1, 2)  =", operator.or_(1, 2))     # 3  (bitwise OR)
    print("xor(1, 3)  =", operator.xor(1, 3))     # 2

    # Bitwise shift and invert
    print("lshift(1, 4) =", operator.lshift(1, 4))  # 16  (1 << 4)
    print("rshift(16,2) =", operator.rshift(16, 2)) # 4   (16 >> 2)
    print("inv(5)       =", operator.inv(5))         # -6  (bitwise NOT)

    # Practical: use reduce + or_ to combine bit flags
    # Permissions: READ=1, WRITE=2, EXEC=4
    READ, WRITE, EXEC = 1, 2, 4
    permissions = [READ, WRITE]
    combined = reduce(operator.or_, permissions)
    print(f"\nCombined permissions {permissions} -> {combined:03b} (binary) = {combined}")
    # 011 = 3

    has_exec  = operator.truth(combined & EXEC)
    has_write = operator.truth(combined & WRITE)
    print(f"Has EXEC:  {has_exec}")    # False
    print(f"Has WRITE: {has_write}")   # True

    print()


# ---------------------------------------------------------------------------
# 4. Sequence operators — getitem, setitem, delitem, contains, indexOf, countOf
# ---------------------------------------------------------------------------

def demo_sequence_ops():
    print("=" * 60)
    print("Sequence operators")
    print("=" * 60)

    # --- getitem / setitem / delitem ---
    data = [10, 20, 30, 40, 50]
    print("getitem(data, 2):", operator.getitem(data, 2))   # 30
    print("getitem(data, slice(1,4)):", operator.getitem(data, slice(1, 4)))  # [20,30,40]

    operator.setitem(data, 2, 99)
    print("After setitem(data,2,99):", data)   # [10,20,99,40,50]

    operator.delitem(data, 0)
    print("After delitem(data,0):  ", data)    # [20,99,40,50]

    # --- contains, indexOf, countOf ---
    inventory = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print("\ncontains 'apple':", operator.contains(inventory, "apple"))  # True
    print("contains 'mango':", operator.contains(inventory, "mango"))    # False
    print("indexOf 'cherry':", operator.indexOf(inventory, "cherry"))    # 3
    print("countOf 'apple': ", operator.countOf(inventory, "apple"))     # 3
    print("countOf 'mango': ", operator.countOf(inventory, "mango"))     # 0

    # --- dict operators ---
    record = {"id": 1, "name": "Alice", "score": 95}
    print("\ngetitem dict:", operator.getitem(record, "name"))   # Alice

    operator.setitem(record, "score", 100)
    print("After setitem score=100:", record)

    operator.delitem(record, "id")
    print("After delitem id:       ", record)

    # --- concat (+ for sequences) ---
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("\nconcat:", operator.concat(a, b))   # [1,2,3,4,5,6]
    print("concat:", operator.concat("Hello, ", "World!"))  # Hello, World!

    print()


# ---------------------------------------------------------------------------
# 5. In-place operators (iadd, imul, etc.)
# ---------------------------------------------------------------------------

def demo_inplace():
    print("=" * 60)
    print("In-place operators  (iadd, imul, isub, …)")
    print("=" * 60)

    # For immutables (int, str) these behave like the regular operators
    # For mutables (list, dict) they modify in place
    x = 10
    x = operator.iadd(x, 5)
    print("iadd(10, 5):", x)   # 15

    x = operator.imul(x, 3)
    print("imul(15, 3):", x)   # 45

    x = operator.isub(x, 10)
    print("isub(45,10):", x)   # 35

    x = operator.itruediv(x, 7)
    print("itruediv(35,7):", x)  # 5.0

    # List in-place (actually mutates the list object)
    lst = [1, 2, 3]
    operator.iadd(lst, [4, 5])
    print("iadd list:", lst)   # [1,2,3,4,5]  — mutated in place

    operator.imul(lst, 2)
    print("imul list:", lst)   # [1,2,3,4,5,1,2,3,4,5]

    # Bitwise in-place
    flags = 0b1010
    flags = operator.ior(flags, 0b0101)
    print(f"ior(1010, 0101) = {flags:04b}")   # 1111

    flags = operator.iand(flags, 0b1100)
    print(f"iand(1111, 1100) = {flags:04b}")  # 1100

    print()


# ---------------------------------------------------------------------------
# 6. itemgetter — extract multiple fields at once
# ---------------------------------------------------------------------------

def demo_itemgetter():
    print("=" * 60)
    print("itemgetter  (multiple fields, dict and tuple)")
    print("=" * 60)

    records = [
        {"name": "Alice", "dept": "Eng",  "salary": 95_000, "years": 8},
        {"name": "Bob",   "dept": "Mkt",  "salary": 72_000, "years": 3},
        {"name": "Carol", "dept": "Eng",  "salary": 105_000,"years": 5},
        {"name": "Dave",  "dept": "HR",   "salary": 80_000, "years": 7},
    ]

    # Extract a single field
    get_name   = operator.itemgetter("name")
    get_salary = operator.itemgetter("salary")

    names   = list(map(get_name, records))
    salaries = list(map(get_salary, records))
    print("Names:   ", names)
    print("Salaries:", salaries)

    # Extract multiple fields at once -> returns a tuple
    get_name_dept = operator.itemgetter("name", "dept")
    print("\nName + dept combos:")
    for combo in map(get_name_dept, records):
        print(" ", combo)

    # Sort by multiple fields (more readable than nested lambda)
    by_dept_salary = sorted(records, key=operator.itemgetter("dept", "salary"))
    print("\nSorted by dept, then salary:")
    for r in by_dept_salary:
        print(f"  {r['dept']:4}  {r['name']:6}  ${r['salary']:,}")

    # Tuple records
    transactions = [
        ("2024-01-15", "Alice", 250.00),
        ("2024-01-15", "Bob",   175.50),
        ("2024-01-16", "Alice", 320.00),
        ("2024-01-16", "Carol", 90.00),
    ]
    get_amount = operator.itemgetter(2)
    amounts    = list(map(get_amount, transactions))
    print("\nTransaction amounts:", amounts)   # [250.0, 175.5, 320.0, 90.0]

    total = reduce(operator.add, amounts)
    print("Total:", total)   # 835.5

    print()


# ---------------------------------------------------------------------------
# 7. attrgetter and methodcaller
# ---------------------------------------------------------------------------

def demo_attrgetter_methodcaller():
    print("=" * 60)
    print("attrgetter  /  methodcaller")
    print("=" * 60)

    class Student:
        def __init__(self, name, gpa, major):
            self.name  = name
            self.gpa   = gpa
            self.major = major

        def honour_roll(self) -> bool:
            return self.gpa >= 3.7

        def grade_label(self) -> str:
            if self.gpa >= 3.7: return "Honours"
            if self.gpa >= 3.0: return "Good Standing"
            return "At Risk"

        def __repr__(self):
            return f"Student({self.name}, gpa={self.gpa})"

    students = [
        Student("Alice",  3.9, "CS"),
        Student("Bob",    3.2, "Math"),
        Student("Carol",  3.7, "CS"),
        Student("Dave",   2.8, "Physics"),
        Student("Eve",    3.5, "CS"),
    ]

    # attrgetter — sort by GPA descending
    by_gpa = sorted(students, key=operator.attrgetter("gpa"), reverse=True)
    print("By GPA desc:    ", by_gpa)

    # attrgetter — extract all GPAs
    get_gpa = operator.attrgetter("gpa")
    gpas = list(map(get_gpa, students))
    print("GPAs:            ", gpas)
    print("Average GPA:    ", sum(gpas) / len(gpas))

    # attrgetter — sort by major then gpa
    by_major_gpa = sorted(students, key=operator.attrgetter("major", "gpa"))
    print("By major then GPA:")
    for s in by_major_gpa:
        print(f"  {s.major:8} {s.name:6} gpa={s.gpa}")

    # methodcaller — call a method on each object
    on_honours = operator.methodcaller("honour_roll")
    honours_students = list(filter(on_honours, students))
    print("\nHonour roll students:", honours_students)

    # methodcaller with arguments — call method with a specific arg
    get_label = operator.methodcaller("grade_label")
    labels = {s.name: get_label(s) for s in students}
    print("Grade labels:", labels)

    print()


# ---------------------------------------------------------------------------
# 8. Operators in functional pipelines — replacing lambdas
# ---------------------------------------------------------------------------

def demo_pipelines():
    print("=" * 60)
    print("Operators in functional pipelines")
    print("=" * 60)

    # --- 8a: running product with reduce ---
    nums = [1.05, 1.03, 0.98, 1.07, 1.02]   # monthly return multipliers
    total_return = reduce(operator.mul, nums, 1.0)
    print(f"Total return over 5 months: {total_return:.4f}")
    # 1.05 * 1.03 * 0.98 * 1.07 * 1.02 ≈ 1.1594

    # --- 8b: all / any with operators ---
    prices = [15.99, 8.50, 24.99, 12.00, 5.00]
    all_above_5 = all(map(lambda p: operator.gt(p, 5.0), prices))
    any_above_20 = any(map(lambda p: operator.gt(p, 20.0), prices))
    print(f"All above $5:  {all_above_5}")    # True
    print(f"Any above $20: {any_above_20}")   # True

    # --- 8c: build a simple expression evaluator ---
    ops_map = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "**": operator.pow,
    }

    def evaluate(a: float, op: str, b: float) -> float:
        return ops_map[op](a, b)

    expressions = [(10, "+", 3), (10, "-", 3), (10, "*", 3),
                   (10, "/", 3), (10, "%", 3), (2, "**", 10)]
    for a, op, b in expressions:
        print(f"  {a} {op} {b} = {evaluate(a, op, b)}")

    # --- 8d: compose pipeline with reduce and operator ---
    # Find the maximum salary increase across departments
    before = {"Eng": 90_000, "HR": 75_000, "Mkt": 68_000}
    after  = {"Eng": 98_000, "HR": 79_000, "Mkt": 72_000}

    increases = list(map(operator.sub,
                         after.values(),
                         before.values()))
    print("\nSalary increases:", increases)     # [8000, 4000, 4000]
    print("Max increase: $", max(increases))   # 8000
    print("Total raises: $", reduce(operator.add, increases))  # 16000

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_arithmetic()
    demo_comparison()
    demo_logical_bitwise()
    demo_sequence_ops()
    demo_inplace()
    demo_itemgetter()
    demo_attrgetter_methodcaller()
    demo_pipelines()
