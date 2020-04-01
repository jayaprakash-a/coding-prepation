class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # majority = A[0]
        # count = 1
        for i in range(len(A)):
            if A.count(A[i]) == len(A)/2:
                return A[i]
            
        return 0
        