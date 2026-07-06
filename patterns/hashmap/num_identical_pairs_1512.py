#1512. Number of Good Pairs
def numIdenticalPairs(nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    """
    A value that appears n times forms one good pair for every unordered pair of
    its positions, i.e. (n-1) + (n-2) + ... + 1 = n(n-1)/2.

    e.g. [1,1,1,1] (n = 4):
        (0,1)(0,2)(0,3) -> 3
        (1,2)(1,3)      -> 2
        (2,3)           -> 1        total 3 + 2 + 1 = 6 = 4*3/2

    Why that sum equals n(n-1)/2: see notes/theory/algorithmic_concepts.md (6. Gauss's sum).
    Use // (integer division) — n*(n-1) is always even, and / would return a float.
    """
    return sum(n * (n - 1) // 2 for n in seen.values())
