#680. Valid Palindrome II
# THOUGHTS: the insight is why branching at the *first* mismatch is enough — every
#           pair matched before it is already fine, so the one deletion has to be
#           s[l] or s[r]. Two O(n) checks, not a re-search.
#           See notes/theory/algorithmic_concepts.md (13.).
def validPalindrome(s):
    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True

    l, r = 0, len(s) - 1

    while l < r:
        # first mismatch: the deleted char must be one of these two, so try both
        if s[l] != s[r]:
            return is_pal(l + 1, r) or is_pal(l, r - 1)

        l += 1
        r -= 1

    return True
