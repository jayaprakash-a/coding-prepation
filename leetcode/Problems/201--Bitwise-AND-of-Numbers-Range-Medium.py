class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diffVal = abs(m-n)
        mVal = str(bin(m)).replace('0b', '')
        nVal = str(bin(n)).replace('0b', '')
        diff = abs(len(mVal)-len(nVal))
        if len(mVal) > len(nVal):
            mVal = mVal[diff:]
        else:
            nVal = nVal[diff:]
        
        
        twoPow = 1<<len(mVal)-1
        value = 0
        for i in range(len(mVal)):
            value = value << 1
            if mVal[i]==nVal[i]=='1' and diffVal<twoPow:
                value += 1
            twoPow = twoPow >> 1
        
        
        return value