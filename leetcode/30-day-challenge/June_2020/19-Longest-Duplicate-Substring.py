class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 1<<63-1
        def valid(length):
            p = pow(26, length, mod)
            curr = 0
            for i in range(length):
                curr = (26*curr+A[i])%mod
            seen = {curr}
            for i in range(length, len(S)):
                curr = (curr * 26 + A[i] - A[i-length] * p) % mod
                if curr in seen:
                    return S[i-length+1:i+1]
                seen.add(curr)
            return ''
        low, high = 0, len(S)-1
        result = ''
        while low <= high:
            mid = (low+high)//2
            answer = valid(mid)
            if answer == '':
                high = mid-1
            else:
                low = mid+1
                result = max(answer, result, key=len)
        return result
                