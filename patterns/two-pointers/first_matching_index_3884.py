#3884. First Matching Character From Both Ends
def firstMatchingIndex(s):
    """
    range(len(s)//2 + 1): we compare the pair (i, n-1-i) moving inward. The +1
    matters for ODD lengths — it includes the middle index n//2, where s[i] is
    compared with itself (always equal), so a lone middle char counts as a match.
    For EVEN lengths that extra index just re-checks an already-seen pair (harmless).
    """
    for i in range(len(s) // 2 + 1):
        if s[i] == s[len(s) - i - 1]:
            return i
    return -1
