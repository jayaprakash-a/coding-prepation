class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        scenario = [[s1,s2] for s1 in [-1,1] for s2 in [-1,1]]
        answer = 0
        for entry in scenario:
            newArr = [entry[0]*arr1[i]+entry[1]*arr2[i]+i for i in range(len(arr1))]
            mx = max(newArr)
            mn = min(newArr)
            answer = max(answer, mx-mn)
        return answer
        
        