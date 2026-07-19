# Python Built-ins & String Methods — Cheat Sheet

Reference for **always-available** built-in functions and `str`/`list`/`set`/`dict`
methods (no `import` needed). Import-required modules (`heapq`, `bisect`,
`collections`, `itertools`, `re`, …) live in [python-stdlib.md](python-stdlib.md).

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
sorted([4, 5, 2, 1])                                  # [1, 2, 4, 5]

# sorting a dict/Counter: sorted(d) sorts its KEYS — usually not what you want.
# use .items() and a key to sort by value:
sorted(counts.items(), key=lambda kv: kv[1], reverse=True)   # (key, count) by count desc
```

Used in: [longest_subsequence_limited_sum_2389.py](../patterns/binary-search/longest_subsequence_limited_sum_2389.py),
[min_set_size_1338.py](../patterns/hashmap/min_set_size_1338.py) (sort Counter items by count)

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

---

## `upper` / `lower`

`str.upper()` / `str.lower()` return a **new** string with every letter cased up or
down (strings are immutable, so the original is unchanged). Non-letters pass
through unchanged. Common for case-insensitive compares and title-casing by hand.

```python
"aB3".upper()              # 'AB3'
"aB3".lower()              # 'ab3'
w = "hELLO"
w[0].upper() + w[1:].lower()  # 'Hello'  — capitalize just the first letter
```

Used in: [capitalize_title_2129.py](../patterns/string/capitalize_title_2129.py)

---

## `ord` / `chr`

`ord(c)` → code point (int); `chr(n)` → char. `ord(c) - ord('a')` maps `'a'..'z'`
to `0..25` for indexing a 26-slot array by letter.

```python
ord('c') - ord('a')  # 2
chr(ord('a') + 2)    # 'c'
```

Used in: [number_of_lines_0806.py](../patterns/string/number_of_lines_0806.py)

---

## `:=` (walrus / assignment expression)

Assigns **and** returns a value inside an expression, so you can read and test in
one place — handy for a loop that consumes input until a sentinel without writing
the read twice.

```python
res = []
while (num := input()) != '0':   # read, assign to num, and test — all at once
    res.append(num)
print("\n".join(res[::-1]))       # collected lines, reversed

# also: if (n := len(data)) > 10: ...   /   [y for x in xs if (y := f(x)) is not None]
```

Without it you'd read once before the loop and again at the end of each iteration.

Used in: _(general Python idiom)_
