# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def __init__(self):
        self.count = 0
    def binSearch(self, r, binMat, e):
        self.count += 1
        if binMat.get(r, e) == 0:
            return -1
        start, end = 0, e
        index = e
        found = False
        while(start <= end):
            
            mid = start + (end-start)//2
            # print(r, mid)
            self.count += 1
            val = binMat.get(r, mid)
            if val == 1:
                index = mid
                found = True
                end = mid-1
            else:
                start = mid+1
        # print(found)
        if found:
            return index
        return -1
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [r, c] = binaryMatrix.dimensions()
        end = c-1
        answer = c
        found = False
        for i in range(r):
            ans = self.binSearch(i, binaryMatrix, end)
            if ans == -1:
                continue
            else:
                found = True
                end = ans-1
                if ans == 0:
                    print(self.count)
                    return 0
                answer = min(answer, ans)
        
        print(self.count)
        if found:
            return answer
        return -1