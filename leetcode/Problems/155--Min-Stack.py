class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myArr = []

    def push(self, x: int) -> None:
        self.myArr.append(x)
        

    def pop(self) -> None:
        self.myArr.pop()
        

    def top(self) -> int:
        return self.myArr[-1]
        

    def getMin(self) -> int:
        return min(self.myArr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()