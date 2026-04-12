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

| Problem | Difficulty | Pattern |
|---------|-----------|---------|
| Two Sum (#1) | Easy | Complement lookup |
| Valid Anagram (#242) | Easy | Frequency count |
| Group Anagrams (#49) | Medium | Sorted key grouping |
| Longest Substring Without Repeating (#3) | Medium | Sliding window |
| Subarray Sum Equals K (#560) | Medium | Prefix sum + hash map |
| Top K Frequent Elements (#347) | Medium | Frequency + heap |
| LRU Cache (#146) | Medium | Hash map + DLL |
| Isomorphic Strings (#205) | Easy | Bidirectional mapping |
| Word Pattern (#290) | Easy | Bidirectional mapping |
| Longest Consecutive Sequence (#128) | Medium | Set membership |
| Contains Duplicate II (#219) | Easy | Index tracking |
| Encode and Decode TinyURL (#535) | Medium | URL mapping |
