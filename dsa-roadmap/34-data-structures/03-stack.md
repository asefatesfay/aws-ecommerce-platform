# Stack

## What is it?
A **Last-In, First-Out (LIFO)** data structure. Think of a stack of plates — you always add and remove from the top.

## Visual Example
```
push(1) → push(2) → push(3) → pop() → peek()

     [3]  ← top
     [2]
     [1]
   -------

pop() returns 3

     [2]  ← top
     [1]
   -------

peek() returns 2 (without removing)
```

## Key Operations
| Operation | Time | Description |
|-----------|------|-------------|
| push(val) | O(1) | Add to top |
| pop() | O(1) | Remove and return top |
| peek() | O(1) | View top without removing |
| is_empty() | O(1) | Check if empty |

## Implementation

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class MinStack:
    """Stack with O(1) minimum retrieval — LeetCode #155"""
    def __init__(self):
        self._data = []
        self._min = []

    def push(self, val):
        self._data.append(val)
        min_val = val if not self._min else min(val, self._min[-1])
        self._min.append(min_val)

    def pop(self):
        self._min.pop()
        return self._data.pop()

    def get_min(self):
        return self._min[-1]

    def top(self):
        return self._data[-1]
```

## Example Usage
```python
s = Stack()
s.push(5)
s.push(3)
s.push(8)
print(s.pop())   # 8
print(s.peek())  # 3
print(len(s))    # 2

# Min Stack
ms = MinStack()
ms.push(3)
ms.push(1)
ms.push(5)
print(ms.get_min())  # 1
ms.pop()
print(ms.get_min())  # 1
ms.pop()
print(ms.get_min())  # 3
```

## When to Use
- Matching/validating parentheses
- Undo/redo operations
- DFS (iterative)
- Expression evaluation
- Backtracking
- Monotonic stack problems

## LeetCode Problems

| Problem | Difficulty | How Stack Helps |
|---------|-----------|-----------------|
| Valid Parentheses (#20) | Easy | Push open brackets, match on close |
| Min Stack (#155) | Medium | Parallel min-tracking stack |
| Evaluate Reverse Polish Notation (#150) | Medium | Push operands, pop on operator |
| Daily Temperatures (#739) | Medium | Monotonic stack for next greater |
| Largest Rectangle in Histogram (#84) | Hard | Monotonic stack for boundaries |
| Basic Calculator (#224) | Hard | Stack for operator precedence |
| Decode String (#394) | Medium | Stack for nested brackets |
| Remove K Digits (#402) | Medium | Monotonic stack |
| Asteroid Collision (#735) | Medium | Stack simulation |
| Simplify Path (#71) | Medium | Stack for directory traversal |
