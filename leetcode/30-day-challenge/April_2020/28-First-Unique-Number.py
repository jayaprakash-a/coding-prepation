class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.seen = set()
        self.nums = collections.deque()
        self.numDict = collections.Counter()
        for value in nums:
            if value not in self.seen:
                self.nums.append(value)
                self.numDict[value] += 1
                self.seen.add(value)
            else:
                if self.numDict[value] > 0:
                    self.nums.remove(value)
                    self.numDict[value] -= 1
        
    def showFirstUnique(self) -> int:
        if len(self.nums) == 0:
            return -1
        return self.nums[0]

    def add(self, value: int) -> None:
        # print(self.nums, self.seen)
        if value not in self.seen:
            self.nums.append(value)
            self.numDict[value] += 1
            self.seen.add(value)
        else:
            if self.numDict[value] > 0:
                self.nums.remove(value)
                self.numDict[value] -= 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)