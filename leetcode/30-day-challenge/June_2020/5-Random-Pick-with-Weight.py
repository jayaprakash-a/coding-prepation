import bisect 

class Solution:

    def __init__(self, w: List[int]):
        sumVal = sum(w)
        self.w, currSum = [], 0
        for num in w:
            currSum += num
            self.w.append(currSum/sumVal)
        
    def pickIndex(self) -> int:
        value = random.uniform(0, 1)
        index = bisect.bisect_left(self.w, value)
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()