# Hash Map

## What is it?
A data structure that maps keys to values using a hash function. Provides O(1) average-case get, put, and delete. Handles collisions via separate chaining (linked lists per bucket) or open addressing.

## Visual Example
```
HashMap with capacity=8, hash(key) = key % 8

put(5, "five"):   bucket[5] → [(5,"five")]
put(13, "thirteen"): hash(13)=5, bucket[5] → [(5,"five"),(13,"thirteen")]
put(3, "three"):  bucket[3] → [(3,"three")]

get(13): hash(13)=5, scan bucket[5] → "thirteen"
get(7):  hash(7)=7,  bucket[7] is empty → None

Load factor = 3/8 = 0.375 (resize at 0.75)
```

## Implementation

```python
class HashMap:
    """
    Hash map with separate chaining.
    Resizes when load factor exceeds 0.75.
    """
    def __init__(self, capacity=16):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(capacity)]
        self._LOAD_FACTOR = 0.75

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        """O(1) average"""
        if self._size / self._capacity >= self._LOAD_FACTOR:
            self._resize()
        idx = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)  # update
                return
        self._buckets[idx].append((key, value))  # insert
        self._size += 1

    def get(self, key, default=None):
        """O(1) average"""
        for k, v in self._buckets[self._hash(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        """O(1) average"""
        idx = self._hash(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx].pop(i)
                self._size -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key) is not None

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    def __len__(self):
        return self._size

    def __setitem__(self, key, value): self.put(key, value)
    def __getitem__(self, key):
        v = self.get(key)
        if v is None: raise KeyError(key)
        return v
    def __contains__(self, key): return self.contains(key)
```

## Common Patterns

### Frequency Counting
```python
from collections import Counter, defaultdict

# Count character frequencies
s = "aabbccaaa"
freq = Counter(s)          # {'a': 5, 'b': 2, 'c': 2}
freq2 = defaultdict(int)
for ch in s: freq2[ch] += 1

# Most common k elements
print(freq.most_common(2))  # [('a', 5), ('b', 2)]
```

### Two Sum Pattern
```python
def two_sum(nums, target):
    """O(N) using hash map — LeetCode #1"""
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

### Sliding Window with Hash Map
```python
def length_of_longest_substring(s):
    """LeetCode #3 — O(N)"""
    char_index = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

## When to Use
- Frequency counting
- Two-sum / complement lookup
- Caching / memoization
- Grouping elements (group anagrams)
- Detecting duplicates
- Mapping relationships

## LeetCode Problems

---

### 1. Two Sum — #1 (Easy)

**Problem**: Given an array of integers and a target, return the indices of the two numbers that add up to the target. Each input has exactly one solution; you may not use the same element twice.

```
Input:  nums=[2,7,11,15], target=9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Input:  nums=[3,2,4], target=6
Output: [1,2]

Input:  nums=[3,3], target=6
Output: [0,1]
```

**Hints**:
1. For each number, check if `target - num` is already in the map
2. Store `{value → index}` as you iterate
3. One pass is enough — you find the complement before storing the current number

---

### 2. Group Anagrams — #49 (Medium)

**Problem**: Given an array of strings, group the anagrams together. Return the groups in any order.

```
Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input:  [""]
Output: [[""]]

Input:  ["a"]
Output: [["a"]]
```

**Hints**:
1. Two strings are anagrams if their sorted characters are equal
2. Use `sorted(word)` as the key in a hash map
3. Group all words with the same sorted key together

---

### 3. Longest Substring Without Repeating Characters — #3 (Medium)

**Problem**: Given a string, find the length of the longest substring without repeating characters.

```
Input:  "abcabcbb"
Output: 3  (substring "abc")

Input:  "bbbbb"
Output: 1  (substring "b")

Input:  "pwwkew"
Output: 3  (substring "wke")
```

**Hints**:
1. Sliding window with a hash map storing `{char → last_seen_index}`
2. When a duplicate is found, move the left pointer to `last_seen[char] + 1`
3. Window size = `right - left + 1`; track the maximum

---

### 4. Subarray Sum Equals K — #560 (Medium)

**Problem**: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

```
Input:  nums=[1,1,1], k=2
Output: 2  (subarrays [1,1] at indices [0,1] and [1,2])

Input:  nums=[1,2,3], k=3
Output: 2  (subarrays [3] and [1,2])

Input:  nums=[1,-1,1], k=1
Output: 3
```

**Hints**:
1. Use prefix sums: `prefix[i] - prefix[j] = k` means subarray `[j+1..i]` sums to k
2. Rearranged: `prefix[j] = prefix[i] - k`
3. Store prefix sum counts in a hash map; for each new prefix sum, check how many times `prefix - k` has appeared

---

### 5. Top K Frequent Elements — #347 (Medium)

**Problem**: Given an integer array and an integer k, return the k most frequent elements. The answer may be in any order.

```
Input:  nums=[1,1,1,2,2,3], k=2
Output: [1,2]

Input:  nums=[1], k=1
Output: [1]
```

**Hints**:
1. Count frequencies with a hash map
2. Use a min-heap of size k: push `(freq, num)`, pop when size exceeds k
3. Alternative: bucket sort — create buckets indexed by frequency (0 to n), then scan from high to low

---

### 6. Longest Consecutive Sequence — #128 (Medium)

**Problem**: Given an unsorted array of integers, return the length of the longest consecutive elements sequence. Must run in O(N).

```
Input:  [100, 4, 200, 1, 3, 2]
Output: 4  (sequence: 1, 2, 3, 4)

Input:  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9  (sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8)
```

**Hints**:
1. Put all numbers in a set for O(1) lookup
2. Only start counting from a number `n` if `n-1` is NOT in the set (it's the start of a sequence)
3. From each start, count how far the consecutive sequence extends
