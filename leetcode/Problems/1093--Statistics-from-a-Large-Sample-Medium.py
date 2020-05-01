class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minVal, maxVal, mean, median, mode = 256, -1, 0, 0, 0
        
        maxCount, sumVal, total = -1, 0, 0
        
        for i in range(len(count)):
            if count[i] != 0:
                if i < minVal:
                    minVal = i
                if i > maxVal:
                    maxVal = i
                
                if count[i] > maxCount:
                    maxCount = count[i]
                    mode = i
                sumVal += (i*count[i])
                
                total += count[i]
        
        mean = sumVal / total
        # print(total)
        total /= 2
        for i in range(len(count)):
            total -= count[i]
            
            if total < 0.0:
                median = i
                break
            if total == 0.0:
                start, end = i, 0
                for j in range(i+1, len(count)):
                    if count[j] != 0:
                        end = j
                        break
                median = (start+end) / 2
                break
        
        return [minVal, maxVal, mean, median, mode]