#344. Reverse String
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        # inline swap (no temp variable) — tuple pack/unpack
        s[right], s[left] = s[left], s[right]
        left += 1
        right -= 1
    return s
