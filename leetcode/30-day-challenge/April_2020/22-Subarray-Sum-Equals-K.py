class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDict = {0:1}
        sumVal = 0
        answer = 0
        for num in nums:
            sumVal += num
            if sumVal not in sumDict.keys():
                sumDict[sumVal] = 1
            else:
                sumDict[sumVal] += 1
            if sumVal-k in sumDict.keys():
                answer += sumDict[sumVal-k]
                if k == 0:
                    answer -= 1
        return answer