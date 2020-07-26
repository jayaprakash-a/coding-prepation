class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        counter = Counter(nums)
        for num in counter:
            if counter[num] == 1:
                answer.append(num)
        return answer