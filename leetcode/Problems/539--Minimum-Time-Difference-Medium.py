class Solution:
    def compare(self, x):
        return int(x.split(':')[0]), int(x.split(':')[1])
    def findMinDifference(self, timePoints: List[str]) -> int:

        tp = sorted(timePoints, key=self.compare)
        newTime = str(int(tp[0].split(':')[0]) + 24) + ':' + tp[0].split(':')[1]
        tp = tp+[newTime]
        # print(tp)
        minDiff = 24*60
        for i in range(len(tp)-1):
            [h1, m1] = list(map(int, tp[i].split(':')))
            [h2, m2] = list(map(int, tp[i+1].split(':')))

            if h1 == h2:
                timeDiff = m2-m1
                minDiff = min(minDiff, timeDiff)
                
            else:
                timeDiff = (60-m1)+m2+(h2-h1-1)*60
                minDiff = min(minDiff, timeDiff)
            if minDiff == 0:
                return 0
        
        return minDiff