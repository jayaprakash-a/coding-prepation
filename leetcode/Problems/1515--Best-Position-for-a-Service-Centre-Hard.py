class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # print('------------------')
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def distSum(x, y):
            return sum([sqrt((pos[0]-x)**2 + (pos[1]-y)**2) for pos in positions])
        meanx, meany = 0, 0
        for pos in positions:
            meanx += pos[0]
            meany += pos[1]
        meanx /= len(positions)
        meany /= len(positions)
        meanDist = distSum(meanx, meany)
        
        delta = 100.0
        epsilon = 0.0000001
        while delta > epsilon:
            valid = False
            for mov in dirs:
                newx, newy = meanx+delta*mov[0], meany+delta*mov[1]
                newDist = distSum(newx, newy)
                if newDist < meanDist:
                    meanDist = newDist
                    meanx = newx
                    meany = newy
                    valid = True
                    break
            if not valid:
                delta /= 2
        return meanDist