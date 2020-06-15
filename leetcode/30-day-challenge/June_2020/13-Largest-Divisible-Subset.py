class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subSetMap = {-1: set()}
        for num in sorted(nums):
            subSetMap[num] = max((subSetMap[i] for i in subSetMap if num % i == 0), key=len) | {num}
        return list(max(subSetMap.values(), key=len))