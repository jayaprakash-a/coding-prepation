class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        def getBit(num, index):
            return (num>>index & 1)
        answer, total, index = 0, len(nums), 0
        maxNum = max(nums)
        maxCount = len(bin(maxNum)) - 2
        while index <= maxCount:
            oneCount = 0
            for num in nums:
                if getBit(num, index) == 1:
                    oneCount += 1
            answer += (oneCount*(total-oneCount))
            index += 1
        return answer