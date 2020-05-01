class Solution:
    def maxScore(self, s: str) -> int:
        zero, one = [] , []
        count = 0
        for i in range(len(s)-1):
            if s[i] == '0':                
                count += 1
            zero.append(count)
        count = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == '1':
                
                count += 1
            one.append(count)
        # print(zero, one)
        answer = 0
        for i in range(len(s)-1):
            answer = max(answer, one[len(one)-1-i]+zero[i])
        return answer
        