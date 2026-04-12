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

---

### 1. Valid Parentheses — #20 (Easy)

**Problem**: Given a string containing only `(`, `)`, `{`, `}`, `[`, `]`, determine if the input string is valid. Open brackets must be closed by the same type in the correct order.

```
Input:  "()"
Output: true

Input:  "()[]{}"
Output: true

Input:  "(]"
Output: false

Input:  "([)]"
Output: false

Input:  "{[]}"
Output: true
```

**Hints**:
1. Push opening brackets onto the stack
2. On a closing bracket, check if the stack top is the matching opener
3. At the end, the stack must be empty

---

### 2. Min Stack — #155 (Medium)

**Problem**: Design a stack that supports `push`, `pop`, `top`, and `getMin` — all in O(1).

```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],        [-2],  [0],   [-3],  [],      [],   [],   []]

Output: [null, null, null, null, -3, null, 0, -2]

Trace:
push(-2) → stack: [-2], min_stack: [-2]
push(0)  → stack: [-2,0], min_stack: [-2,-2]
push(-3) → stack: [-2,0,-3], min_stack: [-2,-2,-3]
getMin() → -3
pop()    → stack: [-2,0], min_stack: [-2,-2]
top()    → 0
getMin() → -2
```

**Hints**:
1. Maintain a parallel `min_stack` where each position stores the minimum up to that point
2. On push: `min_stack.append(min(val, min_stack[-1]))`
3. On pop: pop from both stacks simultaneously

---

### 3. Evaluate Reverse Polish Notation — #150 (Medium)

**Problem**: Evaluate an expression in Reverse Polish Notation (postfix). Valid operators are `+`, `-`, `*`, `/` (integer division truncating toward zero).

```
Input:  ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input:  ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input:  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

**Hints**:
1. Push numbers onto the stack
2. On an operator, pop two numbers, apply the operator, push the result
3. The final answer is the only element left on the stack

---

### 4. Daily Temperatures — #739 (Medium)

**Problem**: Given an array of daily temperatures, return an array where `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature. If no future warmer day exists, put `0`.

```
Input:  [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1,  1,  4,  2,  1,  1,  0,  0]

Explanation:
Day 0 (73°): next warmer is day 1 (74°) → 1 day
Day 1 (74°): next warmer is day 2 (75°) → 1 day
Day 2 (75°): next warmer is day 6 (76°) → 4 days
Day 3 (71°): next warmer is day 5 (72°) → 2 days
Day 6 (76°): no warmer day → 0
```

**Hints**:
1. Use a monotonic decreasing stack of indices
2. When current temp > stack top's temp, pop and record the distance
3. Push current index onto the stack

---

### 5. Largest Rectangle in Histogram — #84 (Hard)

**Problem**: Given an array of bar heights, find the area of the largest rectangle that can be formed.

```
Input:  [2, 1, 5, 6, 2, 3]
Output: 10

Explanation:
The largest rectangle uses bars at indices 2 and 3 (heights 5 and 6):
width=2, height=5 → area=10

Input:  [2, 4]
Output: 4
```

**Hints**:
1. Use a monotonic increasing stack of indices
2. When current height < stack top's height, pop and calculate area
3. Width = current index - (new stack top + 1); height = popped bar's height
4. Append a 0 at the end to flush all remaining bars

---

### 6. Decode String — #394 (Medium)

**Problem**: Given an encoded string like `k[encoded_string]`, decode it by repeating `encoded_string` exactly `k` times. Nesting is possible.

```
Input:  "3[a]2[bc]"
Output: "aaabcbc"

Input:  "3[a2[c]]"
Output: "accaccacc"

Input:  "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

**Hints**:
1. Use a stack to handle nesting
2. On `[`: push current string and current number onto stack, reset both
3. On `]`: pop the previous string and number, append `current_string * number` to previous string
4. On digit: build the current number; on letter: append to current string

---

### 7. Remove K Digits — #402 (Medium)

**Problem**: Given a string of digits and an integer k, remove k digits to make the resulting number as small as possible. Return the result as a string (no leading zeros).

```
Input:  num = "1432219", k = 3
Output: "1219"
Explanation: Remove 4, 3, 2 → "1219"

Input:  num = "10200", k = 1
Output: "200"
Explanation: Remove 1 → "0200" → "200" (strip leading zero)

Input:  num = "10", k = 2
Output: "0"
```

**Hints**:
1. Use a monotonic increasing stack — pop when current digit is smaller than top and k > 0
2. After processing, if k > 0, remove from the end
3. Strip leading zeros from the result

---

### 8. Asteroid Collision — #735 (Medium)

**Problem**: An array of integers represents asteroids. Positive = moving right, negative = moving left. Same-direction asteroids never collide. When two asteroids meet, the smaller one explodes. Equal-size asteroids both explode. Return the state after all collisions.

```
Input:  [5, 10, -5]
Output: [5, 10]
Explanation: -5 collides with 10, 10 wins.

Input:  [8, -8]
Output: []
Explanation: Both explode.

Input:  [10, 2, -5]
Output: [10]
Explanation: -5 destroys 2, then 10 destroys -5.

Input:  [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: No collisions (left-movers never meet right-movers here).
```

**Hints**:
1. Use a stack; push positive asteroids
2. For a negative asteroid, pop positives from the stack while they're smaller
3. If stack top equals the absolute value, both explode (pop and don't push)
4. If stack is empty or top is negative, push the negative asteroid
