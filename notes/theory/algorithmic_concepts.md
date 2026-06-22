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
