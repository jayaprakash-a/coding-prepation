class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        asum, bsum = sum(A), sum(B)
        B = set(B)
        A = set(A)
        for a in A:
            val = (bsum-asum)//2 + a
            if val in B:
                return [a, val]