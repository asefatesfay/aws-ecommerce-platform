# Guess the Word

**Difficulty:** Hard
**Pattern:** Minimax / Interactive / Probability
**LeetCode:** #843

## Problem Statement

You are given an array of unique strings `words` where `words[i]` is 6 letters long. One word in this list is chosen as the secret word. You are given a `Master` API object with a method `guess(word)` that returns the number of exact matches (same character at same position) between your guess and the secret word. You have 10 guesses. Implement a strategy to find the secret word.

## Examples

### Example 1
**Input:** `secret = "acckzz"`, `words = ["acckzz","ccbazz","eiowzz","abcczz","mpbhkz","qinmbl","dbadbh","myuujo","hxntrc","sxqnmn"]`, `allowedGuesses = 10`
**Output:** Calls `guess("acckzz")` at some point
**Explanation:** A good strategy narrows down candidates with each guess.

## Constraints
- `1 <= words.length <= 100`
- `words[i].length == 6`
- All strings in `words` are unique
- The secret word is guaranteed to be in `words`
- `allowedGuesses == 10`

## Hints

> 💡 **Hint 1:** After each guess, you get a match count. Use this to filter the candidate list — only keep words that would give the same match count against your guess as the secret did.

> 💡 **Hint 2:** The key challenge is choosing which word to guess next. A random guess from the remaining candidates works but may not always converge in 10 guesses.

> 💡 **Hint 3:** A better strategy: for each candidate word, count how many other candidates it would eliminate on average. Pick the word that minimizes the expected remaining candidates (minimax). Alternatively, pick the word with the most "0-match" words — guessing a word that shares no characters with many others is informative.

## Approach

**Time Complexity:** O(n²) per guess
**Space Complexity:** O(n)

Maintain a list of candidate words. After each guess, filter candidates to only those with the same match count against the guessed word. For word selection, use a heuristic like picking the candidate that minimizes the maximum remaining candidates after filtering.
