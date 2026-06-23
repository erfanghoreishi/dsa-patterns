#2697. Lexicographically Smallest Palindrome
def makeSmallestPalindrome(s):
    s = list(s)
    # range(len(s)//2): only the mirror pairs; the odd middle char never needs
    # changing. See notes/theory/algorithmic_concepts.md (4. //2 vs //2+1).
    for i in range(len(s) // 2):
        iright = len(s) - i - 1
        if s[iright] != s[i]:
            if s[iright] > s[i]:
                s[iright] = s[i]
            else:
                s[i] = s[iright]

    return ''.join(s)
