#7B. Memory Manager  (Codeforces — https://codeforces.com/problemset/problem/7/B)
# Stateful I/O problem: the logic lives in a class (methods RETURN their output),
# and the stdin/stdout driver is in __main__ — so the logic stays unit-testable.
class MemoryManager:
    def __init__(self, m):
        self.mem = [0] * m            # 0 = free, else the owning allocation id
        self.next_id = 1              # ids are handed out 1, 2, 3, ... on success only
        self.active_ids = set()

    def alloc(self, n):
        """Allocate the first free block of size n. Return its id, or 'NULL'."""
        left = 0
        for right in range(len(self.mem)):
            if self.mem[right] != 0:
                left = right + 1                  # restart the free run past this used cell
            elif right - left + 1 == n:
                self.mem[left:right + 1] = [self.next_id] * (right - left + 1)
                allocated = self.next_id
                self.active_ids.add(allocated)
                self.next_id += 1
                return allocated
        return "NULL"

    def erase(self, x):
        """Free the block with id x. Return 'ILLEGAL_ERASE_ARGUMENT' if invalid, else None."""
        if x not in self.active_ids:
            return "ILLEGAL_ERASE_ARGUMENT"
        self.active_ids.discard(x)
        for i in range(len(self.mem)):
            if self.mem[i] == x:
                self.mem[i] = 0
        return None

    def defragment(self):
        """Compact all used blocks to the front, preserving order. No output."""
        defragged = [0] * len(self.mem)
        idef = 0
        for value in self.mem:
            if value != 0:
                defragged[idef] = value
                idef += 1
        self.mem = defragged
        return None


if __name__ == "__main__":
    t, m = map(int, input().split())
    manager = MemoryManager(m)
    handlers = {
        "alloc": lambda a: manager.alloc(int(a)),
        "erase": lambda a: manager.erase(int(a)),
        "defragment": lambda a: manager.defragment(),
    }
    out = []
    for _ in range(t):
        cmd, *rest = input().split()
        result = handlers[cmd](rest[0] if rest else None)
        if result is not None:                # alloc id / NULL / ILLEGAL_ERASE_ARGUMENT
            out.append(str(result))
    print("\n".join(out))
