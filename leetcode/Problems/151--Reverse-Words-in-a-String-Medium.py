class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        s = ' '.join(s.split())
        splitStr = s.split(' ')
        splitStr = splitStr[::-1]
        answer = ' '.join(splitStr)
        answer = answer.rstrip()
        
        return answer
        