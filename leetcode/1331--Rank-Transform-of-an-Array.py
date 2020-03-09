class Solution:
    def sortFirst(self ,val):
        return val[0]
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return [1]
        
        answer = [0]*len(arr)
        newList = []
        
        
        for index in range(len(arr)):
            newList.append((arr[index], index))
            
        newList.sort(key = self.sortFirst) 
        
        ind, rank = 0, 1
        previous = newList[0][0]
        # print(previous)
        while(ind < len(newList)):
            if previous != newList[ind][0]:
                previous = newList[ind][0]
                rank += 1
            answer[newList[ind][1]] = rank
            ind += 1
            
            

    
            
        return answer
                