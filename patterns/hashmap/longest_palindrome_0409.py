#409. Longest Palindrome
def longestPalindrome(s: str) -> int:
    freq = {}
    has_odd = False
    count = 0

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for v in freq.values():
        if v % 2 == 0:
            count += v
        else:
            count += (v - 1)
            has_odd = True

    return count + (1 if has_odd else 0)
