
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        charStack = []
        for ch in S:
            # print(charStack)
            if ch == '(':
                charStack.append('(')
            elif ch == ')':
                # print(charStack[-1])
                if charStack[-1] == '(':
                    charStack.pop()
                    charStack.append('1')
                elif charStack[-1].isdigit():
                    score = charStack.pop()
                    charStack.pop()
                    charStack.append(str(2*int(score)))
            for i in range(len(charStack)-1, 0, -1):
                if charStack[i].isdigit() and charStack[i-1].isdigit():
                    sum = int(charStack[i]) + int(charStack[i-1])
                    charStack.pop(i-1)
                    charStack[i-1] = str(sum)
                    break
                
        score = 0
        for num in charStack:
            score += int(num)
        
        return score