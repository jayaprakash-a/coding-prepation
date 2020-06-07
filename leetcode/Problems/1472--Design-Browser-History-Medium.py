class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [[homepage, -1, 1]]
        self.length = 1
        self.currIndex = 0
        # print(self.arr, self.currIndex)

    def visit(self, url: str) -> None:
        self.length += 1
        self.arr += [[url, self.currIndex, self.length]]        
        self.arr[self.currIndex][2] = self.length-1
        self.currIndex = self.length-1
        
        # print(self.arr, self.currIndex)

    def back(self, steps: int) -> str:
        start = self.currIndex
        index = start
        count = 0
        while count < steps:
            # print('back', count, index)
            index = self.arr[index][1]
            if index == -1:
                self.currIndex = 0
                break
            count += 1
        if index != -1:    
            self.currIndex = index
        # print(self.arr, self.currIndex)
        return self.arr[self.currIndex][0]
    
    def forward(self, steps: int) -> str:
        start = self.currIndex
        index = start
        count = 0
        while count < steps:
            # print('forward', count, index)
            index = self.arr[index][2]
            if index == self.length:
                self.currIndex = self.length-1
                break
            count += 1
        if index != self.length:
            self.currIndex = index
        # print(self.arr, self.currIndex)
        return self.arr[self.currIndex][0]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)