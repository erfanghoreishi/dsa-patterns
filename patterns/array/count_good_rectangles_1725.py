#1725. Number Of Rectangles That Can Form The Largest Square
# THOUGHTS: the solution is easy; the hard part is understanding the problem.
#           the list .count() method helps a lot here.
def countGoodRectangles(rectangles):
    sides = [min(w, h) for w, h in rectangles]
    max_len = max(sides)

    return sides.count(max_len)
