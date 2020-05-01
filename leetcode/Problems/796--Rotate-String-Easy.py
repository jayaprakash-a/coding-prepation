class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        C = B[1:]+B
        return A in C and len(A)==len(B)