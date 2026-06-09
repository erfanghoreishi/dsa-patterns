#2379. Minimum Recolors to Get K Consecutive Black Blocks
def minimumRecolors(blocks, k):
    whites = blocks[:k].count('W')
    min_whites = whites

    for i in range(k, len(blocks)):
        whites += (blocks[i] == 'W')      # 1 if blocks[i] == 'W' else 0
        whites -= (blocks[i - k] == 'W')
        min_whites = min(whites, min_whites)

    return min_whites
