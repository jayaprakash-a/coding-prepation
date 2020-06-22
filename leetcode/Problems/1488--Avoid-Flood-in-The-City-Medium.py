class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        nonRainyDays = []
        answer = [-1]*len(rains)
        recentlyFilled = {}
        def getIndex(num):
            
            i = bisect.bisect_right(nonRainyDays, num)
            # print(nonRainyDays, num, i)
            return i
            
        for i in range(len(rains)):
            if rains[i] == 0:
                nonRainyDays.append(i)
            else: 
                if rains[i] in recentlyFilled:
                    if len(nonRainyDays) == 0:
                        return []
                    index = getIndex(recentlyFilled[rains[i]])
                    if index == len(nonRainyDays):
                        return []
                    answer[nonRainyDays[index]] = rains[i]
                    nonRainyDays.pop(index)              

                recentlyFilled[rains[i]] = i
        for i in range(len(rains)):
            if rains[i] == 0 and answer[i] == -1:
                answer[i] = 1
        return answer