class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper+lower != sum(colsum):
            return []
        answer = [[-1 for _ in range(len(colsum))]for _ in range(2)]
        indices = []
        for i in range(len(colsum)):
            if colsum[i] == 0:
                answer[0][i] = 0
                answer[1][i] = 0
            elif colsum[i] == 2:
                answer[0][i] = 1
                answer[1][i] = 1
                upper -= 1
                lower -= 1
            else:
                indices.append(i)
        if upper+lower != len(indices):
            return []
        for entry in indices:
            if upper > 0:
                answer[0][entry] = 1
                answer[1][entry] = 0
                upper -= 1
            elif lower > 0:
                answer[1][entry] = 1
                answer[0][entry] = 0
                lower -= 1
            else:
                return []        
        if upper != 0 or lower != 0:
            return []
        return answer
        
        