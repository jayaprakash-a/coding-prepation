class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoSet = {}
        count = 0
        for [x, y] in dominoes:
            domino = (min(x,y), max(x,y))
            if domino in dominoSet.keys():
                dominoSet[domino] += 1
            else:
                dominoSet[domino] = 1
        
        for val in dominoSet.values():
            count += (val*(val-1)//2)
        return count
        