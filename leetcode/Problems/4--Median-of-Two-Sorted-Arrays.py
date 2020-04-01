class Solution:
    def getMedian(self, arr):
        if len(arr) == 0:
            return 0, -1
        if len(arr) % 2 == 1:
            return arr[len(arr)//2], len(arr)//2
        else:
            return 0.5 * (arr[len(arr)//2] + arr[len(arr)//2 - 1]), len(arr)//2 - 1
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.getMedian(sorted(nums1+nums2))[0]
#         med1, medInd1 = self.getMedian(nums1)
#         med2, medInd2 = self.getMedian(nums2)
        
#         if med1 == med2:
#             return med1
        
#         if med1 > med2:
#             return self.findMedianSortedArrays(nums1[:medInd1], nums2[medInd2:])
#         else:
#             return self.findMedianSortedArrays(nums1[medInd1:], nums2[:medInd2])
        