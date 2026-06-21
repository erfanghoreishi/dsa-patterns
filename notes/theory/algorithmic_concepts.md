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
