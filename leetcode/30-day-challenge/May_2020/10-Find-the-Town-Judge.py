class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustee = [False]*(N+1)
        trusted = [0]*(N+1)
        if len(trust) == 0 and N == 1:
            return 1
        if len(trust) == 0 and N > 1:
            return -1
        for a, b in trust:
            trustee[a] = True
            trusted[b] += 1
        remaining = [i for i, x in enumerate(trustee) if x == False]
        if len(remaining) == 0:
            return -1
        for person in remaining:
            if trusted[person] == N-1:
                return person
        return -1
        
        