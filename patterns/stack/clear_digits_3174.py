#3174. Clear Digits
def clearDigits(s: str) -> str:
    s = list(s)
    p = 0
    for char in s:
        if char.isdigit():
            p-=1
        else:
            s[p]=char
            p+=1

    return ''.join(s[0:p])
