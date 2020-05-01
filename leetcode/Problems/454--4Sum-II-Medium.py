class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sumVals = {}
        for a in A:
            for b in B:
                if a+b in sumVals:
                    sumVals[a+b] += 1
                else:
                    sumVals[a+b] = 1
        answer = 0
        for c in C:
            for d in D:
                if -c-d in sumVals:
                    answer += sumVals[-c-d]
        return answer
            