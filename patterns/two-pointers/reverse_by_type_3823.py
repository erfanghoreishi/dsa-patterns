#3823. Reverse Letters Then Special Characters in a String
def reverseByType(s):
    letters = [char for char in s if char.isalpha()][::-1]
    special = [char for char in s if not char.isalpha()][::-1]

    result = []
    li, si = 0, 0
    for i in range(len(s)):
        if s[i].isalpha():
            result.append(letters.pop(0))
        else:
            result.append(special.pop(0))

    return "".join(result)
