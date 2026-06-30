#1071. Greatest Common Divisor of Strings
# THOUGHTS: the slick idea is math.gcd — if a common divisor string exists, both
#   strings are repetitions of it, and then str1 + str2 == str2 + str1. When that
#   holds, the answer is just str1[:gcd(len1, len2)] (see the commented version).
def gcdOfStrings(str1, str2):
    shorter = min(len(str1), len(str2))

    for len_gcd in range(shorter, 0, -1):
        if shorter % len_gcd != 0:
            continue
        candidate = str1[:len_gcd]

        if candidate * (len(str1) // len_gcd) == str1 and \
           candidate * (len(str2) // len_gcd) == str2:
            return candidate

    return ""


"""
Slicker O(n) version using the commutativity test + math.gcd:

    import math
    def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1:      # no shared base pattern
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]
"""
