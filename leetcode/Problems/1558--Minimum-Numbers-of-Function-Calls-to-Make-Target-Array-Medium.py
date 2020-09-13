class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        while True:
            zc, flag = 0, False
            for num in nums:
                if num%2 == 1:
                    flag = True
                    break
                elif num == 0:
                    zc += 1
            if zc == n:
                return answer
            if flag:
                for i in range(n):
                    if nums[i]%2 == 1:
                        nums[i] -= 1
                        answer += 1
            else:
                for i in range(n):
                    nums[i] //= 2
                answer += 1
        