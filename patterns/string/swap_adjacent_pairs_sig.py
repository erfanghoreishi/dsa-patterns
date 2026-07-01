# Swap Adjacent Character Pairs
# Asked in a Susquehanna International Group (SIG) interview — 2026-06-30.
#
# For each adjacent pair, swap them; if the length is odd the last char stays put.
#   "abcdef" -> "badcfe"   "abcde" -> "badce"
def swapAdjacentPairs(s):
    result = []
    # zip pairs each even-index char with the next odd-index char: (s[0], s[1]), ...
    for even, odd in zip(s[0::2], s[1::2]):
        result.append(odd)      # the swap: odd (s[1]) comes out first,
        result.append(even)     # then even (s[0])
    if len(s) % 2 != 0:
        result.append(s[-1])    # odd length: last char has no partner
    return "".join(result)
