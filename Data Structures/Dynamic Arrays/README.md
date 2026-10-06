# Dynamic Arrays in Python

Last updated: 6 October 2026

## Mental model

A dynamic array is an ordered collection whose size can grow. Each item has an index, starting at `0`.

Python's `list` is a dynamic array:

```python
numbers = [10, 20, 30]
```

```text
Index:     0   1   2
Value:    10  20  30
```

Unlike a fixed-size array, a dynamic array can request more storage when it becomes full. Python handles that resizing automatically.

## Core operations

### Read and update by index

```python
numbers[1]       # 20
numbers[1] = 99  # [10, 99, 30]
```

Python can go directly to a known index, so reading or updating one valid position is `O(1)`.

### Add and remove at the end

```python
numbers.append(40)
removed = numbers.pop()
```

`append()` is **amortized `O(1)`**. Most appends are constant time, but occasionally Python must create a larger backing array and copy the existing references, which is `O(N)`. Averaged across many appends, the cost per append remains constant.

Removing the final item with `pop()` is normally `O(1)`.

### Loop through values

```python
for number in numbers:
    print(number)
```

The loop visits every value once, so it is `O(N)`.

The loop variable is the value, not the index.

### Loop through indices and values

```python
for index, number in enumerate(numbers):
    print(index, number)
```

For `[10, 20, 30]`, the first iteration gives:

```python
index = 0
number = 10
```

### Membership and searching

```python
20 in numbers
numbers.index(20)
```

For an ordinary list, Python may need to scan every value. These operations are therefore `O(N)` in the worst case.

### Slicing

```python
numbers = [10, 20, 30, 40]
middle = numbers[1:3]  # [20, 30]
```

The start index is included and the stop index is excluded. Creating a slice copies the selected references, so a slice containing `K` items costs `O(K)` time and space.

## Common operation costs

| Operation | Example | Typical complexity |
|---|---|---:|
| Get length | `len(numbers)` | `O(1)` |
| Read by index | `numbers[i]` | `O(1)` |
| Update by index | `numbers[i] = value` | `O(1)` |
| Append at end | `numbers.append(value)` | Amortized `O(1)` |
| Remove from end | `numbers.pop()` | `O(1)` |
| Search for a value | `value in numbers` | `O(N)` |
| Find a value's index | `numbers.index(value)` | `O(N)` |
| Insert/remove near beginning | `insert(0, value)` / `pop(0)` | `O(N)` |
| Copy a slice of `K` items | `numbers[a:b]` | `O(K)` |

Inserting or removing near the beginning is linear because the later items must shift to new positions.

## Big-O connection

- `O(1)`: work does not grow with the number of items, such as reading a known index.
- `O(log N)`: each step removes a fixed portion of the remaining problem, often half.
- `O(N)`: work grows in proportion to the number of items, such as one complete loop.
- `O(N log N)`: all `N` items are processed across about `log N` levels or rounds, common in efficient sorting.
- `O(N²)`: work grows like `N × N`, common when every item is compared with every item.

## Self-checks

1. For `values = [4, 8, 12]`, what are the index and value on the second iteration of `enumerate(values)`?
2. Why is `values[1]` `O(1)` but `8 in values` `O(N)`?
3. Why is appending called amortized `O(1)` instead of guaranteed `O(1)`?
4. What list is created by `values[0:2]`?

Answer these without running the code first, then use Python to check the predictions.
