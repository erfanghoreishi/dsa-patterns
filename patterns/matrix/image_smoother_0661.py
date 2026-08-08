#661. Image Smoother
# 9 offsets — the 8 neighbours PLUS (0, 0), since the cell itself counts in the average.
DIR = [(-1, -1), (-1, 0), (-1, 1),
       (0, -1),  (0, 0),  (0, 1),
       (1, -1),  (1, 0),  (1, 1)]


def imageSmoother(img):
    ROWS = len(img)
    COLS = len(img[0])
    ans = [[0] * COLS for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            total = 0
            count = 0                    # counted per cell: corners/edges see fewer
            for dr, dc in DIR:
                if 0 <= row + dr < ROWS and 0 <= col + dc < COLS:
                    total += img[row + dr][col + dc]
                    count += 1
            ans[row][col] = total // count   # floor division, per the problem
    return ans
