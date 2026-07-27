#696. Count Binary Substrings
# THOUGHTS: took hours — the trick is you DON'T need the O(n^3) check-every-substring
#           two-pointer approach. Collapse s into run lengths of consecutive equal
#           chars (e.g. "11000111" -> [2, 3, 3]); each adjacent pair contributes
#           min(a, b) valid substrings. Easy once seen, but hard to invent cold.
def countBinarySubstrings(s):
    # build run lengths: "11000" -> [2, 3]
    groups = []
    prev = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            groups.append(i - prev)
            prev = i
    groups.append(len(s) - prev)

    # each adjacent pair of runs yields min(left, right) balanced substrings
    ans = 0
    for i in range(1, len(groups)):
        ans += min(groups[i], groups[i - 1])
    return ans


"""
One-liner with itertools.groupby (groups consecutive equal chars; take run lengths,
then sum the min of each neighbouring pair):

    import itertools
    def countBinarySubstrings(s):
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
"""
