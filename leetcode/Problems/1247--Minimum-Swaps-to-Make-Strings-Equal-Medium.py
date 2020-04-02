class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        fullStr = s1+s2
        xCount = fullStr.count('x')
        yCount = fullStr.count('y')
        newStr = ''
        if xCount%2 != 0 or yCount%2 != 0:
            return -1
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                newStr += c1
        count = 0
        while('xx' in newStr or 'yy' in newStr):
            if 'xx' in newStr:
                count += 1
                newStr = newStr.replace('xx', '', 1)
            if 'yy' in newStr:
                count += 1
                newStr = newStr.replace('yy', '', 1)
        # print(len(newStr))
        return count + ((len(newStr)//2+1)//2)*2
                
