#3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    sub = set()          # characters currently in the window [left, right]
    left = 0
    max_len = 0
    for right in range(len(s)):
        # shrink from the left until s[right] is no longer a duplicate
        while s[right] in sub:
            sub.remove(s[left])
            left += 1
        sub.add(s[right])
        max_len = max(max_len, len(sub))

    return max_len
