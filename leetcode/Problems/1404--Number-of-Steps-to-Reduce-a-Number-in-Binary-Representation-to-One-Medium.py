class Solution:
    def addOne(self, s):
        carry = 1
        sList = list(s)
        for i in range(len(s)-1, -1, -1):
            val = int(sList[i])
            sList[i] = str((carry+int(sList[i])) % 2)
            carry = (carry+val)//2
            if carry == 0:
                break
        if carry == 1:
            sList.insert(0, '1')
        # print(s, sList)
        return ''.join(sList)

    def numSteps(self, s: str) -> int:

        count = 0
        # self.addOne('1101')
        while(s != '1'):
            # print(s)
            count += 1
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = self.addOne(s)
        return count
