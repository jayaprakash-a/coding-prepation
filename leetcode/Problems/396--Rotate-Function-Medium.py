class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:

        s = sum(A)
        r = curr = sum([i*A[i] for i in range(len(A))])
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r