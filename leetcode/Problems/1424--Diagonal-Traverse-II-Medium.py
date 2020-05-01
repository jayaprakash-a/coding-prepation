class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if len(nums)==0:
            return []
        diagEntry = {}
        maxDiag = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # print(nums[i][j], end=' ')
                if (i+j) not in diagEntry.keys():
                    maxDiag = max(i+j, maxDiag)
                    diagEntry[i+j] = [nums[i][j]]
                else:
                    diagEntry[i+j] += [nums[i][j]]
        # print(diagEntry)
        answer = []
        for i in range(maxDiag+1):
            answer += diagEntry[i][::-1]
            # print(answer)
        return answer