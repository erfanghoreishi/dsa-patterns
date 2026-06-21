#290. Word Pattern
# A bijection check: pattern chars <-> words must map one-to-one, both ways.
# See notes/theory/algorithmic_concepts.md (1. Bijection).
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    pattern_map = {}
    for p, w in zip(pattern, words):
        pattern_map[p] = w

    # consistent mapping one way AND equal distinct counts (one-to-one both ways)
    return s == " ".join([pattern_map[p] for p in pattern]) and \
        len(set(pattern)) == len(set(words))
