class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        negVals = []
        posVals = []
        posSum = 0
        for num in A:
            if num < 0:
                negVals.append(num)
            else:
                posVals += [num]
                posSum += num
        negVals = sorted(negVals)
        if K > len(negVals):
            if 0 in A:
                return posSum - sum(negVals)
            if (K-len(negVals)) %2 == 0:
                return posSum - sum(negVals) 
            else:
                if len(negVals) > 0:
                    return posSum - sum(negVals) - 2*min(-negVals[-1], min(posVals))
                else:
                    return posSum - 2*min(A)
        else:
            return posSum  - sum(negVals[:K]) + sum(negVals[K:])
        