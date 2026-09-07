# test_can_attend_meetings_0252.py
from can_attend_meetings_0252 import canAttendMeetings


def test_example_1():
    assert canAttendMeetings([(0, 30), (5, 10), (15, 20)]) is False


def test_example_2():
    assert canAttendMeetings([(5, 8), (9, 15)]) is True


def test_empty():
    assert canAttendMeetings([]) is True


def test_single_meeting():
    assert canAttendMeetings([(3, 7)]) is True


def test_touching_is_not_a_conflict():
    assert canAttendMeetings([(0, 8), (8, 10)]) is True


def test_unsorted_input():
    assert canAttendMeetings([(15, 20), (0, 30), (5, 10)]) is False


def test_identical_meetings():
    assert canAttendMeetings([(1, 5), (1, 5)]) is False


def test_one_contains_another():
    assert canAttendMeetings([(1, 100), (20, 30)]) is False


def test_conflict_only_at_the_end():
    assert canAttendMeetings([(0, 2), (2, 4), (4, 6), (5, 7)]) is False


def test_same_start_different_end():
    assert canAttendMeetings([(4, 9), (4, 5)]) is False
