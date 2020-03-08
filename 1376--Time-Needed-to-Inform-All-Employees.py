class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        if n == 1:
            return 0
        elif n == 2:
            return max(informTime[0], informTime[1])
        
        subOrdinate = {}
        
        for i in range(len(manager)):
            if manager[i] not in subOrdinate.keys():
                subOrdinate[manager[i]] = [i]
            else:
                subOrdinate[manager[i]] += [i]
        
        subSet = subOrdinate[headID]
        time = 0
        timeTaken = [-1]*len(manager)
        timeTaken[headID] = 0
        
        maxVal = 0
        while(len(subSet) != 0):
            newSubSet = []
            for entry in subSet:
                timeTaken[entry] = timeTaken[manager[entry]] + informTime[manager[entry]]
                if timeTaken[entry] > maxVal:
                    maxVal = timeTaken[entry]
                if entry in subOrdinate.keys():
                    newSubSet += subOrdinate[entry]
            subSet = newSubSet
        
        return maxVal
            
                
            
                
                
            
        
        