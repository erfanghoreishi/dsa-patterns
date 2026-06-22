# DSA Patterns

LeetCode practice organized by algorithmic pattern. Each problem has a solution
file and matching pytest tests.

## Structure

```
patterns/<pattern>/<name>_<leetcode#>.py       # solution
patterns/<pattern>/test_<name>_<leetcode#>.py  # tests
notes/                                          # shared reference docs
```

The LeetCode number is a suffix (not a prefix) so the file stays a valid,
importable Python module.

## Problems

| #    | Problem                          | Pattern            |
|------|----------------------------------|--------------------|
| 0053 | Maximum Subarray                 | dynamic-programming |
| 0070 | Climbing Stairs                  | dynamic-programming |
| 0290 | Word Pattern                     | hashmap            |
| 0763 | Partition Labels                 | greedy             |
| 0409 | Longest Palindrome               | hashmap            |
| 1436 | Destination City                 | hashmap            |
| 3174 | Clear Digits                     | stack              |
| 1678 | Goal Parser Interpretation       | string             |
| 2367 | Number of Arithmetic Triplets    | two-pointers       |
| 3794 | Reverse Prefix                   | two-pointers       |
| 0883 | Projection Area of 3D Shapes     | matrix             |
| 1518 | Water Bottles                    | math               |
| 2379 | Minimum Recolors                 | sliding-window     |
| 1725 | Number Of Rectangles That Can Form The Largest Square | array |
| 1790 | Check if One String Swap Can Make Strings Equal | string |
| 2133 | Check if Every Row and Column Contains All Numbers | matrix |
| 2279 | Maximum Bags With Full Capacity of Rocks | greedy        |
| 2357 | Make Array Zero by Subtracting Equal Amounts | heap       |
| 2389 | Longest Subsequence With Limited Sum | binary-search  |
| 2586 | Count the Number of Vowel Strings in Range | string   |
| 2596 | Check Knight Tour Configuration  | matrix             |
| 3668 | Restore Finishing Order          | hashmap            |
| 3823 | Reverse Letters Then Special Characters | two-pointers |
| Quera | Polynomial Evaluation (Horner) | dynamic-programming – math |

Non-LeetCode problems use their source as a tag instead of a number (e.g.
`polynomial_value_quera.py`).

## Notes

- [notes/python-builtins.md](notes/python-builtins.md) — built-ins & string-method cheat sheet
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
