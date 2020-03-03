class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        
        for i in range(len(points)-1):
            maxDiag = max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
            
            answer += maxDiag
            
        return answer
            
            
        
        
        