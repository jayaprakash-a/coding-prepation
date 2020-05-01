class Solution:
    def countElements(self, arr: List[int]) -> int:
        return sum([1 for num in arr if num+1 in arr])