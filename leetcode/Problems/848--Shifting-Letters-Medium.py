class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if len(S) == 0:
            return ''
        suffSum = [0 for i in range(len(S))]
        suffSum[-1] = shifts[-1]%26
        for i in range(len(shifts)-2, -1, -1):
            suffSum[i] = (suffSum[i+1]+shifts[i])%26
        
        strList = list(S)
        # print(suffSum)
        for i in range(len(S)):
            # print((ord(S[i])+suffSum[i])%26)
            strList[i] = chr(ord('a') + (ord(S[i])-ord('a')+suffSum[i])%26)
        return ''.join(strList)
        