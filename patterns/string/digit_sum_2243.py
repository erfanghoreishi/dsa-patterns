#2243. Calculate Digit Sum of a String
# Asked in a Susquehanna International Group (SIG) interview — 2026-06-30.
def digitSum(s, k):
    while len(s) > k:
        group = []
        for left in range(0, len(s), k):
            nums = map(int, s[left:left + k])   # digits of this k-sized chunk
            group.append(sum(nums))
        s = "".join(map(str, group))

    return s
