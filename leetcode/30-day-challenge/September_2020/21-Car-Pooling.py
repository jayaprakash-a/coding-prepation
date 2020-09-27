class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def getFreq(maxDist):            
            minVal = sys.maxsize
            maxVal = 0

            freq = [0 for _ in range(maxDist+1)]   

            for i in range(len(trips)): 
                low = trips[i][1]  
                freq[low] = freq[low] + trips[i][0]
                high = trips[i][2]  
                freq[high] = freq[high] - trips[i][0]
                if low < minVal:  
                    minVal = low  
                if high > maxVal: 
                    maxVal = high  
                
                # print(freq)
            
            for i in range(minVal+1, maxVal + 2):  
                freq[i] = freq[i] + freq[i - 1]
            
            return freq[:-1] 
        maxValue = max(trips[i][2] for i in range(len(trips)))
        freq = getFreq(maxValue+2)
        # print(freq)
        
        return all(freq[i] <= capacity for i in range(len(freq)))