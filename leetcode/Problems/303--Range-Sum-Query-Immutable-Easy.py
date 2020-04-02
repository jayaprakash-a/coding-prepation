class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        
        sum = 0
        for num in nums:
            sum += num
            self.prefixSum.append(sum)
        
            
        
        

    def sumRange(self, i: int, j: int) -> int:
        
        return self.prefixSum[j+1] - self.prefixSum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)