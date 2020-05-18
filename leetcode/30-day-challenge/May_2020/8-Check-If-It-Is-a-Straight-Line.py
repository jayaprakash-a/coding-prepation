class Solution:
    def checkStraightLine(self, points: List[List[int]]) -> bool:
        if len(points) <= 2:
            return True
        if points[1][0] == points[0][0]:
            for i in range(2, len(points)):
                if points[i][0] != points[0][0]:
                    return False
            return True
        slope = (points[1][1]-points[0][1])/ (points[1][0]-points[0][0])
        
        for i in range(2, len(points)):
            newSlope = (points[i][1]-points[0][1])/ (points[i][0]-points[0][0])
            if newSlope != slope:
                return False
        return True