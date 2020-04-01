class Solution:
    def comparator(self, x):
        return x[1], x[0]
    def maxEvents(self, events: List[List[int]]) -> int:
        # eList = [list(x) for x in set(tuple(x) for x in events)]

        newEvents = sorted(events, key=self.comparator)
        startTimes = [row[0] for row in newEvents]
        finishTimes = [row[1] for row in newEvents]


        i, count = 0, 1 
        answerSet = set()
        for j in range(len(finishTimes) ): 
            # if startTimes[j] >= finishTimes[i]:
            time = startTimes[j]
            while(time in answerSet and time<=finishTimes[j]):
                time += 1
            count += 1
            # print(time, j, startTimes[j], finishTimes[j])
            if time > finishTimes[j]:
                continue
            answerSet.add(time)
            # print(answerSet)
            i = j 
        # return count
        return len(answerSet)
        