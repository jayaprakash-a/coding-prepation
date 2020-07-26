class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 1
        result = 0
        val = 0
  
        for i in range(len(arr)): 
            val = ((val + arr[i]) % 2)%2
            if val == 0:
                even += 1
            else:
                odd += 1
        result = even*odd
        return result%(10**9+7)
                  