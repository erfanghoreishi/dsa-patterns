#1603. Design Parking System
class ParkingSystem(object):
    def __init__(self, big, medium, small):
        self.size_map = {1: big, 2: medium, 3: small}   # carType -> remaining slots

    def addCar(self, carType):
        if self.size_map[carType] == 0:
            return False
        self.size_map[carType] -= 1
        return True
