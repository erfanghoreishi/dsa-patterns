#2114. Maximum Number of Words Found in Sentences
# THOUGHTS: max() over a generator (no []) streams items one at a time and never
#   builds the intermediate list — saves memory. The list-comprehension form (with
#   []) materializes the whole list first, then scans it. Both look at every element
#   once; the difference is memory, not the number of passes.
def mostWordsFound(sentences):
    return max(len(sentence.split()) for sentence in sentences)


# Explicit loop equivalent:
# def mostWordsFound(sentences):
#     max_words = 0
#     for sentence in sentences:
#         max_words = max(max_words, len(sentence.split()))
#     return max_words
