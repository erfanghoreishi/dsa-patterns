#2596. Check Knight Tour Configuration
def checkValidGrid(grid):
    if grid[0][0] != 0:
        return False

    n = len(grid)
    pos = {grid[r][c]: (r, c) for r in range(n) for c in range(n)}
    moves = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}

    for step in range(n * n - 1):
        r1, c1 = pos[step]
        r2, c2 = pos[step + 1]
        if (r2 - r1, c2 - c1) not in moves:
            return False

    return True
