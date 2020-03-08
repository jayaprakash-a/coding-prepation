class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N//2, N+1):
            if i > 0:
                if str(bin(i))[2:] not in S:
                    return False
        
        return True
        