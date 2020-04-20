class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(2**len(nums)):
            arr = []
            numRep = str(bin(i)).replace('0b', '')[::-1]
            
            for j in range(len(numRep)):
                if numRep[j] == '1':
                    arr.append(nums[j])
            answer.append(arr)
        return answer