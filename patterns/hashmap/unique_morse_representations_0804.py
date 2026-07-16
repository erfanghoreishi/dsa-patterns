#804. Unique Morse Code Words
# THOUGHTS: good drill for nested inline for-loops — a set comprehension whose
#   element is itself built by a generator: outer `for word in words`, inner
#   `for char in word`. The {..} with no key:value makes it a SET, so duplicate
#   transformations collapse for free and len() is the answer.
def uniqueMorseRepresentations(words):
    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--", "--.."]

    transitions = {"".join(MORSE[ord(char) - ord('a')] for char in word)
                   for word in words}
    return len(transitions)
