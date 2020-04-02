class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        modVal = 2*numRows - 2
        answer, ansRev = '', ''
        for i in range(0, len(s), modVal):
            answer += s[i]
        for i in range(numRows-1, len(s), modVal):
            ansRev += s[i]
        for i in range(1,numRows-1):
            j=i
            while(j<len(s)):

                answer += s[j]
                j += (modVal - 2*i)
                if j >= len(s):
                    break
                answer += s[j]
                j += (2*i)
        
        return answer+ansRev
        