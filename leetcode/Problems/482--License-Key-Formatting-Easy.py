class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        charList = ''.join(S.split('-'))
        charList = charList.upper()
        answer =''
        
        for i in range(len(charList)-1, -1, -1*K):
            startIndex = max(0, i-K+1)
            group = charList[startIndex:i+1]
            answer = '-'+ group+answer
        
        return answer[1:]
        
        
            
        