#1935. Maximum Number of Words You Can Type
def canBeTypedWords(text, brokenLetters):
    count = 0
    broken = set(brokenLetters)
    for word in text.split():
        # cleaner but harder to remember: if set(word).isdisjoint(broken)
        if not (set(word) & broken):
            count += 1
    return count
