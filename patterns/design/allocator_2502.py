#2502. Design Memory Allocator
# Design problem — kept as a class (not a plain function) since the API is the point.
class Allocator(object):
    def __init__(self, n):
        self.memory = [0] * n           # 0 = free, else the owning mID
        self.allocations = {}           # mID -> list of (left, right) blocks

    def allocate(self, size, mID):
        left = 0
        for right in range(len(self.memory)):
            if self.memory[right] != 0:
                left = right + 1                  # restart the free run past this used cell
            elif (right - left) + 1 == size:      # free run reached the requested size
                self.memory[left:right + 1] = [mID] * size
                self.allocations.setdefault(mID, []).append((left, right))
                return left
        return -1

    def freeMemory(self, mID):
        freed = 0
        for left, right in self.allocations.pop(mID, []):
            for i in range(left, right + 1):
                self.memory[i] = 0
            freed += right - left + 1
        return freed
