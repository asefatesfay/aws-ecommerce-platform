# Strings

Strings are arrays of characters with extra constraints and operations. Most string problems reduce to array problems, but strings have unique patterns worth knowing.

Each problem page in this section includes a Python implementation, complexity summary, and typical interview use cases.

## Key Concepts

- **Immutability:** In Python and Java, strings are immutable. Building a string character by character in a loop is O(n²). Use a list/StringBuilder and join at the end.
- **Character frequency:** A 26-element array (for lowercase letters) is often more efficient than a HashMap.
- **Two-pointer on strings:** Palindrome checks, reversals, and comparisons often use two pointers.
- **Sliding window:** Substring problems with a constraint → sliding window.

## Pattern Recognition

- "Palindrome" → two pointers from both ends, or expand from center
- "Anagram" → character frequency comparison (sort or count array)
- "Subsequence" → two pointers (greedy matching)
- "Substring with condition" → sliding window
- "Common prefix" → vertical scan or binary search on length

## Common Techniques

### Character Frequency Array
For lowercase letters only: `freq = [0] * 26`, access with `ord(c) - ord('a')`.

### Two-Pointer Palindrome Check
Left pointer at 0, right pointer at end. Move inward while characters match.

### Expand Around Center
For palindromic substrings: try each character (and each gap between characters) as a center, expand outward while characters match.

## Visual Playbook

### Valid Palindrome (Two-Pointer)

**Input:** `"A man, a plan, a canal: Panama"`
**Output:** `true`

```mermaid
flowchart TD
	A[Set left and right pointers] --> B[Skip non-alphanumeric chars]
	B --> C{lower(s[left]) == lower(s[right])?}
	C -- No --> D[Return false]
	C -- Yes --> E[Move inward]
	E --> F{left < right?}
	F -- Yes --> B
	F -- No --> G[Return true]
```

### Subsequence Check

**Input:** `s = "abc", t = "ahbgdc"`
**Output:** `true`

```mermaid
flowchart TD
	A[Pointer i on s, j on t] --> B{j at end of t?}
	B -- Yes --> C{all chars in s matched?}
	C -- Yes --> D[Return true]
	C -- No --> E[Return false]
	B -- No --> F{s[i] == t[j]?}
	F -- Yes --> G[i += 1, j += 1]
	F -- No --> H[j += 1]
	G --> B
	H --> B
```

Why these visuals matter:
- Many string tasks are pointer movement problems.
- Flow diagrams make skip/compare rules easy to remember in interviews.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Reverse String](./reverse-string.md) | Easy |
| [Length of Last Word](./length-of-last-word.md) | Easy |
| [Find the Index of the First Occurrence in a String](./find-the-index-of-the-first-occurrence-in-a-string.md) | Easy |
| [Valid Palindrome](./valid-palindrome.md) | Easy |
| [Valid Palindrome II](./valid-palindrome-ii.md) | Easy |
| [Longest Palindrome](./longest-palindrome.md) | Easy |
| [Valid Anagram](./valid-anagram.md) | Easy |
| [Rotate String](./rotate-string.md) | Easy |
| [Is Subsequence](./is-subsequence.md) | Easy |
| [Longest Common Prefix](./longest-common-prefix.md) | Easy |
| [Zigzag Conversion](./zigzag-conversion.md) | Medium |
| [Reverse Words in a String](./reverse-words-in-a-string.md) | Medium |
| [One Edit Distance](./one-edit-distance.md) | Medium |
| [Count and Say](./count-and-say.md) | Medium |
| [Determine if Two Strings Are Close](./determine-if-two-strings-are-close.md) | Medium |
| [Add Bold Tag in String](./add-bold-tag-in-string.md) | Medium |
| [Guess the Word](./guess-the-word.md) | Hard |
| [Text Justification](./text-justification.md) | Hard |
