# 6 October 2026 — Foundations: arrays, dictionaries, and Big-O

## Focus

- Learn Python list/array fundamentals.
- Use dictionaries for character counts and number-to-index mappings.
- Understand why algorithm growth matters and recognise common Big-O classes.
- Practise Valid Anagram and begin Two Sum without memorising a finished solution.

## What I demonstrated

### Secure

- Read and update list values using zero-based indices.
- Explain that a direct list lookup such as `numbers[0]` is `O(1)` because it does not scan every item.
- Explain that one full pass grows with the input and is `O(N)`.
- Explain that nested all-pairs work grows like `N × N` and is `O(N²)`.
- Explain that `O(log N)` commonly discards half of the remaining search space at each step.
- Explain that storing one dictionary entry per input requires `O(N)` extra space.
- Build a Valid Anagram solution by counting each character in two dictionaries and comparing the dictionaries.

### Developing

- Keep index variables, values, dictionary keys, and dictionary values distinct while tracing code.
- Use `enumerate()` independently without a reminder.
- Apply the previously-seen-value dictionary pattern to Two Sum without reconstructing each line through prompts.
- Trace nested control flow when an inner variable is reset on every outer iteration.
- Explain and recognise `O(N log N)` from a real algorithm. A fixed-size teaching example initially obscured the fact that the logarithmic work must grow with `N`.
- Explain dynamic-array capacity changes and why `append()` is amortized `O(1)`.

### Not yet assessed

- `O(N³)`, `O(2ᴺ)`, `O(N!)`, `O(√N)`, and complexity with multiple inputs such as `O(N + M)`.
- Independent analysis of time and space complexity for a new solution.

## Evidence from the session

- Correctly traced array indices and values in several fresh examples.
- Correctly calculated `20² = 400` and explained `O(N²)` as input size multiplied by input size.
- Explained `O(log N)` as repeatedly halving the remaining search area.
- Explained `O(N)` as the operation count increasing at the same rate as the number of inputs.
- Identified the time/space trade-off between nested-loop and dictionary approaches.

## Mistakes that improved the mental model

- A direct loop variable was initially mistaken for an index. Tracing the first iteration showed that `for number in numbers` gives values, while `enumerate(numbers)` supplies both index and value.
- `dictionary[key]` was initially interpreted like a list index. Dictionary assignment was clarified as creating or updating a key-value mapping.
- Three displayed values in `4 → 2 → 1` were initially counted as three loop executions. The corrected model counts the two transitions caused by the assignment.
- An `O(N log N)` demonstration used a hardcoded `size = 4`; taken literally, that remains `O(N)`. The logarithmic factor appears only when the halved value grows with the input, such as `size = len(numbers)`.

## Next session

1. Trace how a Python list grows when repeated appends exceed its capacity.
2. Rebuild Two Sum from a concrete example, reducing prompts as understanding strengthens.
3. Learn `O(N log N)` through one real sorting example rather than an artificial loop.
4. Continue to `O(N³)`, `O(2ᴺ)`, and `O(N!)` only after the sorting example can be explained in plain language.

## Reflection prompt

Before the next session, answer briefly:

> What is one concept I can now explain without help, and where did my reasoning first become uncertain?
