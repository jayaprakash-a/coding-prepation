class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         answer = set()
        
#         if len(nums1) < len(nums2):
#             for num1 in nums1:
#                 if num1 in nums2:
#                     answer.add(num1)
#         else:
#             for num2 in nums2:
#                 if num2 in nums1:
#                     answer.add(num2)
#         return answer

        return set(nums1).intersection(set(nums2))
            
        