class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        distMap= {}
        for row in range(R):
            for col in range(C):
                dist = abs(row-r0)+abs(col-c0)
                if dist not in distMap:
                    distMap[dist] = [[row, col]]
                else:
                    distMap[dist].append([row, col])
        answer = []
        for key in sorted(distMap.keys()):
            answer += (distMap[key])
            
        return answer
        