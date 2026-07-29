#909. Snakes and Ladders
# THOUGHTS: straightforward if you're confident with BFS, extra hard if you're not.
#           the fiddly part is converting a square number -> (row, col) in the
#           boustrophedon (snake) layout. See notes/theory/algorithmic_concepts.md (10. BFS).
from collections import deque


def snakesAndLadders(board):
    n = len(board)
    target = n * n
    visited = {1}
    q = deque([(1, 0)])                 # (square, moves so far)

    def label(cell):
        # 1-indexed square -> board value, accounting for the snake/boustrophedon order
        idx = cell - 1
        level = idx // n                # row counted from the bottom
        row = n - 1 - level             # actual row index (board[0] is the top row)
        col = idx % n if level % 2 == 0 else n - 1 - idx % n
        return board[row][col]

    while q:
        curr, moves = q.popleft()
        if curr == target:
            return moves

        for child in range(curr + 1, curr + 7):   # a die roll: 1..6 ahead
            if child > target:
                break
            # if child has a snake/ladder (value != -1), redirect to its destination
            landing_square = label(child) if label(child) != -1 else child
            if landing_square not in visited:
                visited.add(landing_square)
                q.append((landing_square, moves + 1))

    return -1
