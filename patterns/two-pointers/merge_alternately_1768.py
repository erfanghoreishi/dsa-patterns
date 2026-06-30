#1768. Merge Strings Alternately
# THOUGHTS: cool trick — implement the two-pointer pattern with just one pointer.
def mergeAlternately(word1, word2):
    ans = []
    left = 0
    while left < len(word1) or left < len(word2):
        if left < len(word1):
            ans.append(word1[left])
        if left < len(word2):
            ans.append(word2[left])
        left += 1

    return "".join(ans)


"""
Alternative — itertools.zip_longest pads the shorter string with fillvalue="":

    from itertools import zip_longest
    def mergeAlternately(word1, word2):
        result = []
        for c1, c2 in zip_longest(word1, word2, fillvalue=""):
            result.append(c1 + c2)
        return "".join(result)
"""
