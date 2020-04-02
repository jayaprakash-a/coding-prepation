class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''
        i = 0
        while i < len(s):
            if(i+2 < len(s) and s[i+2] == '#'):
                num = int(s[i:i+2])
                # print(num, end=' @ ')
                answer += chr(ord('a') + num - 1)
                i = i + 3
            else:
                num = int(s[i])
                answer += chr(ord('a') + num - 1)

                # print(s[i], end=' @ ')
                i += 1
        return answer
        