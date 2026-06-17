#2586. Count the Number of Vowel Strings in Range
def vowelStrings(words, left, right):
    vowels = set('aeiou')
    # sum() over booleans counts the True's (True == 1) — no explicit counter
    return sum(
        word[0] in vowels and word[-1] in vowels
        for word in words[left:right + 1]
    )
