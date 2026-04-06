# Sliding Window

The sliding window technique maintains a contiguous subarray (window) and efficiently updates it by adding elements to one end and removing from the other, avoiding redundant recomputation.

## Fixed vs Variable Window

### Fixed Window
Window size is constant. Slide by removing the leftmost element and adding the next right element.
- Pattern: initialize first window, then slide one step at a time.

### Variable Window
Window size changes based on a constraint. Expand right to include more elements; shrink left when the constraint is violated.
- Pattern: expand right pointer always; shrink left pointer when constraint violated.

## When to Recognize Sliding Window

- "Subarray/substring of length k" → fixed window
- "Longest/shortest subarray with [condition]" → variable window
- "Number of subarrays with [condition]" → often variable window or "at most k" trick
- Constraint involves a contiguous sequence

## The "At Most K" Trick

For "exactly k" problems: `count(exactly k) = count(at most k) - count(at most k-1)`. This converts an "exactly" constraint into two "at most" sliding window problems.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Maximum Average Subarray I](./maximum-average-subarray-i.md) | Easy |
| [Find All Anagrams in a String](./find-all-anagrams-in-a-string.md) | Medium |
| [Permutation in String](./permutation-in-string.md) | Medium |
| [Maximum Sum of Distinct Subarrays With Length K](./maximum-sum-of-distinct-subarrays-with-length-k.md) | Medium |
| [Maximum Number of Vowels in a Substring of Given Length](./maximum-number-of-vowels-in-a-substring-of-given-length.md) | Medium |
| [Substring with Concatenation of All Words](./substring-with-concatenation-of-all-words.md) | Hard |
| [Longest Substring Without Repeating Characters](./longest-substring-without-repeating-characters.md) | Medium |
| [Longest Repeating Character Replacement](./longest-repeating-character-replacement.md) | Medium |
| [Minimum Size Subarray Sum](./minimum-size-subarray-sum.md) | Medium |
| [Max Consecutive Ones III](./max-consecutive-ones-iii.md) | Medium |
| [Count Number of Nice Subarrays](./count-number-of-nice-subarrays.md) | Medium |
| [Fruit Into Baskets](./fruit-into-baskets.md) | Medium |
| [Maximum Points You Can Obtain from Cards](./maximum-points-you-can-obtain-from-cards.md) | Medium |
| [Subarray Product Less Than K](./subarray-product-less-than-k.md) | Medium |
| [Frequency of the Most Frequent Element](./frequency-of-the-most-frequent-element.md) | Medium |
| [Longest Substring with At Most Two Distinct Characters](./longest-substring-with-at-most-two-distinct-characters.md) | Medium |
| [Longest Substring with At Most K Distinct Characters](./longest-substring-with-at-most-k-distinct-characters.md) | Medium |
| [Longest Substring with At Least K Repeating Characters](./longest-substring-with-at-least-k-repeating-characters.md) | Medium |
| [Minimum Window Substring](./minimum-window-substring.md) | Hard |
| [Minimum Window Subsequence](./minimum-window-subsequence.md) | Hard |
| [Subarrays with K Different Integers](./subarrays-with-k-different-integers.md) | Hard |
