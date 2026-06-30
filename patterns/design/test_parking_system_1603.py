# test_parking_system_1603.py
from parking_system_1603 import ParkingSystem


def test_leetcode_example():
    p = ParkingSystem(1, 1, 0)
    assert p.addCar(1) is True     # big
    assert p.addCar(2) is True     # medium
    assert p.addCar(3) is False    # small full
    assert p.addCar(1) is False    # big now full


def test_independent_types():
    p = ParkingSystem(2, 0, 1)
    assert p.addCar(1) is True
    assert p.addCar(2) is False
    assert p.addCar(3) is True
    assert p.addCar(1) is True
    assert p.addCar(1) is False
