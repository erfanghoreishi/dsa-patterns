#883. Projection Area of 3D Shapes
from typing import List


def projectionArea(grid: List[List[int]]) -> int:
    shadow_xy = sum([1 for row in grid for col in row if col != 0])  # top view: non-zero cells
    shadow_zx = sum([1 * max(row) for row in grid])                  # front view: max of each row
    shadow_yz = sum([1 * max(col) for col in zip(*grid)])            # side view: max of each column

    return shadow_xy + shadow_zx + shadow_yz
