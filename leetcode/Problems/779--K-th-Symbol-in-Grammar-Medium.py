class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # print(N, K)
        if N==1 or K==1:
            return 0
        half = 2**(N-2)
        if K > (half):
            return 1-self.kthGrammar(N-1, K-half)
        else:
            return self.kthGrammar(N-1, K)
        