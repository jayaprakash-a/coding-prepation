class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        ops = []
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                ops.append(1)
            elif A[i]<A[i+1]:
                ops.append(-1)
            else:
                ops.append(0)
        # print(ops)
        maxVal, answer = 0, 0
        if ops[0] != 0:
            maxVal = 1
            answer = 1
        else:
            maxVal = 0
        for i in range(1, len(ops)):
            # print(maxVal)
            if ops[i] == 0:
                maxVal = 0
            elif ops[i] != ops[i-1]:
                maxVal += 1
                answer = max(maxVal, answer)
            elif ops[i] == ops[i-1] and ops[i] != 0:
                maxVal = 1
            elif ops[i] == ops[i-1] and ops[i] == 0:
                maxVal = 0
            
        return answer + 1