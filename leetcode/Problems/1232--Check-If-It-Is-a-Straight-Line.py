class Solution:
    def getSlope(self, p1, p2):
        if p2[0] == p1[0]:
            return 'Eureka'
        return (p2[1] - p1[1])/(p2[0] - p1[0])
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = self.getSlope(coordinates[0], coordinates[1])
        if slope == 'Eureka':
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        for i in range(2, len(coordinates)):
            newSlope = self.getSlope(coordinates[0], coordinates[i])
            if newSlope != slope:
                return False
        
        return True