#482. License Key Formatting
def licenseKeyFormatting(s, k):
    # strip dashes, upper-case, reverse so grouping starts from the RIGHT
    s = s.replace('-', '').upper()[::-1]
    # chunk into k-length groups, join with '-', then reverse the whole thing back
    return '-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1]


"""
Explicit alternative on the cleaned string t = s.replace('-', '').upper():

    ans = []
    counter = 0
    for ch in reversed(t):
        if counter % k == 0 and counter != 0:
            ans.append('-')
        ans.append(ch)
        counter += 1
    return "".join(reversed(ans))

Key info: strings are immutable in Python, so building the result with += makes a
new string every step (O(n) per op, O(n^2) overall). Use a list + append and one
final join instead — O(n) total.
"""
