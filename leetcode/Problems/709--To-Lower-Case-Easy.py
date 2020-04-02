class Solution:
    def toLowerCase(self, str: str) -> str:
        answer = ''
        for ch in str:
            if ord(ch) <= ord('Z') and ord(ch) >= ord('A'):
                answer += chr(ord(ch) - ord('A') + ord('a'))
            else:
                answer += ch
                
        return answer
        