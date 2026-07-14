# Python Standard Library — Cheat Sheet

Reference for **import-required** modules used in DSA solutions (as opposed to
always-available built-ins, which live in [python-builtins.md](python-builtins.md)).
Rule of thumb: if it needs an `import`, it belongs here.

> Add modules as problems use them (`re`, `datetime`/`timedelta`, `math`,
> `functools`, …). Keep the format: what it does, a short example, and a
> `Used in:` link.

---

## `collections.Counter`

`Counter` is a dict subclass that tallies occurrences of hashable items — the
one-step form of `d[x] = d.get(x, 0) + 1` in a loop. `most_common(n)` returns the
n highest-frequency entries.

```python
from collections import Counter
Counter(['a', 'b', 'a'])      # Counter({'a': 2, 'b': 1})
Counter("banana")['a']        # 3  (missing keys give 0, no KeyError)
```

Used in: [find_winners_2225.py](../patterns/hashmap/find_winners_2225.py)

---

## `collections.defaultdict`

A dict that auto-creates a default value (via a factory like `int`, `list`, `set`)
on first access to a missing key — removes the need for `if key not in d` guards.

```python
# TODO: write an example using defaultdict
```

Used in: _(not yet used)_

---

## `collections.deque`

A double-ended queue with O(1) `append`/`appendleft` and `pop`/`popleft`. Ideal
for BFS queues and sliding windows.

```python
# TODO: write an example using deque
```

Used in: _(not yet used)_

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

## `itertools.zip_longest`

Like `zip`, but runs until the **longest** iterable is exhausted, padding the
shorter ones with `fillvalue` (default `None`). Use it to pair up unequal-length
sequences without dropping the tail.

```python
from itertools import zip_longest
list(zip_longest("ab", "pqrs", fillvalue=""))  # [('a','p'), ('b','q'), ('','r'), ('','s')]
```

Used in: [merge_alternately_1768.py](../patterns/two-pointers/merge_alternately_1768.py)
(pads the shorter word with `""` so leftover characters still get appended)

---

## `datetime` (`date` / `timedelta`)

`date` is a calendar date; `timedelta` is a span you add or subtract. Dates compare
and subtract naturally, so most date math is just arithmetic — no manual day/month
juggling, and leap years / month lengths are handled for you.

```python
from datetime import date, timedelta
d = date.fromisoformat("2026-01-01")   # parse "YYYY-MM-DD" (datetime.strptime(s, fmt) for other formats)
d + timedelta(days=30)                 # date(2026, 1, 31)  — add a span
(date(2026, 1, 31) - d).days           # 30                 — difference, in days
d < date(2026, 2, 1)                   # True               — compare chronologically
d.isoformat()                          # "2026-01-01"       — format back to string
d.strftime("%A")                       # "Thursday"         — weekday name (%Y/%m/%d for numbers)
```

Used in: [subscription_tracker_practice.py](../patterns/python/subscription_tracker_practice.py)
