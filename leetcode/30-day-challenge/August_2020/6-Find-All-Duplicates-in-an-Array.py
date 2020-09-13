class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numSet = set()
        answer = []

        for num in nums:
            if num in numSet:
                answer.append(num)
            numSet.add(num)
        return answer