class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        modVal = 10**9+7
        numInd1, numInd2 = Counter(), Counter()
        for i in range(len(nums1)):
            numInd1[nums1[i]] = i
        for i in range(len(nums2)):
            numInd2[nums2[i]] = i
        numInd2[-1] = 0
        numInd1[-1] = 0
        dp1 = [0 for _ in range(len(nums1))] 
        dp2 = [0 for _ in range(len(nums2))] 
        preSum = 0
        for i in range(len(nums1)):
            preSum = (preSum + nums1[i])
            dp1[i] = preSum
        preSum = 0
        for i in range(len(nums2)):
            preSum = (preSum + nums2[i])
            dp2[i] = preSum
        answer = 0
        prev = -1
        valAtPrev, i = 0, 0
        while i < len(nums1):
            answer = max(answer+nums1[i], dp1[i])
            if nums1[i] in numInd2:
                
                prevDp = dp2[numInd2[prev]]
                if prev == -1:
                    prevDp = 0
                change = dp2[numInd2[nums1[i]]] - prevDp
                if change > answer-valAtPrev:
                    answer = change+valAtPrev
                valAtPrev = answer
                prev = nums1[i]
            i += 1
        answer2 = 0
        prev, valAtPrev, i = -1, 0, 0
        while i < len(nums2):
            answer2 = max(answer2+nums2[i], dp2[i])
            if nums2[i] in numInd1:
                prevDp = dp1[numInd1[prev]]
                if prev == -1:
                    prevDp = 0
                change = dp1[numInd1[nums2[i]]] - prevDp
                if change > answer2-valAtPrev:
                    answer2 = change+valAtPrev
                valAtPrev = answer2
                prev = nums2[i]
            i += 1
        return max(answer, answer2)%(modVal)
                
                        
                            