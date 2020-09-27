class Solution:
    def reorderSpaces(self, text: str) -> str:
        spCount = text.count(' ')
        # print(spCount)
        words = text.split()
        if len(words) > 1:
            minCount = spCount // (len(words)-1)
        else:
            minCount = 0
        
        space = ' '*(minCount)
        
        answer = space.join(words)
        value = spCount - (minCount*(len(words)-1))
        space = ' '*((value))
        
        answer += space
        
        return answer