# test_find_peaks_2951.py
from find_peaks_2951 import findPeaks


def test_no_peak_plateau():
    assert findPeaks([2, 4, 4]) == []


def test_two_peaks():
    assert findPeaks([1, 4, 3, 8, 5]) == [1, 3]


def test_monotonic():
    assert findPeaks([1, 2, 3]) == []


def test_single_peak():
    assert findPeaks([1, 5, 1]) == [1]
