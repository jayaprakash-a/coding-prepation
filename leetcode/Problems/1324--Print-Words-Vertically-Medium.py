class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitStr = s.split(' ')
        
        
        maxLen = 0
        
        for entry in splitStr:
            if len(entry) > maxLen:
                maxLen = len(entry)
        answer = ['']*maxLen
        index = 0
        while(index < maxLen):
            
            # exists = False
            for i in range(len(splitStr)):
                if index < len(splitStr[i]):
                    exists = True
                    answer[index] += splitStr[i][index]
                else:
                    answer[index] += ' '
            # if not exists:
                # break
            index += 1
        
        for i in range(index):
            answer[i] = answer[i].rstrip()
        
        return answer
        s