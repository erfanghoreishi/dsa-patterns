#1518. Water Bottles
def numWaterBottles(numBottles, numExchange):
    answer = empty = numBottles

    while empty >= numExchange:
        new_bottles = empty // numExchange
        answer += new_bottles
        empty = empty % numExchange + new_bottles

    return answer


# def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#     total = numBottles
#     rem = 0
#     while numBottles >= 1:
#         total += ((numBottles) / numExchange)
#         numBottles = numBottles / numExchange
#     return math.floor(total)
