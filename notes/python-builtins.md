# Python Built-ins & String Methods — Cheat Sheet

Reference for built-ins and string methods commonly used in DSA solutions.

> **Note:** Entries still marked with a `# TODO` example aren't used in any
> solution under `patterns/` yet. Fill in the `Used in:` line (and replace the
> TODO example) as you start using each one.

---

## `zip`

Pairs up elements from two or more iterables, yielding tuples until the shortest
iterable is exhausted. Great for iterating over two lists in lockstep. Combined
with `*` unpacking, `zip(*grid)` transposes a matrix — rows become columns.

```python
# transpose a 2D grid to iterate over its columns
grid = [[1, 2], [3, 4]]
for col in zip(*grid):
    print(col)        # (1, 3) then (2, 4)
```

Used in: [projection_area_0883.py](../patterns/matrix/projection_area_0883.py),
[check_valid_2133.py](../patterns/matrix/check_valid_2133.py)

---

## `enumerate`

Yields `(index, value)` pairs while iterating, so you get the index without
manually maintaining a counter. Accepts a `start` argument.

```python
# TODO: write an example using enumerate
```

Used in: _(not yet used)_

---

## `sorted`

Returns a new sorted list from any iterable (the original is untouched). Supports
a `key` function and `reverse=True`.

```python
sorted([4, 5, 2, 1])  # [1, 2, 4, 5]
```

Used in: [longest_subsequence_limited_sum_2389.py](../patterns/binary-search/longest_subsequence_limited_sum_2389.py)

---

## `heapq`

Binary **min**-heap on a plain list (smallest stays at index 0). Key functions:
- `heapify(lst)` — turn a list into a heap in place, O(n)
- `heappush(heap, x)` — add an item, O(log n)
- `heappop(heap)` — remove & return the smallest, O(log n)
- `heap[0]` — peek the smallest, O(1)

For a **max**-heap, push negated values (`-x`) and negate again on the way out.

```python
import heapq
h = [3, 1, 2]
heapq.heapify(h)        # [1, 3, 2]
heapq.heappush(h, 0)
heapq.heappop(h)        # 0  (the smallest)
```

Used in: [maximum_score_1753.py](../patterns/heap/maximum_score_1753.py)

---

## `defaultdict`

`collections.defaultdict` is a dict that auto-creates a default value (via a
factory like `int`, `list`, `set`) on first access to a missing key — removes the
need for `if key not in d` guards.

```python
# TODO: write an example using defaultdict
```

Used in: _(not yet used)_

---

## `deque`

`collections.deque` is a double-ended queue with O(1) `append`/`appendleft` and
`pop`/`popleft`. Ideal for BFS queues and sliding windows.

```python
# TODO: write an example using deque
```

Used in: _(not yet used)_

---

## `Counter`

`collections.Counter` is a dict subclass that tallies occurrences of hashable
items. `most_common(n)` returns the n highest-frequency entries.

```python
# TODO: write an example using Counter
```

Used in: _(not yet used)_

---

## `bisect`

Binary search on a sorted list. `bisect_right(list, x)` returns the index where
`x` would be inserted to keep the list sorted — which tells you how many elements
are ≤ x. (`bisect_left` gives the count of elements strictly < x.)

```python
from bisect import bisect_right
bisect_right([1, 3, 5, 7], 5)  # 3 — index after the 5
```

Used in: [longest_subsequence_limited_sum_2389.py](../patterns/binary-search/longest_subsequence_limited_sum_2389.py)

---

## `itertools.accumulate`

Builds a running cumulative sum (or other operation) from a list.

```python
from itertools import accumulate
list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
```

Used in: [running_sum_1480.py](../patterns/array/running_sum_1480.py),
[longest_subsequence_limited_sum_2389.py](../patterns/binary-search/longest_subsequence_limited_sum_2389.py)

---

## `reverse`

`list.reverse()` reverses a list **in place** (returns `None`). For strings or a
reversed copy, use slicing `seq[::-1]` or the `reversed()` built-in.

```python
# TODO: write an example using reverse
```

Used in: _(not yet used)_

---

## `isalpha`

`str.isalpha()` returns `True` if the string is non-empty and every character is
a letter. Handy for filtering/validating alphabetic input.

```python
"abc".isalpha()  # True
"ab3".isalpha()  # False
```

Used in: _(not yet used — the related `str.isdigit()` is used in [clear_digits_3174.py](../patterns/stack/clear_digits_3174.py))_

---

## `isalnum`

`str.isalnum()` returns `True` if the string is non-empty and every character is
a letter or digit. Common in "valid palindrome" style problems for skipping
punctuation.

```python
# TODO: write an example using isalnum
```

Used in: _(not yet used)_

---

## `join`

`sep.join(iterable)` concatenates an iterable of strings into one, with `sep`
between items. `''.join(chars)` is the standard way to turn a list of characters
back into a string.

```python
'-'.join(['a', 'b', 'c'])  # 'a-b-c'  — separator goes *between* items
''.join(['a', 'b', 'c'])   # 'abc'    — empty separator just concatenates
```

Used in: [clear_digits_3174.py](../patterns/stack/clear_digits_3174.py)

---

## `count`

`list.count(x)` (and `str.count(sub)`) returns how many times a value occurs.
Handy for "how many equal the max/target" without an explicit loop.

```python
[5, 3, 5, 5].count(5)  # 3
"banana".count("a")    # 3
```

Used in: [count_good_rectangles_1725.py](../patterns/array/count_good_rectangles_1725.py)
(list), [maximum_bags_2279.py](../patterns/greedy/maximum_bags_2279.py) (list),
[minimum_recolors_2379.py](../patterns/sliding-window/minimum_recolors_2379.py) (str)

---

## `set`

Unordered collection of unique, hashable items — O(1) membership (`x in s`) and
fast algebra. Building a `set` also dedupes (`len(set(xs))` = distinct count).

```python
s = set()

# modify
s.add(x)
s.discard(x)       # remove if present, no error if missing
s.clear()

# set algebra (a, b are sets)
a & b              # intersection (common elements)
a | b              # union
a - b              # difference (in a, not b)
a ^ b              # symmetric difference (in exactly one)

# relations
a.isdisjoint(b)    # True if no common elements
a <= b             # subset
a >= b             # superset
```

Used in: [can_be_typed_words_1935.py](../patterns/hashmap/can_be_typed_words_1935.py)
(`set(word) & broken` to test for a broken letter; `isdisjoint` is the cleaner form)
