#2133. Check if Every Row and Column Contains All Numbers
def checkValid(matrix):
    requiered_nums = set(n for n in range(1, len(matrix) + 1))

    for col in zip(*matrix):
        if set(col) != requiered_nums:
            return False
    for row in matrix:
        if set(row) != requiered_nums:
            return False
    return True
