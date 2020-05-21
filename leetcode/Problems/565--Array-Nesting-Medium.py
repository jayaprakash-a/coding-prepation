class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False for _ in range(len(nums))]
        maxLen = 0
        currLen = 1
        
        visitCount = 0
        
        for i in range(len(nums)):
            if not visited[i]:
                start = i
                currLen = 1
                visited[start] = True
                start = nums[start]
                while(visitCount < len(nums)):
                    # print(start, currLen)
                    if visited[start]:
                        maxLen = max(maxLen, currLen)
                        # currLen = 1
                        break
                    else:
                        visited[start] = True
                        start = nums[start]
                        currLen += 1
                        visitCount += 1
        return maxLen