class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        answer = []
        for num in c:
            if c[num] > len(nums)//3:
                answer.append(num)
        return answer