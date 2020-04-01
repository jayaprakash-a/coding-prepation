class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustee = set()
        trusted = {}
        if len(trust) == 0 and N == 1:
            return 1
        if len(trust) == 0 and N > 1:
            return -1
        for a, b in trust:
            trustee.add(a)
            if b not in trusted.keys():
                trusted[b] = 1
            else:
                trusted[b] += 1
        allPeople = set(range(1, N+1))
        
        remaining = list(allPeople.difference(trustee))
        # print(remaining, trusted)
        if len(remaining) == 0:
            return -1
        for person in remaining:
            if person in trusted.keys() and trusted[person] == N-1:
                return person
        return -1
        
        