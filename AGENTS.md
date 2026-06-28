# DSA Patterns — Repo Conventions

Personal LeetCode/competitive-programming practice, organized by algorithmic pattern.

## Adding a new problem — checklist

1. **Pick the pattern folder** under `patterns/` (e.g. `dynamic-programming`,
   `hashmap`, `stack`, `string`, `two-pointers`, `sliding-window`, `matrix`,
   `math`). Create a new folder if none fits.

2. **Name the solution file** `<name>_<id>.py`, where the id is a **suffix**:
   - LeetCode problem → zero-padded number, e.g. `maximum_subarray_0053.py`.
   - Non-LeetCode problem → source tag, e.g. `polynomial_value_quera.py`.
   - The id is a suffix (not prefix) so the filename stays a valid importable
     Python module (modules can't start with a digit).

3. **Write the solution as a plain function** (no `self` / class wrapper) so the
   test can import it directly. For stdin/stdout problems, keep a pure function
   for the logic and put the I/O in an `if __name__ == "__main__":` block.

4. **Add tests** in the same folder: `test_<name>_<id>.py`, importing by module
   name (`from <name>_<id> import <func>`). Cover the given examples plus edge
   cases. Run from inside the folder: `cd patterns/<pattern> && pytest`.

5. **List it in the README** problems table. Use the source tag in the `#` column
   for non-LeetCode entries.

6. **Add to notes when relevant — but ASK FIRST.** Before editing any file under
   `notes/` (or the README), propose the change and wait for confirmation; don't
   edit them unprompted.
   - `notes/tricks.md` — if there's a clever one-liner or non-obvious pattern.
     Include a snippet and a `From:` link to the file.
   - `notes/python-builtins.md` — this is meant to be a reference for **every**
     Python built-in, not only a fixed tracked subset. When a solution uses a
     built-in (or string method) that isn't documented yet, add an entry for it;
     when it uses one already present as a TODO placeholder, fill in the real
     example and set its `Used in:` link.
   - `notes/redo.md` — if it's a problem to revisit (status ❌ Stuck / ⚠️ Redo).
   - `notes/theory/` — for reusable theory, not per-problem tricks: e.g.
     `algorithmic_concepts.md` (general algorithm/math ideas like bijection,
     counting inversions) and `recursive_functions_big_o_master_theorem.md`. When a
     problem hinges on such a concept, add/extend the concept here and reference the
     solution file from it.
     - In `algorithmic_concepts.md`, each concept is a **numbered** `##` heading
       (`## 1. …`, `## 2. …`); when adding one, give it the next number — the goal
       is a growing list of the ~50 most useful concepts.
   - **Also ask the user for a `THOUGHTS:` note** at this point — if they have any
     reflection on the problem, add it as a `THOUGHTS:` comment in the solution
     file (see below). Don't invent the content — use the user's own words.
     If a thought was already given (in the pasted code's comments or in the
     prompt), capture that instead of asking again, refining it only as needed to
     match the convention and read clearly — keep the user's meaning intact.

7. **If files were moved or renamed**, update everything that points at them:
   - the import line in the matching `test_*.py`
   - links/paths in `README.md` and under `notes/`
   Then re-run the affected tests to confirm nothing broke.

## Personal reflections: the `THOUGHTS:` tag

Per-problem reflections live as a comment **in the solution file**, marked with a
consistent, greppable tag so they can be collected on demand:

```bash
grep -rn "THOUGHTS:" patterns/
```

- **Spelling is fixed:** always `THOUGHTS:` (exact string) — a typo'd tag is silently
  missed by the grep.
- **Where to put it:** right under the `#<id>. <title>` header line, above the
  function. One block per problem.
- **What to write:** the *non-obvious* part for you — e.g. "the code was easy, the
  hard part was understanding the question", the key insight, what tripped you up,
  or what you'd do faster next time. Skip it if there's nothing worth saying.

```python
#1790. Check if One String Swap Can Make Strings Equal
# THOUGHTS: code was easy; the hard part was parsing the question — the two
#           mismatches must *mirror* each other, not just be equal in count.
def areAlmostEqual(s1, s2):
    ...
```

## Stateful I/O problems (Codeforces-style)

For judges that stream a sequence of commands over stdin (e.g. Codeforces 7B):
hold the state in a **class whose methods RETURN their output** (id / `"NULL"` /
`None` for no output) instead of printing, so tests can drive it; keep a thin
`__main__` driver that **dict-dispatches** commands and prints any non-`None`
return. See [memory_manager_cf7b.py](patterns/design/memory_manager_cf7b.py).

## Notes on style

- Keep solutions faithful to the user's own code; don't silently "improve" logic.
  If a change is needed for correctness (e.g. a missing modulo), call it out.
- Comments should be concise. Use short `#` comments for brief notes; for a long
  explanation, use a triple-quoted block (`""" ... """`) instead of many stacked
  `#` lines.
