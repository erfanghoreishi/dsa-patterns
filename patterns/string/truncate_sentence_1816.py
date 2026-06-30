#1816. Truncate Sentence
def truncateSentence(s, k):
    result = s.split()

    return " ".join(result[0:k])
