class Solution:
    def comparator(self, x):
        return x[0], x[1]
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = []
        for i in range(len(groupSizes)):
            group.append((groupSizes[i], i))
        
        groupSorted = sorted(group, key=self.comparator)
        answer = []
        index = 0
        while(index < len(group)):
            smallGroup = []
            count, reqLen = 0, groupSorted[index][0]
            while(count < reqLen):
                smallGroup.append(groupSorted[index][1])
                count += 1
                index += 1
            answer.append(smallGroup)
            
        return answer