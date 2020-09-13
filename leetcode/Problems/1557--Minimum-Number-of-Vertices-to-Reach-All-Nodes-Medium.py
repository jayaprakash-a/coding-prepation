class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [0 for _ in range(n)]
        for [x, y] in edges:
            count[y] += 1
        answer = []
        for i in range(n):
            if count[i] == 0:
                answer.append(i)
        return answer

                
        