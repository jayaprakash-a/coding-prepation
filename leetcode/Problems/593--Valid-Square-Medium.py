class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        distances = []
        
        for i in range(4):
            for j in range(i+1, 4):
                dist = (points[i][1]-points[j][1])**2 + (points[i][0]-points[j][0])**2
                distances.append(dist)
        distances.sort()
        
        if distances.count(distances[0]) == 4 and distances.count(distances[-1]) == 2 and distances[-1] == 2*distances[0]:
            return True
        
        return False