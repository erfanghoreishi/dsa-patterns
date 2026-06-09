#leetcode 3794
def reversePrefix(s, k):
    return s[0:k][::-1]+s[k:]
# def reversePrefix(s, k):
#     l = 0
#     s = list(s)
#     while l < k:
#         s[k-1], s[l] = s[l], s[k-1]
#         l += 1
#         k -= 1
#     return "".join(s)
