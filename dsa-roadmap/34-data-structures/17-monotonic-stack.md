# Monotonic Stack

## What is it?
A stack that maintains elements in **monotonically increasing or decreasing order**. When a new element violates the order, elements are popped until the order is restored. Each element is pushed and popped at most once → O(N) total.

## Visual Example — Next Greater Element
```
nums = [2, 1, 5, 3, 6, 4]
Find next greater element for each position.

Process each element, maintain decreasing stack:

i=0, val=2: stack=[], push 2.  stack=[2]
i=1, val=1: 1<2, push 1.       stack=[2,1]
i=2, val=5: 5>1, pop 1 → NGE[1]=5
            5>2, pop 2 → NGE[0]=5
            push 5.             stack=[5]
i=3, val=3: 3<5, push 3.       stack=[5,3]
i=4, val=6: 6>3, pop 3 → NGE[3]=6
            6>5, pop 5 → NGE[2]=6
            push 6.             stack=[6]
i=5, val=4: 4<6, push 4.       stack=[6,4]

Remaining in stack have no NGE → -1
Result: [5, 5, 6, 6, -1, -1]
```

## Key Insight
- **Decreasing stack** → find next GREATER element
- **Increasing stack** → find next SMALLER element
- Elements waiting in stack haven't found their answer yet

## Implementation

```python
def next_greater_element(nums):
    """
    For each element, find the next greater element to its right.
    O(N) time — each element pushed/popped at most once.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, values are decreasing

    for i in range(n):
        # Current element is greater than stack top → it's the NGE
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_smaller_element(nums):
    """Find next smaller element for each position."""
    n = len(nums)
    result = [-1] * n
    stack = []  # increasing stack

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def daily_temperatures(temperatures):
    """
    LeetCode #739: Days until warmer temperature.
    Same as next greater element, but return distance.
    """
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


def largest_rectangle_histogram(heights):
    """
    LeetCode #84: Largest rectangle in histogram.
    Monotonic increasing stack — when we pop, we found the right boundary.
    Left boundary is the new stack top.
    """
    stack = []
    max_area = 0
    heights = heights + [0]  # sentinel to flush remaining bars

    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i - (stack[-1] + 1 if stack else 0)
            max_area = max(max_area, heights[idx] * width)
            start = idx
        stack.append(start)

    return max_area


def sum_subarray_minimums(arr):
    """
    LeetCode #907: Sum of subarray minimums.
    For each element, find how many subarrays it's the minimum of.
    Use monotonic stack to find left and right boundaries.
    """
    MOD = 10**9 + 7
    n = len(arr)
    left = [0] * n   # distance to previous smaller element
    right = [0] * n  # distance to next smaller or equal element
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    return sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD
```

## Example Usage
```python
print(next_greater_element([2, 1, 5, 3, 6, 4]))
# [5, 5, 6, 6, -1, -1]

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
# 10 (rectangle of height 5, width 2 at indices 2-3)
```

## When to Use
- "Next greater/smaller element"
- "Previous greater/smaller element"
- "Largest rectangle in histogram"
- "Sum/count of subarray min/max"
- "Remove elements to maintain order"
- "Stock span problems"

## LeetCode Problems

---

### 1. Daily Temperatures — #739 (Medium)

**Problem**: Given an array of daily temperatures, return an array where `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature. If no future warmer day exists, put `0`.

```
Input:  [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1,  1,  4,  2,  1,  1,  0,  0]

Explanation:
Day 0 (73°): next warmer is day 1 (74°) → wait 1 day
Day 2 (75°): next warmer is day 6 (76°) → wait 4 days
Day 7 (73°): no warmer day → 0
```

**Hints**:
1. Monotonic decreasing stack of indices
2. When `temperatures[i] > temperatures[stack.top()]`, pop and record `i - popped_index`
3. Remaining indices in stack have no warmer day → answer stays 0

---

### 2. Next Greater Element II — #503 (Medium)

**Problem**: Given a circular integer array (the next element of the last element is the first element), return the next greater number for every element. If no greater number exists, output -1.

```
Input:  [1, 2, 1]
Output: [2, -1, 2]

Explanation:
1 → next greater is 2
2 → no greater element in circular array → -1
1 (last) → wraps around, next greater is 2

Input:  [1, 2, 3, 4, 3]
Output: [2, 3, 4, -1, 4]
```

**Hints**:
1. Iterate the array twice (simulate circular by using index `% n`)
2. Use a monotonic decreasing stack of indices
3. On the second pass, only pop from the stack (don't push new elements)

---

### 3. Largest Rectangle in Histogram — #84 (Hard)

**Problem**: Given an array of bar heights, find the area of the largest rectangle that can be formed within the histogram.

```
Input:  [2, 1, 5, 6, 2, 3]
Output: 10

Visualization:
  _
 _|_
|   |_
|   | |_
|_|_|_|_|_|_
2 1 5 6 2 3

Largest rectangle: height=5, width=2 (bars at index 2 and 3) → area=10
```

**Hints**:
1. Monotonic increasing stack of indices
2. When current height < stack top's height, pop and calculate: `width = i - stack[-1] - 1` (or `i` if stack empty)
3. Append a `0` sentinel at the end to flush all remaining bars

---

### 4. Sum of Subarray Minimums — #907 (Medium)

**Problem**: Given an array of integers, find the sum of `min(subarray)` for every contiguous subarray. Return the answer modulo 10^9+7.

```
Input:  [3, 1, 2, 4]
Output: 17

All subarrays and their minimums:
[3]=3, [1]=1, [2]=2, [4]=4
[3,1]=1, [1,2]=1, [2,4]=2
[3,1,2]=1, [1,2,4]=1
[3,1,2,4]=1
Sum = 3+1+2+4+1+1+2+1+1+1 = 17
```

**Hints**:
1. For each element, find how many subarrays it is the minimum of
2. Use monotonic stack to find `left[i]` = distance to previous smaller element, `right[i]` = distance to next smaller or equal element
3. Element `arr[i]` is the minimum of `left[i] * right[i]` subarrays; contribution = `arr[i] * left[i] * right[i]`

---

### 5. Remove K Digits — #402 (Medium)

**Problem**: Given a string of digits and integer k, remove k digits to make the resulting number as small as possible.

```
Input:  num="1432219", k=3
Output: "1219"
Explanation: Remove 4, 3, 2 → "1219"

Input:  num="10200", k=1
Output: "200"
Explanation: Remove 1 → "0200" → strip leading zero → "200"

Input:  num="10", k=2
Output: "0"
```

**Hints**:
1. Monotonic increasing stack — pop when current digit < top and k > 0
2. After processing, if k > 0, remove from the end
3. Strip leading zeros; return "0" if empty

---

### 6. 132 Pattern — #456 (Medium)

**Problem**: Given an array of n integers, check if there exists a 132 pattern: indices i < j < k such that `nums[i] < nums[k] < nums[j]`.

```
Input:  [1, 2, 3, 4]
Output: false  (no 132 pattern)

Input:  [3, 1, 4, 2]
Output: true   (1 < 2 < 4, indices 1,3,2)

Input:  [-1, 3, 2, 0]
Output: true   (-1 < 0 < 3, or -1 < 2 < 3)
```

**Hints**:
1. Iterate from right to left; maintain a monotonic decreasing stack
2. Track `third` = the largest value popped from the stack (this is the "2" in 132)
3. If current value < `third`, we found the "1" → return true
