class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumVal = 0
        sumArr = [0]
        
        for num in nums:
            sumVal += num
            sumArr.append(sumVal)
        maxVal = None
        for i in range(k, len(sumArr)):
            # print(sumArr[i])
            if not maxVal:
                maxVal = sumArr[i]-sumArr[i-k]
            else:
                if (sumArr[i]-sumArr[i-k]) > maxVal:
                    maxVal = sumArr[i]-sumArr[i-k]
        return maxVal/k
            
        