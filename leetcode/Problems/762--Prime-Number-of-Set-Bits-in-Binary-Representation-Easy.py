class Solution:
    def isPrime(self, num):
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True
    def countPrimeSetBits(self, L: int, R: int) -> int:
        answer = 0
        for num in range(L, R+1):
            bitCount = str(bin(num)).count('1')
            if self.isPrime(bitCount):
                answer += 1
        return answer