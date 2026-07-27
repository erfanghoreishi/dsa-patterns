#146. LRU Cache
class LRUCache:
    """
    Two dicts plus a monotonically increasing "priority" counter:

        by_key[key]         = (value, priority)   # current priority for each live key
        by_priority[prio]   = key                 # reverse lookup; larger priority = newer

    Every access (get or put) assigns the next (largest) priority, so the SMALLEST
    live priority is always the least-recently-used entry. `oldest_priority` is a
    low-water mark that walks upward to find that LRU entry when we must evict.

    NOTE: this is O(1) amortized, but eviction can scan gaps in `oldest_priority`.
    See notes/redo.md — the true O(1) design uses a hashmap + doubly linked list.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.next_priority = 0     # priority to hand out on the next access (grows forever)
        self.oldest_priority = 0   # low-water mark used to locate the LRU entry
        self.by_key = {}           # key      -> (value, priority)
        self.by_priority = {}      # priority -> key

    def _touch(self, key, value):
        """Store key=value with a fresh (largest) priority, marking it most-recent."""
        self.by_key[key] = (value, self.next_priority)
        self.by_priority[self.next_priority] = key
        self.next_priority += 1

    def get(self, key):
        if key not in self.by_key:
            return -1
        value, priority = self.by_key[key]
        del self.by_priority[priority]   # retire the old priority,
        self._touch(key, value)          # then re-assign as most-recently-used
        return value

    def put(self, key, value):
        if key in self.by_key:
            # overwriting an existing key: retire its old priority, no eviction
            _, old_priority = self.by_key[key]
            del self.by_priority[old_priority]
        elif len(self.by_key) >= self.capacity:
            # full and inserting a NEW key: evict the least-recently-used entry.
            # the LRU is the smallest live priority — advance oldest_priority up to it.
            while self.oldest_priority not in self.by_priority:
                self.oldest_priority += 1
            lru_key = self.by_priority.pop(self.oldest_priority)
            del self.by_key[lru_key]
            self.oldest_priority += 1

        self._touch(key, value)
