class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        stack = []
        
        for ch in num:
            while(len(stack) > 0  and stack[-1] > ch and k > 0):
                stack.pop()
                k -= 1
            stack.append(ch)
        while(k > 0):
            stack.pop()
            k -= 1
        i = 0
        if stack[0] == '0':
            print('entered')
            while(i < len(stack) and stack[i] == '0'):
                i += 1
            if i == len(stack):
                return '0'
        return ''.join(stack[i:])
        