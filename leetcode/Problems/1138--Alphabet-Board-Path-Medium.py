class Solution:
    def getIndex(self, char):
        return (ord(char)-ord('a')) // 5, (ord(char)-ord('a')) %5
    def alphabetBoardPath(self, target: str) -> str:
        start = (0, 0)
        path = ''
        for ch in target:
            loc = self.getIndex(ch)
            if loc[0] == 5:
                if loc[1] > start[1]:
                    path += 'R'*(loc[1]-start[1])
                else:
                    path += 'L'*(-loc[1]+start[1])
                # print(start, loc)
                if loc[0] > start[0]:
                    path += 'D'*(loc[0]-start[0])
                else:
                    path += 'U'*(-loc[0]+start[0])
            else:
                if loc[0] > start[0]:
                    path += 'D'*(loc[0]-start[0])
                else:
                    path += 'U'*(-loc[0]+start[0])
                if loc[1] > start[1]:
                    path += 'R'*(loc[1]-start[1])
                else:
                    path += 'L'*(-loc[1]+start[1])
             
            
            path += '!'
            start = loc
        return path
        