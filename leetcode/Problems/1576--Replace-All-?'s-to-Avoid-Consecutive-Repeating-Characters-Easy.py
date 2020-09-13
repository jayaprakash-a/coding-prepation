class Solution:
    def modifyString(self, s: str) -> str:
        alpha = 'qwertyuiopasdfghjklzxcvbnm'
        def getCh(i):
            possible = ''
            if i == 0 and i+1 < len(s) and answer[i+1] != '?':
                possible += answer[i+1]        
            elif i == 0:
                possible += ''
            elif i == len(s) - 1:
                possible += answer[i-1]
            else:
                possible += (answer[i-1] + answer[i+1])
            for ch in alpha:
                if ch not in possible:
                    return ch
        answer = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                answer[i] = getCh(i)
        
        return ''.join(answer)