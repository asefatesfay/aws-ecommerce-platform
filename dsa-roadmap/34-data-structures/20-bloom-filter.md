# Bloom Filter

## What is it?
A **space-efficient probabilistic data structure** that tests whether an element is a member of a set. It can have **false positives** (says "present" when it's not) but **never false negatives** (if it says "absent", the element is definitely not in the set).

## Visual Example
```
Bit array of size 10, using 3 hash functions h1, h2, h3:

Initial: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Insert "apple":
  h1("apple") = 2, h2("apple") = 5, h3("apple") = 8
  Set bits 2, 5, 8:
  [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]

Insert "banana":
  h1("banana") = 1, h2("banana") = 5, h3("banana") = 7
  Set bits 1, 5, 7:
  [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]

Query "apple":  bits 2,5,8 → all 1 → PROBABLY present ✓
Query "cherry": h1=0, h2=3, h3=6 → bit 0 is 0 → DEFINITELY absent ✓
Query "grape":  h1=1, h2=5, h3=7 → all 1 → FALSE POSITIVE! (not inserted)
```

## False Positive Rate
```
With m bits, k hash functions, n inserted elements:
False positive rate ≈ (1 - e^(-kn/m))^k

Optimal k = (m/n) * ln(2) ≈ 0.693 * (m/n)
Optimal m = -n * ln(p) / (ln 2)^2  for desired false positive rate p

Example: 1000 elements, 1% false positive rate
  m = -1000 * ln(0.01) / (ln 2)^2 ≈ 9585 bits ≈ 1.2 KB
  k = 7 hash functions
  Compare to: storing 1000 strings of avg 10 chars = 10 KB
```

## Implementation

```python
import math
import hashlib

class BloomFilter:
    """
    Bloom filter with configurable false positive rate.
    
    Example:
        bf = BloomFilter(capacity=1000, error_rate=0.01)
        bf.add("apple")
        bf.add("banana")
        bf.contains("apple")   # True (probably)
        bf.contains("cherry")  # False (definitely not)
        bf.contains("grape")   # Might be True (false positive)
    """
    def __init__(self, capacity, error_rate=0.01):
        self.capacity = capacity
        self.error_rate = error_rate
        # Optimal bit array size
        self.size = self._optimal_size(capacity, error_rate)
        # Optimal number of hash functions
        self.hash_count = self._optimal_hash_count(self.size, capacity)
        self.bit_array = bytearray(math.ceil(self.size / 8))
        self.count = 0

    def _optimal_size(self, n, p):
        """m = -n * ln(p) / (ln 2)^2"""
        return int(-n * math.log(p) / (math.log(2) ** 2))

    def _optimal_hash_count(self, m, n):
        """k = (m/n) * ln(2)"""
        return max(1, int((m / n) * math.log(2)))

    def _get_positions(self, item):
        """Generate k bit positions for item using k different hash seeds"""
        positions = []
        item_bytes = str(item).encode('utf-8')
        for i in range(self.hash_count):
            # Different seed for each hash function
            h = int(hashlib.md5(item_bytes + i.to_bytes(4, 'big')).hexdigest(), 16)
            positions.append(h % self.size)
        return positions

    def _set_bit(self, pos):
        self.bit_array[pos // 8] |= (1 << (pos % 8))

    def _get_bit(self, pos):
        return bool(self.bit_array[pos // 8] & (1 << (pos % 8)))

    def add(self, item):
        """Add item to filter — O(k)"""
        for pos in self._get_positions(item):
            self._set_bit(pos)
        self.count += 1

    def contains(self, item):
        """
        Check membership — O(k).
        True  → item PROBABLY in set (may be false positive)
        False → item DEFINITELY NOT in set
        """
        return all(self._get_bit(pos) for pos in self._get_positions(item))

    @property
    def false_positive_rate(self):
        """Current estimated false positive rate"""
        if self.count == 0:
            return 0.0
        return (1 - math.exp(-self.hash_count * self.count / self.size)) ** self.hash_count

    def __repr__(self):
        return (f"BloomFilter(size={self.size} bits={self.size//8} bytes, "
                f"k={self.hash_count}, items={self.count}, "
                f"fp_rate≈{self.false_positive_rate:.4f})")


class CountingBloomFilter:
    """
    Bloom filter that supports deletion by using counters instead of bits.
    Uses more space (4 bits per counter) but allows remove().
    """
    def __init__(self, capacity, error_rate=0.01):
        self.size = int(-capacity * math.log(error_rate) / (math.log(2) ** 2))
        self.hash_count = max(1, int((self.size / capacity) * math.log(2)))
        self.counters = [0] * self.size
        self.count = 0

    def _positions(self, item):
        item_bytes = str(item).encode('utf-8')
        return [int(hashlib.md5(item_bytes + i.to_bytes(4, 'big')).hexdigest(), 16) % self.size
                for i in range(self.hash_count)]

    def add(self, item):
        for pos in self._positions(item):
            self.counters[pos] += 1
        self.count += 1

    def remove(self, item):
        """Remove item (only safe if item was definitely added)"""
        if not self.contains(item):
            return False
        for pos in self._positions(item):
            self.counters[pos] -= 1
        self.count -= 1
        return True

    def contains(self, item):
        return all(self.counters[pos] > 0 for pos in self._positions(item))
```

## Example Usage
```python
bf = BloomFilter(capacity=1000, error_rate=0.01)
print(bf)  # BloomFilter(size=9585 bits=1198 bytes, k=7, items=0, fp_rate≈0.0000)

words = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words:
    bf.add(word)

print(bf.contains("apple"))      # True
print(bf.contains("banana"))     # True
print(bf.contains("grape"))      # False (or rare True = false positive)
print(bf.contains("mango"))      # False
print(bf)  # fp_rate≈0.0000 (very low with only 5/1000 items)

# Test false positive rate
import random, string
false_positives = 0
tests = 10000
for _ in range(tests):
    word = ''.join(random.choices(string.ascii_lowercase, k=8))
    if word not in words and bf.contains(word):
        false_positives += 1
print(f"Empirical FP rate: {false_positives/tests:.4f}")  # ≈ 0.01
```

## Real-World Uses
- **Google Chrome**: Safe Browsing — check if URL is malicious (local bloom filter, then server check)
- **Apache Cassandra**: Avoid disk reads for non-existent keys
- **Bitcoin**: SPV wallet transaction filtering
- **Medium**: Avoid showing already-read articles
- **Akamai CDN**: One-hit-wonder detection (don't cache items seen only once)

## When to Use
- "Is this item in a very large set?" with acceptable false positives
- Reduce expensive lookups (DB, network) for definitely-absent items
- Deduplication with space constraints
- Spam filtering, malware detection

## LeetCode Problems

Bloom filters don't map directly to LeetCode problems (they're a systems/infrastructure data structure), but the underlying concepts appear in these problems:

---

### 1. Contains Duplicate — #217 (Easy)

**Problem**: Given an integer array, return true if any value appears at least twice.

```
Input:  [1, 2, 3, 1]
Output: true

Input:  [1, 2, 3, 4]
Output: false

Input:  [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

**Bloom filter connection**: A bloom filter is a probabilistic version of this — it can tell you "definitely not a duplicate" or "probably a duplicate" using much less memory than a hash set.

**Hints**:
1. Use a hash set; add each element and check if it's already present
2. Alternatively, sort and check adjacent elements

---

### 2. Find the Duplicate Number — #287 (Medium)

**Problem**: Given an array of n+1 integers where each integer is in range [1, n], find the one duplicate number. Must use O(1) extra space and not modify the array.

```
Input:  [1, 3, 4, 2, 2]
Output: 2

Input:  [3, 1, 3, 4, 2]
Output: 3
```

**Bloom filter connection**: A bloom filter could detect the duplicate with very low memory, but with a small false positive risk. The O(1) space solution uses Floyd's cycle detection instead.

**Hints**:
1. Treat the array as a linked list: index → value → next index
2. The duplicate creates a cycle (two indices point to the same value)
3. Use Floyd's algorithm to find the cycle entry point

---

### 3. Distinct Echo Substrings — #1316 (Hard)

**Problem**: Return the number of distinct non-empty substrings of a string that can be written as the concatenation of some string with itself (e.g., "abab" = "ab"+"ab").

```
Input:  "abcabcabc"
Output: 3
Substrings: "abcabc", "bcabca", "cabcab" — each is a string repeated twice

Input:  "leetcodeleetcode"
Output: 2
Substrings: "leetcodeleetcode", "eetcodeeetcode"? 
Actually: "leetcodeleetcode" and "eetcodeeetcode" — 2 distinct echo substrings
```

**Bloom filter connection**: You need to track which substrings you've already counted — a bloom filter could do this with less memory (with small false positive risk). In practice, use a hash set.

**Hints**:
1. For each possible half-length L (1 to n//2), check all substrings of length 2L
2. A substring `s[i..i+2L-1]` is an echo if `s[i..i+L-1] == s[i+L..i+2L-1]`
3. Use rolling hash to compare substrings in O(1); store seen echo substrings in a set
