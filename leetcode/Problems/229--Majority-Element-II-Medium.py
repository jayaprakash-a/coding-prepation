class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2, c1, c2 = 0, 1, 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1, c2 = c1-1, c2-1
        
        answer = []
        if nums.count(n1) > len(nums)//3:
            answer.append(n1)
        if nums.count(n2) > len(nums)//3:
            answer.append(n2)
        return answer