# Minesweeper  (Quera — not on LeetCode)
# Given a grid and a set of bomb cells, print each cell as '*' if it's a bomb,
# otherwise the count of bombs among its 8 neighbours.

# 8 neighbour offsets — precomputed once so counting has no repeated if-checks
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def minesweeper(rows, cols, bombs):
    """Return the board as a list of space-joined row strings (1-indexed cells)."""
    bombs = set(bombs)
    board = []
    for r in range(1, rows + 1):
        srow = []
        for c in range(1, cols + 1):
            if (r, c) in bombs:
                srow.append("*")
            else:
                # count bomb neighbours: sum of booleans over the 8 offsets
                count = sum((r + dr, c + dc) in bombs for dr, dc in DIRECTIONS)
                srow.append(str(count))
        board.append(" ".join(srow))
    return board


if __name__ == "__main__":
    row, col = map(int, input().split())
    nbomb = int(input())
    bombs = set()
    for _ in range(nbomb):
        x, y = map(int, input().split())
        bombs.add((x, y))
    print("\n".join(minesweeper(row, col, bombs)))
