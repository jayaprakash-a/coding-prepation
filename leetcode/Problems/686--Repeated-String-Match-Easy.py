class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        orig = A
        times = math.ceil(len(B)/len(A))
        A = A*times
        if B in A:
            return times
        for _ in range(2):
            A += orig
            times += 1
            if B in A:
                return times
            
        return -1
        