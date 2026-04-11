"""
dataclasses — Auto-generate __init__, __repr__, __eq__, and more from field declarations.
enum        — Define named symbolic constants with type safety and iteration.

dataclasses covered:
  @dataclass         — basic field declarations
  field()            — default_factory, compare, repr, hash, metadata
  __post_init__      — validation and derived fields
  frozen=True        — immutable dataclass (hashable)
  order=True         — auto-generate < > <= >=
  asdict / astuple   — convert to plain dict / tuple
  replace()          — create modified copy (like namedtuple._replace)
  ClassVar           — class-level variable excluded from __init__
  InitVar            — init-only variable consumed in __post_init__
  KW_ONLY            — force remaining fields to be keyword-only (3.10+)
  slots=True         — __slots__ for memory efficiency (3.10+)

enum covered:
  Enum          — base class; .name, .value, iteration, membership tests
  IntEnum       — integer-valued enum with arithmetic
  StrEnum       — string-valued enum (3.11+, or mixin)
  Flag          — bit-flag combinations with | and &
  IntFlag       — bit-flags + arithmetic
  auto()        — automatic value assignment
  _missing_()   — custom handling of unknown values
  aliases       — multiple names for the same value
  unique        — enforce no duplicate values (decorator)
"""

from __future__ import annotations
from dataclasses import (
    dataclass, field, asdict, astuple,
    replace, fields, KW_ONLY, InitVar, ClassVar
)
from enum import Enum, IntEnum, Flag, IntFlag, auto, unique
import math


# ===========================================================================
# DATACLASSES
# ===========================================================================

# ---------------------------------------------------------------------------
# 1. Basic @dataclass
# ---------------------------------------------------------------------------

def demo_basic_dataclass():
    print("=" * 60)
    print("Basic @dataclass")
    print("=" * 60)

    @dataclass
    class Point:
        x: float
        y: float

        def distance_to(self, other: Point) -> float:
            return math.hypot(self.x - other.x, self.y - other.y)

    p1 = Point(0.0, 0.0)
    p2 = Point(3.0, 4.0)

    print(f"p1 = {p1}")             # Point(x=0.0, y=0.0)
    print(f"p2 = {p2}")
    print(f"Equal: {p1 == p2}")    # False
    print(f"Distance: {p1.distance_to(p2)}")  # 5.0

    # __repr__ generated automatically
    print(repr(p2))   # Point(x=3.0, y=4.0)

    @dataclass
    class Product:
        id:       int
        name:     str
        price:    float
        in_stock: bool = True   # default value

    prod = Product(1, "Laptop", 999.99)
    print("\n", prod)
    print("In stock:", prod.in_stock)

    print()


# ---------------------------------------------------------------------------
# 2. field() — advanced control
# ---------------------------------------------------------------------------

def demo_field():
    print("=" * 60)
    print("field() — default_factory, exclude from repr/compare")
    print("=" * 60)

    @dataclass
    class Order:
        order_id:  int
        customer:  str
        items:     list  = field(default_factory=list)
        # Mutable defaults MUST use default_factory — never field(default=[])
        tags:      set   = field(default_factory=set)
        _internal: str   = field(default="", repr=False, compare=False)
        total:     float = field(default=0.0, metadata={"unit": "USD"})

        def add_item(self, name: str, price: float) -> None:
            self.items.append({"name": name, "price": price})
            self.total += price

    o1 = Order(101, "Alice")
    o2 = Order(102, "Bob")

    o1.add_item("Laptop", 999.99)
    o1.add_item("Mouse", 29.99)
    o1.tags.add("priority")

    print("Order:", o1)
    # _internal is excluded from repr
    # Order(order_id=101, customer='Alice', items=[...], tags={'priority'}, total=1029.98)

    print("Total: $", o1.total)

    # Access metadata
    for f in fields(Order):
        if f.metadata:
            print(f"Field {f.name} metadata: {f.metadata}")

    print()


# ---------------------------------------------------------------------------
# 3. __post_init__ — validation and derived fields
# ---------------------------------------------------------------------------

def demo_post_init():
    print("=" * 60)
    print("__post_init__ — validation and derived fields")
    print("=" * 60)

    @dataclass
    class Rectangle:
        width:     float
        height:    float
        area:      float = field(init=False)      # computed, not in __init__
        perimeter: float = field(init=False)

        def __post_init__(self):
            if self.width <= 0 or self.height <= 0:
                raise ValueError(f"Dimensions must be positive: {self.width}x{self.height}")
            self.area      = self.width * self.height
            self.perimeter = 2 * (self.width + self.height)

    r = Rectangle(5.0, 3.0)
    print(f"Rectangle: {r}")
    print(f"Area: {r.area}  Perimeter: {r.perimeter}")

    try:
        bad = Rectangle(-1, 5)
    except ValueError as e:
        print(f"Validation error: {e}")

    # InitVar — pass to __post_init__ but don't store as field
    @dataclass
    class Circle:
        radius:        float
        diameter:      float = field(init=False)
        circumference: float = field(init=False)
        unit:          InitVar[str] = "cm"         # consumed in __post_init__
        unit_label:    str  = field(init=False)

        def __post_init__(self, unit: str):
            self.diameter      = self.radius * 2
            self.circumference = 2 * math.pi * self.radius
            self.unit_label    = unit

    c = Circle(5.0, unit="cm")
    print(f"\nCircle radius={c.radius}{c.unit_label}  "
          f"area={math.pi * c.radius**2:.2f}  circumference={c.circumference:.2f}")
    # unit is used but not stored as a persistent field

    print()


# ---------------------------------------------------------------------------
# 4. frozen=True, order=True, asdict, astuple, replace
# ---------------------------------------------------------------------------

def demo_frozen_and_utilities():
    print("=" * 60)
    print("frozen=True  |  order=True  |  asdict  |  astuple  |  replace")
    print("=" * 60)

    @dataclass(frozen=True)   # immutable and hashable — can be used in sets/dicts
    class Coordinate:
        lat: float
        lon: float

    c1 = Coordinate(37.7749, -122.4194)   # San Francisco
    c2 = Coordinate(40.7128,  -74.0060)   # New York

    print("c1:", c1)
    try:
        c1.lat = 0.0    # type: ignore
    except Exception as e:
        print("Cannot modify frozen:", e)

    # Frozen dataclasses are hashable — safe to use as dict keys or set members
    visited = {c1, c2}
    print("In set:", c1 in visited)   # True

    # order=True — generates __lt__, __le__, __gt__, __ge__
    @dataclass(order=True)
    class Version:
        major: int
        minor: int
        patch: int

        def __str__(self):
            return f"{self.major}.{self.minor}.{self.patch}"

    versions = [Version(1, 10, 0), Version(2, 0, 0), Version(1, 9, 5), Version(1, 10, 1)]
    print("\nSorted versions:", sorted(versions))
    print("Latest:", max(versions))

    # asdict — recursive conversion to nested dicts
    @dataclass
    class Address:
        street: str
        city:   str
        zip:    str

    @dataclass
    class Person:
        name:    str
        age:     int
        address: Address

    alice = Person("Alice", 30, Address("123 Main St", "Springfield", "12345"))
    d = asdict(alice)
    print("\nasdict:", d)
    # {'name': 'Alice', 'age': 30, 'address': {'street': '...', 'city': '...', 'zip': '...'}}

    t = astuple(alice)
    print("astuple:", t)
    # ('Alice', 30, ('123 Main St', 'Springfield', '12345'))

    # replace — make a copy with some fields changed (same as frozen._replace)
    alice_ny = replace(alice, address=replace(alice.address, city="New York"))
    print("Original city:", alice.address.city)
    print("New copy city:", alice_ny.address.city)

    print()


# ---------------------------------------------------------------------------
# 5. ClassVar and slots (Python 3.10+)
# ---------------------------------------------------------------------------

def demo_classvar_and_slots():
    print("=" * 60)
    print("ClassVar  |  slots=True  |  kw_only")
    print("=" * 60)

    @dataclass
    class Employee:
        # ClassVar fields are excluded from __init__, __repr__, __eq__
        company:    ClassVar[str] = "Acme Corp"
        count:      ClassVar[int] = 0

        name:       str
        department: str
        salary:     float = 0.0

        def __post_init__(self):
            Employee.count += 1

    e1 = Employee("Alice", "Engineering", 95_000)
    e2 = Employee("Bob",   "Marketing",   72_000)
    print(f"{e1.name} @ {Employee.company}")
    print(f"Total employees: {Employee.count}")
    print("e1 repr:", e1)   # ClassVar fields not shown

    # KW_ONLY — all subsequent fields must be passed as keyword arguments (3.10+)
    @dataclass
    class Config:
        host:    str
        port:    int
        _: KW_ONLY
        debug:   bool  = False
        timeout: int   = 30
        retries: int   = 3

    cfg = Config("localhost", 5432, debug=True, timeout=10)
    print(f"\nConfig: {cfg}")

    # slots=True — uses __slots__ for ~30% less memory per instance (3.10+)
    @dataclass(slots=True)
    class Pixel:
        x: int
        y: int
        r: int = 0
        g: int = 0
        b: int = 0

    px = Pixel(10, 20, 255, 128, 0)
    print(f"Pixel: {px}")
    # No __dict__ — lower memory footprint (important for large numbers of instances)

    print()


# ===========================================================================
# ENUM
# ===========================================================================

# ---------------------------------------------------------------------------
# 6. Basic Enum
# ---------------------------------------------------------------------------

def demo_enum_basics():
    print("=" * 60)
    print("Basic Enum")
    print("=" * 60)

    class Direction(Enum):
        NORTH = "N"
        SOUTH = "S"
        EAST  = "E"
        WEST  = "W"

    d = Direction.NORTH
    print("Value:", d)           # Direction.NORTH
    print(".name:", d.name)      # 'NORTH'
    print(".value:", d.value)    # 'N'
    print("repr:", repr(d))

    # Membership and identity
    print("\nNORTH == NORTH:", Direction.NORTH == Direction.NORTH)
    print("NORTH is NORTH:", Direction.NORTH is Direction.NORTH)  # True (singleton)

    # Access by value
    opposite = Direction("S")
    print("Direction('S'):", opposite)

    # Iteration
    print("\nAll directions:")
    for dir_ in Direction:
        print(f"  {dir_.name:6} -> {dir_.value}")

    # Comparison by identity
    current = Direction.EAST
    if current is Direction.EAST or current is Direction.WEST:
        print("Moving horizontally")

    print()


# ---------------------------------------------------------------------------
# 7. auto() and custom __new__
# ---------------------------------------------------------------------------

def demo_auto_and_custom():
    print("=" * 60)
    print("auto() and custom values")
    print("=" * 60)

    # auto() assigns sequential integers starting at 1
    class Priority(Enum):
        LOW    = auto()
        MEDIUM = auto()
        HIGH   = auto()
        URGENT = auto()

    print("Priorities:")
    for p in Priority:
        print(f"  {p.name:8} = {p.value}")
    # LOW=1, MEDIUM=2, HIGH=3, URGENT=4

    # Enum with methods
    class Planet(Enum):
        MERCURY = (3.303e+23, 2.4397e6)
        VENUS   = (4.869e+24, 6.0518e6)
        EARTH   = (5.976e+24, 6.37814e6)
        MARS    = (6.421e+23, 3.3972e6)

        def __init__(self, mass: float, radius: float):
            self.mass   = mass
            self.radius = radius

        @property
        def surface_gravity(self) -> float:
            G = 6.67300E-11
            return G * self.mass / (self.radius ** 2)

        def weight(self, earth_weight: float) -> float:
            return earth_weight * self.surface_gravity / Planet.EARTH.surface_gravity

    earth_weight = 75.0   # kg
    print(f"\nWeight of {earth_weight}kg person on each planet:")
    for planet in Planet:
        print(f"  {planet.name:8}: {planet.weight(earth_weight):.2f} kg  "
              f"(g={planet.surface_gravity:.2f} m/s²)")

    print()


# ---------------------------------------------------------------------------
# 8. IntEnum and _missing_
# ---------------------------------------------------------------------------

def demo_int_enum():
    print("=" * 60)
    print("IntEnum and _missing_")
    print("=" * 60)

    class HttpStatus(IntEnum):
        OK        = 200
        CREATED   = 201
        NO_CONTENT= 204
        BAD_REQ   = 400
        UNAUTH    = 401
        FORBIDDEN = 403
        NOT_FOUND = 404
        SERVER_ERR= 500

        @classmethod
        def _missing_(cls, value: int):
            """Return a generic enum for unknown status codes."""
            if 200 <= value < 300:
                return cls.OK
            if 400 <= value < 500:
                return cls.BAD_REQ
            if 500 <= value < 600:
                return cls.SERVER_ERR
            return None

    print("HTTP status codes:")
    for code in [200, 404, 500, 201, 422]:
        status = HttpStatus(code)
        print(f"  {code} -> {status.name}")

    # IntEnum supports arithmetic and comparison with ints
    response_code = 200
    if response_code == HttpStatus.OK:
        print("\n200 == HttpStatus.OK:", True)

    success_codes = [s for s in HttpStatus if 200 <= s < 300]
    print("Success codes:", success_codes)

    print()


# ---------------------------------------------------------------------------
# 9. Flag — bit-field permissions
# ---------------------------------------------------------------------------

def demo_flag():
    print("=" * 60)
    print("Flag — bit-field combinations")
    print("=" * 60)

    @unique
    class Permission(Flag):
        NONE    = 0
        READ    = auto()   # 1
        WRITE   = auto()   # 2
        EXECUTE = auto()   # 4
        DELETE  = auto()   # 8

        # Convenience aliases
        READ_WRITE = READ | WRITE                # 3
        ALL        = READ | WRITE | EXECUTE | DELETE  # 15

    # User permissions as a combination of flags
    alice_perms = Permission.READ | Permission.WRITE
    bob_perms   = Permission.READ
    admin_perms = Permission.ALL

    print("Alice:", alice_perms)      # Permission.READ|WRITE
    print("Bob:  ", bob_perms)
    print("Admin:", admin_perms)

    # Test membership
    print("\nAlice can READ? ", Permission.READ  in alice_perms)   # True
    print("Alice can DELETE?", Permission.DELETE in alice_perms)  # False
    print("Admin can DELETE?", Permission.DELETE in admin_perms)  # True

    # Combine and revoke
    bob_promoted = bob_perms | Permission.WRITE
    print("\nBob promoted:", bob_promoted)

    alice_restricted = alice_perms & ~Permission.WRITE
    print("Alice restricted:", alice_restricted)   # READ only

    # Iterate over set bits
    print("\nAlice's individual permissions:")
    for perm in alice_perms:
        print(f"  {perm.name}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("DATACLASSES")
    print("=" * 60)
    demo_basic_dataclass()
    demo_field()
    demo_post_init()
    demo_frozen_and_utilities()
    demo_classvar_and_slots()

    print("=" * 60)
    print("ENUM")
    print("=" * 60)
    demo_enum_basics()
    demo_auto_and_custom()
    demo_int_enum()
    demo_flag()
