#942. DI String Match
def diStringMatch(s):
    lo, hi = 0, len(s)
    ans = []
    for perm in s:
        if perm == 'I':          # increasing: take the smallest unused
            ans.append(lo)
            lo += 1
        elif perm == 'D':        # decreasing: take the largest unused
            ans.append(hi)
            hi -= 1

    ans.append(lo)               # lo == hi here: the last remaining value
    return ans
