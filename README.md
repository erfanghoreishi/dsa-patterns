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
| 0409 | Longest Palindrome               | hashmap            |
| 3174 | Clear Digits                     | stack              |
| 1678 | Goal Parser Interpretation       | string             |
| 2367 | Number of Arithmetic Triplets    | two-pointers       |
| 3794 | Reverse Prefix                   | two-pointers       |
| 0883 | Projection Area of 3D Shapes     | matrix             |
| 1518 | Water Bottles                    | math               |
| 2379 | Minimum Recolors                 | sliding-window     |
| 2389 | Longest Subsequence With Limited Sum | binary-search  |
| Quera | Polynomial Evaluation (Horner) | dynamic-programming – math |

Non-LeetCode problems use their source as a tag instead of a number (e.g.
`polynomial_value_quera.py`).

## Notes

- [notes/python-builtins.md](notes/python-builtins.md) — built-ins & string-method cheat sheet
- [notes/tricks.md](notes/tricks.md) — clever one-liners and non-obvious patterns
- [notes/redo.md](notes/redo.md) — tracker for problems to revisit

## Running tests

Tests import the solution by module name, so run pytest from inside the pattern
folder:

```bash
cd patterns/<pattern>
pytest
```
