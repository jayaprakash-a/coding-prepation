class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        answer = ''
        val, index = 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                val += 1
            else:
                val -= 1
            
            if val == 0:
                answer += S[index+1:i]
                # print(answer)
                index = i+1
        
        return answer
                
            
        