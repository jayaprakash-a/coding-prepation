class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        answer = 0
        
        for ch in J:
            answer += S.count(ch)
        return answer