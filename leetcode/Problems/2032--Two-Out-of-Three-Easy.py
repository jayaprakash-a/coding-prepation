class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1 = [0 for _ in range(100)]
        n2 = [0 for _ in range(100)]
        n3 = [0 for _ in range(100)]
        for num in nums1:
            n1[num-1] = 1
        for num in nums2:
            n2[num-1] = 1 
        for num in nums3:
            n3[num-1] = 1
        answer = []
        for i in range(100):
            if (n1[i]+n2[i]+n3[i]) >= 2:
                answer.append(i+1)
        return answer
