class Solution:
    def sortString(self, s: str) -> str:
        sortString = sorted(s)
        answer = ''
        
        while(len(answer) != len(s)):
            charSet = sorted(list(set(sortString)))
            
            answer += ''.join(charSet)
            # print(answer)
            for ch in charSet:
                sortString.remove(ch)
            
            charSet = sorted(list(set(sortString)), reverse = True)
            
            answer += ''.join(charSet)
            
            for ch in charSet:
                sortString.remove(ch)
                
            # print(answer)
        
        return answer
            
            
                    
            
            
        