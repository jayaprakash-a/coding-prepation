class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        matDict = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (i-j) not in matDict.keys():
                    matDict[i-j] = [mat[i][j]]
                else:
                    matDict[i-j].append(mat[i][j])
        
        for key in matDict.keys():
            matDict[key] = sorted(matDict[key])
            
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = matDict[i-j].pop(0)
                    
        # print(matDict)
        
        return mat
                    
        