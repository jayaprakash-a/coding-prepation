class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for num in nums:
            if num not in numCount.keys():
                numCount[num] = 1
            else:
                numCount[num] += 1
        countNum = {}
        
        for num in numCount.keys():
            if numCount[num] not in countNum.keys():
                countNum[numCount[num]] = [num]
            else:
                countNum[numCount[num]].append(num)
        
        
        # count = 0
        answer = []
        # while(count  < k):
        for val in range(len(nums), 0, -1):
            if val in countNum.keys():
                answer += countNum[val]
        
        return answer[:k]
        
                
        