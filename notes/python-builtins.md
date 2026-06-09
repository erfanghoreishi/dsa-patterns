# Python Built-ins & String Methods — Cheat Sheet

Reference for built-ins and string methods commonly used in DSA solutions.

> **Note:** As of this writing, none of the entries below are actually used in any
> solution file under `patterns/`, so every entry is a placeholder. Fill in the
> `Used in:` line (and replace the TODO example) as you start using each one.

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

Used in: [projection_area_0883.py](../patterns/matrix/projection_area_0883.py)

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
# TODO: write an example using sorted
```

Used in: _(not yet used)_

---

## `heapq`

Module implementing a binary min-heap on a plain list. `heappush`/`heappop` keep
the smallest element at index 0 — the go-to for priority queues and "top-k".

```python
# TODO: write an example using heapq
```

Used in: _(not yet used)_

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

Module for binary search on a sorted list. `bisect_left`/`bisect_right` find an
insertion index in O(log n); `insort` inserts while keeping order.

```python
# TODO: write an example using bisect
```

Used in: _(not yet used)_

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
# TODO: write an example using isalpha
```

Used in: _(not yet used)_

---

## `isalnum`

`str.isalnum()` returns `True` if the string is non-empty and every character is
a letter or digit. Common in "valid palindrome" style problems for skipping
punctuation.

```python
# TODO: write an example using isalnum
```

Used in: _(not yet used)_
