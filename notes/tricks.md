# Clever One-Liners & Non-Obvious Patterns

Patterns worth remembering, spotted in the `patterns/` solutions.

---

## Chained `.replace()` instead of parsing

`str.replace` returns a new string, so calls chain left-to-right. You can decode a
small grammar without any loop or state machine.

```python
# interpret_1678.py  (LC 1678 – Goal Parser Interpretation)
return command.replace("()", "o").replace("(al)", "al")
```

Order matters: replace the most specific / shortest tokens carefully so earlier
replacements don't corrupt later matches.

From: [interpret_1678.py](../patterns/string/interpret_1678.py)

---

## Slice-and-reverse prefix in one line

Slicing makes "reverse the first k characters" a one-liner — no two-pointer swap
loop needed. `s[:k][::-1]` reverses the prefix, then concatenate the untouched
tail.

```python
# reverse_prefix_3794.py
return s[0:k][::-1] + s[k:]
```

Trade-off: clean and readable, but allocates new strings (O(n) extra space) vs.
the in-place two-pointer version kept as a comment in the same file.

From: [reverse_prefix_3794.py](../patterns/two-pointers/reverse_prefix_3794.py)

---

## Kadane's algorithm with chained initialization

`best = dp = nums[0]` seeds both the running subarray sum (`dp`) and the global
best in one statement. Each step, `dp` either extends the previous subarray or
restarts at the current element.

```python
# maximum_subarray_0053.py  (LC 53 – Maximum Subarray)
best = dp = nums[0]
for i in range(1, len(nums)):
    dp = max(nums[i], dp + nums[i])
    best = max(dp, best)
return best
```

From: [maximum_subarray_0053.py](../patterns/dynamic-programming/maximum_subarray_0053.py)

---

## In-place list as a stack with a write pointer

Instead of allocating a separate stack, overwrite the input list in place using a
write index `p`. Pushing writes `s[p]` and increments; popping just decrements
`p`. The answer is the prefix `s[:p]`.

```python
# clear_digits_3174.py  (LC 3174 – Clear Digits)
s = list(s)
p = 0
for char in s:
    if char.isdigit():
        p -= 1          # "pop"
    else:
        s[p] = char     # "push"
        p += 1
return ''.join(s[0:p])
```

O(1) extra space beyond the list copy — the same array doubles as input and stack.

From: [clear_digits_3174.py](../patterns/stack/clear_digits_3174.py)

---

## "Add the center" trick for longest palindrome

When building a palindrome from character counts, take all even pairs, and if *any*
character had a leftover odd count, you can still place one of them in the center —
so add exactly 1.

```python
# longest_palindrome_0409.py  (LC 409 – Longest Palindrome)
return count + (1 if has_odd else 0)
```

The `has_odd` flag captures "was there at least one odd-count char" — you add 1 at
most once, no matter how many odd counts existed.

From: [longest_palindrome_0409.py](../patterns/hashmap/longest_palindrome_0409.py)

---

## Flattening a 2D grid with a nested inline `for` in a comprehension

A list comprehension can chain multiple `for` clauses, read left-to-right like
nested loops. This flattens a 2D grid and counts non-zero cells in a single
expression — no explicit nested loop needed.

```python
# projection_area_0883.py  (LC 883 – Projection Area of 3D Shapes)
shadow_xy = sum([1 for row in grid for col in row if col != 0])
```

`for row in grid` is the outer loop, `for col in row` the inner; the trailing
`if col != 0` filters. Each surviving cell contributes `1` to the `sum`. Pairs
nicely with `zip(*grid)` (column max) and `max(row)` (row max) to get all three
projections.

From: [projection_area_0883.py](../patterns/matrix/projection_area_0883.py)

---

## Booleans as integers (inline `if` without writing one)

In Python `bool` is a subclass of `int`, so `True == 1` and `False == 0`. Adding a
comparison directly is shorthand for the inline conditional `1 if cond else 0` —
handy for incrementally maintaining a count in a sliding window.

```python
# minimum_recolors_2379.py  (LC 2379 – Minimum Recolors)
whites += (blocks[i] == 'W')       # same as: whites += 1 if blocks[i] == 'W' else 0
whites -= (blocks[i - k] == 'W')   # drop the element leaving the window
```

The explicit ternary `1 if blocks[i] == 'W' else 0` is the equivalent inline `if`
form, kept as a comment in the file for clarity.

From: [minimum_recolors_2379.py](../patterns/sliding-window/minimum_recolors_2379.py)

---

## `.count()` to seed a window

`str.count(sub)` (and `list.count(x)`) returns how many times a value occurs.
Slicing first, then counting, gives the tally for the initial sliding window in
one expression — no manual loop to prime it.

```python
# minimum_recolors_2379.py  (LC 2379 – Minimum Recolors)
whites = blocks[:k].count('W')     # whites in the first window of size k
```

After this you only adjust by +/- 1 as the window slides, instead of recounting.

From: [minimum_recolors_2379.py](../patterns/sliding-window/minimum_recolors_2379.py)

---

## Frequency counting with `dict.get(key, default)`

`dict.get(key, 0)` returns the current count or `0` when the key is missing, so you
can increment in one line without a `if key in d` guard or a `try/except`. The
plain-dict equivalent of `collections.Counter` / `defaultdict(int)`.

```python
# longest_palindrome_0409.py  (LC 409 – Longest Palindrome)
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```

The second argument is only used as a fallback — it isn't stored unless you assign
it back, as done here.

From: [longest_palindrome_0409.py](../patterns/hashmap/longest_palindrome_0409.py)

---

## Horner's method for polynomial evaluation (with running modulo)

Evaluate `P(x) = a_n x^n + ... + a_0` in O(n) with no powers and no overflow, by
factoring it as `((...(a_n·x + a_{n-1})·x + a_{n-2})·x + ...) + a_0`. Take `% MOD`
every step so intermediate values stay bounded.

```python
# polynomial_value_quera.py  (Quera – Polynomial Evaluation)
result = 0
for a in coeffs:               # coeffs from a_n down to a_0
    result = (result * x + a) % MOD
```

Because `(a*b + c) mod M == ((a mod M)*(b mod M) + c) mod M`, reducing as you go is
exact. Python's `%` returns a non-negative remainder, so negative `x` or
coefficients wrap correctly with no extra handling. Each step builds on the
previous (`dp0 -> dp1 -> dp2 -> ...`), so it doubles as a gentle DP warm-up.

From: [polynomial_value_quera.py](../patterns/dynamic-programming/polynomial_value_quera.py)

---

## Prefix sums + `bisect_right` to answer "largest count with sum ≤ q"

To find the longest subsequence whose sum stays within a budget, **sort ascending**
(greedily take the smallest elements), build prefix sums, then binary-search each
query. `bisect_right(prefix, q)` is exactly "how many prefix sums are ≤ q" — i.e.
how many of the smallest elements you can afford.

```python
# longest_subsequence_limited_sum_2389.py  (LC 2389)
nums = sorted(nums)
prefix = list(accumulate(nums))
return [bisect_right(prefix, q) for q in queries]
```

Sort + prefix is built once (O(n log n)); each query is then O(log n) instead of
re-scanning. The file keeps a no-built-ins version (manual prefix loop + manual
binary search) in comments.

From: [longest_subsequence_limited_sum_2389.py](../patterns/binary-search/longest_subsequence_limited_sum_2389.py)

---

## Tuple unpacking to name coordinates

A `(row, col)` tuple can be split straight into two variables in one line, so you
work with readable names instead of `pos[step][0]` / `pos[step][1]`.

```python
# check_valid_grid_2596.py  (LC 2596 – Check Knight Tour Configuration)
r1, c1 = pos[step]
r2, c2 = pos[step + 1]
if (r2 - r1, c2 - c1) not in moves:   # the move itself is also a tuple
    ...
```

From: [check_valid_grid_2596.py](../patterns/matrix/check_valid_grid_2596.py)

---

## Counting with `sum()` over a boolean generator

`True == 1` and `False == 0`, so `sum(condition for x in items)` counts how many
items satisfy `condition` — no explicit counter or `if` needed. Pairs well with a
slice to count only within a range.

```python
# vowel_strings_2586.py  (LC 2586 – Count the Number of Vowel Strings in Range)
vowels = set('aeiou')
return sum(
    word[0] in vowels and word[-1] in vowels
    for word in words[left:right + 1]
)
```

Using a generator (no `[]`) avoids building an intermediate list. Same boolean-as-int
idea as the sliding-window count, just summed in one shot instead of incrementally.

From: [vowel_strings_2586.py](../patterns/string/vowel_strings_2586.py)

---

## Comprehension: filter `if` vs ternary `if/else`

Position changes the meaning — don't confuse them.

- **Filter `if` (at the END)** — keeps fewer items, no `else`:
  `[x for x in items if cond]` → skips items where `cond` is False.
- **Ternary `if/else` (at the FRONT)** — keeps all items, `else` required:
  `[x if cond else y for x in items]` → transforms each, never drops.

Memory hook: **`if` at the end = filtering**, **`if/else` at the front = transforming**.

```python
# are_almost_equal_1790.py  (LC 1790) — filter to collect only mismatched pairs
diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
```

From: [are_almost_equal_1790.py](../patterns/string/are_almost_equal_1790.py)

---

## Nested inline `for`: a comprehension inside a comprehension

A comprehension's *element* can itself be a comprehension/generator — giving you two
inline loops in one expression. Here the **outer** loop walks words, the **inner**
generator builds each word's code:

```python
# unique_morse_representations_0804.py  (LC 804)
transitions = {"".join(MORSE[ord(char) - ord('a')] for char in word)   # inner: per char
               for word in words}                                       # outer: per word
return len(transitions)
```

Two things to notice:
- `{...}` with **no `key: value`** is a **set** comprehension (a dict needs a colon).
  So duplicates collapse automatically and `len()` is the answer — no manual dedup.
- This differs from the flat `[x for a in outer for b in inner]` form (see the
  2D-grid trick above): there the `for`s are *chained* in one comprehension; here one
  comprehension is *nested inside* another.

From: [unique_morse_representations_0804.py](../patterns/hashmap/unique_morse_representations_0804.py)

---

## Direction vectors to visit grid neighbours (no repeated ifs)

List the neighbour offsets once, then loop over them — instead of writing eight
separate `if` checks for up/down/left/right/diagonals.

```python
# minesweeper_quera.py  (Quera – Minesweeper)
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

count = 0
for dr, dc in DIRECTIONS:          # one loop covers all 8 neighbours
    if (r + dr, c + dc) in bombs:
        count += 1
```

Storing cells in a `set` (here `bombs`) makes each neighbour test O(1) and sidesteps
bounds checks — an out-of-grid `(r+dr, c+dc)` simply isn't in the set. Use 4 offsets
for orthogonal-only moves, 8 for including diagonals.

Once the loop is clear, it collapses to a one-liner (as in the solution file):
`count = sum((r + dr, c + dc) in bombs for dr, dc in DIRECTIONS)`.

From: [minesweeper_quera.py](../patterns/matrix/minesweeper_quera.py)
