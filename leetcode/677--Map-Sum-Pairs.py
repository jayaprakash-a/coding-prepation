class MapSum:

    def __init__(self):
        self.keys = []
        self.values = []       
        

    def insert(self, key: str, val: int) -> None:
        if len(self.keys) == 0:
            self.keys += [key]
            self.values += [val]
            return
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = val
                return
        
        self.keys += [key]
        self.values += [val]

    def sum(self, prefix: str) -> int:
        answer = 0
        for i in range(len(self.keys)):
            if self.keys[i][:len(prefix)] == prefix:
                answer += self.values[i]
        return answer
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)