#17. Letter Combinations of a Phone Number
def letterCombinations(digits):
    if not digits:
        return []
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    current = []     # the partial combination being built
    result = []

    def backtrack(index):
        # one recursion level per digit; index == len(digits) means a full combination
        if index == len(digits):
            result.append(''.join(current))
            return
        for letter in phone[digits[index]]:
            current.append(letter)
            backtrack(index + 1)
            current.pop()          # undo the choice before trying the next letter

    backtrack(0)
    return result


"""
Built-in one-liner alternative — the cartesian product across one letter group per
digit is exactly "pick one letter from each group, every way":

    from itertools import product
    letter_groups = [phone[d] for d in digits]
    return [''.join(combo) for combo in product(*letter_groups)]
"""
