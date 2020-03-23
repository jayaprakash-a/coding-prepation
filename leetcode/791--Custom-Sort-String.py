class Solution:
    def customSortString(self, S: str, T: str) -> str:
        charCount = [0]*26
        for ch in T:
            charCount[ord(ch)-ord('a')] += 1
        
        answer = ''
        for ch in S:
            answer += (ch*charCount[ord(ch)-ord('a')])
            charCount[ord(ch)-ord('a')] = 0
        
        for i in range(26):
            if charCount[i] != 0:
                answer += (chr(i+ord('a'))*charCount[i])
        
        return answer
        
        
        