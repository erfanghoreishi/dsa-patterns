# Problems to Revisit

| # | Problem | Pattern | Status | Date Added | Notes |
|---|---------|---------|--------|------------|-------|
| 1518 | Water Bottles | math | ⚠️ Redo | 2026-06-08 |#2 06-09 |
| 2596 | Check Knight Tour Configuration | simulation |⚠️ Redo | 2026-06-11 |  |
| 0070 | Climbing Stairs | dynamic-programming | ⚠️ Redo | 2026-06-16 | DP base-case counting |
| 0290 | Word Pattern | hashmap | ⚠️ Redo | 2026-06-18 | bijection check |
| 0763 | Partition Labels | greedy | ⚠️ Redo | 2026-06-18 | furthest-reach greedy |
| 0867 | Transpose Matrix | matrix | ⚠️ Redo | 2026-06-18 | nested list comprehension; in-place square version → 48 Rotate Image |
| 0021 | Merge Two Sorted Lists | linked-list | ⚠️ Redo | 2026-06-18 | dummy head + pointer juggling; trace on paper |
| 2502 | Design Memory Allocator | design | ⚠️ Redo | 2026-06-18 | free-run scan + per-mID block tracking |
| 0539 | Minimum Time Difference | array | ⚠️ Redo | 2026-06-18 | circular clock wraparound |
| 1442 | Count Triplets That Can Form Two Arrays of Equal XOR | bit-manipulation | ⚠️ Redo | 2026-06-30 | prefix XOR; count += k-i (j cancels out) |
| 0804 | Unique Morse Code Words | hashmap | ⚠️ Redo | 2026-06-30 | practice nested inline for (set comprehension + inner generator) |
| 0062 | Unique Paths | dynamic-programming | ⚠️ Redo | 2026-06-30 | O(m*n) DP works; find a more efficient solution (1D DP, or C(m+n-2, m-1)) |
| 0146 | LRU Cache | design | ⚠️ Redo | 2026-07-19 | works via stamp-scan; rewrite with O(1) eviction — hashmap + doubly linked list (move accessed node to one end, LRU is the other end) |
| 0496 | Next Greater Element I | stack | ✅ Done | 2026-07-19 | solved O(n1+n2) with a monotonic stack (concept 9) |
| 0017 | Letter Combinations of a Phone Number | backtracking | ✅ Done | 2026-07-19 | solved by hand with backtracking (product version kept as a comment). Ladder: 78 Subsets ✅ → 77 Combinations → 46 Permutations |
| 0078 | Subsets | backtracking | ⚠️ Redo | 2026-07-19 | include/exclude recursion tree — the base backtracking template; remember current[:] copies (appending current itself stores a reference the pops mutate) |
| 2529 | Maximum Count of Positive Integer and Negative Integer | binary-search | ⚠️ Redo | 2026-07-19 | hand-rolled bisect_left. TODO: write up bisect_left vs bisect_right and the boundary conditions in notes — `l < r` + `r = len` (lower bound, insertion point) vs `l <= r` + `r = len-1` (exact search, needs a found check) |
| 0101 | Symmetric Tree | tree | ⚠️ Redo | 2026-07-19 | mirror recursion: pair CROSSED (left.left vs right.right, left.right vs right.left) — contrast with 100 Same Tree, which pairs same-side |
| 0110 | Balanced Binary Tree | tree | ⚠️ Redo | 2026-07-19 | current solution is O(n^2) — height() is recomputed at every node. Come up with the O(n) version: one DFS that returns the height AND signals imbalance (e.g. return -1 as a sentinel, short-circuiting upward) so each node is visited once |
| 0876 | Middle of the Linked List | linked-list | 📌 TODO | 2026-07-19 | fast & slow (concept 12) — drop the meet-check; when fast runs out, slow is the middle |
| 0142 | Linked List Cycle II | linked-list | 📌 TODO | 2026-07-19 | fast & slow (concept 12) — after they meet, reset one pointer to head and advance both by 1 to find the cycle entrance |
| 0234 | Palindrome Linked List | linked-list | 📌 TODO | 2026-07-19 | find middle with fast & slow, reverse the second half, compare |
| 0287 | Find the Duplicate Number | array | 📌 TODO | 2026-07-19 | Floyd on an implicit graph: treat i -> nums[i] as edges, the duplicate is the cycle entrance |

Status key:

* ❌ Stuck
* ⚠️ Redo
* 📌 TODO
* ✅ Done
