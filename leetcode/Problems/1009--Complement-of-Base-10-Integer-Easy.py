class Solution:
    def bitwiseComplement(self, N: int) -> int:
        answer = 0
        twoPow = 1
        num = N
        while(num):
            if num%2 == 0:
                answer += 1*twoPow
            num = num//2
            twoPow *= 2
        return answer