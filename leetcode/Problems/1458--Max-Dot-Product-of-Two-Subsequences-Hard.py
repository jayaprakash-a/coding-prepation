class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float('-inf') for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        overallMax = float('-inf')
        for i1 in range(len(nums1)):
            for j1 in range(len(nums2)):
                i = i1 + 1
                j = j1 + 1

                dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j-1], dp[i-1][j], nums1[i1]*nums2[j1])
                dp[i][j] = max(dp[i-1][j-1] + nums1[i1]*nums2[j1], dp[i][j])

                        
                
                if dp[i][j] > overallMax:                    
                    overallMax = dp[i][j]

                    
        
        # print(dp)
        return overallMax