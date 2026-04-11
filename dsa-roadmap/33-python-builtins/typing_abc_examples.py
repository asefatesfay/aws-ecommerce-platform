"""
typing — Type annotations and static typing tools for clearer, safer code.
abc    — Abstract Base Classes: enforce interface contracts at runtime.

typing covered:
  Basic annotations       — int, str, list, dict, tuple, set, Any, None
  Generic collections     — List, Dict, Tuple, Set, Optional, Union (legacy)
                            list[int], dict[str,int] (Python 3.9+ PEP 585)
  Optional and Union      — Optional[X] == X | None (3.10+ unions)
  Callable                — type-hint function signatures
  TypeVar                 — generic functions and classes
  Generic classes         — class Stack(Generic[T])
  Protocol                — structural subtyping (duck typing with checking)
  TypedDict               — dict with specific key/value types
  NamedTuple              — like namedtuple but with type hints
  Literal                 — restrict to specific values
  Final                   — mark a value as constant
  ClassVar                — class-level annotation
  overload                — multiple signatures for one function
  get_type_hints          — runtime introspection
  TYPE_CHECKING           — avoid circular imports

abc covered:
  ABC / ABCMeta           — base class for abstract classes
  @abstractmethod         — require subclasses to implement a method
  @abstractproperty       — require a property (use @property + @abstractmethod)
  @abstractclassmethod
  @abstractstaticmethod
  register()              — register a virtual subclass (duck typing + ABC)
  __subclasshook__        — customise isinstance() checks
"""

from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from typing import (
    Any, Callable, ClassVar, Final, Generic, Literal,
    NamedTuple, Optional, Protocol, TypedDict, TypeVar,
    Union, cast, get_type_hints, overload, TYPE_CHECKING,
    runtime_checkable,
)


# ===========================================================================
# TYPING
# ===========================================================================

# ---------------------------------------------------------------------------
# 1. Basic annotations and Optional / Union
# ---------------------------------------------------------------------------

def demo_basic_annotations():
    print("=" * 60)
    print("Basic annotations, Optional, Union (Python 3.10+ X|Y)")
    print("=" * 60)

    # Optional[X] is exactly X | None
    def find_user(user_id: int) -> Optional[dict]:
        users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
        return users.get(user_id)

    u1 = find_user(1)
    u3 = find_user(999)
    print(f"find_user(1):   {u1}")     # {'name': 'Alice'}
    print(f"find_user(999): {u3}")     # None

    # Union: accept multiple types
    def stringify(val: Union[int, float, bool]) -> str:
        return str(val)

    print(stringify(42))      # '42'
    print(stringify(3.14))    # '3.14'

    # Python 3.10+ union syntax: int | str | None
    def process(value: int | str | None) -> str:
        if value is None:
            return "nothing"
        return str(value).upper()

    print(process(None))     # nothing
    print(process("hello"))  # HELLO
    print(process(42))       # 42

    # Any — opt out of type checking
    def accept_anything(x: Any) -> Any:
        return x

    print(accept_anything([1, "mixed", 3.14]))

    print()


# ---------------------------------------------------------------------------
# 2. Callable type hints
# ---------------------------------------------------------------------------

def demo_callable():
    print("=" * 60)
    print("Callable type hints")
    print("=" * 60)

    # Callable[[arg_types], return_type]
    Transform = Callable[[int], int]

    def apply(value: int, transform: Transform) -> int:
        return transform(value)

    double   = lambda x: x * 2
    square   = lambda x: x ** 2
    negate   = lambda x: -x

    for fn in [double, square, negate]:
        print(f"  apply(5, {fn.__name__ if hasattr(fn,'__name__') else fn}): {apply(5, fn)}")

    # Higher-order: decorator type signature
    Decorator = Callable[[Callable], Callable]

    def log_calls(fn: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            print(f"  {fn.__name__}({args}, {kwargs}) -> {result}")
            return result
        return wrapper

    @log_calls
    def add(a: int, b: int) -> int:
        return a + b

    add(3, 4)   # logs the call

    print()


# ---------------------------------------------------------------------------
# 3. TypeVar — generic functions
# ---------------------------------------------------------------------------

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

def demo_typevar():
    print("=" * 60)
    print("TypeVar — generic functions")
    print("=" * 60)

    # Generic identity function
    def identity(x: T) -> T:
        return x

    print(identity(42))       # int -> int
    print(identity("hello"))  # str -> str
    print(identity([1, 2]))   # list -> list

    # Generic first/last
    def first(items: list[T]) -> T:
        return items[0]

    def last(items: list[T]) -> T:
        return items[-1]

    nums   = [10, 20, 30]
    words  = ["alpha", "beta", "gamma"]
    print(f"first({nums})  = {first(nums)}")   # 10
    print(f"last({words}) = {last(words)}")    # gamma

    # Bounded TypeVar — T must be a number
    from typing import TypeVar as TV
    import numbers
    Num = TV("Num", int, float, complex)

    def total(items: list[Num]) -> Num:  # type: ignore[valid-type]
        result = items[0]
        for x in items[1:]:
            result += x  # type: ignore
        return result

    print(f"total([1,2,3]):       {total([1, 2, 3])}")         # 6
    print(f"total([1.1,2.2,3.3]): {total([1.1, 2.2, 3.3])}")  # ≈6.6

    print()


# ---------------------------------------------------------------------------
# 4. Generic classes
# ---------------------------------------------------------------------------

def demo_generic_class():
    print("=" * 60)
    print("Generic classes — class Foo(Generic[T])")
    print("=" * 60)

    class Stack(Generic[T]):
        """Type-safe stack."""
        def __init__(self) -> None:
            self._items: list[T] = []

        def push(self, item: T) -> None:
            self._items.append(item)

        def pop(self) -> T:
            if not self._items:
                raise IndexError("pop from empty stack")
            return self._items.pop()

        def peek(self) -> T:
            return self._items[-1]

        def __len__(self) -> int:
            return len(self._items)

        def __repr__(self) -> str:
            return f"Stack({self._items})"

    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print("int_stack:", int_stack)
    print("pop:", int_stack.pop())
    print("peek:", int_stack.peek())

    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print("\nstr_stack:", str_stack)

    # Generic pair
    class Pair(Generic[K, V]):
        def __init__(self, key: K, value: V) -> None:
            self.key   = key
            self.value = value

        def swap(self) -> Pair[V, K]:
            return Pair(self.value, self.key)

        def __repr__(self) -> str:
            return f"Pair({self.key!r}, {self.value!r})"

    p = Pair("age", 30)
    print("\nPair:", p)
    print("Swapped:", p.swap())

    print()


# ---------------------------------------------------------------------------
# 5. Protocol — structural subtyping (duck typing + static analysis)
# ---------------------------------------------------------------------------

def demo_protocol():
    print("=" * 60)
    print("Protocol — structural subtyping")
    print("=" * 60)

    @runtime_checkable   # allows isinstance() checks at runtime
    class Drawable(Protocol):
        def draw(self) -> str: ...

    @runtime_checkable
    class Saveable(Protocol):
        def save(self, path: str) -> None: ...

    class Circle:
        def __init__(self, radius: float):
            self.radius = radius
        def draw(self) -> str:
            return f"Circle(r={self.radius})"

    class Square:
        def __init__(self, side: float):
            self.side = side
        def draw(self) -> str:
            return f"Square(s={self.side})"
        def save(self, path: str) -> None:
            print(f"  Saved Square to {path}")

    def render_all(shapes: list[Drawable]) -> None:
        for shape in shapes:
            print(f"  Rendering: {shape.draw()}")

    shapes = [Circle(5.0), Square(3.0)]
    render_all(shapes)   # works for both — no inheritance required

    print("\nisinstance checks (runtime_checkable):")
    c = Circle(1.0)
    s = Square(2.0)
    print(f"  Circle is Drawable: {isinstance(c, Drawable)}")   # True
    print(f"  Square is Drawable: {isinstance(s, Drawable)}")   # True
    print(f"  Circle is Saveable: {isinstance(c, Saveable)}")   # False (no save method)
    print(f"  Square is Saveable: {isinstance(s, Saveable)}")   # True

    print()


# ---------------------------------------------------------------------------
# 6. TypedDict and NamedTuple
# ---------------------------------------------------------------------------

def demo_typeddict_namedtuple():
    print("=" * 60)
    print("TypedDict and NamedTuple")
    print("=" * 60)

    # TypedDict — typed dict schema
    class UserRecord(TypedDict):
        id:    int
        name:  str
        email: str
        active: bool

    class PartialUser(TypedDict, total=False):
        """total=False means all keys are optional."""
        id:    int
        name:  str
        email: str

    user: UserRecord = {"id": 1, "name": "Alice", "email": "a@ex.com", "active": True}
    print("UserRecord:", user)
    print("name:", user["name"])

    update: PartialUser = {"name": "Alice Updated"}  # only 'name' specified
    print("Partial update:", update)

    # NamedTuple — superior to collections.namedtuple: field types + defaults
    class Point(NamedTuple):
        x: float
        y: float
        z: float = 0.0   # default value

    class Employee(NamedTuple):
        name:       str
        department: str
        salary:     float = 0.0

    p = Point(1.0, 2.0)
    print(f"\nPoint: {p}  z default: {p.z}")
    print("Unpack:", *p)

    emp = Employee("Alice", "Engineering", 95_000)
    print(f"Employee: {emp}")
    print("As dict:", emp._asdict())

    # NamedTuple is iterable and indexable
    e_list = [
        Employee("Alice", "Eng", 95_000),
        Employee("Bob",   "Mkt", 72_000),
        Employee("Carol", "Eng", 105_000),
    ]
    # Sort by salary using index 2
    e_list.sort(key=lambda e: e.salary, reverse=True)
    for e in e_list:
        print(f"  {e.name:8} ${e.salary:,}")

    print()


# ---------------------------------------------------------------------------
# 7. Literal, Final, and overload
# ---------------------------------------------------------------------------

def demo_literal_final_overload():
    print("=" * 60)
    print("Literal, Final, overload")
    print("=" * 60)

    # Literal — restrict to specific values (like an enum but simpler)
    Direction = Literal["N", "S", "E", "W"]

    def move(steps: int, direction: Direction) -> str:
        return f"Move {steps} steps {direction}"

    print(move(3, "N"))   # valid
    # move(3, "X")  <- type checker would flag this

    # Final — mark a variable as constant (type checker enforces it)
    MAX_CONNECTIONS: Final[int] = 100
    API_KEY: Final[str] = "sk-test-12345"
    print(f"\nMAX_CONNECTIONS: {MAX_CONNECTIONS}")
    print(f"API_KEY: {API_KEY[:5]}...")

    # overload — different return types depending on argument types
    @overload
    def process_input(value: int) -> int: ...
    @overload
    def process_input(value: str) -> str: ...
    @overload
    def process_input(value: list) -> list: ...

    def process_input(value):   # actual implementation
        if isinstance(value, int):
            return value * 2
        if isinstance(value, str):
            return value.upper()
        if isinstance(value, list):
            return [x * 2 for x in value]
        raise TypeError(f"unsupported type: {type(value)}")

    print("\noverload demonstrations:")
    print("  process_input(5):          ", process_input(5))          # 10
    print("  process_input('hello'):    ", process_input("hello"))    # HELLO
    print("  process_input([1,2,3]):    ", process_input([1, 2, 3]))  # [2,4,6]

    print()


# ===========================================================================
# ABC
# ===========================================================================

# ---------------------------------------------------------------------------
# 8. Abstract Base Classes
# ---------------------------------------------------------------------------

def demo_abc():
    print("=" * 60)
    print("ABC — Abstract Base Classes")
    print("=" * 60)

    class Shape(ABC):
        """Abstract base class for all shapes."""

        @abstractmethod
        def area(self) -> float: ...

        @abstractmethod
        def perimeter(self) -> float: ...

        @property
        @abstractmethod
        def name(self) -> str: ...

        def describe(self) -> str:
            return (f"{self.name}: area={self.area():.2f}, "
                    f"perimeter={self.perimeter():.2f}")

    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius

        @property
        def name(self) -> str: return "Circle"

        def area(self)      -> float: return 3.141592653589793 * self.radius ** 2
        def perimeter(self) -> float: return 2 * 3.141592653589793 * self.radius

    class Rectangle(Shape):
        def __init__(self, w: float, h: float):
            self.w, self.h = w, h

        @property
        def name(self) -> str: return "Rectangle"

        def area(self)      -> float: return self.w * self.h
        def perimeter(self) -> float: return 2 * (self.w + self.h)

    shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
    for s in shapes:
        print(" ", s.describe())

    # Cannot instantiate abstract class
    try:
        s = Shape()  # type: ignore
    except TypeError as e:
        print(f"\nCannot instantiate Shape: {e}")

    # Partial implementation — still abstract
    class ColoredShape(Shape):
        def __init__(self, color: str):
            self.color = color
        # area and perimeter still abstract — cannot instantiate

    try:
        cs = ColoredShape("red")  # type: ignore
    except TypeError as e:
        print(f"Cannot instantiate ColoredShape: {e}")

    print()


# ---------------------------------------------------------------------------
# 9. ABC with register() and __subclasshook__
# ---------------------------------------------------------------------------

def demo_abc_register():
    print("=" * 60)
    print("ABC register() and __subclasshook__")
    print("=" * 60)

    class Printable(ABC):
        """Anything with a print_info() method counts as Printable."""

        @abstractmethod
        def print_info(self) -> None: ...

        @classmethod
        def __subclasshook__(cls, C):
            """Make isinstance() return True if the class has print_info."""
            if cls is Printable:
                if any("print_info" in B.__dict__ for B in C.__mro__):
                    return True
            return NotImplemented

    # Third-party class we cannot modify
    class LegacyReport:
        def print_info(self) -> None:
            print("  [LegacyReport] printing...")

    # Using __subclasshook__, no inheritance needed
    print("LegacyReport is Printable:", isinstance(LegacyReport(), Printable))  # True

    # register() for classes that satisfy the contract but lack the method name
    class OldLogger:
        def log_output(self) -> None:
            print("  [OldLogger] logging...")

    Printable.register(OldLogger)   # virtual subclass
    print("OldLogger is registered:", isinstance(OldLogger(), Printable))  # True
    print("OldLogger in Printable subclasses:", issubclass(OldLogger, Printable))  # True

    # Abstract classmethod and staticmethod
    class DataStore(ABC):
        @classmethod
        @abstractmethod
        def from_file(cls, path: str) -> DataStore: ...

        @staticmethod
        @abstractmethod
        def supported_formats() -> list[str]: ...

    class JsonStore(DataStore):
        @classmethod
        def from_file(cls, path: str) -> JsonStore:
            return cls()

        @staticmethod
        def supported_formats() -> list[str]:
            return [".json"]

    store = JsonStore.from_file("data.json")
    print("\nJsonStore formats:", JsonStore.supported_formats())

    print()


# ---------------------------------------------------------------------------
# 10. get_type_hints — runtime introspection
# ---------------------------------------------------------------------------

def demo_get_type_hints():
    print("=" * 60)
    print("get_type_hints — runtime type introspection")
    print("=" * 60)

    class APIResponse:
        status:  int
        message: str
        data:    Optional[list]

        def __init__(self, status: int, message: str, data: Optional[list] = None):
            self.status  = status
            self.message = message
            self.data    = data

    hints = get_type_hints(APIResponse)
    print("Type hints for APIResponse:")
    for name, hint in hints.items():
        print(f"  {name}: {hint}")

    # Use hints for validation
    def validate(obj: object, cls: type) -> list[str]:
        errors = []
        hints  = get_type_hints(cls)
        for attr, expected_type in hints.items():
            val = getattr(obj, attr, None)
            # Simple check (handles Optional[X] naively)
            origin = getattr(expected_type, "__origin__", None)
            if origin is Union:
                args = expected_type.__args__
                if not isinstance(val, tuple(a for a in args if a is not type(None))):
                    if val is not None:
                        errors.append(f"{attr}: expected {expected_type}, got {type(val)}")
        return errors

    resp = APIResponse(200, "OK")
    print("\nValidation errors:", validate(resp, APIResponse) or "none")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("TYPING")
    print("=" * 60)
    demo_basic_annotations()
    demo_callable()
    demo_typevar()
    demo_generic_class()
    demo_protocol()
    demo_typeddict_namedtuple()
    demo_literal_final_overload()

    print("=" * 60)
    print("ABC")
    print("=" * 60)
    demo_abc()
    demo_abc_register()
    demo_get_type_hints()
