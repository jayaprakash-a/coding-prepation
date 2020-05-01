class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        answer = 0
        modVals = [0]*K
        for N in range(1, K+1):
            answer = 10*answer+1
            modVal = answer%K
            if modVal==0:
                return N
            else:
                if modVals[modVal] == 1:
                    return -1
                else:
                    modVals[modVal] = 1
        return -1