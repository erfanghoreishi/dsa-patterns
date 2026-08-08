# Algorithmic Concepts

A running, numbered list of the most useful algorithm & math concepts — building
toward ~50. Each new concept gets the next number; keep them concise and link the
solution that uses them.

---

## 1. Bijection (one-to-one correspondence)

A **bijection** between two sets is a mapping that is both:
- **injective** (one-to-one) — different inputs map to different outputs, and
- **surjective** (onto) — every output is hit.

In short: each element on the left pairs with exactly one element on the right,
**and vice versa** — no sharing, no leftovers.

**How to verify two sequences form a bijection:**
1. The mapping is consistent **one way** (it's a function: each left item always
   maps to the same right item), and
2. the number of **distinct** items is equal on both sides (this forces the reverse
   direction to also be a function).

Together these give a one-to-one correspondence.

**Referenced in:** [word_pattern_0290.py](../../patterns/hashmap/word_pattern_0290.py)
— maps pattern characters to words; checks the forward mapping *and*
`len(set(pattern)) == len(set(words))` to confirm it's one-to-one both ways.

---

## 2. Minimum adjacent swaps = number of inversions

An **inversion** is a pair of indices `i < j` with `arr[i] > arr[j]` (a pair that is
out of order).

The **minimum number of adjacent swaps** needed to sort an array equals its number
of inversions: each adjacent swap fixes exactly one inversion, so you can't do
better than removing them one at a time.

Count inversions in `O(n log n)` with a modified **merge sort** (count cross-pairs
while merging) or a **Fenwick/BIT**. (Brute force is `O(n^2)`.)

---

## 3. Furthest-reach greedy (interval merging / last-occurrence)

Scan left to right tracking the **furthest point** anything seen so far reaches;
close the current group when your position catches that reach. You can't close
earlier without splitting connected elements.

```python
start = end = 0
for i, c in enumerate(s):
    end = max(end, reach(i))          # how far element i extends
    if i == end:                      # group closed
        result.append(i - start + 1)  # finalize (here: its size)
        start = i + 1
```

`reach(i)` changes per problem: last occurrence of `s[i]` (Partition Labels), an
interval's `end` (Merge Intervals 56, Burst Balloons 452), or the furthest index
jumpable (Jump Game II 45, Video Stitching 1024). **Trigger to recognize it:**
"last occurrence / furthest reach / max extent" + "partition / group / merge".

**Referenced in:** [partition_labels_0763.py](../../patterns/greedy/partition_labels_0763.py)
— `reach(i) = last[s[i]]`; closes a partition when `i` reaches the furthest last-occurrence.

---

## 4. Symmetric-pair scan: `n//2` vs `n//2 + 1`

When walking mirror pairs `(i, n-1-i)` from both ends inward, the loop bound
depends on whether the **middle** of an odd-length input matters:

- `range(n // 2)` — visits the **pairs only**; the lone middle char (odd `n`) is
  skipped. Use it when the middle needs no action.
- `range(n // 2 + 1)` — also visits the **middle index** (`i == n-1-i` for odd `n`,
  where an element compares with itself). Use it when the middle itself counts.

**Referenced in:**
[make_smallest_palindrome_2697.py](../../patterns/two-pointers/make_smallest_palindrome_2697.py)
(`n//2` — middle char is already a palindrome center, left untouched) and
[first_matching_index_3884.py](../../patterns/two-pointers/first_matching_index_3884.py)
(`n//2 + 1` — the middle char is a valid self-match).

---

## 5. Circular (clock) time difference

Parse `"HH:MM"` to minutes: `int(t[:2]) * 60 + int(t[3:])`. A day is `1440` minutes
and the clock **wraps**, so the gap between two times is `min(d, 1440 - d)` where
`d` is the straight difference — e.g. `00:00` and `23:59` are `1` minute apart.

For the minimum over many times: **sort**, take the smallest adjacent gap, then also
check the wrap between the largest and smallest, `1440 - max + min`. No other pair
needs a wrap check — sorted order guarantees the straight gap is shortest for them.

**Referenced in:** [min_time_difference_0539.py](../../patterns/array/min_time_difference_0539.py)

---

## 6. Gauss's sum: 1 + 2 + ... + n = n(n+1)/2

Pair the terms from the two ends: `(1 + n), (2 + n-1), (3 + n-2), ...`. Each pair
sums to `n + 1`, and there are `n/2` pairs, so the total is `n(n+1)/2`. (Odd `n`
works too — the lone middle term `(n+1)/2` fits the same formula.)

```
 1 +  2 +  3 + 4
 4 +  3 +  2 + 1     <- same sum reversed
 5 +  5 +  5 + 5  =  4 x 5  =  n(n+1)   ->  half of that is n(n+1)/2
```

Common uses: the number of unordered pairs among `k` items is `k(k-1)/2` (that's the
sum `1..k-1`); triangular numbers; counting iterations of an `O(n^2)` double loop.

**Referenced in:** [num_identical_pairs_1512.py](../../patterns/hashmap/num_identical_pairs_1512.py)
— a value seen `n` times contributes `n(n-1)/2` good pairs; and
[b_nikita_books.py](../../contests/codeforces/round-1109-div3/b_nikita_books.py)
— each prefix sum must reach the triangular number `k(k+1)/2`.

---

## 7. XOR properties (self-inverse) and the prefix-XOR range trick

Core identities: `x ^ x = 0`, `x ^ 0 = x`, and XOR is commutative & associative.
A key consequence: `a == b  ⟺  a ^ b == 0`.

**Range trick:** split `arr[i..k]` at some `j` into `a = XOR(i..j-1)` and
`b = XOR(j..k)`. Because the two halves cover the whole range with no overlap,
`a ^ b = XOR(i..k)` — the split point `j` cancels out entirely. So
`a == b  ⟺  XOR(i..k) == 0`, a condition that **doesn't mention `j`**. One such
`XOR(i..k) == 0` therefore holds for *every* split `j` at once — all `k - i` of them.

**Referenced in:** [count_triplets_1442.py](../../patterns/bit-manipulation/count_triplets_1442.py)
— counts `k - i` triplets (not `1`) each time `XOR(arr[i..k]) == 0`.

---

## 8. Fixed-width zero-padded strings compare like numbers

If values are formatted with **fixed-width, zero-padded** fields in
most-significant-first order (e.g. `"2017:01:01:23:59:59"`), then Python's
lexicographic string comparison (`<`, `<=`) matches their natural / chronological
order — so you can compare (or slice a prefix and compare) without parsing to ints.

```python
"2016:12" < "2017:01"     # True
"09:30"   < "10:00"       # True  — zero-padding is essential ("9" > "1" lexically)
```

Slicing a prefix compares only down to a chosen field (e.g. `ts[:4]` = year,
`ts[:13]` = hour). **Caveat:** breaks the moment fields aren't zero-padded to equal
width.

**Referenced in:** [log_system_0635.py](../../patterns/design/log_system_0635.py)
— compares timestamp prefixes by granularity, no int conversion.

---

## 9. Monotonic stack (next greater / smaller element)

Keep a stack whose values stay ordered (here **decreasing**). Scan the array; while
the incoming value breaks the order — bigger than the top — the incoming value is
the **next greater** for that top, so pop and resolve it. Then push the incoming
value. Each element is pushed and popped at most once → **O(n)** total.

```python
# next_greater_element_0496.py  (LC 496)
next_greater = {}
stack = []
for num in nums2:
    while stack and stack[-1] < num:   # num resolves everything smaller on top
        next_greater[stack.pop()] = num
    stack.append(num)
```

Variations: flip the comparison for **next smaller**; iterate **right-to-left** for
*previous* greater/smaller. Common in "next warmer day", histogram largest-rectangle,
stock-span problems.

**Referenced in:** [next_greater_element_0496.py](../../patterns/stack/next_greater_element_0496.py)

---

## 10. BFS for shortest path in an unweighted graph

Explore level by level from the start with a **queue** (`collections.deque`),
marking nodes **visited when you enqueue** them (not when you dequeue — that avoids
adding the same node twice). Because every edge has the same cost, the first time
BFS reaches a node it's via a shortest path, so the move count on dequeue is optimal.

```python
from collections import deque
visited = {start}
q = deque([(start, 0)])          # (node, distance)
while q:
    node, dist = q.popleft()
    if node == target:
        return dist
    for nxt in neighbours(node):
        if nxt not in visited:
            visited.add(nxt)
            q.append((nxt, dist + 1))
return -1                         # unreachable
```

The whole trick is defining `neighbours` per problem (grid cells, board squares,
word transformations, states). Use plain **DFS/stack** when you only need
reachability, not the *shortest* path.

### The graph is usually *implicit*

No adjacency list: nodes are plain values and `neighbours()` computes edges from
arithmetic. Trigger: *"minimum moves/steps between discrete states"* → BFS.

Snakes & Ladders, 3x3 board, ladder at square 2 -> 7:

```
  7  8  9      neighbours(1) = {3,4,5,6,7}   # roll 1 -> 2 ==ladder==> 7
  6  5  4      neighbours(7) = {8,9}         # fewer than 6 near the end
  1  2  3      1 -> 7 -> 9  =  2 moves
```

Gotchas: **at most** 6 children (two rolls can land on the same node); `-1` does
**not** mean "no edge" — every in-bounds roll is an edge, a non-`-1` value only
redirects where it lands.

**Referenced in:** [snakes_and_ladders_0909.py](../../patterns/graph/snakes_and_ladders_0909.py)
— nodes are board squares; `neighbours` = the next 1..6 squares, redirected through
any snake/ladder.
   