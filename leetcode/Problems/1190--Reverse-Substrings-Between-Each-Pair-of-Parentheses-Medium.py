class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        i = 0
        while(i < len(s)):
            if s[i] != ')':
                stack.append(s[i])
                
            else:
                word = ''
                while(True):
                    char = stack.pop()
                    if char =='(':
                        break
                    else:
                        word += char
                stack += list(word)
            i += 1
        
        answer = ''.join(stack)
        
        return answer
                    
        