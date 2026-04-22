# Daily Practice — Pattern-Based Problem Sets

Each set focuses on one pattern. Do one set per day. For each problem:
1. Read the description
2. Try to identify the data structure / pattern (30 seconds)
3. Try to write the brute force (5 minutes)
4. Try to write the optimal (10 minutes)
5. Check the solution

---

## Day 1 — Hash Map Fundamentals

The hash map pattern: "I need to look something up quickly."

---

### Problem 1.1 — Contains Duplicate (Easy) #217

```
Given an integer array, return true if any value appears at least twice.

Input:  [1, 2, 3, 1]
Output: true  (1 appears twice)

Input:  [1, 2, 3, 4]
Output: false

Input:  [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

Brute force — check every pair:
```python
def contains_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# O(n²) time, O(1) space
```

Optimal — hash set:
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# O(n) time, O(n) space
```

Why hash set? "Have I seen this before?" is a membership check → O(1) with a set.

---

### Problem 1.2 — Valid Anagram (Easy) #242

```
Given two strings s and t, return true if t is an anagram of s.
An anagram uses the exact same characters, same number of times.

Input:  s="anagram", t="nagaram"
Output: true

Input:  s="rat", t="car"
Output: false
```

Brute force — sort both:
```python
def is_anagram_brute(s, t):
    return sorted(s) == sorted(t)
# O(n log n) time, O(n) space
```

Optimal — count characters:
```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
# O(n) time, O(1) space (at most 26 letters)
```

Why hash map? Counting = hash map. Compare two frequency maps.

---

### Problem 1.3 — Ransom Note (Easy) #383

```
Given two strings ransomNote and magazine, return true if ransomNote
can be constructed using the letters from magazine. Each letter in
magazine can only be used once.

Input:  ransomNote="a", magazine="b"
Output: false

Input:  ransomNote="aa", magazine="aab"
Output: true  (magazine has 2 a's, ransom needs 2)

Input:  ransomNote="aa", magazine="ab"
Output: false  (magazine only has 1 'a')
```

Brute force — for each letter in ransom, search magazine:
```python
def can_construct_brute(ransomNote, magazine):
    mag_list = list(magazine)
    for ch in ransomNote:
        if ch in mag_list:
            mag_list.remove(ch)  # O(n) per removal
        else:
            return False
    return True
# O(n × m) time
```

Optimal — count and compare:
```python
from collections import Counter

def can_construct(ransomNote, magazine):
    mag_count = Counter(magazine)
    for ch in ransomNote:
        if mag_count[ch] <= 0:
            return False
        mag_count[ch] -= 1
    return True
# O(n + m) time, O(1) space (26 letters max)
```

---

### Problem 1.4 — Isomorphic Strings (Easy) #205

```
Two strings are isomorphic if characters in s can be replaced to get t.
Each character maps to exactly one character (and vice versa).
No two characters may map to the same character.

Input:  s="egg", t="add"
Output: true  (e→a, g→d)

Input:  s="foo", t="bar"
Output: false  (o maps to both a and r? No — o→a first, then o→r conflicts)

Input:  s="paper", t="title"
Output: true  (p→t, a→i, e→l, r→e)
```

Brute force — check all mappings:
```python
def is_isomorphic_brute(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            s_to_t[cs] = ct
        if ct in t_to_s:
            if t_to_s[ct] != cs:
                return False
        else:
            t_to_s[ct] = cs
    return True
# O(n) time, O(1) space — this IS the optimal solution
```

Why two maps? You need bidirectional mapping. "a→b" and "b→a" must both be
consistent. One map isn't enough — "foo"→"bar" would pass with one map
(f→b, o→a, o→r fails) but you also need to check that no two s-chars map
to the same t-char.

---

## Day 2 — Stack Fundamentals

The stack pattern: "I need the most recent thing" or "I need to match pairs."

---

### Problem 2.1 — Remove All Adjacent Duplicates (Easy) #1047

```
Given a string, repeatedly remove pairs of adjacent equal characters
until no more can be removed.

Input:  "abbaca"
Output: "ca"
Trace:  "abbaca" → remove "bb" → "aaca" → remove "aa" → "ca"

Input:  "azxxzy"
Output: "ay"
Trace:  "azxxzy" → remove "xx" → "azzy" → remove "zz" → "ay"
```

Brute force — repeatedly scan and remove:
```python
def remove_duplicates_brute(s):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i+2:]
                changed = True
            else:
                i += 1
    return s
# O(n²) time — rescans after each removal
```

Optimal — stack:
```python
def remove_duplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()   # adjacent duplicate — remove both
        else:
            stack.append(ch)
    return ''.join(stack)
# O(n) time, O(n) space
```

Why stack? Each new character either matches the top (pop = remove pair)
or doesn't (push). The stack naturally handles chain reactions — after
removing "bb" from "abba", "a" and "a" are now adjacent on the stack.

---

### Problem 2.2 — Baseball Game (Easy) #682

```
You're keeping score. Operations:
  integer → record that score
  "+"     → record sum of previous two scores
  "D"     → record double of previous score
  "C"     → invalidate (remove) previous score

Input:  ["5","2","C","D","+"]
Output: 30

Trace:
  "5" → record 5.           scores: [5]
  "2" → record 2.           scores: [5, 2]
  "C" → remove last (2).    scores: [5]
  "D" → double last (5×2).  scores: [5, 10]
  "+" → sum last two (5+10).scores: [5, 10, 15]
  Total: 5 + 10 + 15 = 30
```

```python
def cal_points(operations):
    stack = []
    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)
# O(n) time, O(n) space
```

Why stack? "Previous score" = top of stack. "Remove previous" = pop.
Every operation works on the most recent element → LIFO → stack.

---

### Problem 2.3 — Next Greater Element I (Easy) #496

```
You have two arrays: nums1 (subset of nums2). For each element in nums1,
find the next greater element in nums2 (the first element to its right
that is larger). Return -1 if none exists.

Input:  nums1=[4,1,2], nums2=[1,3,4,2]
Output: [-1,3,-1]

Explanation:
  4 in nums2: [1,3,4,2]. Right of 4: [2]. No element > 4 → -1
  1 in nums2: [1,3,4,2]. Right of 1: [3,4,2]. First > 1 is 3 → 3
  2 in nums2: [1,3,4,2]. Right of 2: []. No element → -1
```

Brute force — for each element, scan right:
```python
def next_greater_brute(nums1, nums2):
    result = []
    for num in nums1:
        idx = nums2.index(num)
        found = -1
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > num:
                found = nums2[j]
                break
        result.append(found)
    return result
# O(n × m) time
```

Optimal — monotonic stack + hash map:
```python
def next_greater_element(nums1, nums2):
    # Precompute next greater for ALL elements in nums2
    nge = {}       # value → its next greater element
    stack = []     # decreasing stack

    for num in nums2:
        while stack and stack[-1] < num:
            nge[stack.pop()] = num   # num is the next greater for popped element
        stack.append(num)

    # Remaining elements have no next greater
    return [nge.get(num, -1) for num in nums1]
# O(n + m) time, O(n) space
```

Why monotonic stack? "Next greater element" = the classic monotonic stack
pattern. The stack holds elements waiting for their answer. When a larger
element arrives, it's the answer for everything smaller on the stack.

---

## Day 3 — Two Pointers

The two-pointer pattern: "I can narrow down from both ends" or "I need a
read pointer and a write pointer."

---

### Problem 3.1 — Valid Palindrome (Easy) #125

```
Given a string, determine if it's a palindrome considering only
alphanumeric characters and ignoring case.

Input:  "A man, a plan, a canal: Panama"
Output: true  (cleaned: "amanaplanacanalpanama")

Input:  "race a car"
Output: false  (cleaned: "raceacar")

Input:  " "
Output: true  (empty after cleaning)
```

Brute force — clean and reverse:
```python
def is_palindrome_brute(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
# O(n) time, O(n) space
```

Optimal — two pointers, no extra string:
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
# O(n) time, O(1) space
```

Why two pointers? Palindrome = same forwards and backwards. Compare from
both ends, skip non-alphanumeric characters.

---

### Problem 3.2 — Squares of a Sorted Array (Easy) #977

```
Given a sorted array, return an array of the squares of each number,
also sorted.

Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Input:  [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

Brute force — square and sort:
```python
def sorted_squares_brute(nums):
    return sorted(x * x for x in nums)
# O(n log n) time
```

Optimal — two pointers from both ends:
```python
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # fill result from the end (largest first)

    while left <= right:
        l_sq = nums[left] ** 2
        r_sq = nums[right] ** 2
        if l_sq > r_sq:
            result[pos] = l_sq
            left += 1
        else:
            result[pos] = r_sq
            right -= 1
        pos -= 1

    return result
# O(n) time, O(n) space (for result)
```

Why two pointers? The input is sorted, so the largest squares are at the
ENDS (large negatives on the left, large positives on the right). Compare
both ends, take the larger square, fill result from the back.

---

### Problem 3.3 — 3Sum (Medium) #15

```
Given an array, find all unique triplets that sum to zero.

Input:  [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  [0, 1, 1]
Output: []

Input:  [0, 0, 0]
Output: [[0, 0, 0]]
```

Brute force — three nested loops:
```python
def three_sum_brute(nums):
    nums.sort()
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i], nums[j], nums[k]))
    return [list(t) for t in result]
# O(n³) time
```

Optimal — fix one, two-pointer for the rest:
```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicate first element
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1   # skip duplicates
                while left < right and nums[right] == nums[right-1]:
                    right -= 1  # skip duplicates
                left += 1
                right -= 1
            elif total < 0:
                left += 1    # need larger sum
            else:
                right -= 1   # need smaller sum
    return result
# O(n²) time, O(1) extra space
```

Why two pointers? After sorting and fixing one element, the remaining
problem is "find two numbers that sum to -nums[i]" in a sorted array.
That's the classic two-pointer pattern from both ends.

---

## Day 4 — BFS / Queue

The BFS pattern: "level by level" or "shortest path in unweighted graph."

---

### Problem 4.1 — Flood Fill (Easy) #733

```
Given an image (2D grid of pixel colors), a starting pixel (sr, sc),
and a new color, flood fill: change the starting pixel and all
connected pixels of the same original color to the new color.

Input:  image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
Output: [[2,2,2],[2,2,0],[2,0,1]]

The pixel at (1,1) has color 1. All connected pixels with color 1
get changed to 2. The 0's and the isolated 1 at (2,2) don't change.
```

```python
from collections import deque

def flood_fill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image  # no change needed
    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = color
                queue.append((nr, nc))
    return image
# O(m × n) time, O(m × n) space
```

Why BFS? Spreading color to neighbors = exploring connected cells level by
level. BFS with a queue. (DFS also works here — both are fine for flood fill.)

---

### Problem 4.2 — 01 Matrix (Medium) #542

```
Given a matrix of 0s and 1s, for each cell find the distance to the
nearest 0. Distance = number of steps (up/down/left/right).

Input:
  [[0,0,0],
   [0,1,0],
   [1,1,1]]
Output:
  [[0,0,0],
   [0,1,0],
   [1,2,1]]

The 1 at (1,1) is 1 step from (0,1) which is 0. Distance = 1.
The 1 at (2,1) is 2 steps from (0,1). Distance = 2.
```

Brute force — BFS from each 1:
```python
def update_matrix_brute(mat):
    rows, cols = len(mat), len(mat[0])
    result = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                # BFS to find nearest 0
                queue = deque([(r, c, 0)])
                visited = {(r, c)}
                while queue:
                    cr, cc, dist = queue.popleft()
                    if mat[cr][cc] == 0:
                        result[r][c] = dist
                        break
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = cr+dr, cc+dc
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            queue.append((nr, nc, dist+1))
    return result
# O((m×n)²) time — BFS from every cell
```

Optimal — multi-source BFS from all 0s simultaneously:
```python
from collections import deque

def update_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    # Start BFS from ALL 0-cells at once
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = float('inf')  # mark as unvisited

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] > mat[r][c] + 1:
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))

    return mat
# O(m × n) time, O(m × n) space
```

Why multi-source BFS? Instead of asking "for each 1, where's the nearest 0?"
(expensive), flip it: "from all 0s, spread outward." Each cell gets its
distance the first time BFS reaches it. One BFS pass covers everything.

---

## Day 5 — Heap / Priority Queue

The heap pattern: "I always need the min or max" or "top k."

---

### Problem 5.1 — Last Stone Weight (Easy) #1046

```
You have a collection of stones with weights. Each turn, take the two
heaviest stones and smash them. If they're equal, both are destroyed.
If not, the lighter one is destroyed and the heavier one loses weight
equal to the lighter one. Return the weight of the last remaining stone
(or 0 if none).

Input:  [2, 7, 4, 1, 8, 1]
Output: 1

Trace:
  Heaviest: 8 and 7. Smash: 8-7=1. Stones: [2,4,1,1,1]
  Heaviest: 4 and 2. Smash: 4-2=2. Stones: [2,1,1,1]
  Heaviest: 2 and 1. Smash: 2-1=1. Stones: [1,1,1]
  Heaviest: 1 and 1. Smash: equal, both destroyed. Stones: [1]
  Return 1.
```

Brute force — sort each time:
```python
def last_stone_weight_brute(stones):
    while len(stones) > 1:
        stones.sort()
        a, b = stones.pop(), stones.pop()  # two largest
        if a != b:
            stones.append(a - b)
    return stones[0] if stones else 0
# O(n² log n) time — sort n times
```

Optimal — max-heap:
```python
import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]  # negate for max-heap
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)  # largest
        b = -heapq.heappop(heap)  # second largest
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
# O(n log n) time, O(n) space
```

Why heap? "Take the two heaviest" = need the max twice. Max-heap gives
the maximum in O(1) and removal in O(log n). Much faster than sorting
every round.

---

### Problem 5.2 — K Closest Points to Origin (Medium) #973

```
Given points on a 2D plane, return the k closest to the origin (0,0).
Distance = sqrt(x² + y²), but you don't need to compute the sqrt
(just compare x² + y²).

Input:  points=[[1,3],[-2,2]], k=1
Output: [[-2,2]]  (distance² = 4+4=8 < 1+9=10)

Input:  points=[[3,3],[5,-1],[-2,4]], k=2
Output: [[3,3],[-2,4]]  (distances²: 18, 26, 20 → two smallest: 18, 20)
```

Brute force — sort by distance:
```python
def k_closest_brute(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]
# O(n log n) time
```

Optimal — max-heap of size k:
```python
import heapq

def k_closest(points, k):
    heap = []  # max-heap (negate distances)
    for x, y in points:
        dist = -(x*x + y*y)  # negate for max-heap
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # remove farthest
    return [[x, y] for _, x, y in heap]
# O(n log k) time, O(k) space
```

Why heap of size k? I only need the k closest. A max-heap of size k
always holds the k smallest distances seen so far. When a new point is
closer than the farthest in the heap, it replaces it.

---

## Day 6 — Tree Recursion

The tree pattern: "return something up" or "pass something down."

---

### Problem 6.1 — Same Tree (Easy) #100

```
Given two binary trees, check if they are structurally identical
with the same node values.

Input:  p=[1,2,3], q=[1,2,3]
Output: true

Input:  p=[1,2], q=[1,null,2]
Output: false

Input:  p=[1,2,1], q=[1,1,2]
Output: false
```

```python
def is_same_tree(p, q):
    if not p and not q:
        return True          # both None → same
    if not p or not q:
        return False         # one None, one not → different
    if p.val != q.val:
        return False         # values differ
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# O(n) time, O(h) space (recursion depth)
```

Why recursion? Two trees are the same if: roots match, left subtrees match,
right subtrees match. That's a recursive definition.

---

### Problem 6.2 — Count Good Nodes (Medium) #1448

```
Given a binary tree, a node is "good" if there is no node with a
greater value on the path from the root to that node.

Input:
    3
   / \
  1   4
 /   / \
3   1   5

Output: 4  (good nodes: 3, 3, 4, 5)

Node 3 (root): no ancestor → good ✓
Node 1: ancestor 3 > 1 → not good
Node 4: no ancestor > 4 → good ✓
Node 3 (left-left): ancestors [3,1], max=3, 3 >= 3 → good ✓
Node 1 (right-left): ancestor 4 > 1 → not good
Node 5: no ancestor > 5 → good ✓
```

```python
def good_nodes(root):
    count = [0]

    def dfs(node, max_so_far):
        if not node:
            return
        if node.val >= max_so_far:
            count[0] += 1
        new_max = max(max_so_far, node.val)
        dfs(node.left, new_max)
        dfs(node.right, new_max)

    dfs(root, root.val)
    return count[0]
# O(n) time, O(h) space
```

Why pass state down? Each node needs to know the maximum value on the path
from root to itself. That's information from the parent → pass it down as
a parameter.

---

## What's Next

After completing these 6 days, cycle back and try the problems from the
drill section in `00-modeling-intuition.md` — but this time write the code,
not just name the data structure.

The progression:
1. Name the data structure (the drill)
2. Write the brute force
3. Write the optimal
4. Do it without looking at the solution
5. Do it in under 15 minutes

When you can do step 5 for a pattern, that pattern is muscle memory.
Move to the next one.
