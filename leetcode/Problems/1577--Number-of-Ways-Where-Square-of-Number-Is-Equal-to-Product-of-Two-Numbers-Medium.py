class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = Counter(), Counter()
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                p1[nums1[i]*nums1[j]] += 1
        
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                p2[nums2[i]*nums2[j]] += 1
        answer = 0
        for num in nums1:
            answer += p2[num**2]
        for num in nums2:
            answer += p1[num**2]
        
        return answer
        