class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        nums.append(nums[-1]+2)
        answer = []
        entry = str(nums[0])
        prevNum = nums[0]
        for num in nums[1:]:
            if num - 1 == prevNum:
                prevNum = num
                continue
            else:
                if str(prevNum) == entry:
                    answer.append(entry)
                else:
                    entry += ('->' + str(prevNum))
                    answer.append(entry)
                entry = str(num)
                prevNum = num
        
        # answer.append(entry)
        return answer
                    