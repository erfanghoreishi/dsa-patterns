#1845. Seat Reservation Manager
import heapq


class SeatManager:
    def __init__(self, n):
        self.seats = [i for i in range(1, n + 1)]   # all seats start free
        self.n = n
        heapq.heapify(self.seats)                    # min-heap: smallest seat on top

    def reserve(self):
        return heapq.heappop(self.seats)             # always the lowest free seat

    def unreserve(self, seatNumber):
        heapq.heappush(self.seats, seatNumber)       # freed seat rejoins the heap
