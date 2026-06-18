#1790. Check if One String Swap Can Make Strings Equal
def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True

    # collect only the positions that differ (filter `if` at the end)
    diffs = [(a, b) for a, b in zip(s1, s2) if a != b]

    # one swap fixes it iff there are exactly 2 mismatches that mirror each other:
    # (a, b) and (b, a)  ->  diffs[1] reversed equals diffs[0]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
