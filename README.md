# DSA Patterns

LeetCode practice organized by algorithmic pattern. Each problem has a solution
file and matching pytest tests.

## Structure

```
patterns/<pattern>/<name>_<leetcode#>.py       # solution (organized by pattern)
patterns/<pattern>/test_<name>_<leetcode#>.py  # tests
contests/<judge>/<round>/<index>_<slug>.py     # contest solutions (grouped by contest)
notes/                                          # shared reference docs
```

The LeetCode number is a suffix (not a prefix) so the file stays a valid,
importable Python module.

## Problems

| #    | Problem                          | Pattern            |
|------|----------------------------------|--------------------|
| 0003 | Longest Substring Without Repeating Characters | sliding-window |
| 0021 | Merge Two Sorted Lists           | linked-list        |
| 0053 | Maximum Subarray                 | dynamic-programming |
| 0062 | Unique Paths                     | dynamic-programming |
| 0070 | Climbing Stairs                  | dynamic-programming |
| 0119 | Pascal's Triangle II             | dynamic-programming |
| 0121 | Best Time to Buy and Sell Stock  | dynamic-programming |
| 0198 | House Robber                     | dynamic-programming |
| 0338 | Counting Bits                    | dynamic-programming |
| 0258 | Add Digits                       | math               |
| 0290 | Word Pattern                     | hashmap            |
| 0746 | Min Cost Climbing Stairs         | dynamic-programming |
| 0763 | Partition Labels                 | greedy             |
| 0409 | Longest Palindrome               | hashmap            |
| 0482 | License Key Formatting           | string             |
| 1071 | Greatest Common Divisor of Strings | string           |
| 1108 | Defanging an IP Address          | string             |
| 1436 | Destination City                 | hashmap            |
| 1442 | Count Triplets That Can Form Two Arrays of Equal XOR | bit-manipulation |
| 1480 | Running Sum of 1d Array          | array              |
| 2164 | Sort Even and Odd Indices Independently | array         |
| 2225 | Find Players With Zero or One Losses | hashmap        |
| 2243 *SIG | Calculate Digit Sum of a String | string         |
| 3174 | Clear Digits                     | stack              |
| 1678 | Goal Parser Interpretation       | string             |
| 2367 | Number of Arithmetic Triplets    | two-pointers       |
| 3794 | Reverse Prefix                   | two-pointers       |
| 0867 | Transpose Matrix                 | matrix             |
| 0804 | Unique Morse Code Words          | hashmap            |
| 0806 | Number of Lines To Write String  | string             |
| 0929 | Unique Email Addresses           | hashmap            |
| 0883 | Projection Area of 3D Shapes     | matrix             |
| 0938 | Range Sum of BST                 | tree               |
| 0942 | DI String Match                  | greedy             |
| 1338 | Reduce Array Size to The Half    | hashmap            |
| 0539 | Minimum Time Difference          | array              |
| 0635 | Design Log Storage System        | design             |
| 1512 | Number of Good Pairs             | hashmap            |
| 1518 | Water Bottles                    | math               |
| 1603 | Design Parking System            | design             |
| 2379 | Minimum Recolors                 | sliding-window     |
| 1725 | Number Of Rectangles That Can Form The Largest Square | array |
| 1790 | Check if One String Swap Can Make Strings Equal | string |
| 1816 | Truncate Sentence                | string             |
| 1845 | Seat Reservation Manager         | design             |
| 2129 | Capitalize the Title             | string             |
| 2114 | Maximum Number of Words Found in Sentences | string     |
| 2133 | Check if Every Row and Column Contains All Numbers | matrix |
| 2279 | Maximum Bags With Full Capacity of Rocks | greedy        |
| 2357 | Make Array Zero by Subtracting Equal Amounts | heap       |
| 2389 | Longest Subsequence With Limited Sum | binary-search  |
| 2502 *SIG | Design Memory Allocator      | design             |
| 2586 | Count the Number of Vowel Strings in Range | string   |
| 2596 | Check Knight Tour Configuration  | matrix             |
| 2951 | Find the Peaks                   | array              |
| 3637 | Trionic Array I                  | array              |
| 3668 | Restore Finishing Order          | hashmap            |
| 3823 | Reverse Letters Then Special Characters | two-pointers |
| 3754 | Concatenate Non-Zero Digits and Multiply by Sum I | math |
| 3884 | First Matching Character From Both Ends | two-pointers |
| *SIG  | Swap Adjacent Character Pairs    | string             |
| CF 7B | Memory Manager                 | design             |
| Quera | Polynomial Evaluation (Horner) | dynamic-programming – math |
| Quera | Minesweeper                    | matrix             |
| Practice | Subscription Tracker (datetime) | python            |

Non-LeetCode problems use their source as a tag instead of a number (e.g.
`polynomial_value_quera.py`).

<sub>*Company marks an interview question (e.g. *SIG = Susquehanna International Group).</sub>

## Contest problems

Whole contests are grouped by contest under `contests/` (not scattered into the
pattern table above). Each round has its own README.

| Contest | Problems |
|---------|----------|
| [Codeforces Round 1109 (Div. 3)](contests/codeforces/round-1109-div3/) | A. Iskander and Drawings · B. Nikita Books |

## Notes

- [notes/python-builtins.md](notes/python-builtins.md) — built-ins & string-method cheat sheet
- [notes/python-stdlib.md](notes/python-stdlib.md) — import-required stdlib modules (heapq, bisect, collections, itertools, …)
- [notes/tricks.md](notes/tricks.md) — clever one-liners and non-obvious patterns
- [notes/redo.md](notes/redo.md) — tracker for problems to revisit
- [notes/theory/](notes/theory/) — reusable theory: [algorithmic concepts](notes/theory/algorithmic_concepts.md) (bijection, inversions, …) and the [Master Theorem](notes/theory/recursive_functions_big_o_master_theorem.md)

## Running tests

Tests import the solution by module name, so run pytest from inside the pattern
folder:

```bash
cd patterns/<pattern>
pytest
```
