#3754. Concatenate Non-Zero Digits and Multiply by Sum I
def sumAndMultiply(n):
    digits = [d for d in str(n) if d != '0']    # drop every '0' digit
    total = sum(map(int, digits))               # sum of the remaining digits
    x = int(''.join(digits)) if digits else 0   # concatenate them back into a number
    return x * total
