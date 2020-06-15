class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A = sorted(A)
        answer, n, modVal = 0, len(A), int(1e9+7)
        start, end = 1, 1<<n
        for i in range(n): 
            if i > 0:
                start = start<<1
            end = end>>1
            diff = (start-end)%modVal
            # print(start, end, diff)
            answer += (diff*A[i])%modVal
        return answer%modVal