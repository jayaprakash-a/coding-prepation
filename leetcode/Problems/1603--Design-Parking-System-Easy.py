class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.bigFree = big
        self.medium = medium
        self.mediumFree = medium
        self.small = small
        self.smallFree = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigFree > 0:
                self.bigFree -= 1
                return True
            return False
        if carType == 2:
            if self.mediumFree > 0:
                self.mediumFree -= 1
                return True
            return False
        if carType == 3:
            if self.smallFree > 0:
                self.smallFree -= 1
                return True
            return False
            


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)