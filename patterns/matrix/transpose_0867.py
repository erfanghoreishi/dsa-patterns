#867. Transpose Matrix
# THOUGHTS: solution 1 is a good drill for nested list comprehension. Can't do it
#   in constant memory here because the matrix isn't square; the in-place square
#   version (48. Rotate Image) is a good next problem.
def transpose(matrix):
    h = len(matrix)
    w = len(matrix[0])
    return [[matrix[j][i] for j in range(h)] for i in range(w)]


# Solution 2 — one-liner with zip (zip(*matrix) yields tuples, so wrap in list):
#   return [list(row) for row in zip(*matrix)]
#
# Solution 3 — explicit nested loops:
#   new = []
#   for i in range(w):
#       row = []
#       for j in range(h):
#           row.append(matrix[j][i])
#       new.append(row)
#   return new
