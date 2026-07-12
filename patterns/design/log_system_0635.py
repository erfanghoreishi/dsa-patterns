#635. Design Log Storage System  (LeetCode Premium)
"""
Each log has a unique ID and a timestamp of the form "Year:Month:Day:Hour:Minute:Second"
(all zero-padded), e.g. "2017:01:01:23:59:59".

Implement LogSystem:
  - put(id, timestamp): store the log (id, timestamp).
  - retrieve(start, end, granularity): return the IDs of logs whose timestamp is in
    the inclusive range [start, end], compared only down to `granularity`
    (one of "Year","Month","Day","Hour","Minute","Second"). Fields finer than the
    granularity are ignored.

Example:
  put(1, "2017:01:01:23:59:59"); put(2, "2017:01:01:22:59:59"); put(3, "2016:01:01:00:00:00")
  retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year") -> [1, 2, 3]
  retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour") -> [1, 2]
    (log 3 excluded: 2016:01:01:00 comes before the start hour 2016:01:01:01)

Constraints: 1 <= id <= 500; 2000 <= Year <= 2017; timestamps are valid; at most
500 put/retrieve calls. (Output ID order does not matter.)
"""


# THOUGHTS: clever trick — a zero-padded "Y:M:D:H:M:S" timestamp compares
#   lexicographically the same as chronologically, so we can compare string
#   prefixes directly (no int conversion needed). The prefix length picks the
#   granularity (Year = 4 chars, Month = 7, ...).
#   See notes/theory/algorithmic_concepts.md (8. fixed-width strings compare like numbers).
class LogSystem(object):
    def __init__(self):
        self.logs = []
        self.granularity_len = {
            'Year': 4, 'Month': 7, 'Day': 10,
            'Hour': 13, 'Minute': 16, 'Second': 19,
        }

    def put(self, id, timestamp):
        self.logs.append((id, timestamp))

    def retrieve(self, start, end, granularity):
        idx = self.granularity_len[granularity]
        start, end = start[:idx], end[:idx]
        return [key for key, time in self.logs if start <= time[:idx] <= end]


"""
Alternative — encode each timestamp as one mixed-radix integer instead of comparing
string prefixes (each multiplier is the next field's max+1, so fields never
overflow). Works identically:

    def __init__(self):
        self.logs = []
        self.grans = ["Year", "Month", "Day", "Hour", "Minute", "Second"]

    def put(self, id, timestamp):
        self.logs.append((id, timestamp))

    def retrieve(self, start, end, granularity):
        s = self.to_int(start, granularity)
        e = self.to_int(end, granularity)
        return [key for key, t in self.logs if s <= self.to_int(t, granularity) <= e]

    def to_int(self, timestamp, granularity):
        fields = list(map(int, timestamp.split(':')))
        for i in range(self.grans.index(granularity) + 1, 6):
            fields[i] = 0
        year, month, day, hour, minute, second = fields
        return ((((year * 13 + month) * 32 + day) * 24 + hour) * 60 + minute) * 60 + second
"""
