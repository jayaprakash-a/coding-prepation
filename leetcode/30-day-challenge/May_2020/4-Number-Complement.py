class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0
        twoPow = 1
        while(num):
            if num%2 == 0:
                answer += 1*twoPow

            num = num//2
            twoPow *= 2
        return answer