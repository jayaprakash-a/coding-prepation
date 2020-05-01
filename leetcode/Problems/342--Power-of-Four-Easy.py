class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        numStr = str(bin(num)).replace('0b', '')
        if numStr[0] == '1' and len(numStr)%2==1 and numStr.count('0') == len(numStr)-1:
            return True
        return False