# test_log_system_0635.py
from log_system_0635 import LogSystem


def _seeded():
    ls = LogSystem()
    ls.put(1, "2017:01:01:23:59:59")
    ls.put(2, "2017:01:01:22:59:59")
    ls.put(3, "2016:01:01:00:00:00")
    return ls


def test_retrieve_year():
    ls = _seeded()
    assert sorted(ls.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")) == [1, 2, 3]


def test_retrieve_hour():
    ls = _seeded()
    # log 3 excluded: its hour (00) is before the start hour (01)
    assert sorted(ls.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")) == [1, 2]


def test_retrieve_second_exact():
    ls = _seeded()
    # at Second granularity, only log 2 (22:59:59) is within [..01:01:01, ..23:00:00]
    assert sorted(ls.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Second")) == [2]


def test_retrieve_none_in_range():
    ls = _seeded()
    assert ls.retrieve("2018:01:01:00:00:00", "2019:01:01:00:00:00", "Year") == []
