class Solution:
    def nthUglyNumber(self, n: int) -> int:

        answer = [0 for _ in range(n)]
        t2 = t3 = t5 = 0
        answer[0] = 1
        for i in range(1,n):
            answer[i] = min(answer[t2]*2, answer[t3]*3, answer[t5]*5)
            if(answer[i] == answer[t2]*2):
                t2 += 1
            if(answer[i] == answer[t3]*3):
                t3 += 1
            if(answer[i] == answer[t5]*5):
                t5 += 1
        return answer[n-1]