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

Status key:

* ❌ Stuck
* ⚠️ Redo
* 📌 TODO
* ✅ Done
