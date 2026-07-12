#258. Add Digits
def addDigits(num):
    while num >= 10:                 # repeat until a single digit remains
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10    # take the last digit
            num = num // 10          # drop it
        num = digit_sum
    return num


# O(1) closed form (digital root): return 0 if num == 0 else 1 + (num - 1) % 9
