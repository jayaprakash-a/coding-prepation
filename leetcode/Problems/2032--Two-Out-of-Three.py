class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = [0] * 101
        for i in nums1:
            freq[i] += 1
        for i in nums2:
            freq[i] += 1
        for i in nums3:
            freq[i] += 1
        answer = []
        for i in range(1, 101):
            if freq[i] >= 2:
                answer.append(i)
        return answer
