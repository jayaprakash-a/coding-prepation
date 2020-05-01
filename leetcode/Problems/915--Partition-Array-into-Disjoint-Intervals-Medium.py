class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        maxVals = [A[0]]
        minVals = [0 for _ in range(len(A))]
        
        for i in range(1, len(A)):
            val = max(maxVals[-1], A[i])
            maxVals.append(val)
        minVals[-1] = A[-1]
        for i in range(len(A)-2, -1, -1):
            minVals[i] = min(minVals[i+1], A[i])
        
        # print(maxVals, minVals)
        for i in range(len(A)):
            if maxVals[i] <= minVals[i+1]:
                return i+1
        return 1