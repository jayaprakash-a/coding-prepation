class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0:
            return False
        if n == 1:
            return True
        number = bin(n).replace('0b', '')
        print(number)
        strNum = str(number)
        try:
            if int(strNum[0]) == 1 and int(strNum[1:]) == 0:
                return True
        except:
            return False
        