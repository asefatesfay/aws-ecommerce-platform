# Suffix Array

## What is it?
An array of all suffixes of a string, sorted in lexicographic order. Combined with the **LCP (Longest Common Prefix) array**, it enables powerful string operations in O(N log N) preprocessing and O(log N) or O(N) queries.

## Visual Example
```
String: "banana"
Index:   0123456 (including '$' sentinel)

All suffixes:
  0: "banana"
  1: "anana"
  2: "nana"
  3: "ana"
  4: "na"
  5: "a"

Sorted suffixes:
  5: "a"
  3: "ana"
  1: "anana"
  0: "banana"
  4: "na"
  2: "nana"

Suffix Array SA = [5, 3, 1, 0, 4, 2]
(indices of sorted suffixes)

LCP Array (longest common prefix between adjacent sorted suffixes):
LCP = [0, 1, 3, 0, 0, 2]
  SA[0]="a",      SA[1]="ana"    → LCP=1 ("a")
  SA[1]="ana",    SA[2]="anana"  → LCP=3 ("ana")
  SA[2]="anana",  SA[3]="banana" → LCP=0
  SA[3]="banana", SA[4]="na"     → LCP=0
  SA[4]="na",     SA[5]="nana"   → LCP=2 ("na")
```

## Implementation

```python
def build_suffix_array(s):
    """
    Build suffix array using O(N log N) prefix doubling algorithm.
    Returns SA where SA[i] = starting index of i-th smallest suffix.
    
    Example:
        build_suffix_array("banana")  → [5, 3, 1, 0, 4, 2]
    """
    n = len(s)
    # Initial ranking based on single characters
    sa = sorted(range(n), key=lambda i: s[i])
    rank = [0] * n
    rank[sa[0]] = 0
    for i in range(1, n):
        rank[sa[i]] = rank[sa[i-1]] + (s[sa[i]] != s[sa[i-1]])

    k = 1
    while k < n:
        # Sort by (rank[i], rank[i+k])
        def sort_key(i):
            return (rank[i], rank[i + k] if i + k < n else -1)
        sa = sorted(range(n), key=sort_key)
        # Update ranks
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            prev, curr = sa[i-1], sa[i]
            same = (rank[prev] == rank[curr] and
                    (rank[prev+k] if prev+k < n else -1) ==
                    (rank[curr+k] if curr+k < n else -1))
            new_rank[curr] = new_rank[prev] + (0 if same else 1)
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            break  # all ranks unique, done
        k *= 2

    return sa


def build_lcp_array(s, sa):
    """
    Build LCP array using Kasai's algorithm — O(N).
    LCP[i] = length of longest common prefix between SA[i-1] and SA[i].
    
    Example:
        s = "banana"
        sa = build_suffix_array(s)
        build_lcp_array(s, sa)  → [0, 1, 3, 0, 0, 2]
    """
    n = len(s)
    rank = [0] * n
    for i, v in enumerate(sa):
        rank[v] = i

    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i+h] == s[j+h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp


def longest_repeated_substring(s):
    """
    Find the longest repeated substring using suffix array + LCP.
    O(N log N) build + O(N) query.
    
    Example:
        longest_repeated_substring("banana")  → "ana"
        longest_repeated_substring("abcabc")  → "abc"
    """
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)
    max_lcp = max(lcp)
    if max_lcp == 0:
        return ""
    idx = lcp.index(max_lcp)
    return s[sa[idx]:sa[idx] + max_lcp]


def count_distinct_substrings(s):
    """
    Count distinct substrings using suffix array.
    Total substrings = N*(N+1)/2
    Subtract sum of LCP values (these are duplicates).
    O(N log N).
    """
    n = len(s)
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)
    total = n * (n + 1) // 2
    return total - sum(lcp)


def search_pattern(text, pattern):
    """
    Search for pattern in text using binary search on suffix array.
    O(M log N) where M = pattern length, N = text length.
    """
    sa = build_suffix_array(text)
    n, m = len(text), len(pattern)

    # Binary search for leftmost occurrence
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid]:sa[mid]+m] < pattern:
            lo = mid + 1
        else:
            hi = mid

    left = lo
    # Binary search for rightmost occurrence
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if text[sa[mid]:sa[mid]+m] <= pattern:
            lo = mid + 1
        else:
            hi = mid

    return [sa[i] for i in range(left, lo)
            if text[sa[i]:sa[i]+m] == pattern]
```

## Example Usage
```python
s = "banana"
sa = build_suffix_array(s)
lcp = build_lcp_array(s, sa)

print(sa)   # [5, 3, 1, 0, 4, 2]
print(lcp)  # [0, 1, 3, 0, 0, 2]

print(longest_repeated_substring("banana"))   # "ana"
print(longest_repeated_substring("abcabc"))   # "abc"
print(count_distinct_substrings("abc"))        # 6
print(search_pattern("banana", "ana"))         # [1, 3]
```

## When to Use
- Longest repeated substring
- Longest common substring of two strings
- Count distinct substrings
- Pattern matching (multiple patterns efficiently)
- Bioinformatics (DNA sequence analysis)

## LeetCode Problems

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| Longest Duplicate Substring (#1044) | Hard | Suffix array + binary search |
| Longest Common Substring | Classic | Suffix array + LCP |
| Number of Distinct Substrings | Classic | Suffix array + LCP sum |
| Shortest Palindrome (#214) | Hard | KMP / suffix array |
| Longest Happy Prefix (#1392) | Hard | KMP / Z-function |
