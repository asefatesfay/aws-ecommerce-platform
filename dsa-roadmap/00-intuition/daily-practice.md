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

Brute force — try all possible character mappings:
```python
def is_isomorphic_brute(s, t):
    """
    For each unique char in s, check if it consistently maps to one char in t.
    Also check no two s-chars map to the same t-char.
    """
    if len(s) != len(t):
        return False
    # Build mapping by scanning
    mapping = {}
    for cs, ct in zip(s, t):
        if cs in mapping:
            if mapping[cs] != ct:
                return False  # cs mapped to two different chars
        else:
            # Check no other s-char already maps to ct
            if ct in mapping.values():  # O(n) scan each time!
                return False
            mapping[cs] = ct
    return True
# O(n²) time — mapping.values() scan is O(n) per character
# O(n) space
```

Optimal — two hash maps for bidirectional mapping:
```python
def is_isomorphic(s, t):
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
# O(n) time, O(1) space (at most 256 ASCII chars)
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

Brute force — process operations with an array (no stack abstraction):
```python
def cal_points_brute(operations):
    scores = []
    for op in operations:
        if op == "+":
            scores.append(scores[len(scores)-1] + scores[len(scores)-2])
        elif op == "D":
            scores.append(scores[len(scores)-1] * 2)
        elif op == "C":
            scores = scores[:-1]  # rebuild list without last element
        else:
            scores.append(int(op))
    return sum(scores)
# O(n²) time in worst case — scores[:-1] copies the entire list each time
```

Optimal — stack (list with append/pop):
```python
def cal_points(operations):
    stack = []
    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()   # O(1) removal from end
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

Brute force — DFS (recursive, uses call stack instead of explicit queue):
```python
def flood_fill_brute(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image
    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image
# O(m × n) time, O(m × n) space (recursion stack — can overflow on large grids)
```

Optimal — BFS (iterative, no recursion depth limit):
```python
from collections import deque

def flood_fill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image
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
# O(m × n) time, O(m × n) space (queue — no recursion depth issues)
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

Brute force — serialize both trees and compare strings:
```python
def is_same_tree_brute(p, q):
    def serialize(node):
        if not node:
            return "null,"
        return str(node.val) + "," + serialize(node.left) + serialize(node.right)
    return serialize(p) == serialize(q)
# O(n) time, O(n) space — builds two full strings
```

Optimal — recursive comparison (no extra strings):
```python
def is_same_tree(p, q):
    if not p and not q:
        return True          # both None → same
    if not p or not q:
        return False         # one None, one not → different
    if p.val != q.val:
        return False         # values differ
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# O(n) time, O(h) space (recursion depth only, no extra data structures)
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

Brute force — collect all root-to-node paths, check each:
```python
def good_nodes_brute(root):
    count = 0
    def dfs(node, path):
        nonlocal count
        if not node:
            return
        path.append(node.val)
        if node.val >= max(path[:-1]) if len(path) > 1 else True:
            count += 1
        dfs(node.left, path)
        dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return count
# O(n × h) time — max(path) is O(h) per node
# O(h) space
```

Optimal — pass max_so_far down (no path storage, no max() call):
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
# O(n) time — O(1) work per node
# O(h) space
```

Why pass state down? Each node needs to know the maximum value on the path
from root to itself. That's information from the parent → pass it down as
a parameter.

---

## Day 7 — Linked List

The linked list pattern: "pointer manipulation" and "can't go backward."

---

### Problem 7.1 — Reverse Linked List (Easy) #206

```
Given the head of a singly linked list, reverse it.

Input:  [1] → [2] → [3] → [4] → [5]
Output: [5] → [4] → [3] → [2] → [1]

Input:  [1] → [2]
Output: [2] → [1]

Input:  []
Output: []
```

Brute force — collect values, rebuild:
```python
def reverse_brute(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    curr = head
    for v in reversed(vals):
        curr.val = v
        curr = curr.next
    return head
# O(n) time, O(n) space — stores all values
```

Optimal — three pointers in-place:
```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next      # save next before cutting
        curr.next = prev     # redirect arrow backward
        prev = curr          # advance prev
        curr = nxt           # advance curr
    return prev              # prev is the new head
# O(n) time, O(1) space
```

Why three pointers? You're about to cut `curr.next`, so you must save it
first in `nxt`. Without `nxt`, you lose the rest of the list.

---

### Problem 7.2 — Merge Two Sorted Lists (Easy) #21

```
Merge two sorted linked lists into one sorted list.

Input:  l1 = [1] → [2] → [4],  l2 = [1] → [3] → [4]
Output: [1] → [1] → [2] → [3] → [4] → [4]

Input:  l1 = [],  l2 = [0]
Output: [0]
```

Brute force — collect all values, sort, rebuild:
```python
def merge_brute(l1, l2):
    vals = []
    while l1:
        vals.append(l1.val); l1 = l1.next
    while l2:
        vals.append(l2.val); l2 = l2.next
    vals.sort()
    dummy = curr = ListNode(0)
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
# O(n log n) time, O(n) space
```

Optimal — pointer weaving with dummy head:
```python
def merge_two_lists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2   # attach remaining
    return dummy.next
# O(n + m) time, O(1) space
```

Why dummy head? The first node of the result is unknown until we compare
l1 and l2. A dummy node avoids a special case for the first attachment.

---

### Problem 7.3 — Linked List Cycle (Easy) #141

```
Given a linked list, determine if it has a cycle.

Input:  [3] → [2] → [0] → [-4] → (back to [2])
Output: true

Input:  [1] → None
Output: false
```

Brute force — hash set:
```python
def has_cycle_brute(head):
    seen = set()
    curr = head
    while curr:
        if id(curr) in seen:
            return True
        seen.add(id(curr))
        curr = curr.next
    return False
# O(n) time, O(n) space
```

Optimal — Floyd's slow/fast:
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# O(n) time, O(1) space
```

Why slow/fast? If there's a cycle, fast will eventually lap slow (like two
runners on a circular track). If no cycle, fast reaches None.

---

## Day 8 — Binary Search

The binary search pattern: "sorted data" or "search space that can be halved."

---

### Problem 8.1 — Binary Search (Easy) #704

```
Given a sorted array and a target, return the index of the target.
Return -1 if not found.

Input:  nums=[-1,0,3,5,9,12], target=9
Output: 4

Input:  nums=[-1,0,3,5,9,12], target=2
Output: -1
```

Brute force — linear scan:
```python
def search_brute(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
# O(n) time
```

Optimal — binary search:
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# O(log n) time, O(1) space
```

Why binary search? The array is sorted. Each comparison eliminates half
the remaining elements. 1 million elements → only 20 comparisons.

---

### Problem 8.2 — First Bad Version (Easy) #278

```
You have n versions [1, 2, ..., n]. One version is bad, and all
versions after it are bad too. Given an API isBadVersion(version),
find the first bad version. Minimize API calls.

Input:  n=5, bad=4
  isBadVersion(3) → false
  isBadVersion(5) → true
  isBadVersion(4) → true
Output: 4
```

Brute force — check each version:
```python
def first_bad_version_brute(n):
    for i in range(1, n + 1):
        if isBadVersion(i):
            return i
# O(n) API calls
```

Optimal — binary search:
```python
def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid      # mid might be the first bad
        else:
            left = mid + 1   # first bad is after mid
    return left
# O(log n) API calls
```

Why `left < right` (not `<=`)? We're looking for a boundary, not a specific
value. When `left == right`, we've found the first bad version.

---

### Problem 8.3 — Search Insert Position (Easy) #35

```
Given a sorted array and a target, return the index where the target
is found. If not found, return the index where it would be inserted.

Input:  nums=[1,3,5,6], target=5
Output: 2  (found at index 2)

Input:  nums=[1,3,5,6], target=2
Output: 1  (would insert between 1 and 3)

Input:  nums=[1,3,5,6], target=7
Output: 4  (would insert at the end)
```

Brute force — linear scan:
```python
def search_insert_brute(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)
# O(n) time
```

Optimal — binary search:
```python
def search_insert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
# O(log n) time
```

This is `bisect_left` — finds the leftmost position where target could
be inserted to keep the array sorted.

---

## Day 9 — Graph Traversal

The graph pattern: "connections between things" + "visited set."

---

### Problem 9.1 — Find if Path Exists in Graph (Easy) #1971

```
Given n nodes (0 to n-1) and edges, determine if there's a path
between source and destination.

Input:  n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2
Output: true  (path: 0→1→2 or 0→2)

Input:  n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, destination=5
Output: false  (0 is in {0,1,2}, 5 is in {3,4,5} — disconnected)
```

Brute force — BFS:
```python
from collections import deque, defaultdict

def valid_path_bfs(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = {source}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
# O(V + E) time, O(V + E) space
```

Optimal — DFS (same complexity, less overhead for this problem):
```python
from collections import defaultdict

def valid_path(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()

    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(source)
# O(V + E) time, O(V + E) space
```

Both are O(V+E). DFS uses recursion stack, BFS uses explicit queue.
For "does a path exist?" either works. For "shortest path?" use BFS.

---

### Problem 9.2 — Number of Islands (Medium) #200

```
Given a 2D grid of '1' (land) and '0' (water), count the number
of islands. An island is a group of connected '1's (horizontally
or vertically).

Input:
  [["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]]
Output: 3
```

Brute force — visited set (extra space):
```python
def num_islands_brute(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (r,c) in visited or r<0 or r>=rows or c<0 or c>=cols:
            return
        if grid[r][c] != '1':
            return
        visited.add((r, c))
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                dfs(r, c)
                count += 1
    return count
# O(m×n) time, O(m×n) space for visited set
```

Optimal — sink islands in-place (no extra set):
```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1':
            return
        grid[r][c] = '0'   # sink — mark visited by modifying grid
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
# O(m×n) time, O(m×n) recursion stack, but no extra visited set
```

Why modify the grid? Setting `grid[r][c] = '0'` serves as the visited
marker. No need for a separate set. Saves space (if modifying input is ok).

---

## Day 10 — Sliding Window

The sliding window pattern: "contiguous subarray/substring with a condition."

---

### Problem 10.1 — Maximum Average Subarray I (Easy) #643

```
Given an array and integer k, find the contiguous subarray of length k
with the maximum average. Return the average.

Input:  nums=[1,12,-5,-6,50,3], k=4
Output: 12.75  (subarray [12,-5,-6,50] has sum 51, avg 51/4=12.75)
```

Brute force — compute sum for every window:
```python
def find_max_average_brute(nums, k):
    best = float('-inf')
    for i in range(len(nums) - k + 1):
        window_sum = sum(nums[i:i+k])   # O(k) per window
        best = max(best, window_sum)
    return best / k
# O(n × k) time
```

Optimal — sliding window (add right, subtract left):
```python
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]   # slide: add right, remove left
        best = max(best, window_sum)
    return best / k
# O(n) time, O(1) space
```

Why sliding window? Each window overlaps with the previous by k-1 elements.
Instead of recomputing the sum from scratch, just add the new element and
subtract the one that left the window.

---

### Problem 10.2 — Minimum Size Subarray Sum (Medium) #209

```
Given a positive integer array and a target, find the minimal length
of a subarray whose sum is >= target. Return 0 if no such subarray.

Input:  target=7, nums=[2,3,1,2,4,3]
Output: 2  (subarray [4,3] has sum 7 >= 7, length 2)

Input:  target=4, nums=[1,4,4]
Output: 1  (subarray [4] has sum 4 >= 4)

Input:  target=11, nums=[1,1,1,1,1,1,1,1]
Output: 0  (total sum = 8 < 11)
```

Brute force — try all subarrays:
```python
def min_subarray_len_brute(target, nums):
    n = len(nums)
    best = float('inf')
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total >= target:
                best = min(best, j - i + 1)
                break
    return best if best != float('inf') else 0
# O(n²) time
```

Optimal — variable-size sliding window:
```python
def min_subarray_len(target, nums):
    left = 0
    total = 0
    best = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return best if best != float('inf') else 0
# O(n) time — each element added and removed at most once
```

Why variable window? Expand right to grow the sum. Once sum >= target,
shrink left to find the minimum length. Each element enters and leaves
the window at most once → O(n) total.

---

### Problem 10.3 — Permutation in String (Medium) #567

```
Given two strings s1 and s2, return true if s2 contains a permutation
of s1 (i.e., a substring of s2 that is an anagram of s1).

Input:  s1="ab", s2="eidbaooo"
Output: true  (s2 contains "ba" which is a permutation of "ab")

Input:  s1="ab", s2="eidboaoo"
Output: false
```

Brute force — check every substring of length len(s1):
```python
from collections import Counter

def check_inclusion_brute(s1, s2):
    n1, n2 = len(s1), len(s2)
    target = Counter(s1)
    for i in range(n2 - n1 + 1):
        if Counter(s2[i:i+n1]) == target:   # O(n1) per window
            return True
    return False
# O(n2 × n1) time
```

Optimal — fixed-size sliding window with frequency map:
```python
from collections import Counter

def check_inclusion(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
    target = Counter(s1)
    window = Counter(s2[:n1])
    if window == target:
        return True
    for i in range(n1, n2):
        window[s2[i]] += 1           # add right
        left_char = s2[i - n1]
        window[left_char] -= 1       # remove left
        if window[left_char] == 0:
            del window[left_char]
        if window == target:
            return True
    return False
# O(n2) time — each slide updates 2 counts and compares (O(26) = O(1))
```

Why fixed-size window? We're looking for a substring of exactly length
len(s1). Slide a window of that size across s2, maintaining character
counts. When counts match → permutation found.

---

## Day 11 — Union-Find

The union-find pattern: "grouping things" and "are these two connected?"

---

### Problem 11.1 — Number of Provinces (Medium) #547

```
There are n cities. isConnected[i][j] = 1 means city i and j are
directly connected. A province is a group of directly or indirectly
connected cities. How many provinces?

Input:  [[1,1,0],[1,1,0],[0,0,1]]
Output: 2  (cities 0,1 connected; city 2 alone)

Input:  [[1,0,0],[0,1,0],[0,0,1]]
Output: 3  (all isolated)
```

Brute force — DFS from each unvisited city:
```python
def find_circle_num_dfs(isConnected):
    n = len(isConnected)
    visited = set()
    count = 0

    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    for city in range(n):
        if city not in visited:
            dfs(city)
            count += 1
    return count
# O(n²) time, O(n) space
```

Optimal — Union-Find:
```python
def find_circle_num(isConnected):
    n = len(isConnected)
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])   # path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                union(i, j)

    return len(set(find(i) for i in range(n)))
# O(n² × α(n)) time ≈ O(n²), O(n) space
```

Both are O(n²) here because we scan the full matrix. Union-Find shines
when edges arrive one at a time (streaming) or when you need to merge
groups dynamically.

---

### Problem 11.2 — Redundant Connection (Medium) #684

```
A tree of n nodes has one extra edge, creating a cycle. Given the
edges in order, return the edge that creates the cycle. If multiple
answers, return the last one in the input.

Input:  [[1,2],[1,3],[2,3]]
Output: [2,3]  (adding [2,3] creates cycle 1-2-3-1)

Input:  [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

Brute force — for each edge, check if removing it makes a valid tree:
```python
def find_redundant_brute(edges):
    from collections import defaultdict, deque
    n = len(edges)
    for skip in range(n - 1, -1, -1):   # try removing last edge first
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            if i == skip:
                continue
            graph[u].append(v)
            graph[v].append(u)
        # Check if all nodes connected (BFS from node 1)
        visited = {1}
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        if len(visited) == n:
            return edges[skip]
# O(n²) time
```

Optimal — Union-Find (process edges in order):
```python
def find_redundant_connection(edges):
    n = len(edges)
    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for u, v in edges:
        pu, pv = find(u), find(v)
        if pu == pv:
            return [u, v]   # already connected → this edge is redundant
        parent[pu] = pv     # union
    return []
# O(n × α(n)) ≈ O(n) time
```

Why Union-Find? Process edges one by one. If two nodes are already in the
same group when we try to connect them, this edge creates a cycle.

---

## Day 12 — Mixed Patterns (Interview Simulation)

These problems combine multiple patterns. Try to identify which ones.

---

### Problem 12.1 — Product of Array Except Self (Medium) #238

```
Given an array, return an array where output[i] = product of all
elements except nums[i]. No division allowed. Must be O(n).

Input:  [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input:  [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

Brute force — multiply everything except current:
```python
def product_except_self_brute(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
# O(n²) time
```

Optimal — prefix × suffix in two passes:
```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
# O(n) time, O(1) extra space
```

Pattern: prefix/suffix decomposition. `result[i] = product_of_left × product_of_right`.

---

### Problem 12.2 — Top K Frequent Elements (Medium) #347

```
Given an array and integer k, return the k most frequent elements.

Input:  nums=[1,1,1,2,2,3], k=2
Output: [1,2]  (1 appears 3 times, 2 appears 2 times)

Input:  nums=[1], k=1
Output: [1]
```

Brute force — count, sort by frequency:
```python
from collections import Counter

def top_k_frequent_brute(nums, k):
    counts = Counter(nums)
    return [num for num, _ in counts.most_common(k)]
# O(n log n) time (sorting)
```

Optimal — hash map + heap:
```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.get)
# O(n log k) time — heap of size k
```

Alternative optimal — bucket sort:
```python
from collections import Counter

def top_k_frequent_bucket(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(buckets) - 1, -1, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result
# O(n) time — no sorting needed
```

Pattern: hash map (count) + heap (top k) or bucket sort (O(n)).

---

### Problem 12.3 — Course Schedule (Medium) #207

```
There are n courses (0 to n-1). prerequisites[i] = [a, b] means
"take b before a." Can you finish all courses?

Input:  n=2, prerequisites=[[1,0]]
Output: true  (take 0 then 1)

Input:  n=2, prerequisites=[[1,0],[0,1]]
Output: false  (circular: 0 needs 1, 1 needs 0)
```

Brute force — topological sort (Kahn's BFS):
```python
from collections import deque, defaultdict

def can_finish_kahn(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1
    queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return count == numCourses
# O(V + E) time
```

Optimal — DFS cycle detection (3-color):
```python
from collections import defaultdict

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * numCourses

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return False   # cycle!
            if color[neighbor] == WHITE and not dfs(neighbor):
                return False
        color[node] = BLACK
        return True

    return all(dfs(i) for i in range(numCourses) if color[i] == WHITE)
# O(V + E) time
```

Pattern: graph + cycle detection. Both approaches are O(V+E). Kahn's is
BFS-based (count processed nodes). DFS 3-color detects back edges.

---

## What's Next

After completing these 12 days, cycle back and try the problems from the
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
