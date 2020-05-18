class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        answer = 0
        while(X < Y):
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
            answer += 1
        return answer + X - Y